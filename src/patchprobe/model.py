"""Text-only, release-aware training and evaluation for PatchProbe."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import joblib
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.pipeline import FeatureUnion, Pipeline

LABELS = (
    "API/code compatibility",
    "Configuration/deployment",
    "Data/schema migration",
    "UI/output behavior",
    "No targeted check stated",
)
UNCLEAR = "UNCLEAR"
ENTRY_COLUMNS = ("entry_id", "release", "source_url", "source_revision", "section_path", "raw_text", "text")
LABEL_COLUMNS = ("entry_id", "label", "annotator", "review_note", "annotated_at")


@dataclass(frozen=True)
class Example:
    entry_id: str
    release: str
    source_url: str
    text: str
    label: str


def _read_csv(path: Path, required: tuple[str, ...]) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        missing = set(required) - set(reader.fieldnames or ())
        if missing:
            raise ValueError(f"{path}: missing columns: {', '.join(sorted(missing))}")
        return list(reader)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_labeled_examples(entries_path: Path, labels_path: Path) -> tuple[list[Example], dict[str, int]]:
    """Join reviewed labels to entries; reject untraceable or invalid labels."""
    entries = _read_csv(entries_path, ENTRY_COLUMNS)
    labels = _read_csv(labels_path, LABEL_COLUMNS)
    by_id: dict[str, dict[str, str]] = {}
    for row in entries:
        entry_id = row["entry_id"].strip()
        if not entry_id or entry_id in by_id:
            raise ValueError(f"Entries contain an empty or duplicate entry_id: {entry_id!r}")
        by_id[entry_id] = row
    examples: list[Example] = []
    seen: set[str] = set()
    counts = Counter({"source_entries": len(entries), "label_rows": len(labels), "unclear": 0})
    for row in labels:
        entry_id = row["entry_id"].strip()
        if not entry_id or entry_id in seen:
            raise ValueError(f"Labels contain an empty or duplicate entry_id: {entry_id!r}")
        seen.add(entry_id)
        if entry_id not in by_id:
            raise ValueError(f"Label has no matching source entry: {entry_id}")
        label = row["label"].strip()
        if label not in LABELS and label != UNCLEAR:
            raise ValueError(f"Unknown label for {entry_id}: {label!r}")
        if not row["annotator"].strip():
            raise ValueError(f"Missing human annotator for {entry_id}")
        if not row["annotated_at"].strip():
            raise ValueError(f"Missing annotation timestamp for {entry_id}")
        if label == UNCLEAR:
            if not row["review_note"].strip():
                raise ValueError(f"UNCLEAR requires a review_note for {entry_id}")
            counts["unclear"] += 1
            continue
        entry = by_id[entry_id]
        text = entry["text"].strip()
        release = entry["release"].strip()
        if not text or not release:
            raise ValueError(f"Labeled entry lacks text or release: {entry_id}")
        examples.append(Example(entry_id, release, entry["source_url"].strip(), text, label))
    counts["unlabeled"] = len(entries) - len(labels)
    counts["accepted"] = len(examples)
    return examples, dict(counts)


def split_by_release(examples: list[Example], seed: int = 42) -> dict[str, list[Example]]:
    """Deterministic group split; each release occurs in exactly one split."""
    releases = sorted({row.release for row in examples})
    if len(releases) < 5:
        raise ValueError("At least five labeled release groups are needed for train/dev/test splitting")
    np.random.default_rng(seed).shuffle(releases)
    n_test = max(1, round(len(releases) * 0.2))
    n_dev = max(1, round(len(releases) * 0.2))
    groups = {
        "test": set(releases[:n_test]),
        "dev": set(releases[n_test : n_test + n_dev]),
        "train": set(releases[n_test + n_dev :]),
    }
    return {name: [row for row in examples if row.release in group] for name, group in groups.items()}


def reject_cross_split_duplicates(splits: dict[str, list[Example]]) -> None:
    """Catch identical cleaned text leaked across grouped splits."""
    seen: dict[str, tuple[str, str]] = {}
    for split_name, rows in splits.items():
        for row in rows:
            normalized = " ".join(row.text.casefold().split())
            previous = seen.get(normalized)
            if previous and previous[0] != split_name:
                raise ValueError(
                    f"Cross-split duplicate text: {previous[1]} ({previous[0]}) and "
                    f"{row.entry_id} ({split_name}); deduplicate source entries before training"
                )
            seen[normalized] = split_name, row.entry_id


def make_pipeline() -> Pipeline:
    features = FeatureUnion([
        ("word", TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)),
        ("char", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)),
    ])
    return Pipeline([("tfidf", features), ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))])


def keyword_predict(text: str) -> str:
    """Fixed transparent baseline; first matching area wins."""
    patterns = (
        ("Data/schema migration", r"\b(migrat\w*|schema|database|db|column|table|records?)\b"),
        ("Configuration/deployment", r"\b(settings?|configur\w*|middleware|deploy\w*|python version|environment|package)\b"),
        ("UI/output behavior", r"\b(admin|template|render\w*|display\w*|form|html|response|serializ\w*)\b"),
        ("API/code compatibility", r"\b(api|function|method|argument|parameter|import|exception|return value|signature)\b"),
    )
    for label, pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return label
    return "No targeted check stated"


def _metrics(y_true: list[str], y_pred: list[str]) -> dict:
    report = classification_report(y_true, y_pred, labels=list(LABELS), output_dict=True, zero_division=0)
    return {
        "n": len(y_true),
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1_five_labels": f1_score(y_true, y_pred, labels=list(LABELS), average="macro", zero_division=0),
        "per_class": {label: report[label] for label in LABELS},
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=list(LABELS)).tolist(),
        "present_true_labels": sorted(set(y_true)),
        "missing_true_labels": [label for label in LABELS if label not in y_true],
    }


def train_and_evaluate(entries_path: Path, labels_path: Path, output_dir: Path, *, seed: int = 42) -> dict:
    """Train only on human-reviewed rows and persist an auditable result."""
    examples, counts = load_labeled_examples(entries_path, labels_path)
    if not examples:
        raise ValueError("No human-labeled examples are available; collect reviewed labels before training")
    splits = split_by_release(examples, seed)
    reject_cross_split_duplicates(splits)
    train = splits["train"]
    if len({row.label for row in train}) < 2:
        raise ValueError("Training split contains fewer than two model classes")
    x_train = [row.text for row in train]
    y_train = [row.label for row in train]
    model = make_pipeline().fit(x_train, y_train)
    majority = DummyClassifier(strategy="most_frequent").fit(np.zeros((len(train), 1)), y_train)
    evaluations: dict[str, dict] = {}
    prediction_rows: list[dict[str, str | float | bool]] = []
    for name in ("dev", "test"):
        rows = splits[name]
        x = [row.text for row in rows]
        y = [row.label for row in rows]
        predictions = model.predict(x).tolist()
        probabilities = model.predict_proba(x).max(axis=1).tolist()
        for row, predicted, score in zip(rows, predictions, probabilities, strict=True):
            prediction_rows.append({
                "split": name, "entry_id": row.entry_id, "release": row.release,
                "source_url": row.source_url, "text": row.text, "gold_label": row.label,
                "predicted_label": predicted, "max_probability_uncalibrated": score,
                "correct": predicted == row.label,
            })
        evaluations[name] = {
            "model": _metrics(y, predictions),
            "majority": _metrics(y, majority.predict(np.zeros((len(rows), 1))).tolist()),
            "keyword": _metrics(y, [keyword_predict(value) for value in x]),
        }
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "split_manifest.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("entry_id", "release", "split", "label", "source_url"))
        for name, rows in splits.items():
            for row in rows:
                writer.writerow((row.entry_id, row.release, name, row.label, row.source_url))
    with (output_dir / "predictions.csv").open("w", encoding="utf-8", newline="") as stream:
        columns = ("split", "entry_id", "release", "source_url", "text", "gold_label", "predicted_label", "max_probability_uncalibrated", "correct")
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(prediction_rows)
    train_support = Counter(row.label for row in splits["train"])
    dev_support = Counter(row.label for row in splits["dev"])
    test_support = Counter(row.label for row in splits["test"])
    incomplete = any(train_support[label] < 5 or dev_support[label] < 2 or test_support[label] < 5 for label in LABELS)
    result = {
        "status": "pilot" if incomplete else "five_class_evaluation",
        "warning": "Class support below train=5, dev=2, or test=5 in at least one class: pilot result only." if incomplete else None,
        "seed": seed,
        "labels": list(LABELS),
        "input": {
            "entries": str(entries_path), "entries_sha256": _sha256(entries_path),
            "labels": str(labels_path), "labels_sha256": _sha256(labels_path),
        },
        "counts": counts,
        "split_counts": {name: len(rows) for name, rows in splits.items()},
        "split_releases": {name: sorted({row.release for row in rows}) for name, rows in splits.items()},
        "split_class_support": {name: dict(Counter(row.label for row in rows)) for name, rows in splits.items()},
        "evaluation": evaluations,
        "model": "word+character TF-IDF; balanced logistic regression, C=1.0",
        "selection": "Fixed parameters; no test-set tuning was performed.",
    }
    with (output_dir / "metrics.json").open("w", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, ensure_ascii=False)
    joblib.dump(model, output_dir / "model.joblib")
    return result

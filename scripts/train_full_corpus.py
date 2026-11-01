"""Train and audit the complete reviewed PatchProbe corpus.

The held-out model uses release-grouped train/dev/test data. Near-duplicate
evaluation rows that share a high-similarity pair with another split are
excluded before fitting or scoring; every exclusion remains in the manifest.
A separate serving model is fitted to all accepted labels after evaluation.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

import joblib
import numpy as np
from sklearn.dummy import DummyClassifier

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from audit_near_duplicates import find_pairs  # noqa: E402
from patchprobe.model import (  # noqa: E402
    LABELS,
    _metrics,
    _read_csv,
    _sha256,
    keyword_predict,
    load_labeled_examples,
    make_pipeline,
    reject_cross_split_duplicates,
)

THRESHOLD = 0.88
MANIFEST_COLUMNS = (
    "entry_id", "release", "split", "evaluation_role", "label", "source_url",
)
PREDICTION_COLUMNS = (
    "split", "entry_id", "release", "source_url", "text", "gold_label",
    "predicted_label", "max_probability_uncalibrated", "correct",
)

TRAIN_RELEASES = {"4.2", "5.0", "5.1"}
DEV_RELEASES = {"5.2", "5.2.1", "5.2.2", "5.2.3", "5.2.4", "5.2.5", "5.2.6", "5.2.7", "5.2.8"}
TEST_RELEASES = {"6.0", "6.0.1"}


def split_chronological(examples):
    """Freeze a meaningful-size chronological holdout by release family."""
    release_to_split = {
        **{release: "train" for release in TRAIN_RELEASES},
        **{release: "dev" for release in DEV_RELEASES},
        **{release: "test" for release in TEST_RELEASES},
    }
    unknown = sorted({row.release for row in examples} - set(release_to_split))
    if unknown:
        raise ValueError(f"Unassigned releases in frozen split: {unknown}")
    splits = {name: [] for name in ("train", "dev", "test")}
    for row in examples:
        splits[release_to_split[row.release]].append(row)
    return splits


def filter_cross_split_pairs(splits, pairs):
    """Keep train; remove test before dev for any pair spanning splits.

    This is a predeclared text-similarity policy. It does not inspect labels,
    model predictions, or test errors. A test/dev pair removes test; a
    train/dev or train/test pair removes the non-train member. Repeated passes
    handle a row appearing in multiple candidate pairs deterministically.
    """
    location = {
        row.entry_id: name for name, rows in splits.items() for row in rows
    }
    excluded: dict[str, str] = {}
    for pair in pairs:
        left, right = pair["left_id"], pair["right_id"]
        a, b = location.get(left), location.get(right)
        if not a or not b or a == b:
            continue
        if "test" in (a, b):
            victim = left if a == "test" else right
        else:
            victim = left if a == "dev" else right
        excluded.setdefault(victim, "cross_split_near_duplicate")
    filtered = {
        name: [row for row in rows if row.entry_id not in excluded]
        for name, rows in splits.items()
    }
    return filtered, excluded


def write_csv(path: Path, columns, rows) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def train_full_corpus(entries_path: Path, labels_path: Path, output_dir: Path) -> dict:
    examples, counts = load_labeled_examples(entries_path, labels_path)
    if len(examples) < 2:
        raise ValueError("Need at least two reviewed model examples")
    source_rows = _read_csv(entries_path, ("entry_id", "release", "text"))
    pairs = find_pairs(source_rows, THRESHOLD)
    raw_splits = split_chronological(examples)
    splits, excluded = filter_cross_split_pairs(raw_splits, pairs)
    reject_cross_split_duplicates(splits)
    if any(not splits[name] for name in ("train", "dev", "test")):
        raise ValueError("A split became empty after near-duplicate filtering")
    if len({row.label for row in splits["train"]}) < 2:
        raise ValueError("Training data has fewer than two classes")

    train = splits["train"]
    model = make_pipeline().fit([r.text for r in train], [r.label for r in train])
    majority = DummyClassifier(strategy="most_frequent").fit(
        np.zeros((len(train), 1)), [r.label for r in train]
    )
    evaluations = {}
    prediction_rows = []
    for split_name in ("dev", "test"):
        rows = splits[split_name]
        texts = [r.text for r in rows]
        truth = [r.label for r in rows]
        predicted = model.predict(texts).tolist()
        scores = model.predict_proba(texts).max(axis=1).tolist()
        for row, label, score in zip(rows, predicted, scores, strict=True):
            prediction_rows.append({
                "split": split_name, "entry_id": row.entry_id,
                "release": row.release, "source_url": row.source_url,
                "text": row.text, "gold_label": row.label,
                "predicted_label": label,
                "max_probability_uncalibrated": score,
                "correct": label == row.label,
            })
        evaluations[split_name] = {
            "model": _metrics(truth, predicted),
            "majority": _metrics(
                truth, majority.predict(np.zeros((len(rows), 1))).tolist()
            ),
            "keyword": _metrics(truth, [keyword_predict(t) for t in texts]),
        }

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for split_name, rows in raw_splits.items():
        for row in rows:
            manifest.append({
                "entry_id": row.entry_id, "release": row.release,
                "split": split_name,
                "evaluation_role": excluded.get(row.entry_id, "kept"),
                "label": row.label, "source_url": row.source_url,
            })
    write_csv(output_dir / "split_manifest.csv", MANIFEST_COLUMNS, manifest)
    write_csv(output_dir / "predictions.csv", PREDICTION_COLUMNS, prediction_rows)
    audit_rows = []
    location = {r.entry_id: n for n, rows in raw_splits.items() for r in rows}
    for pair in pairs:
        audit_rows.append({
            **pair,
            "left_split": location.get(pair["left_id"], "not_model_label"),
            "right_split": location.get(pair["right_id"], "not_model_label"),
            "excluded_id": next(
                (i for i in (pair["left_id"], pair["right_id"]) if i in excluded),
                "",
            ),
        })
    write_csv(
        output_dir / "near_duplicate_audit.csv",
        (*pairs[0].keys(), "left_split", "right_split", "excluded_id") if pairs
        else ("similarity", "left_id", "left_release", "left_text", "right_id", "right_release", "right_text", "left_split", "right_split", "excluded_id"),
        audit_rows,
    )

    support = {name: dict(Counter(r.label for r in rows)) for name, rows in splits.items()}
    incomplete = any(
        support[name].get(label, 0) < minimum
        for label in LABELS
        for name, minimum in (("train", 5), ("dev", 2), ("test", 5))
    )
    word = model.named_steps["tfidf"].transformer_list[0][1]
    char = model.named_steps["tfidf"].transformer_list[1][1]
    result = {
        "status": "pilot" if incomplete else "five_class_evaluation",
        "warning": "Sparse class support, especially No targeted check stated; this is a diagnostic grouped evaluation, not validated production quality." if incomplete else None,
        "split_strategy": "Frozen chronological release families: train 4.2/5.0/5.1; dev all 5.2.x; test 6.0/6.0.1",
        "seed": None,
        "labels": list(LABELS),
        "input": {
            "entries": str(entries_path), "entries_sha256": _sha256(entries_path),
            "labels": str(labels_path), "labels_sha256": _sha256(labels_path),
        },
        "counts": counts,
        "split_counts": {name: len(rows) for name, rows in splits.items()},
        "raw_split_counts": {name: len(rows) for name, rows in raw_splits.items()},
        "split_releases": {name: sorted({r.release for r in rows}) for name, rows in raw_splits.items()},
        "split_class_support": support,
        "near_duplicate_audit": {
            "threshold": THRESHOLD,
            "candidate_pairs_all_source_entries": len(pairs),
            "excluded_model_row_ids": sorted(excluded),
            "excluded_model_rows": len(excluded),
            "policy": "For a cross-split candidate pair, retain train; otherwise retain dev and exclude test. No labels or predictions used by this policy.",
        },
        "evaluation": evaluations,
        "feature_counts": {
            "word": len(word.vocabulary_), "character": len(char.vocabulary_),
            "total": len(word.vocabulary_) + len(char.vocabulary_),
        },
        "model": "word 1-2 gram plus char_wb 3-5 gram TF-IDF; balanced logistic regression C=1.0",
        "selection": "Fixed prior configuration. No held-out test tuning.",
    }
    (output_dir / "metrics.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    joblib.dump(model, output_dir / "model.joblib")

    serving_dir = output_dir / "serving"
    serving_dir.mkdir(exist_ok=True)
    serving_model = make_pipeline().fit(
        [r.text for r in examples], [r.label for r in examples]
    )
    joblib.dump(serving_model, serving_dir / "model.joblib")
    serving_metadata = {
        "purpose": "deployment inference, not held-out evaluation",
        "training_examples": len(examples),
        "trained_classes": list(serving_model.classes_),
        "input_sha256": result["input"],
        "evaluation_metrics_path": "../metrics.json",
    }
    (serving_dir / "metadata.json").write_text(
        json.dumps(serving_metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entries", type=Path, default=ROOT / "data/processed/entries.csv")
    parser.add_argument("--labels", type=Path, default=ROOT / "data/processed/reviewed_labels.csv")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "artifacts/model")
    args = parser.parse_args()
    try:
        result = train_full_corpus(args.entries, args.labels, args.output_dir)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Training stopped: {error}\n")
    print(json.dumps({
        "status": result["status"],
        "counts": result["counts"],
        "split_counts": result["split_counts"],
        "near_duplicate_audit": result["near_duplicate_audit"],
        "test_macro_f1_five_labels": result["evaluation"]["test"]["model"]["macro_f1_five_labels"],
        "output_dir": str(args.output_dir),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

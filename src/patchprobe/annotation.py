"""CSV-backed, human-controlled annotation for release-note entries.

This module intentionally contains no automated labeling. A row is only saved
after a reviewer makes an explicit choice in the interface.
"""

from __future__ import annotations

import csv
import os
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ENTRY_FIELDS = (
    "entry_id",
    "release",
    "source_url",
    "source_revision",
    "section_path",
    "raw_text",
    "text",
)
LABEL_FIELDS = ("entry_id", "label", "annotator", "review_note", "annotated_at")
LABEL_DEFINITIONS = {
    "API/code compatibility": "Python calls, imports, signatures, return values, exceptions, hooks, or integration code.",
    "Configuration/deployment": "Settings, middleware order, environment, runtime compatibility, packaging, or deployment behavior.",
    "Data/schema migration": "Database schema, ORM data semantics, migrations, data conversion, or persistent storage.",
    "UI/output behavior": "Rendered pages, templates, forms, admin display, responses, serialization, or user-visible output.",
    "No targeted check stated": "A substantive note that gives no concrete downstream behavior to verify from its text alone.",
}
UNCLEAR = "UNCLEAR"
ALL_CHOICES = tuple(LABEL_DEFINITIONS) + (UNCLEAR,)


class AnnotationError(ValueError):
    """The input data or an annotation is malformed."""


def _require_columns(fieldnames: list[str] | None, required: tuple[str, ...], path: Path) -> None:
    missing = set(required) - set(fieldnames or ())
    if missing:
        raise AnnotationError(f"{path} is missing columns: {', '.join(sorted(missing))}")


def load_entries(path: str | Path) -> list[dict[str, str]]:
    """Load the extraction output, preserving its order and provenance."""
    path = Path(path)
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        _require_columns(reader.fieldnames, ENTRY_FIELDS, path)
        rows = []
        seen = set()
        for line_number, row in enumerate(reader, start=2):
            entry_id = (row["entry_id"] or "").strip()
            if not entry_id:
                raise AnnotationError(f"{path}:{line_number} has an empty entry_id")
            if entry_id in seen:
                raise AnnotationError(f"{path}:{line_number} repeats entry_id {entry_id}")
            if not (row["text"] or "").strip():
                raise AnnotationError(f"{path}:{line_number} has empty model text")
            seen.add(entry_id)
            rows.append({field: row[field] or "" for field in ENTRY_FIELDS})
        return rows


def load_labels(path: str | Path, valid_entry_ids: set[str] | None = None) -> dict[str, dict[str, str]]:
    """Load reviewer decisions; a missing file represents no decisions yet."""
    path = Path(path)
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        _require_columns(reader.fieldnames, LABEL_FIELDS, path)
        labels = {}
        for line_number, row in enumerate(reader, start=2):
            entry_id = (row["entry_id"] or "").strip()
            label = row["label"] or ""
            if not entry_id or entry_id in labels:
                raise AnnotationError(f"{path}:{line_number} has an empty or duplicate entry_id")
            if valid_entry_ids is not None and entry_id not in valid_entry_ids:
                raise AnnotationError(f"{path}:{line_number} refers to unknown entry_id {entry_id}")
            if label not in ALL_CHOICES:
                raise AnnotationError(f"{path}:{line_number} has unknown label {label!r}")
            labels[entry_id] = {field: row[field] or "" for field in LABEL_FIELDS}
        return labels


def save_annotation(
    path: str | Path,
    *,
    entry_id: str,
    label: str,
    annotator: str,
    review_note: str = "",
    valid_entry_ids: set[str],
) -> None:
    """Save one explicit decision atomically, replacing any prior decision for the row."""
    path = Path(path)
    if entry_id not in valid_entry_ids:
        raise AnnotationError(f"Unknown entry_id: {entry_id}")
    if label not in ALL_CHOICES:
        raise AnnotationError(f"Unknown label: {label}")
    if not annotator.strip():
        raise AnnotationError("Enter the reviewer's name before saving")
    if label == UNCLEAR and not review_note.strip():
        raise AnnotationError("Explain why this row is UNCLEAR")

    labels = load_labels(path, valid_entry_ids)
    labels[entry_id] = {
        "entry_id": entry_id,
        "label": label,
        "annotator": annotator.strip(),
        "review_note": review_note.strip(),
        "annotated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", newline="", dir=path.parent, prefix=f".{path.stem}-", suffix=".tmp", delete=False
        ) as target:
            temporary_path = Path(target.name)
            writer = csv.DictWriter(target, fieldnames=LABEL_FIELDS)
            writer.writeheader()
            writer.writerows(labels.values())
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def progress(entries: list[dict[str, str]], labels: dict[str, dict[str, str]]) -> dict[str, object]:
    """Return counts for the review dashboard, separating UNCLEAR from model labels."""
    counts = Counter(row["label"] for row in labels.values())
    return {
        "total": len(entries),
        "reviewed": len(labels),
        "remaining": len(entries) - len(labels),
        "unclear": counts[UNCLEAR],
        "model_ready": sum(counts[label] for label in LABEL_DEFINITIONS),
        "by_label": {label: counts[label] for label in ALL_CHOICES},
    }


def next_unreviewed(
    entries: list[dict[str, str]], labels: dict[str, dict[str, str]], skipped_ids: set[str]
) -> dict[str, str] | None:
    """Pick the next unsaved row; skips are only for the current session."""
    return next(
        (row for row in entries if row["entry_id"] not in labels and row["entry_id"] not in skipped_ids),
        None,
    )

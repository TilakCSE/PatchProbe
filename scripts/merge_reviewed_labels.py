"""Merge shareable human-reviewed batches into one validated label CSV."""

from __future__ import annotations

import argparse
import csv
import os
import sys
import tempfile
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from patchprobe.annotation import LABEL_FIELDS, UNCLEAR, load_entries, load_labels  # noqa: E402


def merge_rows(files: list[Path], valid_ids: set[str]) -> list[dict[str, str]]:
    """Reject duplicate, malformed, or personally attributed public rows."""
    if not files:
        raise ValueError("No reviewed batch exports found")
    merged: list[dict[str, str]] = []
    seen: dict[str, Path] = {}
    for path in files:
        for entry_id, row in load_labels(path, valid_ids).items():
            if entry_id in seen:
                raise ValueError(f"Duplicate {entry_id} in {seen[entry_id]} and {path}")
            if not row["annotator"].startswith("Human reviewer"):
                raise ValueError(f"{path}: {entry_id} has a non-anonymized annotator")
            if not row["annotated_at"] or not row["review_note"].strip():
                raise ValueError(f"{path}: {entry_id} lacks a date or review note")
            if row["label"] == UNCLEAR and not row["review_note"].strip():
                raise ValueError(f"{path}: {entry_id} needs an UNCLEAR reason")
            seen[entry_id] = path
            merged.append(row)
    return merged


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entries", type=Path, default=PROJECT_ROOT / "data/processed/entries.csv")
    parser.add_argument("--labels-dir", type=Path, default=PROJECT_ROOT / "data/processed")
    parser.add_argument("--output", type=Path, default=PROJECT_ROOT / "data/processed/reviewed_labels.csv")
    args = parser.parse_args()
    valid_ids = {row["entry_id"] for row in load_entries(args.entries)}
    files = sorted(args.labels_dir.glob("*_reviewed_labels.csv"))
    rows = merge_rows(files, valid_ids)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", dir=args.output.parent, prefix=".reviewed-labels-", suffix=".tmp", delete=False) as target:
            temporary = Path(target.name)
            writer = csv.DictWriter(target, fieldnames=LABEL_FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary, args.output)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    counts = Counter(row["label"] for row in rows)
    print(f"Merged {len(rows)} reviewed rows from {len(files)} exports; {counts[UNCLEAR]} UNCLEAR; {len(rows) - counts[UNCLEAR]} model-usable")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

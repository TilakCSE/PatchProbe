"""Validate full annotation coverage and join decisions with source provenance."""

from __future__ import annotations

import argparse
import csv
import os
import sys
import tempfile
from collections import Counter
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from patchprobe.annotation import ENTRY_FIELDS, LABEL_DEFINITIONS, UNCLEAR, load_entries, load_labels  # noqa: E402

EXCLUSION_FIELDS = ("entry_id", "reason", "reviewed_at")
OUTPUT_FIELDS = (*ENTRY_FIELDS, "review_decision", "model_label", "review_note", "reviewed_at")
EXCLUDE = "EXCLUDE"


def load_exclusions(path: Path, valid_ids: set[str]) -> dict[str, dict[str, str]]:
    """Require traceable, date-stamped exclusions and reject unknown or repeated IDs."""
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if set(reader.fieldnames or ()) != set(EXCLUSION_FIELDS):
            raise ValueError(f"{path}: expected columns {EXCLUSION_FIELDS}")
        exclusions: dict[str, dict[str, str]] = {}
        for line_number, row in enumerate(reader, 2):
            entry_id = (row["entry_id"] or "").strip()
            reason = (row["reason"] or "").strip()
            reviewed_at = (row["reviewed_at"] or "").strip()
            if entry_id not in valid_ids or entry_id in exclusions:
                raise ValueError(f"{path}:{line_number}: unknown or duplicate entry_id {entry_id!r}")
            if not reason:
                raise ValueError(f"{path}:{line_number}: exclusion needs a reason")
            try:
                date.fromisoformat(reviewed_at)
            except ValueError as error:
                raise ValueError(f"{path}:{line_number}: invalid reviewed_at date") from error
            exclusions[entry_id] = {"entry_id": entry_id, "reason": reason, "reviewed_at": reviewed_at}
    return exclusions


def build_rows(
    entries: list[dict[str, str]],
    labels: dict[str, dict[str, str]],
    exclusions: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    """Require exactly one label, UNCLEAR state, or exclusion per source entry."""
    source_ids = {row["entry_id"] for row in entries}
    label_ids = set(labels)
    exclusion_ids = set(exclusions)
    if len(source_ids) != len(entries):
        raise ValueError("Source entries contain duplicate IDs")
    if (label_ids | exclusion_ids) - source_ids:
        raise ValueError("Decisions reference unknown source IDs")
    overlap = label_ids & exclusion_ids
    if overlap:
        raise ValueError(f"Label and exclusion overlap: {sorted(overlap)[:5]}")
    missing = source_ids - label_ids - exclusion_ids
    if missing:
        raise ValueError(f"Missing decisions for {len(missing)} source IDs: {sorted(missing)[:5]}")
    output = []
    for entry in entries:
        entry_id = entry["entry_id"]
        if entry_id in exclusions:
            decision = EXCLUDE
            model_label = ""
            note = exclusions[entry_id]["reason"]
            reviewed_at = exclusions[entry_id]["reviewed_at"]
        else:
            reviewed = labels[entry_id]
            decision = reviewed["label"]
            if decision not in (*LABEL_DEFINITIONS, UNCLEAR):
                raise ValueError(f"Invalid reviewed decision for {entry_id}: {decision}")
            model_label = decision if decision in LABEL_DEFINITIONS else ""
            note = reviewed["review_note"]
            reviewed_at = reviewed["annotated_at"]
        output.append({**{field: entry[field] for field in ENTRY_FIELDS},
                       "review_decision": decision, "model_label": model_label,
                       "review_note": note, "reviewed_at": reviewed_at})
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entries", type=Path, default=PROJECT_ROOT / "data/processed/entries.csv")
    parser.add_argument("--labels", type=Path, default=PROJECT_ROOT / "data/processed/reviewed_labels.csv")
    parser.add_argument("--exclusions", type=Path, default=PROJECT_ROOT / "data/processed/excluded_entries.csv")
    parser.add_argument("--output", type=Path, default=PROJECT_ROOT / "data/processed/annotated_corpus.csv")
    args = parser.parse_args()
    entries = load_entries(args.entries)
    valid_ids = {row["entry_id"] for row in entries}
    labels = load_labels(args.labels, valid_ids)
    exclusions = load_exclusions(args.exclusions, valid_ids)
    rows = build_rows(entries, labels, exclusions)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", dir=args.output.parent,
                                         prefix=".annotated-corpus-", suffix=".tmp", delete=False) as target:
            temporary = Path(target.name)
            writer = csv.DictWriter(target, fieldnames=OUTPUT_FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary, args.output)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    counts = Counter(row["review_decision"] for row in rows)
    print(f"Audited {len(rows)} source IDs: {sum(counts[label] for label in LABEL_DEFINITIONS)} model labels, "
          f"{counts[UNCLEAR]} UNCLEAR, {counts[EXCLUDE]} EXCLUDE")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

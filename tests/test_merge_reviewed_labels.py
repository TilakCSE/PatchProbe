"""Merged labels must be traceable, unique, and safe to publish."""

from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from merge_reviewed_labels import merge_rows  # noqa: E402


class MergeReviewedLabelsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT)
        self.addCleanup(self.temporary.cleanup)
        self.folder = Path(self.temporary.name)

    def write(self, name: str, entry_id: str, *, annotator: str = "Human reviewer", label: str = "API/code compatibility") -> Path:
        path = self.folder / name
        with path.open("w", encoding="utf-8", newline="") as target:
            writer = csv.DictWriter(target, fieldnames=("entry_id", "label", "annotator", "review_note", "annotated_at"))
            writer.writeheader()
            writer.writerow({"entry_id": entry_id, "label": label, "annotator": annotator, "review_note": "Human confirmed", "annotated_at": "2026-10-28"})
        return path

    def test_merges_distinct_reviewed_rows(self) -> None:
        first = self.write("first.csv", "e-1")
        second = self.write("second.csv", "e-2", label="UNCLEAR")
        self.assertEqual([row["entry_id"] for row in merge_rows([first, second], {"e-1", "e-2"})], ["e-1", "e-2"])

    def test_rejects_duplicate_ids_and_named_public_export(self) -> None:
        first = self.write("first.csv", "e-1")
        duplicate = self.write("duplicate.csv", "e-1")
        with self.assertRaisesRegex(ValueError, "Duplicate e-1"):
            merge_rows([first, duplicate], {"e-1"})
        named = self.write("named.csv", "e-2", annotator="Named reviewer")
        with self.assertRaisesRegex(ValueError, "non-anonymized annotator"):
            merge_rows([named], {"e-2"})


if __name__ == "__main__":
    unittest.main()

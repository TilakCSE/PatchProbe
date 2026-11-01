"""Full-corpus output must not silently omit or double-count source entries."""

from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_annotated_corpus import build_rows, load_exclusions  # noqa: E402


class AnnotatedCorpusTests(unittest.TestCase):
    def setUp(self) -> None:
        self.entries = [{"entry_id": entry_id, "release": "5.0", "source_url": "url",
                         "source_revision": "rev", "section_path": "section", "raw_text": "raw",
                         "text": "clean"} for entry_id in ("e-1", "e-2", "e-3")]
        self.labels = {
            "e-1": {"label": "API/code compatibility", "review_note": "code", "annotated_at": "2026-11-01"},
            "e-2": {"label": "UNCLEAR", "review_note": "mixed", "annotated_at": "2026-11-01"},
        }
        self.exclusions = {"e-3": {"entry_id": "e-3", "reason": "fragment", "reviewed_at": "2026-11-01"}}

    def test_builds_all_three_dispositions_in_source_order(self) -> None:
        rows = build_rows(self.entries, self.labels, self.exclusions)
        self.assertEqual([row["entry_id"] for row in rows], ["e-1", "e-2", "e-3"])
        self.assertEqual([row["review_decision"] for row in rows],
                         ["API/code compatibility", "UNCLEAR", "EXCLUDE"])
        self.assertEqual([row["model_label"] for row in rows], ["API/code compatibility", "", ""])

    def test_rejects_missing_and_overlapping_decisions(self) -> None:
        with self.assertRaisesRegex(ValueError, "Missing decisions"):
            build_rows(self.entries, self.labels, {})
        with self.assertRaisesRegex(ValueError, "overlap"):
            build_rows(self.entries, self.labels, {"e-2": self.exclusions["e-3"]})

    def test_exclusions_need_known_id_reason_and_date(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "exclusions.csv"
            def write(entry_id: str, reason: str, reviewed_at: str) -> None:
                with path.open("w", encoding="utf-8", newline="") as target:
                    writer = csv.DictWriter(target, fieldnames=("entry_id", "reason", "reviewed_at"))
                    writer.writeheader()
                    writer.writerow({"entry_id": entry_id, "reason": reason, "reviewed_at": reviewed_at})
            write("e-3", "fragment", "2026-11-01")
            self.assertEqual(len(load_exclusions(path, {"e-3"})), 1)
            write("unknown", "fragment", "2026-11-01")
            with self.assertRaisesRegex(ValueError, "unknown or duplicate"):
                load_exclusions(path, {"e-3"})
            write("e-3", "", "2026-11-01")
            with self.assertRaisesRegex(ValueError, "needs a reason"):
                load_exclusions(path, {"e-3"})
            write("e-3", "fragment", "bad-date")
            with self.assertRaisesRegex(ValueError, "invalid reviewed_at"):
                load_exclusions(path, {"e-3"})


if __name__ == "__main__":
    unittest.main()

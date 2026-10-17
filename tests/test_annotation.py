"""Focused checks for human label persistence and review accounting."""

from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from patchprobe.annotation import (  # noqa: E402
    ENTRY_FIELDS,
    LABEL_FIELDS,
    UNCLEAR,
    AnnotationError,
    load_entries,
    load_labels,
    next_unreviewed,
    progress,
    save_annotation,
)


class AnnotationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1])
        self.addCleanup(self.temporary.cleanup)
        self.folder = Path(self.temporary.name)
        self.entries_path = self.folder / "entries.csv"
        self.labels_path = self.folder / "labels.csv"
        self.rows = [
            {
                "entry_id": f"e-{number}",
                "release": "5.2",
                "source_url": "https://docs.djangoproject.com/en/5.2/releases/5.2/",
                "source_revision": "abc123",
                "section_path": "Backwards incompatible changes",
                "raw_text": f"Note {number}",
                "text": f"Note {number}",
            }
            for number in range(1, 4)
        ]
        self._write_entries(self.rows)

    def _write_entries(self, rows: list[dict[str, str]], fields=ENTRY_FIELDS) -> None:
        with self.entries_path.open("w", encoding="utf-8", newline="") as target:
            writer = csv.DictWriter(target, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    def test_load_entries_preserves_order_and_rejects_duplicates(self) -> None:
        self.assertEqual([row["entry_id"] for row in load_entries(self.entries_path)], ["e-1", "e-2", "e-3"])
        self._write_entries(self.rows + [self.rows[0]])
        with self.assertRaisesRegex(AnnotationError, "repeats entry_id"):
            load_entries(self.entries_path)

    def test_entry_schema_is_required(self) -> None:
        self._write_entries(self.rows, fields=ENTRY_FIELDS[:-1])
        with self.assertRaisesRegex(AnnotationError, "missing columns: text"):
            load_entries(self.entries_path)

    def test_save_is_explicit_and_can_resume(self) -> None:
        valid_ids = {row["entry_id"] for row in self.rows}
        self.assertFalse(self.labels_path.exists())
        self.assertEqual(load_labels(self.labels_path, valid_ids), {})
        self.assertFalse(self.labels_path.exists())
        save_annotation(
            self.labels_path,
            entry_id="e-1",
            label="API/code compatibility",
            annotator="Tilak",
            valid_entry_ids=valid_ids,
        )
        saved = load_labels(self.labels_path, valid_ids)
        self.assertEqual(set(saved), {"e-1"})
        self.assertEqual(saved["e-1"]["annotator"], "Tilak")
        self.assertTrue(saved["e-1"]["annotated_at"])
        with self.labels_path.open(encoding="utf-8", newline="") as source:
            self.assertEqual(tuple(csv.DictReader(source).fieldnames), LABEL_FIELDS)
        self.assertEqual(next_unreviewed(self.rows, saved, set())["entry_id"], "e-2")
        self.assertEqual(next_unreviewed(self.rows, saved, {"e-2"})["entry_id"], "e-3")

    def test_unclear_requires_reason_and_is_not_model_ready(self) -> None:
        valid_ids = {row["entry_id"] for row in self.rows}
        with self.assertRaisesRegex(AnnotationError, "Explain why"):
            save_annotation(
                self.labels_path,
                entry_id="e-1",
                label=UNCLEAR,
                annotator="Tilak",
                valid_entry_ids=valid_ids,
            )
        self.assertFalse(self.labels_path.exists())
        save_annotation(
            self.labels_path,
            entry_id="e-1",
            label=UNCLEAR,
            annotator="Tilak",
            review_note="Two check areas equally primary.",
            valid_entry_ids=valid_ids,
        )
        counts = progress(self.rows, load_labels(self.labels_path, valid_ids))
        self.assertEqual((counts["reviewed"], counts["unclear"], counts["model_ready"], counts["remaining"]), (1, 1, 0, 2))

    def test_revising_saved_decision_replaces_row(self) -> None:
        valid_ids = {row["entry_id"] for row in self.rows}
        for label in (UNCLEAR, "UI/output behavior"):
            save_annotation(
                self.labels_path,
                entry_id="e-1",
                label=label,
                annotator="Tilak",
                review_note="Ambiguous" if label == UNCLEAR else "Rechecked source.",
                valid_entry_ids=valid_ids,
            )
        saved = load_labels(self.labels_path, valid_ids)
        self.assertEqual(len(saved), 1)
        self.assertEqual(saved["e-1"]["label"], "UI/output behavior")

    def test_unknown_entry_cannot_be_saved(self) -> None:
        with self.assertRaisesRegex(AnnotationError, "Unknown entry_id"):
            save_annotation(
                self.labels_path,
                entry_id="missing",
                label="UI/output behavior",
                annotator="Tilak",
                valid_entry_ids={"e-1"},
            )
        self.assertFalse(self.labels_path.exists())


if __name__ == "__main__":
    unittest.main()

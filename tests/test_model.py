"""Synthetic fixtures test mechanics only; they are not model evaluation data."""

from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import joblib

from patchprobe.model import LABELS, Example, load_labeled_examples, reject_cross_split_duplicates, split_by_release, train_and_evaluate


def write_csv(path: Path, columns: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


class ModelTest(unittest.TestCase):
    def test_join_excludes_unclear_and_uses_text_only(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            entries = root / "entries.csv"
            labels = root / "labels.csv"
            write_csv(entries,
                ("entry_id", "release", "source_url", "source_revision", "section_path", "raw_text", "text"),
                [
                    {"entry_id": "one", "release": "1.0", "source_url": "https://example.org/1", "source_revision": "abc", "section_path": "LEAKAGE HEADING", "raw_text": "Raw", "text": "Function argument changed"},
                    {"entry_id": "two", "release": "2.0", "source_url": "https://example.org/2", "source_revision": "abc", "section_path": "Configuration", "raw_text": "Raw", "text": "Both interfaces changed"},
                ])
            write_csv(labels, ("entry_id", "label", "annotator", "review_note", "annotated_at"), [
                {"entry_id": "one", "label": LABELS[0], "annotator": "human", "review_note": "", "annotated_at": "2026-10-17"},
                {"entry_id": "two", "label": "UNCLEAR", "annotator": "human", "review_note": "mixed", "annotated_at": "2026-10-17"},
            ])
            result, counts = load_labeled_examples(entries, labels)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].text, "Function argument changed")
            self.assertEqual(counts["unclear"], 1)
            self.assertEqual(counts["accepted"], 1)

    def test_release_split_is_disjoint_and_reproducible(self) -> None:
        rows = [Example(str(i), str(i // 2), "url", f"text {i}", LABELS[i % 5]) for i in range(20)]
        a = split_by_release(rows, 42)
        b = split_by_release(rows, 42)
        self.assertEqual({k: [r.entry_id for r in v] for k, v in a.items()}, {k: [r.entry_id for r in v] for k, v in b.items()})
        releases = [{r.release for r in rows} for rows in a.values()]
        self.assertFalse(releases[0] & releases[1])
        self.assertFalse(releases[0] & releases[2])
        self.assertFalse(releases[1] & releases[2])

    def test_cross_split_duplicate_is_rejected(self) -> None:
        splits = {
            "train": [Example("a", "1", "url", "Same  note", LABELS[0])],
            "dev": [Example("b", "2", "url", "same note", LABELS[0])],
            "test": [],
        }
        with self.assertRaisesRegex(ValueError, "Cross-split duplicate"):
            reject_cross_split_duplicates(splits)

    def test_synthetic_end_to_end_keeps_test_vocabulary_out_of_fit(self) -> None:
        # This tests mechanics only; the synthetic examples do not estimate NLP quality.
        phrases = (
            "Function parameter changed",
            "Setting middleware changed",
            "Database schema migration changed",
            "Template display changed",
            "Internal cleanup changed",
        )
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            entry_rows = []
            label_rows = []
            for release in range(5):
                for index, label in enumerate(LABELS):
                    entry_id = f"r{release}-{index}"
                    entry_rows.append({
                        "entry_id": entry_id, "release": str(release),
                        "source_url": f"https://example.org/{entry_id}", "source_revision": "abc",
                        "section_path": "headingleakmarker", "raw_text": "Raw",
                        "text": f"{phrases[index]} releasemarker{release} item{index}",
                    })
                    label_rows.append({"entry_id": entry_id, "label": label, "annotator": "synthetic-test-fixture", "review_note": "", "annotated_at": "2026-10-17"})
            write_csv(root / "entries.csv", ("entry_id", "release", "source_url", "source_revision", "section_path", "raw_text", "text"), entry_rows)
            write_csv(root / "labels.csv", ("entry_id", "label", "annotator", "review_note", "annotated_at"), label_rows)
            result = train_and_evaluate(root / "entries.csv", root / "labels.csv", root / "artifacts")
            self.assertEqual(result["status"], "pilot")
            self.assertEqual(sum(result["split_counts"].values()), 25)
            self.assertEqual(len(result["evaluation"]["test"]["model"]["confusion_matrix"]), 5)
            self.assertTrue((root / "artifacts" / "split_manifest.csv").exists())
            with (root / "artifacts" / "predictions.csv").open(encoding="utf-8", newline="") as stream:
                prediction_rows = list(csv.DictReader(stream))
            self.assertEqual(len(prediction_rows), 10)
            self.assertEqual(json.loads((root / "artifacts" / "metrics.json").read_text(encoding="utf-8"))["seed"], 42)
            fitted = joblib.load(root / "artifacts" / "model.joblib")
            vocabulary = fitted.named_steps["tfidf"].transformer_list[0][1].vocabulary_
            self.assertNotIn("headingleakmarker", vocabulary)
            for release in result["split_releases"]["test"]:
                self.assertNotIn(f"releasemarker{release}", vocabulary)

    def test_training_rejects_absent_human_labels(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            write_csv(root / "entries.csv", ("entry_id", "release", "source_url", "source_revision", "section_path", "raw_text", "text"), [])
            write_csv(root / "labels.csv", ("entry_id", "label", "annotator", "review_note", "annotated_at"), [])
            with self.assertRaisesRegex(ValueError, "No human-labeled"):
                train_and_evaluate(root / "entries.csv", root / "labels.csv", root / "artifacts")
            self.assertFalse((root / "artifacts").exists())

    def test_rejects_unreviewed_or_unknown_labels(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            write_csv(root / "entries.csv", ("entry_id", "release", "source_url", "source_revision", "section_path", "raw_text", "text"), [
                {"entry_id": "one", "release": "1", "source_url": "", "source_revision": "", "section_path": "", "raw_text": "", "text": "Some text"}])
            columns = ("entry_id", "label", "annotator", "review_note", "annotated_at")
            write_csv(root / "labels.csv", columns, [{"entry_id": "one", "label": LABELS[0], "annotator": "", "review_note": "", "annotated_at": ""}])
            with self.assertRaisesRegex(ValueError, "Missing human annotator"):
                load_labeled_examples(root / "entries.csv", root / "labels.csv")
            write_csv(root / "labels.csv", columns, [{"entry_id": "one", "label": "not a class", "annotator": "human", "review_note": "", "annotated_at": ""}])
            with self.assertRaisesRegex(ValueError, "Unknown label"):
                load_labeled_examples(root / "entries.csv", root / "labels.csv")


if __name__ == "__main__":
    unittest.main()

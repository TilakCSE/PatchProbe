"""Contract tests for guarded local inference and pilot class scores."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from patchprobe.inference import (  # noqa: E402
    EXPECTED_LABELS,
    InferenceError,
    artifact_status,
    load_local_model,
    predict_review,
)


class FakeModel:
    classes_ = ("API/code compatibility", "UI/output behavior")

    def predict_proba(self, values):
        assert len(values) == 1
        return [[0.2, 0.8]]

    def predict(self, values):
        assert len(values) == 1
        return ["UI/output behavior"]


class InferenceTests(unittest.TestCase):
    def test_missing_artifact_never_loads_a_model(self) -> None:
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as folder:
            root = Path(folder)
            status = artifact_status(root)
            self.assertFalse(status.available)
            self.assertIn("No trained model", status.reason)
            with self.assertRaisesRegex(InferenceError, "No trained model"):
                load_local_model(root)

    def test_requires_complete_matching_training_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as folder:
            root = Path(folder)
            output = root / "artifacts" / "model"
            output.mkdir(parents=True)
            (output / "model.joblib").write_bytes(b"not loaded by this test")
            self.assertIn("incomplete", artifact_status(root).reason)
            (output / "metrics.json").write_text(
                json.dumps({"status": "pilot", "labels": ["wrong class"]}), encoding="utf-8"
            )
            self.assertFalse(artifact_status(root).available)
            (output / "metrics.json").write_text(
                json.dumps({"status": "pilot", "labels": list(EXPECTED_LABELS)}), encoding="utf-8"
            )
            self.assertTrue(artifact_status(root).available)

    def test_pilot_prediction_marks_untrained_classes_without_fake_zero_scores(self) -> None:
        result = predict_review(FakeModel(), "  The admin   form now displays differently. ")
        self.assertEqual(result.predicted_label, "UI/output behavior")
        self.assertEqual(list(result.scores), list(EXPECTED_LABELS))
        self.assertEqual(result.scores["API/code compatibility"], 0.2)
        self.assertEqual(result.scores["UI/output behavior"], 0.8)
        self.assertIsNone(result.scores["Data/schema migration"])
        self.assertEqual(len(result.trained_classes), 2)

    def test_real_saved_pipeline_can_be_reviewed(self) -> None:
        import joblib
        from patchprobe.model import make_pipeline

        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as folder:
            root = Path(folder)
            output = root / "artifacts" / "model"
            output.mkdir(parents=True)
            model = make_pipeline().fit(
                [
                    "The function accepts a new argument.",
                    "The API method returns an exception.",
                    "The admin form displays a new field.",
                    "The template renders a different response.",
                ],
                ["API/code compatibility"] * 2 + ["UI/output behavior"] * 2,
            )
            joblib.dump(model, output / "model.joblib")
            (output / "metrics.json").write_text(
                json.dumps({"status": "pilot", "labels": list(EXPECTED_LABELS)}), encoding="utf-8"
            )
            prediction = predict_review(load_local_model(root), "The function now has an argument.")
            self.assertIn(prediction.predicted_label, model.classes_)
            self.assertEqual(len(prediction.trained_classes), 2)
            self.assertIsNone(prediction.scores["Data/schema migration"])
    def test_rejects_empty_input_and_invalid_model_contract(self) -> None:
        with self.assertRaisesRegex(InferenceError, "Enter a release-note"):
            predict_review(FakeModel(), " \n ")

        class UnknownClass(FakeModel):
            classes_ = ("API/code compatibility", "invented")

        with self.assertRaisesRegex(InferenceError, "label contract"):
            predict_review(UnknownClass(), "Function changed")

        class InvalidScores(FakeModel):
            def predict_proba(self, values):
                return [[0.2, 0.2]]

        with self.assertRaisesRegex(InferenceError, "sum to one"):
            predict_review(InvalidScores(), "Function changed")


if __name__ == "__main__":
    unittest.main()

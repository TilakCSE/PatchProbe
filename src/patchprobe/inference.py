"""Guarded local inference for the presentation review screen.

Serialized models are loaded only from the project's fixed training output.
The caller must still trust the local checkout and its generated artifacts.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from patchprobe.annotation import LABEL_DEFINITIONS


MODEL_RELATIVE_PATH = Path("artifacts/model/model.joblib")
METRICS_RELATIVE_PATH = Path("artifacts/model/metrics.json")
EXPECTED_LABELS = tuple(LABEL_DEFINITIONS)


class InferenceError(ValueError):
    """The local model artifact or its inference output is unusable."""


@dataclass(frozen=True)
class ArtifactStatus:
    available: bool
    reason: str
    metrics: dict[str, Any] | None = None


@dataclass(frozen=True)
class ReviewPrediction:
    predicted_label: str
    scores: dict[str, float | None]
    trained_classes: tuple[str, ...]


def _has_symlink_component(root: Path, relative_path: Path) -> bool:
    current = root
    for part in relative_path.parts:
        current = current / part
        if current.is_symlink():
            return True
    return False


def artifact_status(project_root: Path) -> ArtifactStatus:
    """Check the fixed local training output before exposing prediction mode."""
    root = Path(project_root)
    if _has_symlink_component(root, MODEL_RELATIVE_PATH) or _has_symlink_component(root, METRICS_RELATIVE_PATH):
        return ArtifactStatus(False, "The model artifact path contains a symbolic link; refusing to load it.")
    model_path = root / MODEL_RELATIVE_PATH
    metrics_path = root / METRICS_RELATIVE_PATH
    if not model_path.is_file():
        return ArtifactStatus(
            False,
            "No trained model is present yet. Review entries, then run the documented training command to create artifacts/model/model.joblib.",
        )
    if not metrics_path.is_file():
        return ArtifactStatus(False, "The model file exists, but its metrics.json is missing; training output is incomplete.")
    try:
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return ArtifactStatus(False, "The local metrics.json cannot be read; training output is incomplete.")
    if not isinstance(metrics, dict) or metrics.get("labels") != list(EXPECTED_LABELS):
        return ArtifactStatus(False, "The local metrics.json does not match PatchProbe's five-label contract.")
    if metrics.get("status") not in {"pilot", "five_class_evaluation"}:
        return ArtifactStatus(False, "The local metrics.json has an unrecognized evaluation status.")
    return ArtifactStatus(True, "Local trained model and metrics are available.", metrics)


def load_local_model(project_root: Path) -> Any:
    """Load only the fixed project artifact after its companion metrics pass checks."""
    status = artifact_status(project_root)
    if not status.available:
        raise InferenceError(status.reason)
    import joblib  # Imported only when a local artifact is ready.

    model = joblib.load(Path(project_root) / MODEL_RELATIVE_PATH)
    if not hasattr(model, "predict") or not hasattr(model, "predict_proba") or not hasattr(model, "classes_"):
        raise InferenceError("The local artifact is not a fitted classifier with class scores.")
    return model


def predict_review(model: Any, text: str) -> ReviewPrediction:
    """Return every class score; use None for classes absent from pilot training."""
    clean_text = " ".join(text.split())
    if not clean_text:
        raise InferenceError("Enter a release-note sentence or paragraph before predicting.")
    classes = tuple(str(label) for label in model.classes_)
    if len(classes) < 2 or len(set(classes)) != len(classes) or any(label not in EXPECTED_LABELS for label in classes):
        raise InferenceError("Model classes do not match the PatchProbe label contract.")
    probability_rows = model.predict_proba([clean_text])
    if len(probability_rows) != 1 or len(probability_rows[0]) != len(classes):
        raise InferenceError("Model returned the wrong number of class scores.")
    values = [float(value) for value in probability_rows[0]]
    if any(not math.isfinite(value) or value < 0 or value > 1 for value in values):
        raise InferenceError("Model returned an invalid class score.")
    if not math.isclose(sum(values), 1.0, abs_tol=1e-3):
        raise InferenceError("Model class scores do not sum to one.")
    predictions = model.predict([clean_text])
    if len(predictions) != 1 or str(predictions[0]) not in classes:
        raise InferenceError("Model returned a label outside its trained classes.")
    present = dict(zip(classes, values, strict=True))
    scores = {label: present.get(label) for label in EXPECTED_LABELS}
    return ReviewPrediction(str(predictions[0]), scores, classes)

"""The deployable Node implementation must match sklearn probabilities."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

from patchprobe.model import LABELS, make_pipeline
from scripts.export_portal_model import export_model


ROOT = Path(__file__).resolve().parents[1]
NODE_MODULE = ROOT / "portal/src/lib/portable-inference.mjs"


def test_node_probabilities_match_sklearn(tmp_path: Path) -> None:
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js unavailable")
    training = [
        "The function now accepts an optional argument.",
        "The API method returns a different error.",
        "Set the cache option in your deployment configuration.",
        "The environment package minimum version has changed.",
        "A migration changes the database column type.",
        "Run the schema migration for stored records.",
        "The admin form now renders a different label.",
        "The HTML response displays the new value.",
        "Internal documentation has been clarified.",
        "A minor note now has a clearer description.",
    ]
    labels = [label for label in LABELS for _ in range(2)]
    model = make_pipeline().fit(training, labels)
    payload = export_model(model, version="test", trained_on="synthetic test rows",
                           warning="test only", model_sha256="0" * 64)
    model_path = tmp_path / "model.json"
    model_path.write_text(json.dumps(payload), encoding="utf-8")
    notes = [
        "The API method accepts a new parameter.",
        "Run schema migration after upgrading.",
        "  The admin   HTML response changed.  ",
        "Django's make_random_password() is deprecated.",
        "SQL XOR (^), SQLite transaction_mode, and café.",
        "No targeted action is stated.",
    ]
    script = """
import fs from 'node:fs';
const {predictWithModel,validateModel}=await import(process.argv[2]);
const model=JSON.parse(fs.readFileSync(process.argv[1],'utf8'));
validateModel(model);
const notes=JSON.parse(fs.readFileSync(0,'utf8'));
process.stdout.write(JSON.stringify(notes.map(note=>predictWithModel(model,note))));
"""
    result = subprocess.run([node, "--input-type=module", "-e", script,
                             str(model_path), NODE_MODULE.as_uri()],
                            input=json.dumps(notes), text=True, capture_output=True, check=True)
    observed = json.loads(result.stdout)
    expected = model.predict_proba(notes)
    for row_index, prediction in enumerate(observed):
        assert prediction["label"] == model.predict([notes[row_index]])[0]
        actual_scores = [prediction["scores"][str(label)] for label in model.classes_]
        np.testing.assert_allclose(actual_scores, expected[row_index], rtol=0, atol=1e-10)


def test_export_rejects_wrong_pipeline() -> None:
    with pytest.raises(ValueError, match="Expected PatchProbe pipeline"):
        export_model(object(), version="test", trained_on="test", warning="test",
                     model_sha256="0" * 64)

"""Compare the shipped Node predictor with the exact local sklearn serving model."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from pathlib import Path

import joblib
import numpy as np


def read_texts(path: Path, column: str) -> list[str]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if column not in (reader.fieldnames or ()):
            raise ValueError(f"{path} does not contain {column!r}")
        return [row[column].strip() for row in reader if row[column].strip()]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=root / "artifacts/model/serving/model.joblib")
    parser.add_argument("--export", type=Path, default=root / "portal/src/lib/model.generated.json")
    parser.add_argument("--corpus", type=Path, default=root / "data/processed/annotated_corpus.csv")
    parser.add_argument("--extra-csv", type=Path)
    parser.add_argument("--extra-column", default="text")
    args = parser.parse_args()
    model = joblib.load(args.model)
    exported = json.loads(args.export.read_text(encoding="utf-8"))
    notes = read_texts(args.corpus, "text")
    if args.extra_csv:
        notes.extend(read_texts(args.extra_csv, args.extra_column))
    if not notes:
        raise ValueError("No notes to compare")
    script = """
import fs from 'node:fs';
const {predictWithModel,validateModel}=await import(process.argv[2]);
const model=JSON.parse(fs.readFileSync(process.argv[1],'utf8'));
validateModel(model);
const notes=JSON.parse(fs.readFileSync(0,'utf8'));
process.stdout.write(JSON.stringify(notes.map(note=>predictWithModel(model,note))));
"""
    result = subprocess.run(["node", "--input-type=module", "-e", script,
                             str(args.export), (root / "portal/src/lib/portable-inference.mjs").as_uri()],
                            input=json.dumps(notes), text=True, capture_output=True, check=True)
    observed = json.loads(result.stdout)
    expected = model.predict_proba(notes)
    actual = np.array([[row["scores"][str(label)] for label in model.classes_] for row in observed])
    max_difference = float(np.max(np.abs(expected - actual)))
    predicted = [row["label"] for row in observed]
    agreement = sum(a == b for a, b in zip(predicted, model.predict(notes), strict=True))
    print(json.dumps({"notes": len(notes), "label_agreement": agreement,
                      "max_probability_difference": max_difference,
                      "model_sha256": exported["model"]["sha256"]}, indent=2))
    if agreement != len(notes) or max_difference > 1e-9:
        raise SystemExit("Python–Node parity failed")


if __name__ == "__main__":
    main()

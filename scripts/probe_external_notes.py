"""Run a qualitative transfer probe on source-linked non-Django notes.

Reference labels in this file are agent-proposed interpretations, not an
independent human gold set. Agreement is descriptive only.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

import joblib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from patchprobe.model import LABELS  # noqa: E402


def run_probe(model_path: Path, input_path: Path, output_path: Path) -> dict:
    with input_path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows or any(
        not row.get(key, "").strip()
        for row in rows
        for key in ("probe_id", "product", "source_url", "text", "proposed_reference_label")
    ):
        raise ValueError("Probe CSV has missing required fields or no rows")
    if len({r["probe_id"] for r in rows}) != len(rows):
        raise ValueError("Probe IDs must be unique")
    if any(r["proposed_reference_label"] not in LABELS for r in rows):
        raise ValueError("Probe has an unknown proposed reference label")
    model = joblib.load(model_path)
    texts = [r["text"] for r in rows]
    predictions = model.predict(texts).tolist()
    scores = model.predict_proba(texts).max(axis=1).tolist()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_rows = []
    for row, prediction, score in zip(rows, predictions, scores, strict=True):
        output_rows.append({
            **row,
            "predicted_label": prediction,
            "max_probability_uncalibrated": score,
            "agrees_with_agent_proposal": prediction == row["proposed_reference_label"],
        })
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=output_rows[0].keys())
        writer.writeheader()
        writer.writerows(output_rows)
    return {
        "kind": "exploratory qualitative probe; not an independent accuracy test",
        "total": len(rows),
        "products": dict(Counter(r["product"] for r in rows)),
        "agreements_with_agent_proposals": sum(r["agrees_with_agent_proposal"] for r in output_rows),
        "output": str(output_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=ROOT / "artifacts/model/serving/model.joblib")
    parser.add_argument("--input", type=Path, default=ROOT / "data/external/official_notes_probe.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "artifacts/external_probe/predictions.csv")
    args = parser.parse_args()
    try:
        result = run_probe(args.model, args.input, args.output)
    except (OSError, ValueError) as error:
        parser.exit(2, f"External probe stopped: {error}\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

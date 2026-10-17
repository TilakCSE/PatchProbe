"""Train PatchProbe from human-reviewed annotation CSVs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from patchprobe.model import train_and_evaluate  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entries", type=Path, default=PROJECT_ROOT / "data/processed/entries.csv")
    parser.add_argument("--labels", type=Path, default=PROJECT_ROOT / "data/annotations/pilot_labels.csv")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "artifacts/model")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    try:
        result = train_and_evaluate(args.entries, args.labels, args.output_dir, seed=args.seed)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Training stopped: {error}\n")
    print(json.dumps({
        "status": result["status"],
        "counts": result["counts"],
        "split_counts": result["split_counts"],
        "test_model_macro_f1_five_labels": result["evaluation"]["test"]["model"]["macro_f1_five_labels"],
        "metrics_path": str(args.output_dir / "metrics.json"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

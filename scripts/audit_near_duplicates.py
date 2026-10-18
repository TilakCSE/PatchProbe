"""List similar entries from different releases for human leakage review.

Run from the repository root: ``python scripts/audit_near_duplicates.py``.
This is an audit, not an automatic exclusion or label assignment.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"entry_id", "release", "text"}


def find_pairs(rows: list[dict[str, str]], threshold: float = 0.88) -> list[dict[str, str]]:
    """Return cross-release candidate pairs ranked by character TF-IDF similarity."""
    if not 0 < threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    if len(rows) < 2:
        return []
    if any(not REQUIRED.issubset(row) or not row["text"].strip() for row in rows):
        raise ValueError("each row needs entry_id, release, and nonempty text")
    if len({row["entry_id"] for row in rows}) != len(rows):
        raise ValueError("entry IDs must be unique")
    matrix = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5)).fit_transform(
        [row["text"] for row in rows]
    )
    similarity = cosine_similarity(matrix)
    pairs = []
    for left in range(len(rows)):
        for right in range(left + 1, len(rows)):
            if rows[left]["release"] == rows[right]["release"]:
                continue
            score = float(similarity[left, right])
            if score >= threshold:
                pairs.append({
                    "similarity": f"{score:.6f}",
                    "left_id": rows[left]["entry_id"],
                    "left_release": rows[left]["release"],
                    "left_text": rows[left]["text"],
                    "right_id": rows[right]["entry_id"],
                    "right_release": rows[right]["release"],
                    "right_text": rows[right]["text"],
                })
    return sorted(pairs, key=lambda pair: float(pair["similarity"]), reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entries", type=Path, default=ROOT / "data/processed/entries.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "artifacts/data_audit/near_duplicates.csv")
    parser.add_argument("--threshold", type=float, default=0.88)
    args = parser.parse_args()
    with args.entries.open("r", newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))
    pairs = find_pairs(rows, args.threshold)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=(
            "similarity", "left_id", "left_release", "left_text",
            "right_id", "right_release", "right_text",
        ))
        writer.writeheader()
        writer.writerows(pairs)
    print(f"Found {len(pairs)} cross-release pairs at similarity >= {args.threshold:.2f}; wrote {args.output}")


if __name__ == "__main__":
    main()

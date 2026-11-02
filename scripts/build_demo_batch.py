"""Build a small, source-linked CSV for the public portal batch demo.

The selection is illustrative. It is not a random sample or an evaluation set.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DJANGO_IDS = (
    "dj-9bb0f2c834a0031c",  # dependency version
    "dj-7339e91a634f4dda",  # migration serialization
    "dj-336f88e0d839a604",  # template output
    "dj-011546728c329f4d",  # removed API
    "dj-084daac63d98e842",  # ambiguous configuration/code surface
    "dj-c0f7b469ad475d3a",  # template tag surface
)
EXTERNAL_IDS = (
    "react-02",
    "react-05",
    "vscode-01",
    "vscode-04",
    "chrome-01",
    "chrome-04",
)


def read_rows(path: Path, key: str) -> dict[str, dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))
    return {row[key]: row for row in rows}


def build_demo_batch(output: Path) -> int:
    django = read_rows(ROOT / "data/processed/entries.csv", "entry_id")
    external = read_rows(ROOT / "data/external/official_notes_probe.csv", "probe_id")
    rows = []
    for entry_id in DJANGO_IDS:
        row = django[entry_id]
        rows.append({"id": entry_id, "product": f"Django {row['release']}",
                     "text": row["text"], "source_url": row["source_url"]})
    for probe_id in EXTERNAL_IDS:
        row = external[probe_id]
        rows.append({"id": probe_id, "product": row["product"],
                     "text": row["text"], "source_url": row["source_url"]})
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=("id", "product", "text", "source_url"))
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    destination = ROOT / "data/demo/batch_demo.csv"
    count = build_demo_batch(destination)
    print(f"Wrote {count} source-linked notes to {destination}")

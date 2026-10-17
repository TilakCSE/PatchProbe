"""Build pinned, unlabeled Django release-note entries and a review pilot.

Run from the repository root: ``python scripts/build_dataset.py``.
``--offline`` rebuilds from the ignored source cache after the first fetch.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from patchprobe.ingest import (  # noqa: E402
    FIELDNAMES,
    SOURCE_GROUPS,
    deduplicate_exact,
    fetch_release,
    parse_release_notes,
    raw_url,
    select_pilot,
)


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Use cached raw release-note files only")
    parser.add_argument("--pilot-size", type=int, default=50)
    parser.add_argument("--cache-root", type=Path, default=ROOT / "data" / "raw" / "django")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data" / "processed")
    args = parser.parse_args()

    all_entries = []
    files = []
    for tag, revision, releases in SOURCE_GROUPS:
        for release in releases:
            source = fetch_release(revision, release, args.cache_root, offline=args.offline)
            entries = parse_release_notes(source, release, revision)
            all_entries.extend(entries)
            files.append(
                {
                    "release": release,
                    "tag": tag,
                    "source_revision": revision,
                    "raw_url": raw_url(revision, release),
                    "sha256_utf8": hashlib.sha256(source.encode("utf-8")).hexdigest(),
                    "extracted_entries_before_dedup": len(entries),
                }
            )
            print(f"{release}: {len(entries)} candidate entries")

    entries, exact_duplicates = deduplicate_exact(all_entries)
    pilot = select_pilot(entries, size=args.pilot_size)
    write_csv(args.output_dir / "entries.csv", [entry.row() for entry in entries])
    write_csv(args.output_dir / "pilot_queue.csv", [entry.row() for entry in pilot])
    manifest = {
        "dataset_kind": "unlabeled Django release-note candidate entries",
        "extraction_method": "patchprobe.ingest.parse_release_notes, source-controlled RST block parser",
        "source_license": "Django BSD-3-Clause; see docs/DATA_PROVENANCE.md",
        "files": files,
        "candidate_count_before_exact_dedup": len(all_entries),
        "exact_duplicate_count": exact_duplicates,
        "entry_count": len(entries),
        "counts_by_release": dict(sorted(Counter(entry.release for entry in entries).items())),
        "pilot_count": len(pilot),
        "pilot_entry_ids": [entry.entry_id for entry in pilot],
        "pilot_selection": "pilot-v1 substantive bullets only, stable SHA-256 order within release, release round-robin, text length 70–700",
        "labels_present": False,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(entries)} unlabeled entries and {len(pilot)} pilot rows to {args.output_dir}")


if __name__ == "__main__":
    main()

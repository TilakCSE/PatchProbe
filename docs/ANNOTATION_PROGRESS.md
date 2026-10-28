# Annotation progress — 2026-10-28

| Batch | Human decisions | Model labels | `UNCLEAR` | Status |
| --- | ---: | ---: | ---: | --- |
| Original pilot | 50 | 49 | 1 | Confirmed |
| Kavya batch 01 | 50 | 47 | 3 | Confirmed |
| Bhargav batch 01 | 50 | 48 | 2 | Confirmed |
| Om batch 01 | 50 | 50 | 0 | Confirmed |
| **Total** | **200** | **194** | **6** | **Confirmed** |

The source CSV has 571 entries. Exactly 371 source entries have no human decision yet. Each confirmed entry appears once in [the merged label CSV](../data/processed/reviewed_labels.csv). The named local reviewer records are ignored by Git; committed exports use reviewer aliases and date-only timestamps.

## Confirmed label support

| Label | Count |
| --- | ---: |
| API/code compatibility | 89 |
| Configuration/deployment | 29 |
| Data/schema migration | 36 |
| UI/output behavior | 40 |
| No targeted check stated | 0 |
| `UNCLEAR` (excluded from model fitting) | 6 |

The fifth model class remains unobserved. Reviewers should apply [the guide](DATA_AND_LABELS.md) based on the note text rather than fill a quota. If further review still finds no fifth-class examples, the team must document a taxonomy decision before a final model claim.

## Reproduce the aggregate

From the repository root, run `python scripts/merge_reviewed_labels.py`. It reads the four `data/processed/*_reviewed_labels.csv` exports, checks source IDs and duplicates, and writes `data/processed/reviewed_labels.csv`. For a future model run, pass `--labels data/processed/reviewed_labels.csv` to `scripts/train_model.py` only after a fresh release-grouped split and near-duplicate audit are planned. The existing model card and score refer to the original pilot, not these 200 decisions.

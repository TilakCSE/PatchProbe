# Annotation progress — 2026-11-01

| Batch | Human decisions | Model labels | `UNCLEAR` | Status |
| --- | ---: | ---: | ---: | --- |
| Original pilot | 50 | 49 | 1 | Confirmed |
| Kavya batch 01 | 50 | 47 | 3 | Confirmed |
| Bhargav batch 01 | 50 | 48 | 2 | Confirmed |
| Om batch 01 | 50 | 50 | 0 | Confirmed |
| Tilak batch 02 | 100 | 95 | 5 | Confirmed |
| **Total** | **300** | **289** | **11** | **Confirmed** |
| Kavya batch 02 | 0 | 0 | 0 | 50 draft suggestions; awaiting review |

The source CSV has 571 entries. Exactly 271 source entries have no human decision. Each confirmed entry appears once in [the merged label CSV](../data/processed/reviewed_labels.csv). Named local reviewer records are ignored by Git; committed exports use reviewer aliases and date-only timestamps. The draft Kavya batch is separate from the confirmed totals.

## Confirmed label support

| Label | Count |
| --- | ---: |
| API/code compatibility | 129 |
| Configuration/deployment | 44 |
| Data/schema migration | 55 |
| UI/output behavior | 61 |
| No targeted check stated | 0 |
| `UNCLEAR` (excluded from model fitting) | 11 |

The fifth model class remains unobserved in confirmed data. Kavya batch 02 includes one proposed example, which must be reviewed before it can count. Do not force a class quota. If the fifth class remains unsupported, document a taxonomy decision before a final model claim.

## Reproduce the aggregate

From the repository root, run `python scripts/merge_reviewed_labels.py`. It reads five `data/processed/*_reviewed_labels.csv` exports, checks source IDs and duplicates, and writes `data/processed/reviewed_labels.csv`. For a future model run, pass `--labels data/processed/reviewed_labels.csv` to `scripts/train_model.py` only after a fresh release-grouped split and near-duplicate audit are planned. The existing model card and score refer to the original pilot, not these 300 decisions.

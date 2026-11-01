# Annotation progress — 2026-11-01

| Batch | Human decisions | Model labels | `UNCLEAR` | Status |
| --- | ---: | ---: | ---: | --- |
| Original pilot | 50 | 49 | 1 | Confirmed |
| Kavya batch 01 | 50 | 47 | 3 | Confirmed |
| Bhargav batch 01 | 50 | 48 | 2 | Confirmed |
| Om batch 01 | 50 | 50 | 0 | Confirmed |
| Tilak batch 02 | 100 | 95 | 5 | Confirmed |
| Kavya batch 02 | 50 | 48 | 2 | Confirmed |
| Om batch 02 | 100 | 100 | 0 | Confirmed |
| **Total** | **450** | **437** | **13** | **Confirmed** |
| Bhargav batch 02 | 0 | 0 | 0 | 50 draft suggestions; awaiting review |

The source CSV has 571 entries. Exactly 121 source entries have no human decision. Each confirmed entry appears once in [the merged label CSV](../data/processed/reviewed_labels.csv). Named local reviewer records are ignored by Git; committed exports use reviewer aliases and date-only timestamps. The draft Bhargav batch is separate from the confirmed totals.

## Confirmed label support

| Label | Count |
| --- | ---: |
| API/code compatibility | 199 |
| Configuration/deployment | 60 |
| Data/schema migration | 87 |
| UI/output behavior | 89 |
| No targeted check stated | 2 |
| `UNCLEAR` (excluded from model fitting) | 13 |

The fifth class now has two human-confirmed examples, one from Kavya batch 02 and one from Om batch 02. This remains too sparse for a credible class-specific metric. Do not force class quotas. Bhargav batch 02 has no proposed fifth-class row, but its labels remain draft until review.

## Reproduce the aggregate

From the repository root, run `python scripts/merge_reviewed_labels.py`. It reads seven `data/processed/*_reviewed_labels.csv` exports, checks source IDs and duplicates, and writes `data/processed/reviewed_labels.csv`. For a future model run, pass `--labels data/processed/reviewed_labels.csv` to `scripts/train_model.py` only after a fresh release-grouped split and near-duplicate audit are planned. The existing model card and score refer to the original pilot, not these 450 decisions.

# Annotation progress — 2026-11-01

| Batch | Human decisions | Model labels | `UNCLEAR` | Status |
| --- | ---: | ---: | ---: | --- |
| Original pilot | 50 | 49 | 1 | Confirmed |
| Kavya batch 01 | 50 | 47 | 3 | Confirmed |
| Bhargav batch 01 | 50 | 48 | 2 | Confirmed |
| Om batch 01 | 50 | 50 | 0 | Confirmed |
| Tilak batch 02 | 100 | 95 | 5 | Confirmed |
| Kavya batch 02 | 50 | 48 | 2 | Confirmed |
| **Total** | **350** | **337** | **13** | **Confirmed** |
| Om batch 02 | 0 | 0 | 0 | 100 draft suggestions; awaiting review |

The source CSV has 571 entries. Exactly 221 source entries have no human decision. Each confirmed entry appears once in [the merged label CSV](../data/processed/reviewed_labels.csv). Named local reviewer records are ignored by Git; committed exports use reviewer aliases and date-only timestamps. The draft Om batch is separate from the confirmed totals.

## Confirmed label support

| Label | Count |
| --- | ---: |
| API/code compatibility | 146 |
| Configuration/deployment | 49 |
| Data/schema migration | 68 |
| UI/output behavior | 73 |
| No targeted check stated | 1 |
| `UNCLEAR` (excluded from model fitting) | 13 |

The fifth class now has one human-confirmed example: Kavya batch 02 row 30. This is still too little for a credible final estimate of fifth-class performance. Om batch 02 contains another proposed example at row 13; it remains only a draft until review. Do not force class quotas.

## Reproduce the aggregate

From the repository root, run `python scripts/merge_reviewed_labels.py`. It reads six `data/processed/*_reviewed_labels.csv` exports, checks source IDs and duplicates, and writes `data/processed/reviewed_labels.csv`. For a future model run, pass `--labels data/processed/reviewed_labels.csv` to `scripts/train_model.py` only after a fresh release-grouped split and near-duplicate audit are planned. The existing model card and score refer to the original pilot, not these 350 decisions.

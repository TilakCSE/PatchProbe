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
| Bhargav batch 02 | 50 | 50 | 0 | Confirmed |
| **Total** | **500** | **487** | **13** | **Confirmed** |
| Kavya final batch | 0 | 0 | 0 | All 71 remaining entries drafted; awaiting review |

The source CSV has 571 entries. Exactly 71 source entries have no human decision. Each confirmed entry appears once in [the merged label CSV](../data/processed/reviewed_labels.csv). Named local reviewer records are ignored by Git; committed exports use reviewer aliases and date-only timestamps.

Kavya's [final review sheet](KAVYA_FINAL_71_REVIEW.md) covers **all 71 remaining source IDs**. It proposes 44 model labels and 27 `EXCLUDE` decisions for fragments, generic headings, or missing examples. These are drafts, not confirmed counts. `EXCLUDE` is a data-quality disposition and never a model class. After Kavya reviews the sheet, preserve confirmed exclusions with entry IDs and reasons in a separate public CSV and verify that every one of the 571 source IDs has exactly one label, `UNCLEAR`, or exclusion disposition.

## Confirmed label support

| Label | Count |
| --- | ---: |
| API/code compatibility | 219 |
| Configuration/deployment | 81 |
| Data/schema migration | 94 |
| UI/output behavior | 91 |
| No targeted check stated | 2 |
| `UNCLEAR` (excluded from model fitting) | 13 |

The fifth class has two human-confirmed examples and remains too sparse for a credible class-specific metric. Kavya's draft has three proposed examples, which must be reviewed before they count. Do not force a class quota.

## Reproduce the aggregate

From the repository root, run `python scripts/merge_reviewed_labels.py`. It reads eight `data/processed/*_reviewed_labels.csv` exports, checks source IDs and duplicates, and writes `data/processed/reviewed_labels.csv`. For a future model run, pass `--labels data/processed/reviewed_labels.csv` to `scripts/train_model.py` only after a fresh release-grouped split and near-duplicate audit are planned. The existing model card and score refer to the original pilot, not these 500 decisions.

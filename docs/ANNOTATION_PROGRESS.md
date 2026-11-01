# Annotation progress — 2026-11-01

| Batch | Human dispositions | Model labels | `UNCLEAR` | `EXCLUDE` |
| --- | ---: | ---: | ---: | ---: |
| Original pilot | 50 | 49 | 1 | 0 |
| Kavya batch 01 | 50 | 47 | 3 | 0 |
| Bhargav batch 01 | 50 | 48 | 2 | 0 |
| Om batch 01 | 50 | 50 | 0 | 0 |
| Tilak batch 02 | 100 | 95 | 5 | 0 |
| Kavya batch 02 | 50 | 48 | 2 | 0 |
| Om batch 02 | 100 | 100 | 0 | 0 |
| Bhargav batch 02 | 50 | 50 | 0 | 0 |
| Kavya final batch | 71 | 44 | 0 | 27 |
| **Total** | **571** | **531** | **13** | **27** |

All **571 extracted source IDs** have one human-confirmed disposition. [The full annotated corpus](../data/processed/annotated_corpus.csv) keeps source provenance and a `review_decision` for every entry. Its `model_label` column is filled only for the 531 usable classification rows. [The merged label CSV](../data/processed/reviewed_labels.csv) has 544 decisions, including 13 `UNCLEAR`; [the exclusions CSV](../data/processed/excluded_entries.csv) has 27 reviewed fragments and headings with reasons. `EXCLUDE` is not a model class. Named reviewer records with exact timestamps remain ignored locally; public exports use aliases and date-only timestamps.

## Confirmed model-label support

| Label | Count |
| --- | ---: |
| API/code compatibility | 233 |
| Configuration/deployment | 91 |
| Data/schema migration | 106 |
| UI/output behavior | 96 |
| No targeted check stated | 5 |

The fifth class is present but still sparse. A final five-class metric needs support reported by release and split; no class-specific quality claim can be made from five examples alone. The review was non-blind: reviewers saw agent suggestions and confirmed or changed them. A separate blind re-review would be needed to estimate independent agreement.

The five `No targeted check stated` examples occur only in Django 4.2 (two), 5.0 (two), and 5.1 (one); 5.2 and 6.0 have none. A release-held-out test therefore cannot establish stable fifth-class quality from this corpus.

## Rebuild and verify

From the repository root, run `python scripts/merge_reviewed_labels.py`, then `python scripts/build_annotated_corpus.py`. The first command validates and merges nine public reviewer exports; the second rejects unknown, duplicate, overlapping, or missing IDs and regenerates the 571-row full-corpus CSV. For training, use `data/processed/reviewed_labels.csv`; the trainer excludes `UNCLEAR`. The 27 `EXCLUDE` entries are absent from that file. [Evaluation protocol](EVALUATION.md) requires a fresh release-grouped split and cross-release near-duplicate audit before reporting updated model performance. The existing model card and score describe only the original pilot.

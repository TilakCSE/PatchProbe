# Data layout

- `raw/`: pinned upstream release-note sources, cached locally and ignored by Git.
- `processed/entries.csv`: 571 extracted source entries with URLs, revisions, raw text, and cleaned model text; no labels.
- `processed/*_reviewed_labels.csv`: nine reviewer-name-free, date-only exports of confirmed decisions.
- `processed/reviewed_labels.csv`: validated merge of 544 label or `UNCLEAR` decisions. Training excludes `UNCLEAR`.
- `processed/excluded_entries.csv`: 27 confirmed non-standalone extraction fragments with reasons. These are not training examples.
- `processed/annotated_corpus.csv`: full 571-row source-and-decision join. `review_decision` includes five classes, `UNCLEAR`, or `EXCLUDE`; `model_label` is blank for `UNCLEAR` and `EXCLUDE`.
- `review_batches/`: historical queue and suggestion sheets showing what reviewers saw; not an extra source of labels.
- `annotations/`: named reviewer decisions with exact timestamps, local and ignored by Git.

Rebuild the merged labels with `python scripts/merge_reviewed_labels.py`; then run `python scripts/build_annotated_corpus.py` to regenerate and validate full coverage. Keep source IDs and revisions stable. The final evaluation must audit cross-release near-duplicates before splitting.

# Data layout

- `raw/`: pinned upstream release-note sources, cached locally and ignored by Git.
- `processed/entries.csv`: 571 extracted source entries with URLs, revisions, raw text, and cleaned model text; no labels.
- `processed/*_reviewed_labels.csv`: nine reviewer-name-free, date-only exports of confirmed decisions.
- `processed/reviewed_labels.csv`: validated merge of 544 label or `UNCLEAR` decisions. Training excludes `UNCLEAR`.
- `processed/excluded_entries.csv`: 27 confirmed non-standalone extraction fragments with reasons. These are not training examples.
- `processed/annotated_corpus.csv`: full 571-row source-and-decision join. `review_decision` includes five classes, `UNCLEAR`, or `EXCLUDE`; `model_label` is blank for `UNCLEAR` and `EXCLUDE`.
- `review_batches/`: historical queue and suggestion sheets showing what reviewers saw; not an extra source of labels.
- `annotations/`: named reviewer decisions with exact timestamps, local and ignored by Git.
- `demo/batch_demo.csv`: 12 source-linked notes for the portal CSV import demonstration; illustrative, without target labels. Rebuild with `python scripts/build_demo_batch.py`.
- `external/`: source-linked React, VS Code, and Chrome probe inputs and qualitative results. Proposed reference interpretations are not independent human ground truth.

Rebuild the merged labels with `python scripts/merge_reviewed_labels.py`; then run `python scripts/build_annotated_corpus.py` to regenerate and validate full coverage. Keep source IDs and revisions stable. The completed evaluation audits cross-release near-duplicates before scoring; see `docs/FULL_CORPUS_EVALUATION.md`.

# Full-corpus evaluation and transfer probe

## Reproduce

From the repository root after installing `pip install -e ".[dev]"`:

```powershell
python scripts/train_full_corpus.py
python scripts/probe_external_notes.py
```

The first command joins the 531 accepted labels from `data/processed/reviewed_labels.csv` to the pinned Django entries. It does not train on the 13 `UNCLEAR` decisions or 27 `EXCLUDE` fragments. It writes the evaluated model and metrics to `artifacts/model/` for the local Streamlit review screen. It also fits a separate model on all 531 accepted labels at `artifacts/model/serving/model.joblib`; the latter has no independent score of its own. Generated model files and result CSVs are ignored by Git.

## Frozen split and similarity policy

The five-class word and character TF-IDF plus balanced logistic regression configuration was fixed before this full-corpus run. The frozen chronological release split uses Django 4.2/5.0/5.1 for training (305 labels), all 5.2.x releases for development (111), and 6.0/6.0.1 for test (115), before similarity exclusions. The text input contains no release IDs or section headings. Before fitting, a label-free audit compares all 571 entries across releases with character 3–5 gram TF-IDF cosine similarity at threshold 0.88. A pair crossing splits removes the test row; if no test row is involved, it removes the dev row. Train rows stay. This policy uses source text and release group only, not the reference labels or predictions. All 531 model-labeled IDs remain in `split_manifest.csv`, with filtered rows marked `cross_split_near_duplicate`; the 20 corpus-level candidate pairs and split placement are in `near_duplicate_audit.csv`.

An initial seed-42 random assignment of whole release groups produced only seven held-out test notes because the 14 release groups vary greatly in size. Its diagnostic five-label macro-F1 was 0.405 on seven notes. We rejected that split because of **test size**, not to select a better score. No model parameters were changed. The chronological split was chosen to hold out a substantial later release family. This sequence is disclosed because the final test design was revised after the first run; do not describe the final test as never seen by the project team.

This is a conservative topic-overlap filter, not proof that all remaining examples are independent. Some flagged pairs describe distinct deprecation and removal events. The filtered held-out score covers notes from unseen Django releases after the stated exclusion rule; it does not describe every note in those releases. Both raw and filtered split sizes and each class's support are in `metrics.json`.

## Measured chronological run (2026-11-01)

The audit found 20 candidate pairs across the 571 source entries. Twelve model-labeled evaluation rows crossed split boundaries and were excluded: two dev and ten test. The resulting train/dev/test sizes are **305/109/105**. Test labels are API/code 47, Configuration/deployment 17, Data/schema 22, UI/output 19, and No targeted check stated 0. Train contains all five of the fifth-class examples.

On the 105 filtered test notes, the fixed model has **0.733 accuracy and 0.555 five-label macro-F1**. The majority baseline has 0.124 five-label macro-F1; the keyword baseline has 0.444. The fifth class has no test support and contributes zero to five-label macro-F1, so this is a `pilot` diagnostic score, not five-class validation. Test recall is 0.894 API/code, 0.471 Configuration/deployment, 0.682 Data/schema, and 0.632 UI/output. The high API/code recall alongside lower Configuration/deployment recall shows a common routing failure. The fitted evaluation vectorizers have **4,970 word + 17,292 character = 22,262 sparse features**. These are learned vocabulary dimensions, not dense embedding dimensions.

For concrete errors, the model routed a `ADMINS`/`MANAGERS` settings change to API/code instead of Configuration/deployment, a model-renaming permission migration issue to API/code instead of Data/schema, and a `querystring` output regression to API/code instead of UI/output. These are short or mixed notes where API identifiers can dominate the true verification area. Full per-class precision/recall, confusion matrix, IDs, links, and individual predictions are in the generated metrics and prediction CSV. No test-set tuning followed this run.

## Reporting boundary

The fifth class, `No targeted check stated`, has just five accepted examples across the entire corpus, limited to Django 4.2, 5.0, and 5.1. Any release-held-out split will have weak or missing fifth-class support. We report five-label macro-F1 for consistency, but use the status `pilot` when train/dev/test class-support guards are not met. The result is a diagnostic course evaluation, not a validated production classifier. The held-out model is never tuned on test results. The majority and fixed keyword baselines use the same filtered dev/test IDs.

## External transfer probe

`data/external/official_notes_probe.csv` contains 15 short **paraphrases** of source-linked notes from the official [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide), [Visual Studio Code 1.100 notes](https://code.visualstudio.com/updates/v1_100), and [Chrome 130 notes](https://developer.chrome.com/release-notes/130). These are three different product families, maintained by Meta, Microsoft, and Google respectively. The `source_section` field identifies the original claim. The text is adapted for a consistent one-note input and is not a byte-for-byte copy of the release page.

Each proposed reference label and reason was written by an agent after reading the official source. It is **not independent human ground truth**. `scripts/probe_external_notes.py` uses the all-531-label serving model and writes every prediction, uncalibrated maximum score, and agreement indicator to `artifacts/external_probe/predictions.csv`. A committed snapshot of all per-example predictions is `data/external/probe_results.csv`. The initial run agreed with the proposals on **6 of 15** notes: React 2/5, VS Code 2/5, Chrome 2/5. This is a warning about transfer, not a cross-company accuracy estimate. The model routed React's JSX-transform and UMD deployment changes to API/code, VS Code's ESM extension support to Data/schema, and Chrome's IndexedDB missing-data exception to UI/output. Those disagreements show product vocabulary and target-area ambiguity. Uncalibrated maximum class scores ranged from about 0.26 to 0.45 and must not be read as correctness probabilities. An independent reviewer should adjudicate the examples before any accuracy claim. No model changes were made in response to this probe.

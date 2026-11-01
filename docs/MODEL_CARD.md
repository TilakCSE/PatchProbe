# PatchProbe model card

Updated 2026-11-01. The first 49-label pilot score (five-label macro-F1 0.276 on ten test notes) is historical. The complete review and new run below supersede it for the current MVP.

## Intended use

Given one substantive software release-note entry, PatchProbe suggests the **first downstream area a developer or QA reviewer should verify**: API/code compatibility, Configuration/deployment, Data/schema migration, UI/output behavior, or No targeted check stated. The suggestion is triage support, not assurance that an upgrade is safe. It cannot know whether a particular application uses the changed feature, and it does not generate executable tests.

## Data and labels

The source is 14 pinned official Django release-note files. The extractor produced 571 entries. The team confirmed a disposition for each: 531 model labels, 13 `UNCLEAR`, and 27 `EXCLUDE` fragments. Five-class counts are 233/91/106/96/5 in the guide's order. Reviewers saw proposed decisions, so the labels are human-confirmed but do not measure independent annotation agreement. `UNCLEAR` and `EXCLUDE` are not model classes. Every training example has a source ID, release, and URL; the model sees only the cleaned `text` field, without release, heading, or URL.

## Model and features

The fixed CPU baseline joins word TF-IDF 1–2 grams and `char_wb` character TF-IDF 3–5 grams, then fits balanced logistic regression (`C=1.0`, `max_iter=1000`). TF-IDF and classifier are fitted on training releases only for evaluation. The evaluation artifact has 4,970 word features and 17,292 character features, **22,262 sparse dimensions** total. These dimensions are vocabulary features, not a dense embedding size. No LLM, transformer, or RAG is required.

## Evaluation

The frozen chronological release split uses Django 4.2/5.0/5.1 for train, 5.2.x for dev, and 6.0/6.0.1 for test. Before fitting, the predeclared cross-release similarity audit (character TF-IDF cosine ≥0.88) flags 20 candidate pairs across all 571 source entries. A model-labeled test row involved in a cross-split pair is removed; otherwise a dev row is removed, while train is retained. Twelve model-labeled evaluation rows were removed (two dev, ten test), leaving **305 train / 109 dev / 105 test**. The split manifest keeps all IDs and exclusion reasons. The filtered test score describes held-out Django releases after this topic-overlap filter; it does not represent every note in those releases.

| Test measure | Fixed model | Majority baseline | Keyword baseline |
| --- | ---: | ---: | ---: |
| Accuracy | 0.733 | 0.448 | 0.457 |
| Five-label macro-F1 | **0.555** | 0.124 | 0.444 |

Test class support is 47 API/code, 17 Configuration/deployment, 22 Data/schema, 19 UI/output, and **zero** No targeted check stated. The latter has only five examples, all in train. Its test recall cannot be measured. The run is therefore marked `pilot`: it is a useful four-observed-class diagnostic, **not** validated five-class performance. Test recall for the four observed classes is 0.894, 0.471, 0.682, and 0.632 respectively. Configuration/deployment is often misrouted to API/code. Exact precision, recall, confusion matrix, input hashes, split IDs, and prediction rows are in generated `artifacts/model/metrics.json`, `split_manifest.csv`, and `predictions.csv`.

An earlier random release-group assignment produced only seven test notes and a diagnostic five-label macro-F1 of 0.405. We discarded that split because its test set was too small and fixed the chronological split without changing model parameters. This happened after the first run, so the final test design should not be described as never seen by the project team. No tuning followed the chronological test run.

## Artifacts and inference

`python scripts/train_full_corpus.py` writes the **evaluated model** to `artifacts/model/model.joblib` for local Streamlit review, with matching `metrics.json`. It then fits a **separate serving model** on all 531 accepted labels at `artifacts/model/serving/model.joblib`. That all-data model has no independent held-out score of its own; the evaluation describes the fixed training recipe, not an identical fitted artifact. Model binaries are ignored by Git. Load joblib only from a trusted local checkout.

The model returns all class scores, but they are **uncalibrated**. A high maximum score is not a measured probability that a suggestion is right. Users should review the source note and may change or reject a suggestion.

## External transfer probe

Fifteen short paraphrases trace to official React 19, VS Code 1.100, and Chrome 130 release notes. The all-data model agreed with **6/15 agent-proposed reference labels**: 2/5 for each product. This is exploratory and **not an independent cross-company accuracy result**. Examples include JSX/UMD deployment changes routed to API/code and an IndexedDB missing-data issue routed to UI/output. The model was not tuned on these notes. See [FULL_CORPUS_EVALUATION.md](FULL_CORPUS_EVALUATION.md), `data/external/official_notes_probe.csv` for inputs, and `data/external/probe_results.csv` for all predictions.

## Main limitations and next evidence

- Fifth-class support is far too small and absent from dev/test; collect more independently reviewed examples or revise the taxonomy before making five-class claims.
- Reviewers saw proposed labels, so independent annotation agreement is unknown. Audit a blind re-review sample.
- Text similarity filtering reduces visible topic overlap but can miss related notes and changes the evaluation distribution.
- The Django-trained model transfers poorly to the small external probe. Collect a larger independently labeled multi-product set before deployment claims.
- A note may imply several verification areas even though the present classifier selects one. Add multi-label review only after measuring this ambiguity.
- No calibration, abstention threshold, drift monitoring, access control, or production feedback loop exists yet.

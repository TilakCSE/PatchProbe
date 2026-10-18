# PatchProbe model card

## Status

The first model is trained from 49 human-confirmed, agent-assisted pilot labels. The 50th reviewed entry is `UNCLEAR` and excluded. The observed labels cover only four of the five intended classes, so this is a presentation pilot, not a validated five-class classifier. Synthetic fixtures in tests verify software behavior only.

## Intended use

Given one substantive Django release-note entry, suggest the first downstream verification area for a developer or QA reviewer. The prediction is a review aid, not a claim that an upgrade is safe or unsafe. It does not generate test cases or infer which specific applications use a feature.

## Inputs and labels

The model reads only the cleaned `text` field in `data/processed/entries.csv`. It never receives release version, URL, source revision, section heading, or raw text. Human-confirmed, agent-assisted decisions from `data/annotations/pilot_labels.csv` are joined by `entry_id`; the agent may recommend a class, but only the reviewer confirms or corrects a saved label. The five model labels and their decision rules are in [DATA_AND_LABELS.md](DATA_AND_LABELS.md). `UNCLEAR` is excluded and counted. Every labeled row requires an annotator and timestamp; `UNCLEAR` also requires a reason.

## Model choice

The initial fixed candidate combines word 1–2 gram and character 3–5 gram TF-IDF features with balanced logistic regression (`C=1.0`, `max_iter=1000`). Technical notes contain identifiers and variant spellings, so character features may help. Both vectorizers are fitted only on train releases. There is no arbitrary dense embedding dimension: the sparse feature count is learned from the training vocabulary. This is a CPU-friendly baseline, not a tuned optimum. Compare it with majority-class and fixed keyword baselines.

## Evaluation design

Release IDs are assigned deterministically to train, dev, and test with seed 42, and a split manifest is saved. At least five labeled release groups are required. Repeated cleaned text across splits stops training. Report the five-class macro-F1, accuracy, per-class precision/recall/support, and a confusion matrix for held-out releases. `metrics.json` also records input file hashes, class support, exclusions, and absent test classes. If any class has fewer than five train, two dev, or five test examples, describe the result as a pilot. These thresholds are reporting guards, not statistical guarantees. The fixed keyword baseline is a deliberately simple heuristic; it is not ground truth. See [EVALUATION.md](EVALUATION.md).

## First pilot result (2026-10-18)

The fixed seed-42 split holds out Django 6.0 for test (10 rows), Django 5.1 for dev (9), and uses 4.2, 5.0, and 5.2 for train (30). The fitted sparse feature union has 5,838 dimensions. Test accuracy is 0.60; five-label macro-F1 is 0.276. Majority baseline: accuracy 0.50, macro-F1 0.133. Fixed keyword baseline: accuracy 0.30, macro-F1 0.280. The missing fifth class contributes zero to five-label macro-F1. The model predicts API/code for 9 of 10 test entries, exposing weak minority routing. The fixed keyword baseline is slightly higher on five-label macro-F1 (0.280 versus 0.276); the trained model has not earned a superiority claim. This is an honest pilot diagnostic from a tiny held-out release, not evidence of deployment quality. Exact support, per-class metrics, and the confusion matrix are in ignored `artifacts/model/metrics.json`. The detailed annotation CSV and trained artifacts stay local. A reviewer-name-free label export is committed at `data/processed/pilot_reviewed_labels.csv` for reproducible pilot training.

## Presentation inference

The Streamlit app exposes Prediction review only after local training writes a model and matching metrics. It displays a suggested area and all five class rows, marking classes absent from pilot training as untrained. Its scores are uncalibrated and should not be read as probabilities of correctness. Pasted text does not become a human label or a test example.

## Known limitations

- The pilot has 49 usable labels, heavily concentrated in API/code (29), and no `No targeted check stated` examples. Neither production suitability nor five-class quality is established.
- A single text entry can imply multiple checks. The guide allows `UNCLEAR`; forcing one area would conceal ambiguity.
- Release-group splitting reduces one leakage source but does not guarantee generalization to other libraries or writing styles. A separate similarity audit flags 20 cross-release candidate pairs in the current corpus at threshold 0.88; review any pairs crossing a future split before reporting metrics.
- Annotator identity is recorded in the CSV; software cannot independently verify that a person made the decision.
- The fixed word/character features and class balancing may work poorly when label support is very small.
- This classifier offers no calibrated confidence or abstention threshold yet. Its maximum predicted probability in the audit output is uncalibrated and only helps prioritize error review.

## Reproduction and artifacts

From the repository root, after installing project dependencies, run `python scripts/train_model.py --labels data/processed/pilot_reviewed_labels.csv`. It reads the two default CSV paths and writes `artifacts/model/model.joblib`, `metrics.json`, `split_manifest.csv`, and `predictions.csv`. The latter contains text and source links for correct/error review. Artifacts are ignored by Git. The command stops without writing artifacts if no human labels exist. Treat `joblib` files as trusted local artifacts only; loading untrusted serialized models can execute code.

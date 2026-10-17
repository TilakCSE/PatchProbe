# PatchProbe model card

## Status

The training pipeline is implemented, but no model trained on human labels or real evaluation score exists yet. The team must first complete the guided labeling pilot. Synthetic fixtures in tests only verify software behavior.

## Intended use

Given one substantive Django release-note entry, suggest the first downstream verification area for a developer or QA reviewer. The prediction is a review aid, not a claim that an upgrade is safe or unsafe. It does not generate test cases or infer which specific applications use a feature.

## Inputs and labels

The model reads only the cleaned `text` field in `data/processed/entries.csv`. It never receives release version, URL, source revision, section heading, or raw text. Human decisions from `data/annotations/pilot_labels.csv` are joined by `entry_id`. The five model labels and their decision rules are in [DATA_AND_LABELS.md](DATA_AND_LABELS.md). `UNCLEAR` is excluded and counted. Every labeled row requires an annotator and timestamp; `UNCLEAR` also requires a reason.

## Model choice

The initial fixed candidate combines word 1–2 gram and character 3–5 gram TF-IDF features with balanced logistic regression (`C=1.0`, `max_iter=1000`). Technical notes contain identifiers and variant spellings, so character features may help. Both vectorizers are fitted only on train releases. There is no arbitrary dense embedding dimension: the sparse feature count is learned from the training vocabulary. This is a CPU-friendly baseline, not a tuned optimum. Compare it with majority-class and fixed keyword baselines.

## Evaluation design

Release IDs are assigned deterministically to train, dev, and test with seed 42, and a split manifest is saved. At least five labeled release groups are required. Repeated cleaned text across splits stops training. Report the five-class macro-F1, accuracy, per-class precision/recall/support, and a confusion matrix for held-out releases. `metrics.json` also records input file hashes, class support, exclusions, and absent test classes. If any class has fewer than five train, two dev, or five test examples, describe the result as a pilot. These thresholds are reporting guards, not statistical guarantees. The fixed keyword baseline is a deliberately simple heuristic; it is not ground truth. See [EVALUATION.md](EVALUATION.md).

## Known limitations

- Human labels are pending. No measured quality or production suitability can be claimed yet.
- A single text entry can imply multiple checks. The guide allows `UNCLEAR`; forcing one area would conceal ambiguity.
- Release-group splitting reduces one leakage source but does not guarantee generalization to other libraries or writing styles.
- Annotator identity is recorded in the CSV; software cannot independently verify that a person made the decision.
- The fixed word/character features and class balancing may work poorly when label support is very small.
- This classifier offers no calibrated confidence or abstention threshold yet. Its maximum predicted probability in the audit output is uncalibrated and only helps prioritize error review.

## Reproduction and artifacts

From the repository root, after installing project dependencies, run `python scripts/train_model.py`. It reads the two default CSV paths and writes `artifacts/model/model.joblib`, `metrics.json`, `split_manifest.csv`, and `predictions.csv`. The latter contains text and source links for correct/error review. Artifacts are ignored by Git. The command stops without writing artifacts if no human labels exist. Treat `joblib` files as trusted local artifacts only; loading untrusted serialized models can execute code.

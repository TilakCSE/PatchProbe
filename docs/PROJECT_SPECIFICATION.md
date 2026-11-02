# PatchProbe project specification

Updated 2026-11-02. This describes the working MVP and its measured limits. The current public portal is a research demo, not a validated production safety system.

## Purpose and users

PatchProbe reads one substantive software release-note entry and suggests the **first downstream area to verify** during an upgrade. A developer, QA engineer, or release manager can use the suggestion to prioritize review. The product does not inspect an application's code, prove that a change affects it, generate executable tests, or certify an upgrade as safe.

The five target areas are **API/code compatibility**, **Configuration/deployment**, **Data/schema migration**, **UI/output behavior**, and **No targeted check stated**. `UNCLEAR` is a reviewer state for ambiguous notes; `EXCLUDE` marks non-standalone extraction fragments. Neither is a model class. The decision rules and examples are in [DATA_AND_LABELS.md](DATA_AND_LABELS.md).

## Data contract and provenance

| Item | Current value |
| --- | --- |
| Source | 14 official Django release-note RST files pinned to immutable Git revisions |
| Extracted candidates | 571 source-linked entries |
| Confirmed dispositions | 531 model labels, 13 `UNCLEAR`, 27 `EXCLUDE` |
| Class counts, guide order | 233 / 91 / 106 / 96 / 5 |
| Main public file | `data/processed/annotated_corpus.csv` |
| Model input | Cleaned `text` only; no release ID, heading, URL, or source revision |
| Audit fields | `entry_id`, `release`, `source_url`, `source_revision`, `section_path`, `raw_text`, review decision, note, date |

The extractor flattens release-note entries and preserves their source location. It performs deterministic whitespace cleanup and exact duplicate removal. It does not remove stopwords. Word TF-IDF's default regular-expression token pattern keeps word tokens of at least two characters; the character branch uses boundary-aware `char_wb` n-grams. Reviewers saw proposed decisions and confirmed or corrected them, so the labels are **human-confirmed** but do not measure blind inter-annotator agreement. See [DATA_PROVENANCE.md](DATA_PROVENANCE.md), [ANNOTATION_PROGRESS.md](ANNOTATION_PROGRESS.md), and [DECISIONS.md](../DECISIONS.md).

## NLP methodology

```text
Pinned Django notes → extraction and source IDs → human-confirmed decisions
→ chronological release split + cross-release similarity audit
→ train-only word and character TF-IDF → balanced logistic regression
→ majority/keyword baselines + per-class error review
→ evaluated local model for Streamlit
→ separate all-531-label fit → portable JSON → Next.js Node prediction routes
```

The fixed evaluated model uses `TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)` for words and `TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)` for characters. Both use scikit-learn's default lowercase, IDF weighting, and L2 normalization. `FeatureUnion` concatenates them. `LogisticRegression(C=1.0, class_weight="balanced", max_iter=1000)` maps the sparse vector to five class scores. The multiclass output uses softmax over linear logits; there is no neural-network hidden layer or chosen dense embedding dimension. The evaluated vocabulary is **4,970 word + 17,292 character = 22,262 sparse features**. The all-data serving fit has **32,140** features. Parameters were fixed before the current held-out run; the test set was not used for hyperparameter search.

## Evaluation and honest result

The frozen chronological split is Django 4.2/5.0/5.1 for train, all 5.2.x for development, and 6.0/6.0.1 for test. A predeclared character-TF-IDF cosine audit at threshold **0.88** found 20 candidate cross-release pairs in the 571 source entries. Twelve model-labeled dev/test rows crossing splits were excluded from scoring; every ID and reason remains in the generated manifest. Raw split sizes were **305/111/115** and filtered sizes are **305/109/105**. An earlier random release-group assignment was rejected after it produced only seven test notes; [FULL_CORPUS_EVALUATION.md](FULL_CORPUS_EVALUATION.md) discloses that sequence.

| Held-out Django 6.0/6.0.1 metric | TF-IDF + logistic | Majority | Fixed keywords |
| --- | ---: | ---: | ---: |
| Accuracy | 0.733 | 0.448 | 0.457 |
| Five-label macro-F1 | **0.555** | 0.124 | 0.444 |

Test support in label-guide order is **47/17/22/19/0**. All five `No targeted check stated` examples are in train, so that class's test recall is not measurable. The run remains marked `pilot`, despite improving on both baselines. The all-data serving fit is distinct from the evaluated train-only artifact and has no independent held-out score. Scores shown to users are uncalibrated model outputs, not probabilities of correctness.

For a transparent transfer check, 15 short source-linked paraphrases from official React 19, VS Code 1.100, and Chrome 130 notes were submitted to the all-data model. Six predictions matched agent-proposed interpretations, two of five per product. Those proposals are **not independent human ground truth**, so this is a qualitative failure probe rather than cross-company accuracy. Inputs and every result are in `data/external/`. The model was not tuned on the probe.

## Interfaces and technology

| Layer | Stack and responsibility |
| --- | --- |
| Extraction, labeling, training | Python 3.11+, pandas, NumPy, scikit-learn, joblib |
| Local research interface | Streamlit: full-corpus explorer, evaluation tables, source-linked errors, external probe, prediction review, historical guided annotation pilot |
| Public portal | Next.js 16.4.3 App Router, React 19.3, TypeScript, CSS; responsive single-note, CSV batch, human review, and export |
| Serving | Next.js Node route handlers; a committed portable JSON export of word/character TF-IDF and logistic coefficients; no Python runtime on Vercel |
| Verification | pytest, Python–Node parity checker, Next.js production build, GitHub Actions |
| Hosting target | Vercel project with repository Root Directory `portal/`; no deployed URL is verified yet |

The evaluated Streamlit model is generated locally at `artifacts/model/model.joblib` with matching `metrics.json`. The full-data model is generated at `artifacts/model/serving/model.joblib`, then exported to committed `portal/src/lib/model.generated.json`. Joblib files are ignored; the JSON lets a clean clone build the portal. Python and Node matched all five scores to numerical tolerance on **571 Django notes plus 15 external probe notes** (586/586 labels, maximum score difference about 5.11×10⁻¹⁵). This verifies implementation parity, not predictive accuracy.

`POST /api/predict` accepts `{ "text": "..." }`; `POST /api/predict/batch` accepts `{ "texts": ["...", "..."] }`. Each note must contain 1–10,000 characters, a batch contains 1–100 notes, and request bodies are capped at about 1.1 MB. Both routes return a prediction and model version/warning; invalid requests return structured errors. The portal stores no submitted notes on the server. Review decisions stay in browser memory until CSV export. The exported review draft does not enter training automatically.

The production Next.js build passes. The two API routes' traced files total about **6.3 MB uncompressed each**, well below Vercel's currently documented [250 MB Node function bundle limit](https://vercel.com/docs/functions/limitations). Vercel's [4.5 MB request/response payload limit](https://vercel.com/docs/functions/limitations) is separate from the bundled model file. A Vercel preview deployment still needs verification. The portal is a public demo with no accounts or rate limiting; users should not submit confidential notes.

## Demo files and commands

Upload [`data/demo/batch_demo.csv`](../data/demo/batch_demo.csv) in the portal's **Batch workspace**. It contains 12 source-linked notes (six Django, six React/VS Code/Chrome), intentionally including difficult cases. It has no expected labels and is not a benchmark. The portal accepts the `text`, `id`, and `source_url` columns and ignores the extra `product` column.

From the repository root: `python scripts/train_full_corpus.py`, `python scripts/probe_external_notes.py`, and `python scripts/build_demo_batch.py`. Run Streamlit with `python -m streamlit run app.py`. In `portal/`, run `npm ci`, `npm run build`, then `npm run start`. Full steps are in [PORTAL_DEPLOYMENT.md](PORTAL_DEPLOYMENT.md).

## Future encoder or transformer path

An encoder is feasible, but it should be an **evaluated comparison**, not an assumed upgrade. The lowest-risk next experiment is a frozen [all-MiniLM-L6-v2 sentence encoder](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), which produces **384-dimensional dense embeddings**. Encode the notes, fit a class-weighted logistic classifier on training embeddings, and compare per-class results with the TF-IDF baseline. [Sentence Transformers documents `encode()`](https://sbert.net/docs/sentence_transformer/usage/usage.html) for this use. Keep the encoder frozen initially; the small fifth class and domain-shift probe do not justify claiming that end-to-end fine-tuning will help.

If independently reviewed multi-product data and fifth-class support grow, a compact sequence classifier such as [DistilBERT](https://huggingface.co/docs/transformers/main/tasks/sequence_classification) could be fine-tuned with class-aware loss, early stopping, multiple seeds, and a newly frozen temporal/external test. That is a **future experiment**, not part of the current model. The existing Django 6.0 test has already influenced project decisions, so future model selection needs fresh untouched evidence. A transformer may also increase runtime size and latency; benchmark its actual serving cost before replacing the small Node model. Do not claim improvement until it beats the fixed baseline on an independently adjudicated evaluation set.

## Remaining work for wider deployment

1. Verify a Vercel preview end to end, then record the URL and build settings. Local build and API smoke tests do not prove cloud runtime behavior.
2. Blindly re-review a sample to estimate human agreement, collect more fifth-class examples, and build an independently labeled multi-product test set.
3. Add access control, rate limiting, privacy policy, abuse monitoring that excludes note text, calibrated or abstaining predictions, and a feedback/retraining process before handling sensitive or high-volume organizational use.

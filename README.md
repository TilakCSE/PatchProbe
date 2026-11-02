# PatchProbe

PatchProbe classifies a software release-note entry into the **first downstream area a developer should verify** after an upgrade. It is a course NLP MVP centered on official, version-pinned Django release notes. The classifier suggests a review priority; it does not prove an upgrade is safe.

## Team

- Tilaksinh Chauhan (23000740)
- Kavya Jariwala (23000543)
- Bhargav Panchal (23000502)
- Om Nathani (23000883)

## Current state

All **571** entries extracted from 14 pinned Django release-note files now have a human-confirmed disposition: **531 model labels, 13 `UNCLEAR`, and 27 `EXCLUDE`**. The five model classes have support of 233/91/106/96/5 in [label-guide order](docs/DATA_AND_LABELS.md). [The full annotated corpus](data/processed/annotated_corpus.csv) includes every source entry and decision; [reviewed labels](data/processed/reviewed_labels.csv) contain 544 rows and [exclusions](data/processed/excluded_entries.csv) contain 27. See [annotation progress](docs/ANNOTATION_PROGRESS.md) for batch details.

The full-corpus evaluation holds out later Django releases. After a documented cross-release similarity filter, the split contains **305 train / 109 development / 105 test** notes. The fixed TF-IDF and logistic-regression model reaches **0.733 test accuracy and 0.555 five-label macro-F1**, compared with 0.124 for the majority and 0.444 for the keyword baseline. This remains a **pilot result**: the fifth class has only five training examples and no development or test examples. Read the [model card](docs/MODEL_CARD.md) and [full evaluation](docs/FULL_CORPUS_EVALUATION.md) before citing the score.

A separate model fitted to all 531 accepted labels powers the portable Next.js portal. A 15-note exploratory probe from React, VS Code, and Chrome matched **6 agent-proposed reference labels**. These are not independent human gold labels, so cross-product accuracy remains unknown. The [source-linked inputs and per-note results](data/external/probe_results.csv) make the limitation inspectable.

## Run locally

From the project root with Python 3.11 or newer:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe scripts\train_full_corpus.py
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL printed by Streamlit. **Reviewed corpus** shows the complete dataset, label chart, filters, and source links. **Model evaluation** shows the current full-corpus split, per-class metrics, errors, and external probe. **Prediction review** uses the evaluated local model. **Guided annotation (pilot)** preserves the original 50-row review workflow, saved locally to a CSV; it does not change the committed full corpus automatically.

The committed `data/processed/` files make the review demo work offline. To rebuild the source dataset, run `python scripts/build_dataset.py` once with internet access. It caches pinned upstream RST sources under ignored `data/raw/django/`. Later, `python scripts/build_dataset.py --offline` uses that cache. Source revisions, hashes, counts, and selection rules are in [docs/DATA_PROVENANCE.md](docs/DATA_PROVENANCE.md) and `data/processed/manifest.json`.

Run `python scripts/audit_near_duplicates.py` to list highly similar notes from different releases in ignored `artifacts/data_audit/near_duplicates.csv`. Review these pairs before interpreting a release-held-out score; the script does not delete or relabel entries.

To reproduce the validated full-corpus CSVs, run `python scripts/merge_reviewed_labels.py` and then `python scripts/build_annotated_corpus.py`. The named reviewer records stay local; the committed exports contain aliases and dates.

To generate the current evaluated Streamlit model, the separate full-data serving model, and the external probe:

```powershell
.\.venv\Scripts\python.exe scripts\train_full_corpus.py
.\.venv\Scripts\python.exe scripts\probe_external_notes.py
```

This writes ignored artifacts under `artifacts/model/`: `metrics.json`, `split_manifest.csv`, `predictions.csv`, an evaluated `model.joblib`, and `serving/model.joblib`. The latter is fitted to all 531 labels and has no independent held-out score. The original 49-label pilot is still reproducible with `scripts/train_model.py --labels data/processed/pilot_reviewed_labels.csv`.

## Next.js portal

The public-facing `portal/` app provides one-note classification, CSV batch suggestions for up to 100 notes, a guided human review session, and CSV export. Upload the [12-row batch demo CSV](data/demo/batch_demo.csv) to show Django, React, VS Code, and Chrome examples. The prediction routes use a committed portable JSON model, so a clean clone can serve predictions without Python or a secret key. Scores are uncalibrated, and browser review drafts are not training labels.

```powershell
cd portal
npm ci
npm run dev
```

Set the Vercel project Root Directory to `portal`. Build and deployment details, API limits, and model export commands are in [PORTAL_DEPLOYMENT.md](docs/PORTAL_DEPLOYMENT.md). The portal has not been deployed from this repository yet.

## Pipeline

Pinned Django RST → deterministic entry extraction and provenance → human-confirmed dispositions → chronological release-grouped split and similarity audit → train-only word and character TF-IDF → balanced logistic regression → majority and keyword baselines → per-class error review → evaluated Streamlit model plus a separate all-label portable model for the Next.js portal.

Read the [project specification](docs/PROJECT_SPECIFICATION.md) for the full pipeline, stack, parameters, measured results, API, and future encoder path. [DECISIONS.md](DECISIONS.md) explains material choices; [ARCHITECTURE.md](docs/ARCHITECTURE.md), [LITERATURE_SURVEY.md](docs/LITERATURE_SURVEY.md), and [PORTAL_DEPLOYMENT.md](docs/PORTAL_DEPLOYMENT.md) cover implementation, related work, and deployment.

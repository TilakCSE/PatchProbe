# PatchProbe

PatchProbe classifies a software release-note entry into the **first downstream area a developer should verify** after an upgrade. It is a course NLP MVP centered on official, version-pinned Django release notes. The classifier suggests a review priority; it does not prove an upgrade is safe.

## Team

- Tilaksinh Chauhan (23000740)
- Kavya Jariwala (23000543)
- Bhargav Panchal (23000502)
- Om Nathani (23000883)

## Current state

The repository contains 571 extracted **unlabeled** candidate entries from 14 release-note files, a 50-entry guided review pilot, and a CPU-only classification/evaluation pipeline. There are no human labels or real classification metrics yet. The five intended labels and an `UNCLEAR` review state are defined in [docs/DATA_AND_LABELS.md](docs/DATA_AND_LABELS.md). Read [PROJECT_STATUS.md](PROJECT_STATUS.md) for the remaining work.

## Run locally

From the project root with Python 3.11 or newer:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL printed by Streamlit. Enter your name, read one entry, choose the first area to verify, and save. The app resumes from `data/annotations/pilot_labels.csv`; that file is personal review data and is not committed by default. If a row is ambiguous, save `UNCLEAR` with a reason. The app offers a copyable prompt so an agent can explain the row while the reviewer retains the decision.

The committed `data/processed/` files make the review demo work offline. To rebuild the source dataset, run `python scripts/build_dataset.py` once with internet access. It caches pinned upstream RST sources under ignored `data/raw/django/`. Later, `python scripts/build_dataset.py --offline` uses that cache. Source revisions, hashes, counts, and selection rules are in [docs/DATA_PROVENANCE.md](docs/DATA_PROVENANCE.md) and `data/processed/manifest.json`.

After a sufficient set of human decisions exists, run:

```powershell
.\.venv\Scripts\python.exe scripts\train_model.py
```

Training deliberately stops if the labels file is absent, too small, or lacks enough release groups. A completed run writes an ignored `artifacts/model/` directory with the split manifest, metrics, predictions, and fitted model. No metric from unlabeled data should be reported as classifier quality.

## Pipeline

Pinned Django RST → deterministic entry extraction and provenance → human annotation → release-grouped train/dev/test split → train-only word and character TF-IDF → balanced logistic regression → majority and keyword baselines → review of per-class results and errors. The Streamlit app currently supports **annotation**; a prediction interface follows once a validated model exists.

See [DECISIONS.md](DECISIONS.md) for why we chose these parts, [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for how they connect, [docs/LITERATURE_SURVEY.md](docs/LITERATURE_SURVEY.md) for related work and the originality boundary, [docs/PRESENTATION_QA.md](docs/PRESENTATION_QA.md) for likely professor questions, and [docs/CLOUD_WORKFLOW.md](docs/CLOUD_WORKFLOW.md) for cloud/phone setup.

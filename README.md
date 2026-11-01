# PatchProbe

PatchProbe classifies a software release-note entry into the **first downstream area a developer should verify** after an upgrade. It is a course NLP MVP centered on official, version-pinned Django release notes. The classifier suggests a review priority; it does not prove an upgrade is safe.

## Team

- Tilaksinh Chauhan (23000740)
- Kavya Jariwala (23000543)
- Bhargav Panchal (23000502)
- Om Nathani (23000883)

## Current state

All **571** entries extracted from 14 pinned Django release-note files now have a human-confirmed disposition: **531 model labels, 13 `UNCLEAR`, and 27 `EXCLUDE`**. The five model classes have support of 233/91/106/96/5 in [label-guide order](docs/DATA_AND_LABELS.md). [The full annotated corpus](data/processed/annotated_corpus.csv) includes every source entry and decision; [reviewed labels](data/processed/reviewed_labels.csv) contain 544 rows and [exclusions](data/processed/excluded_entries.csv) contain 27. See [annotation progress](docs/ANNOTATION_PROGRESS.md) for batch details.

The existing local model and its score still use only the original 49-label pilot. The full dataset has **not yet been used for a final model evaluation**. A new release-grouped split and cross-release near-duplicate audit are required before retraining and reporting performance. Read [PROJECT_STATUS.md](PROJECT_STATUS.md) for the remaining work.

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

Run `python scripts/audit_near_duplicates.py` to list highly similar notes from different releases in ignored `artifacts/data_audit/near_duplicates.csv`. Review these pairs before interpreting a release-held-out score; the script does not delete or relabel entries.

To reproduce the validated full-corpus CSVs, run `python scripts/merge_reviewed_labels.py` and then `python scripts/build_annotated_corpus.py`. The named reviewer records stay local; the committed exports contain aliases and dates.

To reproduce the **historical pilot** training run:

```powershell
.\.venv\Scripts\python.exe scripts\train_model.py --labels data\processed\pilot_reviewed_labels.csv
```

The committed label export records only a reviewer alias and date; the original name and exact timestamps remain in the ignored local annotation file. To show the 50/50 annotation count in a fresh clone, copy the export to `data/annotations/pilot_labels.csv` before starting the app. Training stops if the selected labels file is absent or lacks enough release groups. A completed run writes an ignored `artifacts/model/` directory with the split manifest, metrics, predictions, and fitted model. The currently documented model run has only 49 usable labels across four observed classes; see [docs/MODEL_CARD.md](docs/MODEL_CARD.md) before citing a number.

## Pipeline

Pinned Django RST → deterministic entry extraction and provenance → human annotation → release-grouped train/dev/test split → train-only word and character TF-IDF → balanced logistic regression → majority and keyword baselines → review of per-class results and errors. The Streamlit app supports guided annotation and **Prediction review**. The local pilot model and matching metrics now unlock the latter on this machine. A clean clone without the ignored labels and model artifacts starts with annotation only.

For the classroom walkthrough, use [docs/DEMO_RUNBOOK.md](docs/DEMO_RUNBOOK.md). See [DECISIONS.md](DECISIONS.md) for why we chose these parts, [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for how they connect, [docs/LITERATURE_SURVEY.md](docs/LITERATURE_SURVEY.md) for related work and the originality boundary, [docs/PRESENTATION_QA.md](docs/PRESENTATION_QA.md) for likely professor questions, and [docs/CLOUD_WORKFLOW.md](docs/CLOUD_WORKFLOW.md) for cloud/phone setup.

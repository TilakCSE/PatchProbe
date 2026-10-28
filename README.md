# PatchProbe

PatchProbe classifies a software release-note entry into the **first downstream area a developer should verify** after an upgrade. It is a course NLP MVP centered on official, version-pinned Django release notes. The classifier suggests a review priority; it does not prove an upgrade is safe.

## Team

- Tilaksinh Chauhan (23000740)
- Kavya Jariwala (23000543)
- Bhargav Panchal (23000502)
- Om Nathani (23000883)

## Current state

The repository contains 571 extracted candidate entries from 14 release-note files. The 50-entry guided pilot is now human-confirmed with agent assistance: 49 usable model labels and one `UNCLEAR` review state are saved locally. A reviewer-name-free export is committed at `data/processed/pilot_reviewed_labels.csv` so others can reproduce the pilot. A CPU-only pilot model has been trained; its held-out result is a small-sample diagnostic, not validated five-class quality. The five intended labels and an `UNCLEAR` review state are defined in [docs/DATA_AND_LABELS.md](docs/DATA_AND_LABELS.md). Read [PROJECT_STATUS.md](PROJECT_STATUS.md) for the remaining work. As of 2026-10-28, four batches total 200 human-confirmed decisions (194 model labels, six `UNCLEAR`). The [merged annotated CSV](data/processed/reviewed_labels.csv) is reproducible from four reviewer-name-free exports. Om has confirmed the [fourth review sheet](docs/BATCH_04_REVIEW.md). The older model score still describes only the original pilot.

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

With the confirmed pilot decisions, reproduce the pilot training run:

```powershell
.\.venv\Scripts\python.exe scripts\train_model.py --labels data\processed\pilot_reviewed_labels.csv
```

The committed label export records only a reviewer alias and date; the original name and exact timestamps remain in the ignored local annotation file. To show the 50/50 annotation count in a fresh clone, copy the export to `data/annotations/pilot_labels.csv` before starting the app. Training stops if the selected labels file is absent or lacks enough release groups. A completed run writes an ignored `artifacts/model/` directory with the split manifest, metrics, predictions, and fitted model. The current run has only 49 usable labels across four observed classes; see [docs/MODEL_CARD.md](docs/MODEL_CARD.md) before citing a number.

## Pipeline

Pinned Django RST → deterministic entry extraction and provenance → human annotation → release-grouped train/dev/test split → train-only word and character TF-IDF → balanced logistic regression → majority and keyword baselines → review of per-class results and errors. The Streamlit app supports guided annotation and **Prediction review**. The local pilot model and matching metrics now unlock the latter on this machine. A clean clone without the ignored labels and model artifacts starts with annotation only.

For the classroom walkthrough, use [docs/DEMO_RUNBOOK.md](docs/DEMO_RUNBOOK.md). See [DECISIONS.md](DECISIONS.md) for why we chose these parts, [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for how they connect, [docs/LITERATURE_SURVEY.md](docs/LITERATURE_SURVEY.md) for related work and the originality boundary, [docs/PRESENTATION_QA.md](docs/PRESENTATION_QA.md) for likely professor questions, and [docs/CLOUD_WORKFLOW.md](docs/CLOUD_WORKFLOW.md) for cloud/phone setup.

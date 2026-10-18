# Presentation demo runbook

Team 8 should be ready for the earliest possible presentation, 2026-10-19. Run every command from the PatchProbe project root in PowerShell.

## Before class

1. On the existing laptop checkout, run `.\.venv\Scripts\python.exe -m pytest` and `.\.venv\Scripts\python.exe scripts\train_model.py --labels data\processed\pilot_reviewed_labels.csv`.
2. Start `.\.venv\Scripts\python.exe -m streamlit run app.py` and open the printed local URL. Keep this terminal open.
3. Verify **Guided annotation** shows **50 / 50 reviewed** on the original laptop. A fresh clone starts with 0 / 50 because the detailed local CSV is intentionally ignored; copy `data/processed/pilot_reviewed_labels.csv` to `data/annotations/pilot_labels.csv` if you want to demonstrate the completed queue there.
4. Select **Prediction review**. Paste: “The minimum supported version of SQLite is increased to 3.31.0.” The current pilot model suggests **Configuration/deployment**. Do not rely on this exact output after retraining or changing labels.
5. Keep `docs/MODEL_CARD.md`, `docs/PRESENTATION_QA.md`, and `data/processed/manifest.json` ready to show.

For a fresh clone, install dependencies first with the commands in [README.md](../README.md). The committed processed data and reviewer-name-free label export are enough to train offline after installation. The raw upstream RST cache and model binary are intentionally uncommitted.

## Five-minute sequence

1. **Problem (30 s):** A dependency release note names a change, but a developer still needs to decide where to verify their application first. PatchProbe suggests one area, leaving the actual test decision to the developer.
2. **Data and labels (60 s):** Show 571 extracted Django entries from 14 pinned source files and the 50 reviewed pilot rows. Explain four verification surfaces plus `No targeted check stated`; `UNCLEAR` is a separate review state. Say the reviewer confirmed agent suggestions, so this is not blind independent labeling.
3. **Pipeline (60 s):** Show source extraction and provenance, text-only input, release-group split, train-only word and character TF-IDF, balanced logistic regression, and majority/keyword baselines. No stopword-removal stage or dense embedding dimension is used.
4. **Live app (90 s):** Show the 50/50 review count, revisit one saved choice, then enter the SQLite sentence in Prediction review. Point to the pilot warning and the untrained fifth class.
5. **Evidence and limits (60 s):** The split has 30 train, 9 dev, 10 test rows. Test accuracy is 0.60 and five-label macro-F1 is 0.276, with no `No targeted check stated` examples. The model predicts API/code for 9 of 10 test entries and its macro-F1 is slightly below the fixed keyword baseline (0.280). This proves the pipeline runs and reveals a class coverage problem; it does not establish a reliable five-class product.

## If something fails during the live demo

- If the app is already using port 8501, use `--server.port 8502` when starting it.
- If the prediction mode is missing, rerun the training command above; it writes ignored `artifacts/model/model.joblib` and `metrics.json`.
- If the completed review count is missing on a fresh clone, copy the committed export into `data/annotations/pilot_labels.csv`. Keep the original laptop's detailed local file intact.
- If internet is unavailable, use the committed `data/processed` CSVs; source downloading is unnecessary for the demo.
- If asked whether 0.276 is good accuracy, say it is **macro-F1**, not accuracy, and explain why the 10-row test and absent fifth class make it a pilot diagnostic.

## Next work after presentation

Independently re-review a subset without showing the agent's recommendations; sample more possible `No targeted check stated` cases and minority classes; inspect cross-release near duplicates; freeze a larger split; then report per-class errors again. Record any taxonomy change in [DECISIONS.md](../DECISIONS.md) before retraining.

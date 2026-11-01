# Next.js portal and model serving

The public portal is a separate Next.js application in `portal/`. Its Node route handlers classify submitted text with a committed, portable JSON export of the full-data scikit-learn model. The browser sends text only to the same-origin API. The server does not store notes or log their contents. Both the UI and API describe scores as **uncalibrated** and predictions as review suggestions.

## Rebuild the model export

From the repository root after the full-data training run:

```powershell
.\.venv\Scripts\python.exe scripts\train_full_corpus.py
.\.venv\Scripts\python.exe scripts\export_portal_model.py
.\.venv\Scripts\python.exe -m pytest tests\test_portable_inference.py
.\.venv\Scripts\python.exe scripts\check_portal_parity.py
```

The exporter reads `artifacts/model/serving/model.joblib` and writes `portal/src/lib/model.generated.json`. The binary stays ignored; the JSON is the portable deployment artifact and must be reviewed and committed with the model card after retraining. Never load a joblib artifact from an untrusted source. The JSON records the binary SHA-256 and model version. A fresh clone can build the portal from the committed JSON, with no Python runtime on Vercel.

For the 531-label full model, the export has 32,140 TF-IDF features and is 4,526,422 bytes. The parity checker compared all 571 source notes plus 15 external probes with the Python model: 586/586 matching labels and a maximum absolute class-score difference of 5.11×10⁻¹⁵. This checks implementation parity, not classification accuracy or cross-project generalization.

## Local portal

```powershell
cd portal
npm ci
npm run dev
```

Open the local URL printed by Next.js. `npm run build` verifies the production bundle. If the JSON export is missing or malformed, the build fails rather than displaying made-up results.

## Vercel

1. Import `TilakCSE/PatchProbe` into Vercel and set **Root Directory** to `portal`.
2. Select the Next.js framework preset. Use the committed lockfile and default `npm run build` command.
3. Deploy a preview first. Submit a note, a multi-row CSV, an invalid empty note, and a 101-note batch to verify successful and rejected requests. Confirm that the response includes the model version and warning.
4. Promote to production only after the preview passes and the model card reflects the same export.

The route handlers run on the Node runtime. Request bodies are capped at about 1.1 MB; each note is 1–10,000 characters, and a batch is 1–100 notes. No API key is required. The current portal is a public demonstration, not an enterprise data processing service. Do not submit confidential release notes. Production use would require access controls, rate limiting, monitoring that excludes note text, a privacy policy, and a validated model for the intended software ecosystem.

## API

`POST /api/predict` accepts `{ "text": "..." }` and returns `{ "prediction": { "label": "...", "scores": { "...": 0.0 }, "score": 0.0 }, "model": { "version": "...", "sha256": "...", "trainedOn": "...", "warning": "..." } }`.

`POST /api/predict/batch` accepts `{ "texts": ["...", "..."] }` and returns the same model object plus `predictions` in input order. Errors return `{ "error": { "code": "...", "message": "..." } }` with a non-2xx status. Scores sum to one but are not calibrated confidence estimates.

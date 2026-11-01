# PatchProbe portal

The public-facing Next.js interface for PatchProbe. It makes one-note and CSV-batch predictions, then lets a person record review decisions. It uses the same-origin prediction routes in the portal; no API key or external prediction service is needed.

## Run

Use Node.js 20.9 or newer. From this directory:

```bash
npm install
npm run dev
```

Open http://localhost:3000. Build with `npm run build`.

The deployment's project root is `portal/`. The app uses `/api/predict`, `/api/predict/batch`, and its bundled portable model JSON. The interface shows a service error when those parts are unavailable; it never substitutes a fabricated result.

## Use

- **Classify one note:** paste one substantive release-note entry, up to 10,000 characters. The output includes the suggested first verification area and uncalibrated score breakdown.
- **Batch workspace:** import a CSV with a `text`, `note`, `release_note`, or `entry` column. Optional `id`/`entry_id` and `source_url`/`source`/`url` columns are accepted. Maximum 100 nonempty notes. Export suggestions as CSV.
- **Human review:** confirm, change, or mark suggestions `UNCLEAR`. A reason is required for `UNCLEAR`. Export only decided rows as a review draft. This file is not an independently labeled gold set or an automatic training source.

CSV parsing handles quoted commas and newlines. User notes and decisions live only in browser memory until the user exports; reloading clears the session. Requests send note text to the same-origin server route for prediction. The portal stores no notes on the server. Source links are clickable only for HTTP or HTTPS URLs. Exported cells beginning with spreadsheet formula characters are prefixed with an apostrophe.

## Scope

The model learns from official Django release-note entries. A prediction is a triage suggestion and cannot establish that an upgrade is safe. The fifth class has only five confirmed training examples. Scores are uncalibrated, and other ecosystems require independent evaluation before any generalization claim.




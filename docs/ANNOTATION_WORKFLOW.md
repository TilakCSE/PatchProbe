# Guided annotation workflow

## What the reviewer decides

For each substantive Django release-note entry, answer: **Which one area should a developer verify first after upgrading an application that uses the affected feature?** Choose only from evidence in the note text. The release number and source link provide provenance; the section heading is tucked into a collapsed provenance panel so it does not lead the choice. The five choices and tie-break rules are in [DATA_AND_LABELS.md](DATA_AND_LABELS.md).

This is a human decision. The interface never guesses or saves a label on its own. A reviewer can ask an agent to explain a row and the label definitions, then make the choice personally. When two checks are equally primary, choose `UNCLEAR` and write why. `UNCLEAR` is a review state, not a sixth model class.

## Run the pilot

1. Generate or obtain an entries CSV with columns `entry_id, release, source_url, source_revision, section_path, raw_text, text`. The default path is `data/processed/pilot_queue.csv`, the varied 50-entry pilot. The sidebar can point to `data/processed/entries.csv` or another file for later review.
2. From the project root, install project dependencies and run `streamlit run app.py`.
3. Enter the reviewer name. Read the note and the definitions, open the official source when needed, then select one label and click **Save decision**. `UNCLEAR` needs a review note. **Skip for now** moves to the next row without saving a label.
4. Saved decisions are written to `data/annotations/pilot_labels.csv` by default, with columns `entry_id, label, annotator, review_note, annotated_at`. Restarting the app resumes after saved rows. Skips are only temporary in that browser session; use **Return to skipped entries** to revisit them.
5. Use **Revisit a saved decision** to correct an earlier choice. The new decision replaces the prior row in the CSV. Keep backups or versioned copies if an audit trail of revisions is required.

If the dataset does not exist or has no rows, the app explains what is missing. It checks required columns, unique entry IDs, nonempty model text, valid labels, and matching entry IDs before displaying or saving decisions. Do not edit the source CSV's IDs after annotation begins.

## Pilot review and effort estimate

Time the 50-entry pilot, including source lookups and discussion, rather than assuming a fixed number of minutes per row. Record total time, `UNCLEAR` count, class counts, difficult examples, and any changes to the guide. A second reviewer can independently annotate a subset to assess whether the definitions are usable; each reviewer should use a separate labels CSV to avoid overwriting one another.

A human-confirmed, agent-assisted pilot may be trained to verify the end-to-end pipeline, but do not present its class-sparse score as validated five-class quality. Independent second review and broader class support are needed for a stronger evaluation. `UNCLEAR` rows stay out of five-class training, and their count must be reported.

## Prediction review for the presentation

The sidebar offers **Prediction review** only after the local training command has produced both `artifacts/model/model.joblib` and a matching `artifacts/model/metrics.json`. Without them, the sidebar explains that no trained model is available; the annotation queue still works. The app accepts one pasted release-note entry and shows a suggested first-check area with all five class rows. Classes absent from pilot training show **Not trained in this pilot**, not a made-up zero. All displayed scores are explicitly uncalibrated model outputs, not correctness probabilities.

The app reads only the fixed artifact path inside this project and refuses symbolic-link artifact paths. `joblib` deserialization can execute code, so run inference only with an artifact you generated locally and trust. The free-text prediction is a temporary review preview; it does not create a human label or enter the evaluation set. Use Guided annotation to save a source-linked human decision.

## Data handling limits

The app is a local reviewer aid, not a shared multi-user annotation server. It rewrites one CSV atomically on each save, but simultaneous sessions writing the same file can lose edits. Assign separate output files to simultaneous reviewers and reconcile them deliberately. The label CSV contains reviewer names; follow the team's data-sharing preference before committing it. The original source URL and revision remain in the entry CSV so each decision can be traced to the source.
## Chat-assisted pilot review

For this pilot, the agent showed source entries, recommended areas, and explained the evidence. Tilaksinh confirmed rows 1–9 individually and then all recommendations for rows 10–50 from the full review sheet. The agent then saves only that explicit human choice using the same annotation helper as the app, with `annotator`, UTC timestamp, and a review note identifying the agent assistance. `UNCLEAR` requires the human's reason. The original `data/annotations/pilot_labels.csv` remains ignored by Git. A separate name-free export at `data/processed/pilot_reviewed_labels.csv` is committed for reproducible training. This is **human-confirmed, agent-assisted** labeling, not blind independent annotation or an automated gold set. A second reviewer should label a subset without seeing recommendations if the team wants an agreement estimate.

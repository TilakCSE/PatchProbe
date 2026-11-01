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


## Batch review after the pilot (2026-10-28)

Kavya reviewed all 50 suggestions in [KAVYA_BATCH_01_REVIEW.md](KAVYA_BATCH_01_REVIEW.md) and confirmed them, including three `UNCLEAR` rows (32, 36, 46). The original local file `data/annotations/kavya_batch_01_labels.csv` records her name and exact timestamps and remains ignored by Git. `data/processed/kavya_batch_01_reviewed_labels.csv` is a name-free, date-only export of the same 50 decisions. There are 47 new model labels and three review-only `UNCLEAR` decisions. The suggestion sheet was visible to the reviewer, so this is a human-confirmed batch review, not independent blind labeling.

Bhargav's next 50 entries are in [BHARGAV_BATCH_01_REVIEW.md](BHARGAV_BATCH_01_REVIEW.md), with source links, draft recommendations, and reasons. `data/review_batches/bhargav_batch_01_suggestions.csv` has blank human-decision fields. These rows must not be joined into training until Bhargav confirms or changes them. They do not overlap the first 100 reviewed entries. Reviewers can respond with all confirmed except specific row numbers; `UNCLEAR` may remain unresolved with its reason.

When combining batches, count `UNCLEAR` separately and exclude it from model fitting. Recheck near-duplicate text across releases and freeze a new release-grouped split, because this broader review includes releases that were held out in the first pilot run.


## Three-batch merge and fourth batch (2026-10-28)

Bhargav reviewed all 50 rows in [BHARGAV_BATCH_01_REVIEW.md](BHARGAV_BATCH_01_REVIEW.md) and confirmed them, leaving rows 07 and 45 as `UNCLEAR`. His ignored local CSV holds the named and timestamped record; `data/processed/bhargav_batch_01_reviewed_labels.csv` is the reviewer-name-free, date-only export. Together with the pilot and Kavya exports, [the merged annotated CSV](../data/processed/reviewed_labels.csv) has 150 distinct source IDs, 144 model-usable labels, and six `UNCLEAR` decisions. Run `python scripts/merge_reviewed_labels.py` to validate and regenerate it.

Om Nathani reviewed all 50 rows in [Batch 04](BATCH_04_REVIEW.md) and confirmed the suggestions, with no `UNCLEAR` rows. The ignored local `data/annotations/om_batch_01_labels.csv` records his name and exact timestamps; `data/processed/om_batch_01_reviewed_labels.csv` is the alias-and-date-only export. The [merged annotated CSV](../data/processed/reviewed_labels.csv) now contains 200 distinct source IDs, 194 model labels, and six `UNCLEAR` rows. The later three batches used non-blind human review of agent suggestions; do not use them as an independent agreement estimate.


## Tilak's 100-row draft batch (2026-11-01)

[TILAK_BATCH_02_REVIEW.md](TILAK_BATCH_02_REVIEW.md) presents 100 new, source-linked entries with proposed labels and short reasons. The corresponding queue and suggestion CSVs are in `data/review_batches/`. They exclude the first 200 reviewed IDs and have blank human-decision fields. Tilak can confirm all, list corrections by row number, keep or change proposed `UNCLEAR` states, or mark a visibly broken extraction `EXCLUDE`. Do not save the proposals as reviewer labels until he explicitly confirms them. Any excluded extraction remains outside training and is counted separately.


## Fifth confirmed batch and Kavya's second draft (2026-11-01)

Tilaksinh Chauhan confirmed all 100 visible suggestions in [Tilak batch 02](TILAK_BATCH_02_REVIEW.md), retaining five `UNCLEAR` states. The ignored named CSV records his decisions with exact timestamps; `data/processed/tilak_batch_02_reviewed_labels.csv` is a name-free date-only export. The validated merged CSV now has 300 decisions, 289 model labels, and 11 `UNCLEAR` states.

[Kavya batch 02](KAVYA_BATCH_02_REVIEW.md) contains 50 new draft suggestions from five feature releases. The suggestion CSV has blank reviewer-decision fields. None may enter training until Kavya confirms or changes it. Row 30 proposes the first `No targeted check stated` label and deserves particular scrutiny against the guide. The two proposed `UNCLEAR` rows are 10 and 45. The review remains non-blind because proposed labels are visible.


## Sixth confirmed batch and Om's second draft (2026-11-01)

Kavya Jariwala confirmed all 50 visible suggestions in [Kavya batch 02](KAVYA_BATCH_02_REVIEW.md), retaining two `UNCLEAR` states and confirming one `No targeted check stated` decision. The ignored named CSV records her decisions with exact timestamps; `data/processed/kavya_batch_02_reviewed_labels.csv` is a name-free date-only export. The validated merged CSV now has 350 decisions, 337 model labels, and 13 `UNCLEAR` states.

[Om batch 02](OM_BATCH_02_REVIEW.md) contains 100 new draft suggestions from four feature releases. The suggestion CSV has blank reviewer-decision fields. None may enter training until Om confirms or changes it. Row 13 proposes another `No targeted check stated` example and should be checked carefully against the guide. This review remains non-blind because proposed labels are visible.


## Seventh confirmed batch and Bhargav's second draft (2026-11-01)

Om Nathani confirmed all 100 visible suggestions in [Om batch 02](OM_BATCH_02_REVIEW.md), including one `No targeted check stated` label and no `UNCLEAR`. The ignored named CSV records his decisions with exact timestamps; `data/processed/om_batch_02_reviewed_labels.csv` is a name-free date-only export. The validated merged CSV now has 450 decisions, 437 model labels, and 13 `UNCLEAR` states.

[Bhargav batch 02](BHARGAV_BATCH_02_REVIEW.md) contains 50 new draft suggestions from four feature releases. The suggestion CSV has blank reviewer-decision fields. None may enter training until Bhargav confirms or changes it. The first similarity threshold left too few unused candidates, so this batch uses 0.96 to exclude only very close text; cross-release near-duplicates at the original 0.88 audit threshold need explicit handling before evaluation. This review remains non-blind because proposed labels are visible.


## Eighth confirmed batch and full remaining queue (2026-11-01)

Bhargav Panchal confirmed all 50 visible suggestions in [Bhargav batch 02](BHARGAV_BATCH_02_REVIEW.md), with no `UNCLEAR`. His ignored named CSV has exact timestamps; `data/processed/bhargav_batch_02_reviewed_labels.csv` is the name-free date-only export. The validated merged CSV now has 500 decisions: 487 model labels and 13 `UNCLEAR`.

[Kavya's final sheet](KAVYA_FINAL_71_REVIEW.md) includes every remaining source ID, including short fragments that earlier selection filters skipped. It proposes 44 model labels and 27 `EXCLUDE` decisions; none are saved as human decisions yet. On confirmation, save labels to Kavya's named local CSV and name-free public export. Put confirmed exclusions, source IDs, reasons, and date in a separate public CSV. Then assert that the union of reviewed labels and exclusions is exactly the 571-entry source set, with no overlap. The batch is non-blind because suggestions are visible.

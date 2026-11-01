# Decision log

Each decision records the choice, evidence, alternatives, and what would change it. A model configuration is not an experimental result; measured performance enters this log only after human labeling and a frozen evaluation.

## D001 — Project and source domain (accepted, 2026-10-17)

**Choice:** Build PatchProbe for software release-note verification triage using version-pinned Django notes.

**Why:** The user chose this classification task after an originality audit. Official Django notes provide discrete entries, stable source revisions, and an offline demo without paid APIs.

**Boundary:** Prior work covers release-note change types and action-required summaries; PatchProbe targets a first downstream verification area. This is a scoped classroom originality claim, not a worldwide-first claim. Training on Django alone cannot show cross-ecosystem generalization.

## D002 — Labels and human review (accepted for pilot, 2026-10-17)

**Choice:** Keep five suggested verification areas and a separate `UNCLEAR` review state. A person chooses the label from the note text. Start with a guided 50-entry pilot and measure effort before scaling.

**Why:** Tilaksinh chose a row-by-row workflow in which the agent recommends a label and explains the text, then he confirms or corrects it. The agent saves only an explicit human decision, with an assistance note and timestamp. These are human-confirmed, agent-assisted labels; they must not be presented as blind independent annotation. A small pilot tests guide clarity, class support, and review time. The provisional estimate is 45–90 minutes for 50 rows, to be replaced with observed time.

**Alternatives:** Labels inferred from Django section headings would be cheaper, but would answer an editorial-topic task rather than the proposed verification question. LLM-generated labels without independent review would not be a valid gold set.

**Pivot trigger:** If the pilot is too slow, ambiguous, or class-sparse, narrow the taxonomy or report only the annotation pilot. Record any pivot here before retraining; do not silently change the target.

## D003 — Source snapshot and extraction (accepted, 2026-10-17)

**Choice:** Fetch 14 official Django release-note RST files from two immutable Git commits. Extract substantive bullet and prose entries, preserve source URL/revision and raw text, remove exact normalized-text duplicates, and commit the small unlabeled output.

**Why:** Pinned files and hashes make the dataset auditable; committed processed CSVs support an offline classroom demo. The current extraction yields 571 candidate entries, not 571 labeled examples. See `data/processed/manifest.json` and [docs/DATA_PROVENANCE.md](docs/DATA_PROVENANCE.md).

**Limit:** RST flattening may miss or distort unusual markup; entries can depend on context. Human reviewers should inspect uncertain rows. Pilot selection seeks release and section variety; it is not class balancing.

## D004 — Model representation and family (accepted baseline, 2026-10-17)

**Choice:** Use a word TF-IDF vectorizer with 1–2-grams and a `char_wb` TF-IDF vectorizer with 3–5-grams, joined in a scikit-learn feature union. Fit logistic regression with `class_weight="balanced"`, `C=1.0`, and `max_iter=1000`. Compare with majority and transparent keyword baselines.

**Why:** Short technical notes contain identifiers, spelling variants, and sparse phrases. Word features capture phrases; character features tolerate token variation. Logistic regression runs on a CPU and supports feature inspection. Balanced weighting reduces dominance from frequent classes, though it cannot cure missing classes.

**Dimension:** There is no fixed embedding dimension. Each TF-IDF vocabulary is learned from training text; record the fitted feature count after a real training run. No transformer fine-tuning, RAG, or LLM is required for the MVP.

**Change rule:** This is a fixed starting configuration, not a tuned winner. Any tuning must use training/development data and be recorded before test evaluation.

## D005 — Evaluation and release split (accepted protocol, 2026-10-17)

**Choice:** Split by release group, fit vectorizers on training rows only, reject identical text that crosses splits, and save the split manifest. Report class support, majority and keyword baselines, macro-F1, per-class precision/recall, confusion matrix, and traceable errors when human labels exist.

**Why:** Notes within a release share vocabulary and context. Random row splits can make evaluation too optimistic. Exact split memberships are generated with seed 42 and will be saved with each trained run; five labeled release groups are the minimum for the program to proceed.

**Limit:** A release-grouped score tests held-out Django releases, not later chronological upgrades or other projects. If a class lacks sufficient support, the run is marked a pilot rather than presented as a valid five-class result. The 2026-10-18 run is a class-sparse pilot; see D008 and the model card.

## D006 — User interface and privacy (accepted, 2026-10-17)

**Choice:** Use a local Streamlit one-row review screen that saves reviewer name, timestamp, decision, and optional note to a CSV. Keep labels, raw upstream cache, and trained artifacts out of Git by default.

**Why:** The user requested one-by-one help while labeling later. A local interface makes progress visible, allows correction, and keeps the human decision explicit. Streamlit is quick to run for a presentation.

**Limit:** Concurrent reviewers must use distinct label files; the CSV is not a shared production annotation service. Prediction review appears only when a local trained artifact and matching metrics exist; scores are uncalibrated and remain review suggestions.

## D007 — Cross-release near-duplicate audit (accepted, 2026-10-18)

**Choice:** Keep exact deduplication during extraction and add a separate review-only similarity audit across releases (character TF-IDF 3–5 grams, cosine threshold 0.88). The current 571-entry corpus flags 20 candidate pairs.

**Why:** Deprecation and later removal notes can refer to the same API. If near-matching notes land in different splits, a grouped score may still benefit from familiar wording. A saved candidate list makes the risk visible.

**Limit:** Similarity alone cannot decide that two notes are equivalent. Human reviewers must decide whether cross-split pairs should be excluded or retained before final evaluation; the audit does not alter source rows or labels.

## D008 — First reviewed pilot and class gap (2026-10-18)

**Evidence:** Tilaksinh explicitly confirmed agent recommendations for rows 1–9 individually and rows 10–50 after receiving the full review draft. Each local CSV row records his name, timestamp, and agent-assistance note; this is human-confirmed review, not blind independent labeling. Of 50 decisions, one is `UNCLEAR` and 49 are model-usable. The five class counts are API/code 29, configuration/deployment 6, data/schema 5, UI/output 9, and No targeted check stated 0.

**Choice:** Train the fixed baseline for an end-to-end MVP demonstration, mark its result as `pilot`, and keep the fifth label visible as untrained. Do not tune on the ten-row test release or claim five-class performance. Seed 42 yields train/dev/test sizes 30/9/10 across disjoint Django releases; test accuracy is 0.60 and five-label macro-F1 is 0.276. The model predicts API/code on 9 of 10 test rows. The keyword baseline is slightly higher on macro-F1 (0.280). These numbers show the workflow runs and expose severe class support limits.

**Next decision:** If more review time is available, deliberately sample notes that might meet `No targeted check stated`, have a reviewer decide them using the fixed guide, and review minority-class examples across releases. If that class remains absent, evaluate a four-class target only after recording a separate taxonomy decision and retraining from a fresh frozen split. Do not relabel the current data merely to fill a class.

## D009 — Shareable pilot labels (2026-10-18)

**Choice:** Keep the original reviewer CSV with name, exact UTC timestamps, and detailed notes local and ignored. Commit `data/processed/pilot_reviewed_labels.csv` as a shareable export of the same 50 confirmed decisions, replacing the reviewer name with `Human reviewer (agent-assisted)` and truncating timestamps to the true review date.

**Why:** A clean GitHub clone can reproduce the pilot model without publishing the detailed local annotation record. The export preserves label values, entry IDs, and technical review notes, and openly discloses agent assistance. Training from this export reproduces the same 30/9/10 split and 0.276 test five-label macro-F1.

**Limit:** The public export is a release artifact, not a separate independent annotation. If a decision changes locally, regenerate and validate the export before a new model run. The original reviewer identity and exact review time are not reconstructable from the export.


## D010 — Second human review batch and new evaluation boundary (2026-10-28)

**Evidence:** Kavya explicitly confirmed 50 separate source-linked suggestions, keeping three mixed rows as `UNCLEAR`. The resulting batch has 47 five-class labels. A new Bhargav batch contains 50 different source rows and remains draft until his review. The local named record and a reviewer-name-free export are separate, as in D009.

**Choice:** Preserve the reviewed Kavya labels, exclude `UNCLEAR` from training, and present the next reviewer with suggested labels plus reasons while saving no decision before confirmation. Sample different releases and sections and reject obvious near-duplicates; do not force the absent fifth class.

**Evaluation consequence:** The original test release has now been viewed during broader annotation. Keep its reported score as a pilot diagnostic only. Before a final model claim, audit near-duplicates and freeze a fresh release-grouped evaluation split; record class support and baselines again.


## D011 — Merge 150 reviewed entries and continue bounded batches (2026-10-28)

**Evidence:** Bhargav explicitly confirmed all 50 proposed decisions, retaining two `UNCLEAR` rows. The three reviewed batches contain 150 distinct source IDs: 144 model-usable labels and six `UNCLEAR`. The observed model classes have counts 64/22/26/32/0 in guide order.

**Choice:** Keep each named review file local and ignored, publish a date-only alias export per batch, and regenerate `data/processed/reviewed_labels.csv` with a validator that rejects duplicate or unknown IDs. Prepare a separate 50-row fourth suggestion batch without assigning a reviewer or treating those suggestions as labels.

**Limit:** The fourth batch is not a random test sample. The fifth class still has zero reviewed examples; do not force it. If further review finds none, make an explicit four-class taxonomy decision and fresh evaluation plan before presenting final classification quality. The old pilot test score remains a historical diagnostic.


## D012 — Fourth human review batch (2026-10-28)

**Evidence:** Om explicitly confirmed all 50 source-linked suggestions in Batch 04. There were no changed labels and no `UNCLEAR` decisions in this batch. The four batches now contain 200 distinct confirmed IDs: 194 model-usable labels and six `UNCLEAR`. Label support is 89/29/36/40/0 in the guide's five-class order.

**Choice:** Save Om's named, timestamped record only in ignored local annotations, publish a reviewer-name-free export, and regenerate the validated merged CSV from all four shareable batch exports. Keep the fifth class visible but untrained while further evidence is collected; do not manufacture examples.

**Next decision:** Review the remaining 371 source entries in manageable batches or select a defensible smaller set for final training. Before a final score, resolve the absent fifth class, audit cross-release near-duplicates, and freeze a new release-grouped evaluation. The previous score describes only the original pilot.


## D013 — Larger fifth review batch (draft, 2026-11-01)

**Choice:** Prepare 100 distinct unlabeled entries for Tilak to review in one sheet: 19 from each feature release 4.2, 5.0, 5.1, 5.2, and 6.0, and five patch-release notes. Exclude all 200 confirmed IDs, obvious near-duplicates, and incomplete flattened fragments. Attach a source link and a text-based reason to every draft suggestion. Save no human label before Tilak's explicit confirmation.

**Why:** A larger batch reduces review handoffs while preserving source and release variety. It is an annotation work queue, not a random sample for final evaluation or a way to fill class quotas. Five mixed rows are proposed as `UNCLEAR`; no row clearly supports the still-unobserved fifth class.

**Limit:** Reviewers may find additional extraction defects or disagree with the suggestions. `EXCLUDE` is a review instruction, not a model class. The confirmed dataset remains 200 rows until the review is complete, and the old model score still reflects only the original pilot.


## D014 — Tilak confirmation and next reviewer queue (2026-11-01)

**Evidence:** Tilaksinh explicitly confirmed every proposal in the 100-row batch. Five remain `UNCLEAR`; the other 95 add 40 API/code, 15 configuration/deployment, 19 data/schema, and 21 UI/output labels. The five reviewed batches now have 300 distinct IDs, 289 model labels, and 11 `UNCLEAR` states. The fifth target class still has zero confirmed support.

**Choice:** Store Tilak's named, timestamped decisions locally, publish a name-free date-only export, and regenerate the validated merged CSV. Prepare 50 new draft entries for Kavya: ten per feature release. Only two patch-release candidates survived the existing text-length, fragment, and near-duplicate filters, so this queue does not claim patch-release coverage. Each draft label has a text-based reason and a source link; human-decision fields remain blank.

**Risk and next decision:** All confirmed batches involved visible agent suggestions, so they do not measure independent annotator agreement. One Kavya draft row may fit the previously absent `No targeted check stated` class; she must review it under the fixed guide before it counts. Recheck data quality, class support, and cross-release duplicates before a new held-out evaluation. The existing model score remains pilot-only.


## D015 — Kavya confirmation and Om's larger queue (2026-11-01)

**Evidence:** Kavya explicitly confirmed all 50 proposals in her second batch, including two `UNCLEAR` states and one `No targeted check stated` label. Six reviewed batches now contain 350 distinct IDs: 337 model labels and 13 `UNCLEAR`. Confirmed class support is 146/49/68/73/1 in guide order.

**Choice:** Keep Kavya's named, timestamped record local, publish a name-free date-only export, and regenerate the validated merge. Prepare 100 source-linked draft suggestions for Om from remaining IDs: 26 from Django 4.2, 32 from 5.0, 12 from 5.1, and 30 from 6.0. Filter obvious near-duplicates and incomplete fragments. Remaining 5.2 entries failed the current similarity filter; patch-release candidates were too few for a balanced quota. Suggestions have reasons and blank human-decision fields.

**Risk and next decision:** One confirmed fifth-class example is insufficient for a meaningful class-specific score. Om's row 13 is only a suggestion. All reviews so far showed recommendations to reviewers, so they do not estimate independent agreement. Audit cross-release similarity and select a fresh held-out split before retraining; the original model score remains pilot-only.


## D016 — Om confirmation and broader final annotation queue (2026-11-01)

**Evidence:** Om explicitly confirmed all 100 proposals in his second batch, including one `No targeted check stated` label and no `UNCLEAR`. Seven reviewed batches now contain 450 distinct IDs: 437 model labels and 13 `UNCLEAR`. Confirmed class support is 199/60/87/89/2 in guide order.

**Choice:** Keep Om's named, timestamped record local, publish a name-free date-only export, and regenerate the validated merge. Prepare 50 source-linked draft suggestions for Bhargav from unused IDs: 14 from Django 4.2, 17 from 5.0, 10 from 5.1, and 9 from 6.0. Exclude incomplete fragments and text pairs at SequenceMatcher similarity at least 0.96. The prior 0.88 threshold left only 27 unused candidates; widening this annotation queue allows review of related release entries without claiming that they are independent evaluation examples.

**Risk and next decision:** The 0.96 queue can contain near-duplicate entries by the earlier 0.88 audit criterion. Cluster or exclude cross-split related notes before a final model score. Two fifth-class labels are still inadequate for a class-specific quality claim. Om's confirmation was non-blind because suggestions were visible. The original model score remains pilot-only.


## D017 — Bhargav confirmation and full-corpus disposition queue (2026-11-01)

**Evidence:** Bhargav explicitly confirmed all 50 proposals in his second batch. Eight reviewed batches contain 500 distinct IDs: 487 model labels and 13 `UNCLEAR`. Confirmed class support is 219/81/94/91/2 in guide order. Exactly 71 source IDs remain without a decision.

**Choice:** Keep Bhargav's named, timestamped record local, publish a name-free date-only export, and regenerate the validated merge. Present every remaining ID to Kavya without the earlier text-length and similarity filters. Propose labels for 44 substantive entries and `EXCLUDE` for 27 incomplete or generic extraction fragments. `EXCLUDE` is a corpus-quality disposition, not a sixth class; await her explicit review before creating the exclusions CSV or adding any of the 44 labels.

**Risk and next decision:** Similar entries across releases remain in the annotated corpus; a final grouped split must audit or cluster them to prevent leakage. The fifth class has only two confirmed examples. After Kavya reviews the final queue, reconcile every source ID to one label, `UNCLEAR`, or exclusion and record exact counts. The original model score remains pilot-only.


## D018 — Complete source disposition and public corpus (2026-11-01)

**Evidence:** Kavya explicitly confirmed all 71 decisions in the final queue: 44 model labels and 27 exclusions. Across nine batches, all 571 pinned source IDs have exactly one disposition: 531 five-class labels, 13 `UNCLEAR`, and 27 `EXCLUDE`. Confirmed class support is 233/91/106/96/5 in guide order. The 27 exclusions are non-standalone fragments or headings, not negative examples. Reviewers saw proposed decisions, so these labels do not measure independent agreement.

**Choice:** Keep Kavya's named, timestamped label and exclusion records local. Publish a name-free label export and an exclusion CSV with IDs, reasons, and dates. Regenerate the 544-row reviewed-label merge and a 571-row `annotated_corpus.csv` that preserves source provenance, decisions, and a model-only target column. A new builder rejects missing IDs, overlaps, unknown IDs, and malformed exclusions. Keep historical queue and suggestion files as review provenance.

**Next decision:** The five examples in `No targeted check stated` are still sparse. Review cross-release near-duplicate families, freeze a fresh grouped split, then retrain and report baselines, per-class support, errors, and uncertainty. Until then, the 0.276 macro-F1 and local artifact remain pilot-only. Refresh the presentation and UI after the final evaluation.

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

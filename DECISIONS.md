# Decision log

Each decision records the choice, evidence, alternatives, and what would change it. A model configuration is not an experimental result; measured performance enters this log only after human labeling and a frozen evaluation.

## D001 — Project and source domain (accepted, 2026-10-17)

**Choice:** Build PatchProbe for software release-note verification triage using version-pinned Django notes.

**Why:** The user chose this classification task after an originality audit. Official Django notes provide discrete entries, stable source revisions, and an offline demo without paid APIs.

**Boundary:** Prior work covers release-note change types and action-required summaries; PatchProbe targets a first downstream verification area. This is a scoped classroom originality claim, not a worldwide-first claim. Training on Django alone cannot show cross-ecosystem generalization.

## D002 — Labels and human review (accepted for pilot, 2026-10-17)

**Choice:** Keep five suggested verification areas and a separate `UNCLEAR` review state. A person chooses the label from the note text. Start with a guided 50-entry pilot and measure effort before scaling.

**Why:** Tilaksinh is unavailable for several hours but is willing to label with row-by-row explanation later. No one has authorized the agent to fabricate human ground truth. A small pilot tests whether the definitions are usable and how much review time is realistic. The current working estimate is 45–90 minutes for 50 rows, to be replaced with observed time.

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

**Limit:** A release-grouped score tests held-out Django releases, not later chronological upgrades or other projects. If a class lacks sufficient support, the run is marked a pilot rather than presented as a valid five-class result. There are no real metrics yet.

## D006 — User interface and privacy (accepted, 2026-10-17)

**Choice:** Use a local Streamlit one-row review screen that saves reviewer name, timestamp, decision, and optional note to a CSV. Keep labels, raw upstream cache, and trained artifacts out of Git by default.

**Why:** The user requested one-by-one help while labeling later. A local interface makes progress visible, allows correction, and keeps the human decision explicit. Streamlit is quick to run for a presentation.

**Limit:** Concurrent reviewers must use distinct label files; the CSV is not a shared production annotation service. Prediction review appears only when a local trained artifact and matching metrics exist; scores are uncalibrated and remain review suggestions.

## D007 — Cross-release near-duplicate audit (accepted, 2026-10-18)

**Choice:** Keep exact deduplication during extraction and add a separate review-only similarity audit across releases (character TF-IDF 3–5 grams, cosine threshold 0.88). The current 571-entry corpus flags 20 candidate pairs.

**Why:** Deprecation and later removal notes can refer to the same API. If near-matching notes land in different splits, a grouped score may still benefit from familiar wording. A saved candidate list makes the risk visible.

**Limit:** Similarity alone cannot decide that two notes are equivalent. Human reviewers must decide whether cross-split pairs should be excluded or retained before final evaluation; the audit does not alter source rows or labels.


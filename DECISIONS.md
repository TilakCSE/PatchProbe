# Decision log

Each entry records the decision, its basis, alternatives, and what would change it. Status can be accepted, provisional, or open. Do not turn a provisional choice into an experimental result.

## D001 — Project and source domain (accepted, 2026-10-17)
**Choice:** Build PatchProbe around versioned Django release notes for a course MVP.
**Why:** The user selected PatchProbe after an originality audit. Django publishes official, discrete release-note entries, source files, and release identifiers; an offline demo requires no paid API.
**Alternatives:** CrisisQueue and other shortlist projects were set aside by the user.
**Risk:** A classifier may reflect Django writing conventions rather than generalize to other ecosystems. External transfer is future work.

## D002 — Human-label assumption and pivot (open, 2026-10-17)
**Earlier proposal:** Manually label 600–800 entries into five regression-check areas, beginning with a 50-entry pilot.
**New evidence:** Tilaksinh cannot label while away for several hours, but is willing to label later if the agent explains the task row by row. The team will measure pilot labeling time before committing to 600–800 rows. Without independent labels, five-way performance cannot be honestly reported.
**Current direction:** Keep the original five-label target and build a guided one-row-at-a-time annotation queue. Prepare a 50-entry pilot now; wait for human decisions before training and reporting five-class results.
**Alternatives under evaluation:** If the pilot is too slow or agreement is poor, consider a narrower taxonomy or a heading-derived proxy task. Heading labels would measure editorial categories, not actual regression-check correctness.
**Pivot trigger:** If pilot labeling is too slow, the five classes lack enough examples, or annotators cannot apply the guide consistently, narrow the scope or change the target rather than fabricate gold labels.

## D003 — Model family (provisional, 2026-10-17)
**Starting point:** TF-IDF word and character n-grams with logistic regression or a linear SVM; compare with a majority baseline.
**Why:** Short technical entries contain identifiers, spelling variants, and sparse cues. These models run on a CPU and expose feature weights for a presentation.
**Unchosen for MVP:** Transformer fine-tuning, RAG, and LLM classification add compute, cost, or uncontrolled behavior before a valid target is established.
**Open details:** Vocabulary limits, n-gram ranges, regularization, and any embedding dimension are not selected. Record them after training-only tuning and measurement.

## D004 — Evaluation (provisional, 2026-10-17)
**Plan:** Hold out entire release versions; report class counts, majority baseline, macro-F1, per-class precision and recall, confusion matrix, and example errors.
**Why:** Adjacent entries in one release can share wording, and random paragraph splits risk optimistic results.
**Limit:** If labels come from headings, metrics estimate heading-proxy prediction on held-out releases, not correctness of downstream test recommendations.
**Open details:** Exact versions, dates, and split sizes depend on source audit and class support.

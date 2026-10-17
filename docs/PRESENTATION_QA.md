# Presentation guide and likely professor questions

## One sentence
PatchProbe helps a developer review a dependency upgrade by routing each release-note entry to a suggested area for the first downstream verification check.

## Pipeline to show
Official versioned notes → entry extraction and provenance → five-label human annotation → release-grouped split → training-only TF-IDF → linear model → held-out evaluation → review board with source links.

## Likely questions
**What is original?** The exact routing target, label guide, small reviewed dataset, leakage-aware experiment, and reviewer workflow. We do not claim no similar system exists anywhere.

**Who uses it?** Developers, QA engineers, and maintainers planning upgrade checks. They retain the final decision.

**Why no blanket stopword removal?** Negation and words such as removed, required, and unsupported matter in technical notes. Document-frequency filtering can still remove very common terms.

**Why TF-IDF and a linear model?** It is fast, reproducible on a CPU, appropriate for a small dataset, and its feature weights can be inspected. Compare it to simple baselines before adding complexity.

**Why split by release?** Notes within one release share wording and context. Holding out releases better tests transfer to an unseen version.

**What does the metric mean?** It measures agreement with the team's documented human label decisions on held-out releases. It does not measure whether a codebase passes its actual upgrade tests.

**Why five classes?** Four concrete downstream check surfaces plus a no-targeted-check class. UNCLEAR is a review state so ambiguous notes are not forced into training.

**What are the limitations?** A note may imply multiple checks; a single lane cannot certify compatibility; the corpus is Django-specific; and results depend on annotation consistency.

Add exact counts, model settings, error examples, and live demo steps after implementation.

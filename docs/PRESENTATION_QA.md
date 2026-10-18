# Presentation guide and likely professor questions

Team 8 should be ready for the earliest possible date, Monday 2026-10-19. The turn may instead be 21 or 23 October; the rubric has not been supplied.

## One sentence

PatchProbe helps a developer review a dependency upgrade by routing each release-note entry to a suggested area for the first downstream verification check.

## Five-minute walkthrough

1. State the task boundary: classify one published Django release-note entry into one of four verification areas or `No targeted check stated`. `UNCLEAR` is a human review state, not a sixth model label.
2. Show the source manifest: 14 pinned release-note RST files, 571 unlabeled extracted entries, source URLs/hashes, and a 50-entry pilot with 10 from each of Django 4.2, 5.0, 5.1, 5.2, and 6.0.
3. Open `python -m streamlit run app.py`. Read one entry, consult the label guide, make a human choice, save, and show resume/revisit. Demonstrate `UNCLEAR` for an ambiguous note.
4. Explain the model pipeline: note `text` only → release-grouped split → training-only word 1–2 and character 3–5 TF-IDF → balanced logistic regression → majority and keyword baselines → per-class metrics and errors. No stopword-removal step is required. No dense embedding dimension exists.
5. If a human-labeled model has been trained, show its real held-out results and a prediction in the app. If labels are still pending, show the deliberate training gate and describe the annotation pilot as the current deliverable. Never substitute synthetic test fixtures for measured accuracy.

## Likely questions

**What is original?** The exact routing target, label guide, curated human-reviewed subset, release-aware experiment, and reviewer workflow. The literature review finds adjacent work on release-note change types and test selection; we do not claim worldwide uniqueness.

**Who uses it?** Developers, QA engineers, and maintainers planning upgrade checks. They retain the final decision.

**What exactly is in the dataset?** One row is a candidate note entry, usually a substantive bullet or prose block, extracted from official release notes. Each has an ID, release, exact source URL/revision, section path, raw RST, and cleaned text. The 571 current rows have **no target labels**. A separate CSV stores explicit reviewer decisions.

**Why these five labels?** Four practical downstream check surfaces cover API/code, configuration/deployment, data/schema, and UI/output behavior. `No targeted check stated` prevents inventing a check when a note does not support one. `UNCLEAR` preserves ambiguity instead of forcing a class.

**Why no blanket stopword removal?** Small words and negation can change technical meaning. TF-IDF already downweights very common terms; the pipeline retains the original cleaned wording.

**Why TF-IDF and logistic regression?** It is reproducible on a CPU and suitable as a transparent starting point for a small labeled dataset. Character features help with identifiers and spelling variants. The model is a baseline until human-labeled evaluation demonstrates its quality.

**Why split by release?** Notes within one release can share wording and context. Whole-release holdout reduces this leakage path. It does not prove performance on future releases or other software ecosystems.

**What does the metric mean?** It measures agreement with documented human decisions on held-out Django releases. It does not measure whether an actual application passes upgrade tests. Macro-F1 highlights weak minority classes; report per-class support and errors alongside it.

**What if labels are missing or classes are rare?** The training command stops without human labels. A small or class-sparse run is marked a pilot, not a validated five-class result. The 50-row pilot measures annotation time and guide clarity before the team commits to a larger review set.

**What are the main limitations?** A note may imply several checks; RST extraction can lose context; Django-only writing style limits transfer; labels can vary between reviewers; classifier scores are not calibrated. The product recommends a first review area, not a compatibility guarantee.

Record the actual presentation date, rubric, labeling time, class counts, split sizes, model feature count, and held-out errors here when they are known.

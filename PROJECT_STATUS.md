# Project status

Updated 2026-10-28.

## Current annotation status

- The original pilot, Kavya's batch, and Bhargav's batch each contain 50 human-confirmed decisions. The merged shareable file is `data/processed/reviewed_labels.csv` and can be regenerated with `python scripts/merge_reviewed_labels.py`.
- Across all 150 reviewed rows, **144 have a model label and six remain `UNCLEAR`**. The observed model-label counts are API/code 64, configuration/deployment 22, data/schema 26, UI/output 32, and No targeted check stated 0. The source corpus has 571 entries, leaving 421 unreviewed.
- The named reviewer files remain ignored locally. The three shareable batch exports contain reviewer aliases and date-only timestamps. Bhargav confirmed all 50 suggestions, including two `UNCLEAR` rows.
- A distinct 50-row fourth batch is at `docs/BATCH_04_REVIEW.md`. It is assigned to Om Nathani for review and has no saved human decisions yet.
- The published 0.276 five-label macro-F1 belongs to the **original 49-label pilot only**. New labels include entries from the old held-out release. Freeze a fresh release-grouped split and audit near-duplicates before reporting a final model score. The fifth class still has zero support; do not invent labels to fill it.

## Historical MVP snapshot from 2026-10-18

## Working now

- The authoritative checkout is `D:\Development\Projects\PatchProbe`. Earlier sibling worktrees were temporary Git checkouts for parallel agent work; their code was integrated and the three extra folders were removed. The local feature branches remain as recovery points.
- The pinned Django extractor yields 571 unlabeled candidate entries from 14 source files. The 50-entry pilot has 10 entries from each of Django 4.2, 5.0, 5.1, 5.2, and 6.0. Source URLs, revisions, hashes, and license notice are recorded. The 14 raw files are cached inside the primary checkout for offline rebuilding.
- The Streamlit app guides one human decision at a time, saving and resuming labels. A prediction review mode is implemented and remains hidden until local training produces a model and matching metrics.
- The CPU-only TF-IDF/logistic-regression training program uses release-grouped splits, majority and keyword baselines, and auditable output. It refuses to train without human labels.
- All 23 tests pass in the system Python; the offline dataset rebuild also passes. A reproducible audit flagged 20 cross-release near-duplicate candidate pairs at character TF-IDF similarity ≥ 0.88; those pairs need human review before final evaluation. The local virtual-environment install succeeded. All 23 tests pass there; the Streamlit health and landing endpoints return HTTP 200, both app modes render, and a sample note returns a pilot prediction.
- The repository is authenticated for local GitHub push. Codex Cloud setup is deferred at the user's request.

## Remaining for a credible presentation

1. The 50-entry pilot is complete: 49 model labels and one `UNCLEAR`. Class counts are API/code 29, configuration/deployment 6, data/schema 5, UI/output 9, and No targeted check stated 0. These were human-confirmed after agent recommendations, not independent blind labels. Record the actual review time when known.
2. The first release-held-out pilot run uses 30 train, 9 dev, and 10 test entries. Its five-label macro-F1 is 0.276 on the 10-row test release, with 0 support for one label; do not cite this as validated five-class quality. Review more entries for class coverage and leakage before a final result.
3. Rehearse the verified local app and prepare concise slides. The app runs with `.\.venv\Scripts\python.exe -m streamlit run app.py` from the project root. The first demo should show the 50/50 review count, the pilot warning, and one prediction.
4. Obtain the rubric if one is provided. The presentation slot is not yet confirmed beyond the possible dates above.

## Boundaries

All 50 human-confirmed, agent-assisted pilot decisions are saved locally; a reviewer-name-free export is committed for clean-clone reproduction. The 49 usable labels support a pilot model only. The default UI is an annotation aid. Django-only notes limit generalization. A suggested verification area is a triage aid, not assurance of upgrade safety. Similar release notes across different versions remain a leakage risk to audit before final evaluation.

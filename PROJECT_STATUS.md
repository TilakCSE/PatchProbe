# Project status

Updated 2026-10-18.

## Working now

- The authoritative checkout is `D:\Development\Projects\PatchProbe`. Earlier sibling worktrees were temporary Git checkouts for parallel agent work; their code was integrated and the three extra folders were removed. The local feature branches remain as recovery points.
- The pinned Django extractor yields 571 unlabeled candidate entries from 14 source files. The 50-entry pilot has 10 entries from each of Django 4.2, 5.0, 5.1, 5.2, and 6.0. Source URLs, revisions, hashes, and license notice are recorded. The 14 raw files are cached inside the primary checkout for offline rebuilding.
- The Streamlit app guides one human decision at a time, saving and resuming labels. A prediction review mode is implemented and remains hidden until local training produces a model and matching metrics.
- The CPU-only TF-IDF/logistic-regression training program uses release-grouped splits, majority and keyword baselines, and auditable output. It refuses to train without human labels.
- All 23 tests pass in the system Python; the offline dataset rebuild also passes. A reproducible audit flagged 20 cross-release near-duplicate candidate pairs at character TF-IDF similarity ≥ 0.88; those pairs need human review before final evaluation. A virtual-environment installation and Streamlit smoke test are in progress.
- The repository is authenticated for local GitHub push. Codex Cloud setup is deferred at the user's request.

## Remaining for a credible presentation

1. Tilaksinh or teammates review the 50-entry pilot with row-by-row help, measure actual time, and resolve confusing definitions. The provisional estimate is 45–90 minutes for 50 entries.
2. Review enough additional entries for class coverage across releases. Freeze the guide and split, then train and report actual per-class metrics and errors. If support remains small, present it honestly as a pilot.
3. Finish the virtual-environment install, smoke-test the Streamlit app, and prepare a concise presentation walkthrough and slides.
4. Confirm the presentation date and rubric when available.

## Boundaries

There are no human labels or trained-model accuracy claims yet. The default UI is an annotation aid. Django-only notes limit generalization. A suggested verification area is a triage aid, not assurance of upgrade safety. Similar release notes across different versions remain a leakage risk to audit before final evaluation.

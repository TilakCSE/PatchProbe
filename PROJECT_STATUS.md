# Project status

Updated 2026-11-01.

## Current annotation status

- The full 571-entry source corpus has a confirmed disposition: **531 model labels, 13 `UNCLEAR`, and 27 `EXCLUDE`**. The merged labels file has 544 rows; the exclusions file has 27. The [full annotated corpus](data/processed/annotated_corpus.csv) joins every decision with source text and provenance. See [annotation progress](docs/ANNOTATION_PROGRESS.md).
- Five-class support is API/code 233, configuration/deployment 91, data/schema 106, UI/output 96, and No targeted check stated 5. The fifth class remains sparse.
- Kavya confirmed all 71 proposals in [the final review sheet](docs/KAVYA_FINAL_71_REVIEW.md): 44 model labels and 27 exclusions for non-standalone extracted fragments. The ignored local records keep her name and exact timestamps; public files omit them.
- `python scripts/merge_reviewed_labels.py` regenerates the merged 544-row labels file from nine exports. `python scripts/build_annotated_corpus.py` verifies complete non-overlapping coverage and writes the 571-row annotated corpus. The full test suite passes (28 tests on 2026-11-01).
- The existing 0.276 five-label macro-F1 and local model artifact still describe the original **49-label pilot only**. A new release-grouped split, duplicate audit, retraining, and per-class evaluation are the next work. The later annotation batches were non-blind confirmation of visible suggestions and cannot estimate independent reviewer agreement.
- Presentation slides, speaking guide, and live demo were prepared for the original pilot and need a refresh after final evaluation. The Streamlit UI currently loads the local pilot model until a newly evaluated artifact replaces it.

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

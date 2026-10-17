# Project status

Updated 2026-10-17.

## Working now

- The selected PatchProbe task, five-label guide, originality boundary, and team roster are documented.
- The pinned Django extractor produced 571 unlabeled candidate entries from 14 source files and a 50-entry human review pilot. Source URLs, revisions, hashes, and a license notice are recorded.
- The one-row-at-a-time Streamlit annotation app can save, resume, skip, and revisit decisions. It exposes an explanation prompt without generating a gold label.
- The TF-IDF/logistic-regression training program, release-grouped split, baselines, audit files, and tests are implemented. Training intentionally requires human labels.
- GitHub local authentication works, and the initial documentation commits were pushed to `TilakCSE/PatchProbe`.

## Remaining for a credible presentation

1. Tilaksinh or teammates review the 50-entry pilot, measure time, and resolve confusing label definitions. The working estimate is 45–90 minutes for 50 entries, to be revised from actual time.
2. Review enough additional entries for class coverage across releases. Freeze the guide and split, then train and report real per-class metrics and examples. If the pilot is too small or imbalanced, present it honestly as a pilot.
3. Run the app and final checks in the presentation environment; prepare a concise demo walkthrough and slides.
4. Confirm the presentation date and rubric.
5. Select and publish `TilakCSE/PatchProbe` as a Codex Cloud environment if off-laptop work is needed. Local GitHub authentication does not establish Cloud access. The mobile app currently shows the user only `Base Environment`.

## Boundaries

No human labels have been submitted yet, so there are no trained-model accuracy claims. The UI is an annotation aid, not a live prediction product. Django-only notes limit generalization to other ecosystems. A suggested verification area is a triage aid, not an assurance of upgrade safety.

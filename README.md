# PatchProbe

PatchProbe is a course NLP project for routing software release-note entries to a suggested area of downstream verification. The intended user is a developer or QA reviewer planning checks after a dependency upgrade.

**Status: project setup.** The previous research plan proposed five human-created labels on Django release-note paragraphs. The team has said it cannot currently label examples, so the final target and source of evaluation labels must be resolved before training. There are no model results yet.

## Team
- Tilaksinh Chauhan (23000740)
- Kavya Jariwala (23000543)
- Bhargav Panchal (23000502)
- Om Nathani (23000883)

## MVP contract
1. Obtain versioned Django release-note text with provenance.
2. Form document entries and labels from an explicitly documented source.
3. Train a CPU-friendly classifier with a release-aware split.
4. Show class metrics, concrete errors, and any abstention behavior.
5. Display predictions alongside original source links for human review.

The five-label taxonomy is documented; guided human labeling is planned after the 50-entry pilot is prepared. See DECISIONS.md, PROJECT_STATUS.md, and docs/DATA_AND_LABELS.md.

## Source and research
- Official Django release notes: https://docs.djangoproject.com/en/6.0/releases/
- Django source files: https://github.com/django/django/tree/main/docs/releases
- Earlier research: NEW_PROJECT_SHORTLIST.md and NOVELTY_AUDIT.md in the NLP Mid-Sem research folder. The focused literature survey is in docs/LITERATURE_SURVEY.md.

Closest work found in the earlier audit addresses release-note change types and action-required summaries. PatchProbe's intended output is a verification area. This is a scoped classroom originality claim, not a worldwide-first claim.

The authoritative code folder is D:/Development/Projects/PatchProbe.

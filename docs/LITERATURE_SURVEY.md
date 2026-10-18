# Focused literature survey and novelty boundary

Checked 2026-10-17. These sources establish the problem context and the closest adjacent work; PatchProbe is an independently defined classification product, not an attempt to repair one paper.

| Source | What it studied or built | Relationship to PatchProbe |
| --- | --- | --- |
| [Django's upgrade guide](https://docs.djangoproject.com/en/6.0/howto/upgrade-version/) | Tells upgraders to read each relevant release note, focus on backwards-incompatible changes, and run their application tests. | Establishes the real review workflow. It does not supply verification-area labels for individual notes. |
| [Wu et al., Demystifying Software Release Note Issues on GitHub, ICPC 2022](https://arxiv.org/abs/2203.15592) | Analyzed 1,731 release-note-related GitHub issues and organized their problems into content, presentation, accessibility, and production. | Evidence that release-note quality and findability matter. Its observations are about issues in producing/using notes, not classifying each note by a downstream check area. |
| [Jiang et al., DeepRelease, 2022](https://arxiv.org/abs/2201.06720) | Generated release-note entries from pull-request text and classified broad change types such as features and fixes; evaluated on more than 46,000 notes. | The closest classification precedent in this review. Its input is PR text and its target is change type; PatchProbe reads already published note entries and predicts a verification lane. |
| [Pan et al., Test Case Selection and Prioritization Using Machine Learning, 2021](https://arxiv.org/abs/2106.13891) | Surveyed 29 ML-based regression-test selection/prioritization studies. | Shows that choosing concrete tests is an established, deeper engineering problem. PatchProbe only suggests a broad check area and does not select or run tests. |

## Exact task boundary
Input: one published Django release-note entry, without the source heading or release metadata as model features.

Output: one of four downstream verification areas or “no targeted check stated,” plus a separate UNCLEAR review state for ambiguous entries. The prediction is a suggested first review lane, not a severity label, breaking-change detector, generated test, or compatibility certificate.

The earlier targeted search found adjacent release-note category work and test-selection work, but not a ready dataset with these exact five human-reviewed labels. Search absence does not prove worldwide novelty. We will describe the contribution as our taxonomy, annotated subset, release-aware evaluation, and reviewer workflow.

## Methodological implications
- Published notes may contain several changes in one paragraph; extraction and UNCLEAR handling matter.
- Django release headings can leak a likely answer. Keep them as provenance only.
- A random paragraph split may share wording from one release across train and test. Hold out releases.
- Genuine five-class evaluation requires human decisions. Agent suggestions alone or heading-derived labels are not ground truth. This pilot uses explicit human confirmation after an agent recommendation; report that assistance and, if possible, have a second reviewer independently label a subset.
- A simple sparse-text model gives a transparent benchmark before considering a larger model.

## Source reuse
Django's repository carries a [BSD 3-Clause license](https://github.com/django/django/blob/main/LICENSE). Preserve its copyright/license notice if distributing derived source text. Record the exact upstream revision used for extraction.

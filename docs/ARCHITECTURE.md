# Architecture and stack

## End-to-end flow

```text
Official Django release-note RST at pinned Git commits
  → source cache, SHA-256 manifest, and entry extraction
  → `entries.csv` with 571 source candidates
  → human-confirmed labels, UNCLEAR states, and exclusions
  → `annotated_corpus.csv` with complete source coverage
  → chronological release-grouped train/dev/test split and similarity audit
  → train-only word (1–2) and character (3–5) TF-IDF
  → balanced logistic regression and two simple baselines
  → class metrics, errors, split manifest, and evaluated model for Streamlit
  → separate all-label fit and portable JSON export for the Next.js portal
```

`UNCLEAR` and `EXCLUDE` are recorded in the annotation workflow and excluded from five-class training. The complete review has 531 model labels, 13 `UNCLEAR`, and 27 `EXCLUDE`. The interface shows note text first; source section headings are available in collapsed provenance so they do not silently become target cues. Only the `text` field enters the model. Release IDs are used to keep whole releases in one split. The fitted TF-IDF vocabulary is learned on training rows only.

## Files and responsibilities

| Location | Responsibility |
| --- | --- |
| `src/patchprobe/ingest.py`, `scripts/build_dataset.py` | Fetch pinned upstream files, parse entries, deduplicate exact text, select the pilot, write provenance. |
| `src/patchprobe/annotation.py`, `app.py` | Validate inputs, guide one decision at a time, save and resume review. |
| `src/patchprobe/model.py`, `scripts/train_model.py` | Validate human labels, make grouped splits, fit baselines and classifier, write auditable evaluation artifacts. |
| `src/patchprobe/inference.py`, `app.py` | Guard local model loading and show review-only predictions once a trained artifact exists. |
| `scripts/audit_near_duplicates.py` | Flag similar notes from different releases for human leakage review. |
| `scripts/merge_reviewed_labels.py`, `scripts/build_annotated_corpus.py` | Validate reviewer exports, exclusions, and full source-ID coverage. |
| `data/processed/` | Pinned source entries, public reviewed labels, exclusions, full annotated corpus, and manifest. |
| `data/annotations/`, `artifacts/`, `data/raw/` | Local reviewer decisions, trained outputs, and upstream cache; excluded from Git. |
| `scripts/train_full_corpus.py`, `scripts/probe_external_notes.py` | Rebuild the chronological evaluation and source-linked external qualitative probe. |
| `scripts/export_portal_model.py`, `scripts/check_portal_parity.py` | Export the all-label model to portable JSON and compare Python and Node scores. |
| `portal/src/app/`, `portal/src/lib/` | Next.js review portal, Node prediction routes, and dependency-free TF-IDF/logistic inference. |

## Dependencies and operation

Python 3.11+, pandas, scikit-learn, numpy, joblib, and Streamlit are declared in `pyproject.toml`; pytest is an optional development dependency. The portal uses Next.js, React, TypeScript, and Node as declared in `portal/package.json`. Both model fits run on a CPU. No dense embedding dimension is chosen: the evaluated model learned 4,970 word and 17,292 character sparse features (22,262 total). The full-data serving model has 32,140 features. No LLM, RAG, GPU, paid API, or runtime secret is needed for the MVP.

The annotation UI is deliberately local and writes a CSV; simultaneous reviewers should use separate output files. The primary checkout now has the evaluated 305-row training artifact for Streamlit, with 105 held-out test notes after similarity filtering. The status remains `pilot` because the fifth class has no dev/test support. A clean clone must run `scripts/train_full_corpus.py` before Streamlit prediction review appears.

The Next.js portal uses the committed portable JSON export of a **separate** model fitted on all 531 accepted labels. Server routes receive note text, validate length/count, run Node inference, and return a review suggestion with uncalibrated class scores; they do not save submitted text. The client supports single notes, CSV batches, and browser-session review drafts. This model has no independent held-out score of its own; the evaluated model measures the fixed recipe. The portable implementation matched Python on all 571 corpus notes and 15 external probes. See [PORTAL_DEPLOYMENT.md](PORTAL_DEPLOYMENT.md), [EVALUATION.md](EVALUATION.md), and [MODEL_CARD.md](MODEL_CARD.md) for exact limits.

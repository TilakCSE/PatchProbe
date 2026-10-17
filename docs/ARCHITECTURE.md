# Architecture and stack

## End-to-end flow

```text
Official Django release-note RST at pinned Git commits
  → source cache, SHA-256 manifest, and entry extraction
  → `entries.csv` plus a diverse 50-entry `pilot_queue.csv`
  → guided human decisions in `pilot_labels.csv`
  → release-grouped train/dev/test split and duplicate check
  → train-only word (1–2) and character (3–5) TF-IDF
  → balanced logistic regression and two simple baselines
  → class metrics, errors, split manifest, and saved model
```

`UNCLEAR` is recorded in the annotation workflow and excluded from five-class training. The interface shows note text first; source section headings are available in collapsed provenance so they do not silently become target cues. Only the `text` field enters the model. Release IDs are used to keep whole releases in one split. The fitted TF-IDF vocabulary is learned on training rows only.

## Files and responsibilities

| Location | Responsibility |
| --- | --- |
| `src/patchprobe/ingest.py`, `scripts/build_dataset.py` | Fetch pinned upstream files, parse entries, deduplicate exact text, select the pilot, write provenance. |
| `src/patchprobe/annotation.py`, `app.py` | Validate inputs, guide one decision at a time, save and resume review. |
| `src/patchprobe/model.py`, `scripts/train_model.py` | Validate human labels, make grouped splits, fit baselines and classifier, write auditable evaluation artifacts. |
| `data/processed/` | Small committed unlabeled dataset and manifest for an offline demo. |
| `data/annotations/`, `artifacts/`, `data/raw/` | Local reviewer decisions, trained outputs, and upstream cache; excluded from Git. |

## Dependencies and operation

Python 3.11+, pandas, scikit-learn, numpy, joblib, and Streamlit are declared in `pyproject.toml`; pytest is an optional development dependency. The app and baseline model run on a CPU. No embedding dimension is chosen: TF-IDF uses a sparse vocabulary whose size is learned from the training split. No LLM, RAG, GPU, paid API, or runtime secret is needed for the offline MVP.

The annotation UI is deliberately local and writes a CSV; simultaneous reviewers should use separate output files. The current UI does not serve model predictions because there is no labeled model to display. See [EVALUATION.md](EVALUATION.md) and [MODEL_CARD.md](MODEL_CARD.md) for gates and limits.

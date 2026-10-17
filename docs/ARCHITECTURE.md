# Architecture and planned stack

## Pipeline
Django versioned source files → entry extraction → provenance and duplicate checks → human annotation → release-grouped split → train-only TF-IDF → linear classifier → evaluation → Streamlit review board.

## Components
- Python 3 for data and modeling.
- A deterministic reStructuredText entry extractor. Use docutils if it makes hierarchy reliable; otherwise document a bounded parser for selected release files.
- CSV or Parquet for a small reviewed dataset, with a stable example ID and source link.
- pandas for inspection, scikit-learn for TF-IDF and linear classification, matplotlib for evaluation figures.
- Streamlit for a local annotation queue and release-note review board.
- pytest for extraction, provenance, split, and inference contract tests.

No GPU, live social-media API, LLM, RAG, paid service, or secret key is required for the offline MVP. Exact Python/package versions and commands will be pinned once the implementation is chosen.

## Presentation boundary
Until real labels exist, the app may demonstrate extraction and annotation but cannot claim trained five-class accuracy. The model and review board become a complete demonstration after the pilot and training set are labeled.

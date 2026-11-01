# PatchProbe agent instructions

## Purpose
Build a presentation-ready NLP classifier that routes Django release-note entries to suggested areas of downstream verification. Predictions are review suggestions, never proof that an upgrade is safe.

## Read first
Read README.md, DECISIONS.md, and PROJECT_STATUS.md before changing scope. All 571 extracted source IDs have human-confirmed dispositions: 531 model labels, 13 `UNCLEAR`, and 27 `EXCLUDE` (as of 2026-11-01). The complete corpus and public review exports are in `data/processed/`; named reviewer files remain ignored locally. The current full-corpus run uses a chronological release-grouped split and a documented near-duplicate filter. Its test score is a pilot result because the fifth class has no dev/test support; read `docs/MODEL_CARD.md` before changing or citing it. Streamlit uses the evaluated model; the Next.js portal uses a separate all-label model export.

## Working rules
- Keep the MVP focused: reproducible data collection, transparent labels, a defensible split, a baseline model, measured evaluation, and usable review interfaces.
- Use official versioned source data. Store source URL, release identifier, and extraction provenance for every example.
- Never present rules, pseudo-labels, synthetic labels, or document headings as independent human ground truth.
- Keep release metadata and headings out of model text when those fields produce labels. Split by release or another defensible group.
- Fit vectorizers and calibrators on training data only. Keep the held-out test set untouched until final evaluation.
- Document material choices and pivots in DECISIONS.md: alternatives, reason, evidence, and remaining risk.
- Record data version, license, counts, exclusions, split, seed, metrics, and failure modes in the relevant docs.
- Prefer a simple CPU-friendly baseline before adding a transformer, LLM, or RAG.
- Keep data acquisition and training runnable without secret credentials. Never commit secrets, virtual environments, downloaded corpora, or model binaries.
- Write focused tests for parsing, splitting, model export parity, and results that could otherwise be misleading. Run Python tests and the portal production build before merging.
- Keep implementation, data, and documentation in the primary `D:\Development\Projects\PatchProbe` checkout. Do not create sibling worktree folders unless the user requests them. Coordinate file ownership for parallel edits.
- Do not claim the project is globally first. Describe the exact task and limits of the originality search.

## Delivery gate
A contribution is ready when it runs from a clean checkout, tests pass, docs reflect reality, and limitations are visible in the demo and presentation.

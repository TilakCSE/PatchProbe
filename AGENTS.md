# PatchProbe agent instructions

## Purpose
Build a presentation-ready NLP classifier that routes Django release-note entries to suggested areas of downstream verification. Predictions are review suggestions, never proof that an upgrade is safe.

## Read first
Read README.md, DECISIONS.md, and PROJECT_STATUS.md before changing scope. The five-label human review plan remains the target. A guided 50-entry pilot is committed; all 50 decisions were human-confirmed with agent assistance and saved in the ignored local annotations CSV. The 571 candidate entries are unlabeled source text until a reviewer explicitly confirms individual labels. Do not report five-class results before reviewed labels and a defensible split exist.

## Working rules
- Keep the MVP narrow: reproducible data collection, transparent labels, a defensible split, a baseline model, measured evaluation, and a small demo.
- Use official versioned source data. Store source URL, release identifier, and extraction provenance for every example.
- Never present rules, pseudo-labels, synthetic labels, or document headings as independent human ground truth.
- Keep release metadata and headings out of model text when those fields produce labels. Split by release or another defensible group.
- Fit vectorizers and calibrators on training data only. Keep the held-out test set untouched until final evaluation.
- Document material choices and pivots in DECISIONS.md: alternatives, reason, evidence, and remaining risk.
- Record data version, license, counts, exclusions, split, seed, metrics, and failure modes in the relevant docs.
- Prefer a simple CPU-friendly baseline before adding a transformer, LLM, or RAG.
- Keep data acquisition and training runnable without secret credentials. Never commit secrets, virtual environments, downloaded corpora, or model binaries.
- Write focused tests for parsing, splitting, and results that could otherwise be misleading. Run the documented quality gate before merging.
- Keep implementation, data, and documentation in the primary `D:\Development\Projects\PatchProbe` checkout. Do not create sibling worktree folders unless the user requests them. Coordinate file ownership for parallel edits.
- Do not claim the project is globally first. Describe the exact task and limits of the originality search.

## Delivery gate
A contribution is ready when it runs from a clean checkout, tests pass, docs reflect reality, and limitations are visible in the demo and presentation.

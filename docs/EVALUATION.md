# Evaluation protocol

1. Freeze the five-label guide after the pilot and document any changes.
2. Store annotation provenance. Never replace a human label silently with an agent suggestion.
3. Make a deterministic release-grouped train/dev/test split and save a manifest.
4. Fit text transforms on train only. Choose features, model, regularization, and thresholds on dev only.
5. Compare against a majority baseline and a small transparent keyword baseline.
6. On held-out test releases, report accuracy, macro-F1, per-class precision/recall/support, and a confusion matrix.
7. Show representative correct, wrong, ambiguous, and low-confidence notes with links.
8. Report exclusions and abstentions; do not hide them from the demo.

A model cannot be validated against the same rules that generated its labels and called independently correct. If the gold set is too small or some classes lack support, report a pilot result with its limitation rather than a misleading percentage.

## Near-duplicate audit

Run `python scripts/audit_near_duplicates.py` before freezing the split. The script compares cleaned entry text from different releases with character `char_wb` TF-IDF 3–5 grams and cosine similarity; the default threshold is 0.88. It writes candidate pairs to ignored `artifacts/data_audit/near_duplicates.csv` for manual review. The pinned 571-entry corpus currently yields **20 cross-release candidate pairs** at that threshold. Several are deprecation/removal updates for the same API; they may be legitimately distinct, so similarity does not automatically remove a row. Inspect any pairs crossing train/dev/test after human labeling, and document exclusions or retained pairs before reporting held-out metrics.

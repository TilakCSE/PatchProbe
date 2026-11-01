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

## First pilot audit

The 50-decision pilot has 49 usable model labels. At the default 0.88 corpus-wide similarity threshold, one flagged pair has both entries labeled and crosses the dev/test split: `dj-b142f460d25e91a9` (Django 5.1, dev, deprecation) and `dj-d6a87abb10b5e5c1` (Django 6.0, test, removal), similarity 0.890675. There is no flagged train/test pair among labeled rows at this threshold. No parameter tuning used the dev set, but the pair still makes the tiny test less independent in topic. Retain both in the first pilot result and disclose the issue; review the pair and define a duplicate-family policy before a final evaluation.


The five `No targeted check stated` examples occur only in Django 4.2 (two), 5.0 (two), and 5.1 (one); 5.2 and 6.0 have none. A release-held-out test therefore cannot establish stable fifth-class quality from this corpus.

## Full-corpus evaluation gate (2026-11-01)

All 571 source candidates are accounted for: 531 model labels, 13 `UNCLEAR`, and 27 `EXCLUDE`. Before a new score, audit related entries across releases, decide whether to cluster or keep them within the same split, then freeze release-grouped train/dev/test assignments. The fifth class has only five labels; show its exact support in each split, and avoid claiming stable class-specific performance. Fit TF-IDF and model selection on train/dev only. Report both baselines and the classifier on an untouched test release, with per-class support and errors. The existing pilot score cannot be transferred to the expanded data.

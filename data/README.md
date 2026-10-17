# Data layout

- raw/: downloaded upstream documents; ignored by Git.
- processed/entries.csv: extracted notes with provenance. No labels.
- processed/pilot_queue.csv: 50 entries for the first human labeling pass. No labels.
- annotations/pilot_labels.csv: human choices saved by the annotation app.

Only a human choice counts as a gold label. Keep source revision and example IDs stable. Raw upstream files and generated model artifacts are rebuilt from the documented source.

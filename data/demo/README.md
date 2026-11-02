# Batch demo CSV

Upload [`batch_demo.csv`](batch_demo.csv) in the Next.js portal's **Batch workspace**. It has 12 short, source-linked entries: six from held-out Django 6.0/6.0.1 notes and six paraphrased entries from React, VS Code, and Chrome. The `text` column is the model input; `id`, `product`, and `source_url` are for inspection. The portal accepts this CSV directly and ignores the extra `product` column.

The set is deliberately varied, including notes the model can misroute. It is a UI demonstration, **not** a random sample, a benchmark, or evidence of cross-product accuracy. No target or expected label is supplied in the file. The external phrases and their source links come from `data/external/official_notes_probe.csv`; their proposed labels are not independent human ground truth.

Regenerate from committed source data with `python scripts/build_demo_batch.py` from the project root.

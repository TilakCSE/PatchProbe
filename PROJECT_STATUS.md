# Project status

Updated 2026-11-02. The current build is a complete, locally verified research MVP. A Vercel deployment has not been verified.

## Data and models

- All **571** source-linked Django entries have a disposition: **531** five-class labels, **13** `UNCLEAR`, and **27** `EXCLUDE`. The [annotated corpus](data/processed/annotated_corpus.csv) preserves the source and review fields. Confirmations were made with suggestions visible, so blind reviewer agreement is unknown.
- A chronological release-grouped evaluation, after 12 documented cross-split similarity exclusions, uses **305 train / 109 development / 105 test** notes. Test accuracy is **0.733** and five-label macro-F1 is **0.555**, versus **0.124** for the majority and **0.444** for the fixed-keyword macro-F1 baselines. The fifth class has five training examples and no test support. See [full-corpus evaluation](docs/FULL_CORPUS_EVALUATION.md).
- The separate serving model fits all 531 labels. Its committed portable JSON reproduces Python labels on all 571 corpus notes and 15 external probes (**586/586**); this is an implementation check, not an accuracy result. The 15 external notes are a qualitative probe with non-independent reference interpretations, not a cross-product benchmark.

## Working interfaces

- Streamlit shows the full reviewed corpus, a 105-note evaluation view with per-class and error tables, prediction review, and the historical 50-note guided annotation pilot. The pilot screen is marked as historical.
- The Next.js portal accepts a single note or a CSV batch of up to **100** notes, returns model suggestions, supports in-browser human review, and exports decisions. The [12-row demo CSV](data/demo/batch_demo.csv) includes six Django and six React/VS Code/Chrome notes. Its external examples are illustrative and may fail.
- The portal production build, local homepage and API smoke checks, Python–Node parity, and **33 Python tests** pass. Valid requests and rejected empty and 101-note inputs were checked locally. The two API routes each trace about **6.3 MB** of uncompressed files.

## Remaining before a wider deployment

1. Verify a Vercel preview end to end with `portal/` as Root Directory; the local build is not proof of cloud behavior. Record the preview URL and settings after a successful deployment.
2. For a credible claim beyond Django, collect independently adjudicated examples from multiple products, add support for the sparse fifth class, and evaluate on a new untouched set.
3. Before handling private or high-volume notes, add access control, rate limiting, a privacy policy, and monitoring that excludes note text. Model scores are uncalibrated and are not safety guarantees.

See the [project specification](docs/PROJECT_SPECIFICATION.md), [decision log](DECISIONS.md), and [deployment runbook](docs/PORTAL_DEPLOYMENT.md) for the full pipeline and reproducible commands.

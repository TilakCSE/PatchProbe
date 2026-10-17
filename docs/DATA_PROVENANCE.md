# Release-note data provenance

## Source and rights

All source text comes from [Django's official release-note source directory](https://github.com/django/django/tree/main/docs/releases). The extractor fetches immutable Git commits rather than a moving branch. Django's copyright and BSD license notice are reproduced in [DJANGO_LICENSE.txt](DJANGO_LICENSE.txt). The two pinned revisions use the same notice. PatchProbe is an independent educational project; Django does not endorse it.

| Django tag | Resolved commit used for source files | Releases |
| --- | --- | --- |
| `5.2.8` | `47fe39af56ecd0ad73b9c7562511015e96b91b80` | 4.2, 5.0, 5.1, 5.2, 5.2.1–5.2.8 |
| `6.0.1` | `85eb963c5297fb285aecf4a90c97141a1b9c5bee` | 6.0, 6.0.1 |

Each row has a source URL pointing to the exact source file and line span, and its own `source_revision`. `data/processed/manifest.json` records per-file SHA-256 hashes, source URLs, release counts, and pilot entry IDs. Downloaded full RST files are cached under ignored `data/raw/django/`.

## Build and output

From the repository root, run `python scripts/build_dataset.py`. After the first successful download, run `python scripts/build_dataset.py --offline` to rebuild from the cached files. The build writes:

- `data/processed/entries.csv`: all unlabeled candidate entries.
- `data/processed/pilot_queue.csv`: 50 unlabeled entries for human review.
- `data/processed/manifest.json`: exact source and extraction counts.

The CSV schema is `entry_id, release, source_url, source_revision, section_path, raw_text, text`. `raw_text` preserves the extracted RST note; `text` removes common inline RST roles and whitespace for later modeling. The model must use `text` only. Headings and release metadata are stored for review and splitting, not appended to model text. The `entry_id` hashes revision, release, first source line, and raw content. No target variable or inferred label is written by this step.

The parser treats one substantive bullet or prose block as a candidate, keeps an indented continuation paragraph with its bullet, and skips headings, directives, literal code, very short blocks, and some editorial boilerplate. Exact duplicate cleaned texts are removed globally. This is a deterministic extraction rule, not a guarantee that every row is a self-contained change. The 50-row pilot is restricted to bullets of 70–700 characters and selected by stable hash order within each release, then round-robin across releases. Selection does not inspect or assign a class.

## Counts from the current pinned build

| Release | Candidates after exact dedup | Pilot rows |
| --- | ---: | ---: |
| 4.2 | 107 | 5 |
| 5.0 | 127 | 5 |
| 5.1 | 89 | 5 |
| 5.2 | 71 | 5 |
| 5.2.1 | 16 | 4 |
| 5.2.2 | 12 | 4 |
| 5.2.3 | 3 | 3 |
| 5.2.4 | 3 | 3 |
| 5.2.5 | 5 | 4 |
| 5.2.6 | 2 | 1 |
| 5.2.7 | 3 | 1 |
| 5.2.8 | 5 | 2 |
| 6.0 | 118 | 4 |
| 6.0.1 | 10 | 4 |
| **Total** | **571** | **50** |

There were 571 extracted candidates before exact deduplication and zero exact duplicates by normalized `text`. Near duplicates have not yet been audited. These are **unlabeled** examples, so there are no class counts, model splits, or test metrics. Treat 6.0 as a possible release-level holdout, not a frozen test set until the human-label distribution is known. Do not tune or report five-way performance against automatically inferred labels.

## Known extraction limits

- A prose block can rely on an earlier paragraph; the pilot favors bullets to reduce this problem but still requires human review.
- RST is richer than this block parser. Embedded directives, unusual nested lists, and cross-references may be omitted or imperfectly flattened.
- Security and patch notes are much shorter than feature-release notes. Release-balanced pilot sampling does not imply class balance.
- Exact deduplication does not catch paraphrases or near-identical notes. Audit them before choosing release-level train/test groups.
- The upstream notes describe Django changes, not observed downstream failures. The intended labels are reviewer judgments about which area to verify first.

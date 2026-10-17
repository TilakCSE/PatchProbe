# Data and labeling guide

## Source and prediction unit
Use official Django release-note source files. Save source revision, release ID, URL, section path, raw text, and extraction method. One example is one substantive bullet or short paragraph. Keep a multi-paragraph bullet intact; exclude headings, navigation, and boilerplate.

## The question for every row
Based only on the note text, which ONE area should a developer verify first after upgrading an application that uses the affected feature? Choose the most specific area explicitly suggested by the note. This is a review aid, not an assertion that the change will break every app.

## Five model labels
1. API/code compatibility — Python calls, imports, signatures, return values, exceptions, hooks, or integration code.
2. Configuration/deployment — settings, middleware order, environment, runtime compatibility, packaging, or deployment behavior.
3. Data/schema migration — database schema, ORM data semantics, migrations, data conversion, or persistent storage.
4. UI/output behavior — rendered pages, templates, forms, admin display, responses, serialization, or user-visible output.
5. No targeted check stated — a substantive note that gives no concrete downstream behavior to verify from the text alone.

## Separate review state
Use UNCLEAR for genuinely mixed or underspecified rows. UNCLEAR is not a training class; record its count and reason. Never force a model label for a row that reasonably needs two first checks.

## Tie-break order
- Read the change itself, not the section heading.
- Prefer an explicitly named affected interface over general words such as feature or improvement.
- If two areas are both explicitly affected, mark UNCLEAR and explain why.
- Do not infer a database check from the mere presence of a model class, or a UI check from the mere presence of a view.
- If a note only says an internal bug was fixed without a downstream action or observable surface, use No targeted check stated.

## Illustrative examples, not source rows
- “The function now raises ValueError for an empty argument.” → API/code compatibility.
- “A setting must be added before this middleware runs.” → Configuration/deployment.
- “Existing records need a schema migration.” → Data/schema migration.
- “The admin form now displays the field differently.” → UI/output behavior.
- “Documentation was clarified.” → exclude as non-substantive, not No targeted check stated.
- “The cache and database adapter both changed.” → UNCLEAR if both checks are equally primary.

## Human workflow
Start with 50 varied entries. The interface should show one row at a time with the original source link, these definitions, a label button, and an optional note. The user can ask the agent about each row. The agent may explain the definitions and point to evidence in the text, but the human chooses the saved label. Review disagreements and refine this guide before a larger batch. Estimate labeling time from the pilot rather than promise a fixed total.

## Data quality and split
Deduplicate near-identical notes across releases before splitting. Group by release version; no release belongs to more than one split. Keep section headings and release metadata out of model input. Freeze test releases before tuning. Report exact accepted, excluded, and UNCLEAR counts plus class support.

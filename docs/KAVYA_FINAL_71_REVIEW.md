# Kavya final batch: all 71 source entries reviewed

> **REVIEW COMPLETE.** Kavya Jariwala confirmed all 71 proposed dispositions on 2026-11-01: 44 model labels and 27 `EXCLUDE` decisions. Suggestions were visible during review.

Prepared: 2026-11-01. Source: pinned official Django release notes. This sheet covers every source ID without a confirmed decision after the first 500 reviews. It is not a representative test set.

**Selection:** All 71 remaining source entries, without text-length or similarity filtering. Some are incomplete fragments produced by extraction; others resemble already reviewed notes across releases. No class quota was used. The earlier 500 decisions are not repeated here.

**Review outcome:** Kavya confirmed all proposals. The 44 labels are in `data/processed/kavya_final_71_reviewed_labels.csv`; the 27 exclusions are in `data/processed/excluded_entries.csv`. Named records and exact timestamps stay in ignored local files. `EXCLUDE` is not a training class.

**Confirmed counts:** API/code compatibility: 14; Configuration/deployment: 10; Data/schema migration: 12; UI/output behavior: 5; No targeted check stated: 3; UNCLEAR: 0; EXCLUDE: 27.

## Quick index

| No. | Django | Confirmed decision | Status |
| ---: | --- | --- | --- |
| 01 | 4.2 | Data/schema migration | Confirmed |
| 02 | 4.2 | No targeted check stated | Confirmed |
| 03 | 4.2 | Data/schema migration | Confirmed |
| 04 | 4.2 | Configuration/deployment | Confirmed |
| 05 | 4.2 | Data/schema migration | Confirmed |
| 06 | 4.2 | EXCLUDE | Confirmed |
| 07 | 4.2 | UI/output behavior | Confirmed |
| 08 | 4.2 | Data/schema migration | Confirmed |
| 09 | 5.0 | Data/schema migration | Confirmed |
| 10 | 5.0 | Data/schema migration | Confirmed |
| 11 | 5.0 | API/code compatibility | Confirmed |
| 12 | 5.0 | API/code compatibility | Confirmed |
| 13 | 5.0 | No targeted check stated | Confirmed |
| 14 | 5.0 | No targeted check stated | Confirmed |
| 15 | 5.0 | Data/schema migration | Confirmed |
| 16 | 5.0 | EXCLUDE | Confirmed |
| 17 | 5.0 | EXCLUDE | Confirmed |
| 18 | 5.0 | EXCLUDE | Confirmed |
| 19 | 5.0 | EXCLUDE | Confirmed |
| 20 | 5.0 | EXCLUDE | Confirmed |
| 21 | 5.0 | EXCLUDE | Confirmed |
| 22 | 5.0 | EXCLUDE | Confirmed |
| 23 | 5.0 | API/code compatibility | Confirmed |
| 24 | 5.0 | Data/schema migration | Confirmed |
| 25 | 5.0 | Configuration/deployment | Confirmed |
| 26 | 5.0 | EXCLUDE | Confirmed |
| 27 | 5.0 | API/code compatibility | Confirmed |
| 28 | 5.1 | EXCLUDE | Confirmed |
| 29 | 5.1 | EXCLUDE | Confirmed |
| 30 | 5.1 | Configuration/deployment | Confirmed |
| 31 | 5.1 | Configuration/deployment | Confirmed |
| 32 | 5.1 | EXCLUDE | Confirmed |
| 33 | 5.1 | Data/schema migration | Confirmed |
| 34 | 5.1 | API/code compatibility | Confirmed |
| 35 | 5.1 | API/code compatibility | Confirmed |
| 36 | 5.2 | UI/output behavior | Confirmed |
| 37 | 5.2 | EXCLUDE | Confirmed |
| 38 | 5.2 | Data/schema migration | Confirmed |
| 39 | 5.2 | API/code compatibility | Confirmed |
| 40 | 5.2 | EXCLUDE | Confirmed |
| 41 | 5.2 | EXCLUDE | Confirmed |
| 42 | 5.2 | EXCLUDE | Confirmed |
| 43 | 5.2 | EXCLUDE | Confirmed |
| 44 | 5.2 | UI/output behavior | Confirmed |
| 45 | 5.2 | Configuration/deployment | Confirmed |
| 46 | 5.2 | Configuration/deployment | Confirmed |
| 47 | 5.2 | Configuration/deployment | Confirmed |
| 48 | 5.2.1 | Data/schema migration | Confirmed |
| 49 | 5.2.2 | UI/output behavior | Confirmed |
| 50 | 5.2.8 | Configuration/deployment | Confirmed |
| 51 | 6.0 | Configuration/deployment | Confirmed |
| 52 | 6.0 | API/code compatibility | Confirmed |
| 53 | 6.0 | EXCLUDE | Confirmed |
| 54 | 6.0 | EXCLUDE | Confirmed |
| 55 | 6.0 | EXCLUDE | Confirmed |
| 56 | 6.0 | UI/output behavior | Confirmed |
| 57 | 6.0 | EXCLUDE | Confirmed |
| 58 | 6.0 | API/code compatibility | Confirmed |
| 59 | 6.0 | EXCLUDE | Confirmed |
| 60 | 6.0 | Configuration/deployment | Confirmed |
| 61 | 6.0 | EXCLUDE | Confirmed |
| 62 | 6.0 | EXCLUDE | Confirmed |
| 63 | 6.0 | EXCLUDE | Confirmed |
| 64 | 6.0 | EXCLUDE | Confirmed |
| 65 | 6.0 | API/code compatibility | Confirmed |
| 66 | 6.0 | API/code compatibility | Confirmed |
| 67 | 6.0 | API/code compatibility | Confirmed |
| 68 | 6.0 | EXCLUDE | Confirmed |
| 69 | 6.0 | API/code compatibility | Confirmed |
| 70 | 6.0 | API/code compatibility | Confirmed |
| 71 | 6.0.1 | Data/schema migration | Confirmed |

## Full review

### 01. Django 4.2 — `dj-8155f8094555f2d8`

> The new Field.db_comment and Meta.db_table_comment options allow creating comments on columns and tables, respectively. For example::

**Confirmed decision:** Data/schema migration

**Why:** Column and table comments are database schema metadata; the example lead-in is incomplete but the change is stated.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L56-L59)

**Kavya's decision:** Confirmed as shown above.

### 02. Django 4.2 — `dj-e630a54fcc28e73b`

> jQuery is upgraded from version 3.6.0 to 3.6.4.

**Confirmed decision:** No targeted check stated

**Why:** Only the bundled jQuery version is stated; the note names no concrete downstream behavior to verify.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L144-L144)

**Kavya's decision:** Confirmed as shown above.

### 03. Django 4.2 — `dj-b7a2dba7c3fbca59`

> CharField.max_length is no longer required to be set on PostgreSQL, which supports unlimited VARCHAR columns.

**Confirmed decision:** Data/schema migration

**Why:** Unlimited PostgreSQL VARCHAR length changes model field and database schema options.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L308-L310)

**Kavya's decision:** Confirmed as shown above.

### 04. Django 4.2 — `dj-e07f5ab4ed32bb3e`

> The minimum supported version of SQLite is increased from 3.9.0 to 3.21.0.

**Confirmed decision:** Configuration/deployment

**Why:** The installed SQLite runtime must meet the new minimum version.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L448-L448)

**Kavya's decision:** Confirmed as shown above.

### 05. Django 4.2 — `dj-37b04ba8e37ed1b0`

> Migrating existing index_together should be handled as a migration. For example::

**Confirmed decision:** Data/schema migration

**Why:** Existing index_together definitions require a migration; the example lead-in is incomplete.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L494-L495)

**Kavya's decision:** Confirmed as shown above.

### 06. Django 4.2 — `dj-3c217f5005290bdd`

> Code that used to pass JSON encoded string literals::

**Confirmed decision:** EXCLUDE

**Why:** This is only the introduction to a missing code example and states no actual change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L536-L536)

**Kavya's decision:** Confirmed as shown above.

### 07. Django 4.2 — `dj-8371b13dae6e758d`

> The length_is template filter is deprecated in favor of length and the == operator within an {% if %}<if> tag. For example

**Confirmed decision:** UI/output behavior

**Why:** The deprecated template filter affects template rendering; the example tail is truncated.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L569-L570)

**Kavya's decision:** Confirmed as shown above.

### 08. Django 4.2 — `dj-7a26560120e26fcd`

> django.contrib.postgres.fields.CICharField is deprecated in favor of CharField(db_collation="…") with a case-insensitive non-deterministic collation.

**Confirmed decision:** Data/schema migration

**Why:** Replacing CICharField requires a database collation and field schema review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L588-L590)

**Kavya's decision:** Confirmed as shown above.

### 09. Django 5.0 — `dj-5084ce202f4fdf73`

> The new Field.db_default parameter sets a database-computed default value. For example::

**Confirmed decision:** Data/schema migration

**Why:** db_default is a database-computed field default; the example lead-in is incomplete.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L120-L121)

**Kavya's decision:** Confirmed as shown above.

### 10. Django 5.0 — `dj-c37c08bcaf63b52a`

> The new django.db.models.GeneratedField allows creation of database generated columns. This field can be used on all supported database backends to create a field that is always computed from other fields. For example::

**Confirmed decision:** Data/schema migration

**Why:** GeneratedField creates computed database columns; the example lead-in is incomplete.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L135-L137)

**Kavya's decision:** Confirmed as shown above.

### 11. Django 5.0 — `dj-0b7f1c3e09600abd`

> Field.choices (for model fields) and ChoiceField.choices (for form fields) allow for more flexibility when declaring their values. In previous versions of Django, choices should either be a list of 2-tuples, or an field-choices-enum-types subclass, but the latter required accessing the .choices attribute to provide the values in the expected form::

**Confirmed decision:** API/code compatibility

**Why:** Field and form choices are declared in application code, though the example is truncated.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L154-L159)

**Kavya's decision:** Confirmed as shown above.

### 12. Django 5.0 — `dj-b1a95b13877c5ed7`

> Django 5.0 adds support for accepting a mapping or a callable instead of an iterable, and also no longer requires .choices to be used directly to expand enumeration types::

**Confirmed decision:** API/code compatibility

**Why:** Choices declarations can now use mappings, callables, or enum types directly.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L177-L179)

**Kavya's decision:** Confirmed as shown above.

### 13. Django 5.0 — `dj-75c9dd1982b2c506`

> XRegExp is upgraded from version 3.2.0 to 5.1.1.

**Confirmed decision:** No targeted check stated

**Why:** Only the bundled XRegExp version is stated; no concrete downstream check is named.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L221-L221)

**Kavya's decision:** Confirmed as shown above.

### 14. Django 5.0 — `dj-ed6a8abe11eb55d9`

> jQuery is upgraded from version 3.6.4 to 3.7.1.

**Confirmed decision:** No targeted check stated

**Why:** Only the bundled jQuery version is stated; no concrete downstream check is named.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L229-L229)

**Kavya's decision:** Confirmed as shown above.

### 15. Django 5.0 — `dj-10c5c6f1564e1a96`

> GIS aggregates now support the filter argument.

**Confirmed decision:** Data/schema migration

**Why:** The GIS aggregate filter argument changes database query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L266-L267)

**Kavya's decision:** Confirmed as shown above.

### 16. Django 5.0 — `dj-65ce9c733debb429`

> django.views.decorators.common.no_append_slash

**Confirmed decision:** EXCLUDE

**Why:** A bare decorator name does not state the change or affected behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L303-L303)

**Kavya's decision:** Confirmed as shown above.

### 17. Django 5.0 — `dj-4a304aeb5488a053`

> django.views.decorators.csrf.ensure_csrf_cookie

**Confirmed decision:** EXCLUDE

**Why:** A bare decorator name does not state the change or affected behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L306-L306)

**Kavya's decision:** Confirmed as shown above.

### 18. Django 5.0 — `dj-543ff7c6f42ed38e`

> django.views.decorators.csrf.requires_csrf_token

**Confirmed decision:** EXCLUDE

**Why:** A bare decorator name does not state the change or affected behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L307-L307)

**Kavya's decision:** Confirmed as shown above.

### 19. Django 5.0 — `dj-cd019b306a8915f2`

> django.views.decorators.debug.sensitive_variables

**Confirmed decision:** EXCLUDE

**Why:** A bare decorator name does not state the change or affected behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L308-L308)

**Kavya's decision:** Confirmed as shown above.

### 20. Django 5.0 — `dj-6fca5ca4579f3578`

> django.views.decorators.debug.sensitive_post_parameters

**Confirmed decision:** EXCLUDE

**Why:** A bare decorator name does not state the change or affected behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L309-L309)

**Kavya's decision:** Confirmed as shown above.

### 21. Django 5.0 — `dj-7ba114cbe9497a34`

> django.views.decorators.http.require_http_methods

**Confirmed decision:** EXCLUDE

**Why:** A bare decorator name does not state the change or affected behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L315-L315)

**Kavya's decision:** Confirmed as shown above.

### 22. Django 5.0 — `dj-3aa0ba2f057e974c`

> In order to improve accessibility, the following changes are made:

**Confirmed decision:** EXCLUDE

**Why:** This is an introduction to a list of changes, with no change stated in the extracted entry.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L344-L344)

**Kavya's decision:** Confirmed as shown above.

### 23. Django 5.0 — `dj-5b473a4a6ddd246b`

> DatabaseFeatures.supports_default_keyword_in_bulk_insert should be set to False if the database doesn't support the DEFAULT keyword in bulk INSERT queries.

**Confirmed decision:** API/code compatibility

**Why:** Custom database backend code must set this capability flag correctly.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L464-L466)

**Kavya's decision:** Confirmed as shown above.

### 24. Django 5.0 — `dj-e0c7cd09189e6b2b`

> On MariaDB 10.7+, UUIDField is now created as UUID column rather than CHAR(32) column. As a consequence, any UUIDField created in Django < 5.0 should be replaced with a UUIDField subclass backed by CHAR(32)::

**Confirmed decision:** Data/schema migration

**Why:** Existing MariaDB UUIDField columns need migration or a compatibility subclass.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L503-L506)

**Kavya's decision:** Confirmed as shown above.

### 25. Django 5.0 — `dj-4017b1ea8b70b1f2`

> The minimum supported version of SQLite is increased from 3.21.0 to 3.27.0.

**Confirmed decision:** Configuration/deployment

**Why:** The deployed SQLite version must meet the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L577-L577)

**Kavya's decision:** Confirmed as shown above.

### 26. Django 5.0 — `dj-51a058ccf97f81d0`

> These features have reached the end of their deprecation cycle and are removed in Django 5.0.

**Confirmed decision:** EXCLUDE

**Why:** This is a generic heading sentence; the actual removed features are separate entries.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L658-L659)

**Kavya's decision:** Confirmed as shown above.

### 27. Django 5.0 — `dj-00b72b91c4f90c15`

> The SitemapIndexItem.__str__() method is removed.

**Confirmed decision:** API/code compatibility

**Why:** Code relying on SitemapIndexItem.__str__ must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L714-L714)

**Kavya's decision:** Confirmed as shown above.

### 28. Django 5.1 — `dj-f15b4ff3e018bf5b`

> For instance, navigating pagination and query strings in templates can be cumbersome. Consider this template fragment that dynamically generates a URL for navigating to the next page within a paginated view:

**Confirmed decision:** EXCLUDE

**Why:** This describes a forthcoming template example, not a released change on its own.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L38-L40)

**Kavya's decision:** Confirmed as shown above.

### 29. Django 5.1 — `dj-fd948218719b6737`

> When switching to using this new template tag, the above magically becomes:

**Confirmed decision:** EXCLUDE

**Why:** The note points to an omitted example and names no standalone behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L53-L53)

**Kavya's decision:** Confirmed as shown above.

### 30. Django 5.1 — `dj-cc651ac2bfdeaca4`

> To use a connection pool with psycopg, you can set the "pool" option inside OPTIONS to be a dict to be passed to psycopg:psycopg_pool.ConnectionPool, or to True to use the ConnectionPool defaults::

**Confirmed decision:** Configuration/deployment

**Why:** PostgreSQL connection pooling is enabled through database OPTIONS settings.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L66-L69)

**Kavya's decision:** Confirmed as shown above.

### 31. Django 5.1 — `dj-d05b8ab4c1944849`

> The default iteration count for the PBKDF2 password hasher is increased from 720,000 to 870,000.

**Confirmed decision:** Configuration/deployment

**Why:** The default password-hasher work factor changes runtime cost and security policy.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L116-L117)

**Kavya's decision:** Confirmed as shown above.

### 32. Django 5.1 — `dj-913598c6f5c064a4`

> These features have reached the end of their deprecation cycle and are removed in Django 5.1.

**Confirmed decision:** EXCLUDE

**Why:** This is a generic heading sentence; the actual removed features are separate entries.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L456-L457)

**Kavya's decision:** Confirmed as shown above.

### 33. Django 5.1 — `dj-766c38b4d85227d3`

> The model's Meta.index_together option is removed.

**Confirmed decision:** Data/schema migration

**Why:** Removing Meta.index_together affects model index definitions and migrations.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L464-L464)

**Kavya's decision:** Confirmed as shown above.

### 34. Django 5.1 — `dj-8517d40446f63bea`

> The django.contrib.auth.hashers.SHA1PasswordHasher, django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher, and django.contrib.auth.hashers.UnsaltedMD5PasswordHasher are removed.

**Confirmed decision:** API/code compatibility

**Why:** Code or configuration referencing the removed hasher classes must change; the named classes are the direct interface.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L468-L470)

**Kavya's decision:** Confirmed as shown above.

### 35. Django 5.1 — `dj-3989c4537569848c`

> The django.contrib.postgres.fields.CIText mixin is removed.

**Confirmed decision:** API/code compatibility

**Why:** Code importing the removed CIText mixin must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L477-L477)

**Kavya's decision:** Confirmed as shown above.

### 36. Django 5.2 — `dj-80689adac735bec0`

> The shell management command now automatically imports models from all installed apps. You can view further details of the imported objects by setting the --verbosity flag to 2 or more:

**Confirmed decision:** UI/output behavior

**Why:** The interactive shell now exposes automatically imported model names.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L38-L40)

**Kavya's decision:** Confirmed as shown above.

### 37. Django 5.2 — `dj-a938e708b944403b`

> This behavior can be customized to add or remove automatic imports.

**Confirmed decision:** EXCLUDE

**Why:** The sentence refers to prior context and gives no standalone setting or behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L52-L53)

**Kavya's decision:** Confirmed as shown above.

### 38. Django 5.2 — `dj-41ff06db6a8aa983`

> To use a composite primary key, when defining a model set the pk attribute to be a CompositePrimaryKey::

**Confirmed decision:** Data/schema migration

**Why:** CompositePrimaryKey changes the model's database key definition.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L61-L62)

**Kavya's decision:** Confirmed as shown above.

### 39. Django 5.2 — `dj-e10f1f3c5b14d767`

> Prior to version 5.2, overriding Field.get_bound_field() was the only option to use a custom django.forms.BoundField. Django now supports specifying the following attributes to customize form rendering:

**Confirmed decision:** API/code compatibility

**Why:** Custom BoundField implementations can use new attributes instead of a prior hook.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L77-L79)

**Kavya's decision:** Confirmed as shown above.

### 40. Django 5.2 — `dj-4e03e59dd540443f`

> BaseRenderer.bound_field_class at the project level,

**Confirmed decision:** EXCLUDE

**Why:** This is a fragment of a list and does not say what the attribute does on its own.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L81-L81)

**Kavya's decision:** Confirmed as shown above.

### 41. Django 5.2 — `dj-802649339fdb0eb5`

> Form.bound_field_class at the form level, and

**Confirmed decision:** EXCLUDE

**Why:** This is a fragment of a list and does not say what the attribute does on its own.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L82-L82)

**Kavya's decision:** Confirmed as shown above.

### 42. Django 5.2 — `dj-89d1d6955bf1654a`

> For example, to customize the BoundField of a Form class::

**Confirmed decision:** EXCLUDE

**Why:** This only introduces a missing code example.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L85-L85)

**Kavya's decision:** Confirmed as shown above.

### 43. Django 5.2 — `dj-53628809ef71e5fc`

> When rendering a CustomForm instance, the following HTML is included:

**Confirmed decision:** EXCLUDE

**Why:** This only introduces missing HTML output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L113-L113)

**Kavya's decision:** Confirmed as shown above.

### 44. Django 5.2 — `dj-81d5c5feeb4c54e3`

> Links to components in docstrings now supports custom link text, using the format link text. See documentation helpers for more details.

**Confirmed decision:** UI/output behavior

**Why:** Admin documentation links can show custom link text, though markup detail is flattened.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L145-L147)

**Kavya's decision:** Confirmed as shown above.

### 45. Django 5.2 — `dj-181a2c7204b0faed`

> The default iteration count for the PBKDF2 password hasher is increased from 870,000 to 1,000,000.

**Confirmed decision:** Configuration/deployment

**Why:** The default password-hasher work factor changes runtime cost and security policy.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L155-L156)

**Kavya's decision:** Confirmed as shown above.

### 46. Django 5.2 — `dj-921d8d2be656a09d`

> Upstream support for PostgreSQL 13 ends in November 2025. Django 5.2 supports PostgreSQL 14 and higher.

**Confirmed decision:** Configuration/deployment

**Why:** The deployed PostgreSQL version must be at least 14.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L419-L420)

**Kavya's decision:** Confirmed as shown above.

### 47. Django 5.2 — `dj-7a9d699f7f5f0382`

> The minimum supported version of oracledb is increased from 1.3.2 to 2.3.0.

**Confirmed decision:** Configuration/deployment

**Why:** The installed oracledb version must meet the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L465-L466)

**Kavya's decision:** Confirmed as shown above.

### 48. Django 5.2.1 — `dj-0c2fa2afae144ffe`

> Fixed a bug in Django 5.2 that caused a redundant unique_together constraint to be generated for composite primary keys when using inspectdb (36357).

**Confirmed decision:** Data/schema migration

**Why:** inspectdb no longer generates a redundant composite-key constraint.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L80-L82)

**Kavya's decision:** Confirmed as shown above.

### 49. Django 5.2.2 — `dj-ac417e0075e0ce6f`

> Internal HTTP response logging used request.path directly, allowing control characters (e.g. newlines or ANSI escape sequences) to be written unescaped into logs. This could enable log injection or forgery, letting attackers manipulate log appearance or structure, especially in logs processed by external systems or viewed in terminals.

**Confirmed decision:** UI/output behavior

**Why:** The security fix concerns escaping request paths in HTTP response logs.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L13-L17)

**Kavya's decision:** Confirmed as shown above.

### 50. Django 5.2.8 — `dj-1d862c7e81f8a7d3`

> Added compatibility for oracledb 3.4.0 (36646).

**Confirmed decision:** Configuration/deployment

**Why:** The Oracle driver version compatibility affects dependency deployment.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.8.txt#L31-L31)

**Kavya's decision:** Confirmed as shown above.

### 51. Django 6.0 — `dj-c081e2aa74aded85`

> Django 6.0 supports Python 3.12, 3.13, and 3.14. We highly recommend, and only officially support, the latest release of each series.

**Confirmed decision:** Configuration/deployment

**Why:** The deployed Python runtime must match the supported versions.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L21-L22)

**Kavya's decision:** Confirmed as shown above.

### 52. Django 6.0 — `dj-8871962e9ae3baea`

> Following the release of Django 6.0, we suggest that third-party app authors drop support for all versions of Django prior to 5.2. At that time, you should be able to run your package's tests using python -Wd so that deprecation warnings appear. After making the deprecation warning fixes, your app should be compatible with Django 6.0.

**Confirmed decision:** API/code compatibility

**Why:** Third-party package code and tests should address deprecations for Django 6.0.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L29-L33)

**Kavya's decision:** Confirmed as shown above.

### 53. Django 6.0 — `dj-61d6953f6615cbb3`

> These settings accept Python dictionaries and support Django-provided constants for clarity and safety. For example::

**Confirmed decision:** EXCLUDE

**Why:** The phrase 'These settings' has no named referent in the extracted entry; the example is missing.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L56-L57)

**Kavya's decision:** Confirmed as shown above.

### 54. Django 6.0 — `dj-ed581c8f20c4e925`

> The resulting Content-Security-Policy header would be set to:

**Confirmed decision:** EXCLUDE

**Why:** This refers to a missing Content-Security-Policy header example.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L67-L67)

**Kavya's decision:** Confirmed as shown above.

### 55. Django 6.0 — `dj-62259fa7f2df222c`

> To get started, follow the CSP how-to guide. For in-depth guidance, see the CSP security overview and the reference docs, which include details about decorators to override or disable policies on a per-view basis.

**Confirmed decision:** EXCLUDE

**Why:** This points to documentation rather than stating an affected behavior.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L73-L76)

**Kavya's decision:** Confirmed as shown above.

### 56. Django 6.0 — `dj-51c93f31c9f0a85f`

> Partials can also be referenced using the template_name#partial_name syntax with django.template.Engine.get_template, django.shortcuts.render, {% include %}<include>, and other template-loading tools, enabling more modular and maintainable templates without needing to split components into separate files.

**Confirmed decision:** UI/output behavior

**Why:** Template-partial references change how components are loaded and rendered.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L87-L91)

**Kavya's decision:** Confirmed as shown above.

### 57. Django 6.0 — `dj-d2e6e50dd5f278ab`

> A migration guide is available if you're updating from the django-template-partials third-party package.

**Confirmed decision:** EXCLUDE

**Why:** This only points to a separate migration guide and states no change.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L93-L94)

**Kavya's decision:** Confirmed as shown above.

### 58. Django 6.0 — `dj-df99d4a90dc58aac`

> Tasks are defined using the django.tasks.task decorator::

**Confirmed decision:** API/code compatibility

**Why:** Task-definition code can use the named django.tasks.task decorator.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L110-L110)

**Kavya's decision:** Confirmed as shown above.

### 59. Django 6.0 — `dj-c0429469c52c9b51`

> Once defined, tasks can be enqueued through a configured backend::

**Confirmed decision:** EXCLUDE

**Why:** This introduces a missing enqueue example and names no method or concrete behavior.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L120-L120)

**Kavya's decision:** Confirmed as shown above.

### 60. Django 6.0 — `dj-f0fe77c17653b2f2`

> Because Python 3.12 is now the minimum supported version for Django, any optional dependencies must also meet that requirement. The following versions of each library are the first to add or confirm compatibility with Python 3.12:

**Confirmed decision:** Configuration/deployment

**Why:** Optional dependencies and the Python runtime must support Python 3.12.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L393-L395)

**Kavya's decision:** Confirmed as shown above.

### 61. Django 6.0 — `dj-1153b44d9ccc16a4`

> Since Django 3.2, when the DEFAULT_AUTO_FIELD setting was added, the default startproject template's settings.py contained::

**Confirmed decision:** EXCLUDE

**Why:** This introduces an omitted historical settings example, not a standalone change.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L432-L433)

**Kavya's decision:** Confirmed as shown above.

### 62. Django 6.0 — `dj-f75d4f5c9f437094`

> and the default startapp template's AppConfig contained::

**Confirmed decision:** EXCLUDE

**Why:** This is a fragment introducing an omitted AppConfig example.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L437-L437)

**Kavya's decision:** Confirmed as shown above.

### 63. Django 6.0 — `dj-5950434072b40045`

> At that time, the default value of DEFAULT_AUTO_FIELD remained django.db.models.AutoField for backwards compatibility.

**Confirmed decision:** EXCLUDE

**Why:** This historical background does not state the current change on its own.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L441-L442)

**Kavya's decision:** Confirmed as shown above.

### 64. Django 6.0 — `dj-e4334074ebb8b266`

> Most projects shouldn't be affected, since Django 3.2 has raised the system check warning models.W042 for projects that don't set DEFAULT_AUTO_FIELD.

**Confirmed decision:** EXCLUDE

**Why:** This reassurance refers to prior context and does not identify a standalone change.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L448-L450)

**Kavya's decision:** Confirmed as shown above.

### 65. Django 6.0 — `dj-d3718b29380710b6`

> Prior to Django 6.0, custom lookups and custom expressions implementing the as_sql() method (and its supporting methods process_lhs() and process_rhs()) were allowed to return a sequence of params in either a list or a tuple. To address the interoperability problems that resulted, the second return element of the as_sql() method should now be a tuple::

**Confirmed decision:** API/code compatibility

**Why:** Custom ORM as_sql implementations must return parameters as a tuple.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L460-L465)

**Kavya's decision:** Confirmed as shown above.

### 66. Django 6.0 — `dj-fbcfc6a881e46dc7`

> If your custom expressions support multiple versions of Django, you should adjust any pre-processing of parameters to be resilient against either tuples or lists. For instance, prefer unpacking like this::

**Confirmed decision:** API/code compatibility

**Why:** Cross-version custom expressions must accept tuple or list parameters.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L469-L471)

**Kavya's decision:** Confirmed as shown above.

### 67. Django 6.0 — `dj-abdce59827ec12b0`

> django.core.mail APIs now require keyword arguments for less commonly used parameters. Using positional arguments for these now emits a deprecation warning and will raise a TypeError when the deprecation period ends:

**Confirmed decision:** API/code compatibility

**Why:** Mail API calls should use keyword arguments to avoid future TypeError.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L492-L494)

**Kavya's decision:** Confirmed as shown above.

### 68. Django 6.0 — `dj-54eb887a13f51045`

> These features have reached the end of their deprecation cycle and are removed in Django 6.0.

**Confirmed decision:** EXCLUDE

**Why:** This is a generic heading sentence; the actual removed features are separate entries.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L556-L557)

**Kavya's decision:** Confirmed as shown above.

### 69. Django 6.0 — `dj-ece85e6c30a75c99`

> BaseDatabaseOperations.field_cast_sql() is removed.

**Confirmed decision:** API/code compatibility

**Why:** Custom database backends cannot call the removed field_cast_sql method.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L567-L567)

**Kavya's decision:** Confirmed as shown above.

### 70. Django 6.0 — `dj-a4d6ecd610075d12`

> The Prefetch.get_current_queryset() method is removed.

**Confirmed decision:** API/code compatibility

**Why:** Custom prefetch code cannot call the removed method.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L593-L593)

**Kavya's decision:** Confirmed as shown above.

### 71. Django 6.0.1 — `dj-3778d8d420591d0e`

> Fixed a bug in Django 5.2 where data exceeding max_length was silently truncated by QuerySet.bulk_create on PostgreSQL (33647).

**Confirmed decision:** Data/schema migration

**Why:** bulk_create no longer silently truncates oversized PostgreSQL field data.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L12-L13)

**Kavya's decision:** Confirmed as shown above.

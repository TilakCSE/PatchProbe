# Bhargav batch 01: 50 draft label suggestions

> **DRAFT - AGENT SUGGESTIONS ONLY.** These are not Bhargav's decisions and must not enter model training until he confirms or changes them. Kavya's 50 reviewed rows and the original pilot are separate.

Prepared: 2026-10-28. The 50 entries come from pinned official Django release-note source files. They are a review batch, not a representative test set.

**Selection:** Seven rows each from feature releases 4.2, 5.0, 5.1, 5.2, and 6.0, plus 15 patch-release rows. The sampler excluded all 100 rows from the first pilot and Kavya's batch, excluded visibly incomplete fragments, preferred varied source sections and patch releases, and filtered near-duplicates before fixed-hash selection. No labels were used to choose rows. Any new model evaluation must freeze a fresh release-grouped test set; previous pilot test scores are no longer a final untouched test.

**How to review:** Read the full note, suggested label, reason, and official source. Suggestions use note text only, not headings. Reply `Confirm all except: 07 -> Data/schema migration; 45 -> API/code compatibility` with any corrections, or confirm a smaller range. For `UNCLEAR`, say whether it remains UNCLEAR or choose a first-check area. I will save only your explicit decisions with your name.

Guide: [Data and labeling guide](DATA_AND_LABELS.md). `UNCLEAR` is a review state and is excluded from model training.

Draft counts: API/code compatibility: 19; Configuration/deployment: 10; Data/schema migration: 8; UI/output behavior: 11; UNCLEAR: 2. No row clearly merits `No targeted check stated`; do not force it for a quota.

## Quick index

| No. | Django | Suggested label | Your decision |
| ---: | --- | --- | --- |
| 01 | 4.2 | API/code compatibility | __________ |
| 02 | 4.2 | Configuration/deployment | __________ |
| 03 | 4.2 | Configuration/deployment | __________ |
| 04 | 4.2 | Configuration/deployment | __________ |
| 05 | 4.2 | API/code compatibility | __________ |
| 06 | 4.2 | UI/output behavior | __________ |
| 07 | 4.2 | UNCLEAR | __________ |
| 08 | 5.0 | Configuration/deployment | __________ |
| 09 | 5.0 | API/code compatibility | __________ |
| 10 | 5.0 | Configuration/deployment | __________ |
| 11 | 5.0 | API/code compatibility | __________ |
| 12 | 5.0 | API/code compatibility | __________ |
| 13 | 5.0 | API/code compatibility | __________ |
| 14 | 5.0 | API/code compatibility | __________ |
| 15 | 5.1 | API/code compatibility | __________ |
| 16 | 5.1 | Configuration/deployment | __________ |
| 17 | 5.1 | Configuration/deployment | __________ |
| 18 | 5.1 | API/code compatibility | __________ |
| 19 | 5.1 | API/code compatibility | __________ |
| 20 | 5.1 | UI/output behavior | __________ |
| 21 | 5.1 | API/code compatibility | __________ |
| 22 | 5.2 | API/code compatibility | __________ |
| 23 | 5.2 | Configuration/deployment | __________ |
| 24 | 5.2 | API/code compatibility | __________ |
| 25 | 5.2 | UI/output behavior | __________ |
| 26 | 5.2 | Data/schema migration | __________ |
| 27 | 5.2 | Configuration/deployment | __________ |
| 28 | 5.2 | API/code compatibility | __________ |
| 29 | 6.0 | Data/schema migration | __________ |
| 30 | 6.0 | UI/output behavior | __________ |
| 31 | 6.0 | UI/output behavior | __________ |
| 32 | 6.0 | API/code compatibility | __________ |
| 33 | 6.0 | UI/output behavior | __________ |
| 34 | 6.0 | Configuration/deployment | __________ |
| 35 | 6.0 | UI/output behavior | __________ |
| 36 | 6.0.1 | UI/output behavior | __________ |
| 37 | 5.2.1 | Data/schema migration | __________ |
| 38 | 5.2.2 | Data/schema migration | __________ |
| 39 | 5.2.7 | UI/output behavior | __________ |
| 40 | 5.2.5 | Data/schema migration | __________ |
| 41 | 5.2.8 | Data/schema migration | __________ |
| 42 | 5.2.4 | UI/output behavior | __________ |
| 43 | 6.0.1 | Data/schema migration | __________ |
| 44 | 5.2.2 | API/code compatibility | __________ |
| 45 | 5.2.1 | UNCLEAR | __________ |
| 46 | 6.0.1 | UI/output behavior | __________ |
| 47 | 6.0.1 | Data/schema migration | __________ |
| 48 | 5.2.2 | API/code compatibility | __________ |
| 49 | 5.2.2 | API/code compatibility | __________ |
| 50 | 6.0.1 | API/code compatibility | __________ |

## Notes and reasons

### 01. Django 4.2 - `dj-41274f447b6aa9d2`

> The new encoder parameter for django.utils.html.json_script function allows customizing a JSON encoder class.

**Suggestion:** API/code compatibility

**Why:** json_script gains a callable encoder parameter; check code that passes or wraps it.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L343-L344)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 02. Django 4.2 - `dj-6b5f892973151526`

> The minimum supported version of mysqlclient is increased from 1.4.0 to 1.4.3.

**Suggestion:** Configuration/deployment

**Why:** The mysqlclient minimum version is an installed dependency requirement.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L457-L458)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 03. Django 4.2 - `dj-c3af907b99f386e0`

> The new "server_side_binding" option is now supported in OPTIONS on PostgreSQL with psycopg 3.1.8+ to allow using server-side binding cursors.

**Suggestion:** Configuration/deployment

**Why:** The PostgreSQL server_side_binding option belongs in database connection configuration.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L225-L227)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 04. Django 4.2 - `dj-a81abc4bead1cab1`

> The default iteration count for the PBKDF2 password hasher is increased from 390,000 to 600,000.

**Suggestion:** Configuration/deployment

**Why:** The changed hasher work factor affects runtime cost and password-hasher configuration.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L149-L150)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 05. Django 4.2 - `dj-70c2211eff7797d9`

> MySQL 8+ allows functional dependencies on GROUP BY columns, so the pre-Django 4.2 workaround of grouping by primary keys of the main table is removed. As a consequence, using RawSQL() aggregations is no longer supported on MySQL as there is no way to determine if such aggregations are needed or valid in the GROUP BY clause. Use aggregation-functions instead.

**Suggestion:** API/code compatibility

**Why:** Code using RawSQL aggregations on MySQL must change because that use is unsupported.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L415-L420)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 06. Django 4.2 - `dj-57dc2e80bb05a092`

> The admin/delete_confirmation.html template now has some additional blocks and scripting hooks to ease customization.

**Suggestion:** UI/output behavior

**Why:** The admin confirmation template gains blocks and hooks that affect template customization.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L129-L131)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 07. Django 4.2 - `dj-aff6af34e2fac918`

> django.contrib.postgres.fields.CIEmailField is deprecated in favor of EmailField(db_collation="…") with a case-insensitive non-deterministic collation.

**Suggestion:** UNCLEAR

**Why:** The replacement names both a Python model field and a database collation; code and schema checks are both plausible first steps.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L592-L594)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 08. Django 5.0 - `dj-c61084cd8a05ad8c`

> The default scheme for forms.URLField will change from "http" to "https" in Django 6.0. Set FORMS_URLFIELD_ASSUME_HTTPS transitional setting to True to opt into assuming "https" during the Django 5.x release cycle.

**Suggestion:** Configuration/deployment

**Why:** The note explicitly calls for a transitional FORMS_URLFIELD_ASSUME_HTTPS setting.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L624-L627)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 09. Django 5.0 - `dj-d8cf5078a9d75264`

> The AlreadyRegistered and NotRegistered exceptions are moved from django.contrib.admin.sites to django.contrib.admin.exceptions.

**Suggestion:** API/code compatibility

**Why:** Imports of the moved exception classes must use their new module.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L574-L575)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 10. Django 5.0 - `dj-377da69d918b9c36`

> The default value of the USE_TZ setting is changed from False to True.

**Suggestion:** Configuration/deployment

**Why:** The default value of a Django setting changes; check the application's setting.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L670-L671)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 11. Django 5.0 - `dj-07d486f925b67af3`

> The new AdminSite.get_log_entries method allows customizing the queryset for the site's listed log entries.

**Suggestion:** API/code compatibility

**Why:** An AdminSite method is added for code that customizes the log-entry queryset.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L213-L214)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 12. Django 5.0 - `dj-7a57243eb1f0c26d`

> The new ExclusionConstraint.violation_error_code attribute of django.contrib.postgres.constraints.ExclusionConstraint allows customizing the code of ValidationError raised during model validation.

**Suggestion:** API/code compatibility

**Why:** ExclusionConstraint gains a Python attribute controlling a ValidationError code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L284-L287)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 13. Django 5.0 - `dj-1290ffa57cd99944`

> The new ClosestPoint() function returns a 2-dimensional point on the geometry that is closest to another geometry.

**Suggestion:** API/code compatibility

**Why:** The new ClosestPoint function is a callable interface used in GIS code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L261-L264)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 14. Django 5.0 - `dj-2faca5a05d4d2636`

> django.test.Client and django.test.AsyncClient now provide asynchronous methods, using an a prefix: django.test.Client.asession, django.test.Client.alogin, django.test.Client.aforce_login, and django.test.Client.alogout.

**Suggestion:** API/code compatibility

**Why:** Test Client and AsyncClient gain named async methods for code to call.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L427-L431)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 15. Django 5.1 - `dj-9621260a12d66045`

> The new from_queryset argument of Model.refresh_from_db and Model.arefresh_from_db allows customizing the queryset used to reload a model's value. This can be used to lock the row before reloading or to select related objects.

**Suggestion:** API/code compatibility

**Why:** refresh_from_db gains a named argument that application code can use.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L274-L277)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 16. Django 5.1 - `dj-b1651aff0f4fbafe`

> django.contrib.gis.db.models.Collect is now supported on MySQL 8.0.24+.

**Suggestion:** Configuration/deployment

**Why:** Collect support depends on the deployed MySQL version, 8.0.24 or later.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L145-L146)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 17. Django 5.1 - `dj-7e925deb98cd6af6`

> Django 5.1 also introduces connection pool support for PostgreSQL. As the time to establish a new connection can be relatively long, keeping connections open can reduce latency.

**Suggestion:** Configuration/deployment

**Why:** PostgreSQL connection pooling is a database connection setup choice.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L62-L64)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 18. Django 5.1 - `dj-6bbbc8a088188e4d`

> django.db.models.FileField now raises a django.core.exceptions.FieldError when saving a file without a name.

**Suggestion:** API/code compatibility

**Why:** Saving a nameless FileField now raises FieldError; caller exception handling may change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L392-L394)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 19. Django 5.1 - `dj-d959af03ec5ba16d`

> The django.contrib.gis.geoip2.GeoIP2.coords() method is deprecated. Use django.contrib.gis.geoip2.GeoIP2.lon_lat() instead.

**Suggestion:** API/code compatibility

**Why:** Callers of the deprecated GeoIP2.coords method should use lon_lat.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L426-L427)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 20. Django 5.1 - `dj-a164a11a27166e80`

> Django 5.1 introduces the {% querystring %} template tag, simplifying the modification of query parameters in URLs, making it easier to generate links that maintain existing query parameters while adding or changing specific ones.

**Suggestion:** UI/output behavior

**Why:** The querystring template tag changes the URLs rendered in page links.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L33-L36)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 21. Django 5.1 - `dj-bd050fedc89aba5f`

> The model django.contrib.postgres.fields.CICharField, django.contrib.postgres.fields.CIEmailField, and django.contrib.postgres.fields.CITextField are removed, except for support in historical migrations.

**Suggestion:** API/code compatibility

**Why:** The removed CI model field classes require code references to change; historical migrations remain supported.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L472-L475)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 22. Django 5.2 - `dj-6fa40a5f9d9c888a`

> The ordering keyword argument of the PostgreSQL specific aggregation functions django.contrib.postgres.aggregates.ArrayAgg, django.contrib.postgres.aggregates.JSONBAgg, and django.contrib.postgres.aggregates.StringAgg is deprecated in favor of the order_by argument.

**Suggestion:** API/code compatibility

**Why:** Calls using the deprecated ordering keyword should switch to order_by.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L487-L491)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 23. Django 5.2 - `dj-5c5d2b04ae2173a1`

> Django 5.2 supports Python 3.10, 3.11, 3.12, 3.13, and 3.14 (as of 5.2.8). We highly recommend and only officially support the latest release of each series.

**Suggestion:** Configuration/deployment

**Why:** The note states which Python runtimes are supported for deployment.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L26-L28)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 24. Django 5.2 - `dj-d3edaa87ce8b253a`

> The new asset object django.forms.Script is available for adding custom HTML-attributes to JavaScript in form media. See paths as objects for more details.

**Suggestion:** API/code compatibility

**Why:** The new django.forms.Script object is a Python interface for form media customization.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L271-L273)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 25. Django 5.2 - `dj-0cc1acf852043dd7`

> The attribute SafeExceptionReporterFilter.hidden_settings now treats values as sensitive if their name includes AUTH.

**Suggestion:** UI/output behavior

**Why:** Error-report output now hides more setting values as sensitive.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L244-L245)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 26. Django 5.2 - `dj-ec3e5e75bc45b053`

> The SELECT clause generated when using QuerySet.values and QuerySet.values_list now matches the specified order of the referenced expressions. Previously, the order was based on a set of counterintuitive rules which made query combination through methods such as QuerySet.union unpredictable.

**Suggestion:** Data/schema migration

**Why:** The generated SELECT and combined queryset behavior change ORM data results.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L300-L304)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 27. Django 5.2 - `dj-0b3c7c48bbee90ab`

> MySQL connections now default to using the utf8mb4 character set, instead of utf8, which is an alias for the deprecated character set utf8mb3.

**Suggestion:** Configuration/deployment

**Why:** The default MySQL connection character set changes; check database connection setup.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L211-L213)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 28. Django 5.2 - `dj-dc0f40c9b1aa4825`

> Tuple items of EmailMessage.attachments and EmailMultiAlternatives.attachments are now named tuples, as opposed to regular tuples.

**Suggestion:** API/code compatibility

**Why:** Attachment tuple objects change shape to named tuples, affecting consuming code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L227-L231)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 29. Django 6.0 - `dj-7339e91a634f4dda`

> Migrations now support serialization of zoneinfo.ZoneInfo instances.

**Suggestion:** Data/schema migration

**Why:** Serialization of ZoneInfo instances is a migration-data behavior.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L272-L272)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 30. Django 6.0 - `dj-336f88e0d839a604`

> The new variable forloop.length is now available within a for loop.

**Suggestion:** UI/output behavior

**Why:** The new template loop variable changes what a rendered template can show.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L339-L340)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 31. Django 6.0 - `dj-ddba9b903cdaeed4`

> Widgets from django.contrib.gis.forms.widgets now render without inline JavaScript in templates. If you have customized any geometry widgets or their templates, you may need to update them to match the new layout.

**Suggestion:** UI/output behavior

**Why:** GIS widgets render with a new template layout and no inline JavaScript.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L203-L206)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 32. Django 6.0 - `dj-011546728c329f4d`

> The undocumented django.utils.itercompat.is_iterable() function and the django.utils.itercompat module are removed.

**Suggestion:** API/code compatibility

**Why:** The removed module and function require import or call sites to change.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L610-L611)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 33. Django 6.0 - `dj-d5bdeb4d58793c93`

> Added support and translations for the Haitian Creole language.

**Suggestion:** UI/output behavior

**Why:** New translations affect the language visible in the interface.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L255-L255)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 34. Django 6.0 - `dj-084daac63d98e842`

> Setting ADMINS or MANAGERS to a list of (name, address) tuples is deprecated. Set to a list of email address strings instead. Django never used the name portion. To include a name, format the address string as '"Name" &lt;address>' or use Python's email.utils.formataddr.

**Suggestion:** Configuration/deployment

**Why:** ADMINS and MANAGERS must use a new settings value format.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L525-L528)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 35. Django 6.0 - `dj-1d4b9ff2c767f776`

> Common utilities, such as django.conf.settings, are now automatically imported to the shell by default.

**Suggestion:** UI/output behavior

**Why:** The shell command now shows common utilities already imported in its interactive namespace.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L263-L264)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 36. Django 6.0.1 - `dj-59245797e13cfb5e`

> Fixed a regression in Django 6.0 where querystring mishandled multi-value django.http.QueryDict keys, both by only preserving the last value and by incorrectly handling None values (36783).

**Suggestion:** UI/output behavior

**Why:** The querystring tag now preserves multi-value query parameters in generated URLs.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L15-L17)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 37. Django 5.2.1 - `dj-c7bd7fe39300849a`

> Fixed a regression in Django 5.2 that caused fields to be incorrectly selected when using QuerySet.alias() after values() (36299).

**Suggestion:** Data/schema migration

**Why:** The fix changes fields selected by an ORM query using alias after values.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L40-L42)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 38. Django 5.2.2 - `dj-04a3fe93d7b8d201`

> Fixed a regression in Django 5.2 that caused a crash when using OuterRef in PostgreSQL aggregate functions ArrayAgg, StringAgg, and JSONBAgg (36405).

**Suggestion:** Data/schema migration

**Why:** The fix concerns an ORM aggregate query with OuterRef.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L44-L46)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 39. Django 5.2.7 - `dj-df0e5e3fd9cd3d49`

> Fixed a regression in Django 5.2 that reduced the color contrast of the chosen label of filter_horizontal and filter_vertical widgets within a TabularInline (36601).

**Suggestion:** UI/output behavior

**Why:** The fix restores the visible color contrast of admin widgets.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.7.txt#L31-L33)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 40. Django 5.2.5 - `dj-6aaeff8cf7961fc4`

> Fixed a crash in Django 5.2 when using a ManyToManyField on a model with a composite primary key, by extending the fields.E347 system check (36530).

**Suggestion:** Data/schema migration

**Why:** A ManyToManyField with a composite primary key is a model data relationship check.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.5.txt#L25-L27)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 41. Django 5.2.8 - `dj-e25c824b03887d30`

> Fixed a bug in Django 5.2 where proxy models having a CompositePrimaryKey incorrectly raised a models.E042 system check error.

**Suggestion:** Data/schema migration

**Why:** The system check concerns proxy models with composite primary keys.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.8.txt#L37-L38)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 42. Django 5.2.4 - `dj-bbc20fda80685fcc`

> Fixed a regression in Django 5.2.2 where HttpRequest.get_preferred_type() incorrectly preferred more specific media types with a lower quality (36447).

**Suggestion:** UI/output behavior

**Why:** The selected media type can change the HTTP response behavior seen by a client.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.4.txt#L12-L14)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 43. Django 6.0.1 - `dj-ba412e63aeda0cd0`

> Reverted an undocumented optimization in Django 6.0 that modified permission django.contrib.auth.models.Permission.name and django.contrib.auth.models.Permission.codename values when renaming models via a migration. This change could affect unrelated django.contrib.auth.models.Permission objects (36843) and did not report conflicts (36793).

**Suggestion:** Data/schema migration

**Why:** The migration changed persisted Permission names and codenames, including unrelated objects.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L46-L51)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 44. Django 5.2.2 - `dj-4a8efa894f79d51e`

> Fixed a bug in Django 5.2 where subqueries using "pk" to reference models with a CompositePrimaryKey failed to raise ValueError when too many or too few columns were selected (36392).

**Suggestion:** API/code compatibility

**Why:** The affected subquery now raises ValueError for an invalid column count.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L30-L32)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 45. Django 5.2.1 - `dj-3ff986b6ec1f8f96`

> django.utils.html.strip_tags would be slow to evaluate certain inputs containing large sequences of incomplete HTML tags. This function is used to implement the striptags template filter, which was thus also vulnerable.

**Suggestion:** UNCLEAR

**Why:** The note explicitly names both the strip_tags function and striptags template filter; code and template checks are both plausible.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L18-L21)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 46. Django 6.0.1 - `dj-6622909c675e5b94`

> Fixed a regression in Django 6.0 where the Widget.use_fieldset attribute of django.forms.ClearableFileInput was flipped from False to True (36829).

**Suggestion:** UI/output behavior

**Why:** The widget's fieldset setting affects the rendered file input form.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L42-L44)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 47. Django 6.0.1 - `dj-b80011775cf9c280`

> Fixed a regression in Django 6.0 that prevented changing the name of a django.db.models.ManyToManyField from taking effect when applying migrations (36800).

**Suggestion:** Data/schema migration

**Why:** Renaming a ManyToManyField now takes effect when applying migrations.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L19-L21)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 48. Django 5.2.2 - `dj-53764143ae68d36e`

> Fixed a regression in Django 5.2 that caused a crash when no arguments were passed into QuerySet.union() (36388).

**Suggestion:** API/code compatibility

**Why:** QuerySet.union with no arguments previously crashed; check such method calls.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L34-L35)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 49. Django 5.2.2 - `dj-92d2ac7ed0baf73b`

> Fixed a regression in Django 5.2 where subclasses of RemoteUserMiddleware that had overridden process_request() were no longer supported (36390).

**Suggestion:** API/code compatibility

**Why:** RemoteUserMiddleware subclasses that override process_request are the affected code interface.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L37-L39)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 50. Django 6.0.1 - `dj-b84631950773a092`

> Fixed a crash in Django 6.0 caused by infinite recursion when calling repr() on an unevaluated django.utils.csp.LazyNonce instance (36810).

**Suggestion:** API/code compatibility

**Why:** Calling repr on a LazyNonce object is the affected Python interface.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L34-L36)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

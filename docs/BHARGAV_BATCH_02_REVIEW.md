# Bhargav batch 02: 50 draft label suggestions

> **DRAFT — AGENT SUGGESTIONS ONLY.** Bhargav Panchal must review these 50 rows. No label from this batch is in the confirmed dataset.

Prepared: 2026-11-01. Source: pinned official Django release notes. This is an annotation queue, not a representative test set.

**Selection:** Fourteen entries from Django 4.2, seventeen from 5.0, ten from 5.1, and nine from 6.0. A fixed hash order selected entries after excluding 450 confirmed IDs, short or incomplete fragments, and pairs with SequenceMatcher text similarity at least 0.96. The earlier 0.88 near-duplicate filter left only 27 unused candidates, so this batch includes additional related notes. They need the final cross-release duplicate audit before evaluation. Selection did not use labels.

**How to review:** Read the complete note, proposed label, reason, and official source, then use [the label guide](DATA_AND_LABELS.md). Reply `Confirm all` or list changes by row number, such as `16 -> Data/schema migration`. You can confirm smaller ranges. Mark a bad extraction `EXCLUDE` instead of forcing a label. Suggestions do not become human decisions until you confirm them.

**Draft counts:** API/code compatibility: 20; Configuration/deployment: 21; Data/schema migration: 7; UI/output behavior: 2; No targeted check stated: 0; UNCLEAR: 0.

## Quick index

| No. | Django | Proposed label | Bhargav's decision |
| ---: | --- | --- | --- |
| 01 | 4.2 | UI/output behavior | __________ |
| 02 | 4.2 | API/code compatibility | __________ |
| 03 | 4.2 | Configuration/deployment | __________ |
| 04 | 4.2 | Data/schema migration | __________ |
| 05 | 4.2 | Configuration/deployment | __________ |
| 06 | 4.2 | Configuration/deployment | __________ |
| 07 | 4.2 | Data/schema migration | __________ |
| 08 | 4.2 | API/code compatibility | __________ |
| 09 | 4.2 | Configuration/deployment | __________ |
| 10 | 4.2 | UI/output behavior | __________ |
| 11 | 4.2 | Data/schema migration | __________ |
| 12 | 4.2 | Configuration/deployment | __________ |
| 13 | 4.2 | Configuration/deployment | __________ |
| 14 | 4.2 | API/code compatibility | __________ |
| 15 | 5.0 | API/code compatibility | __________ |
| 16 | 5.0 | Configuration/deployment | __________ |
| 17 | 5.0 | API/code compatibility | __________ |
| 18 | 5.0 | Configuration/deployment | __________ |
| 19 | 5.0 | API/code compatibility | __________ |
| 20 | 5.0 | Configuration/deployment | __________ |
| 21 | 5.0 | API/code compatibility | __________ |
| 22 | 5.0 | Configuration/deployment | __________ |
| 23 | 5.0 | API/code compatibility | __________ |
| 24 | 5.0 | Data/schema migration | __________ |
| 25 | 5.0 | Data/schema migration | __________ |
| 26 | 5.0 | Configuration/deployment | __________ |
| 27 | 5.0 | API/code compatibility | __________ |
| 28 | 5.0 | Configuration/deployment | __________ |
| 29 | 5.0 | Data/schema migration | __________ |
| 30 | 5.0 | API/code compatibility | __________ |
| 31 | 5.0 | Configuration/deployment | __________ |
| 32 | 5.1 | API/code compatibility | __________ |
| 33 | 5.1 | Configuration/deployment | __________ |
| 34 | 5.1 | Configuration/deployment | __________ |
| 35 | 5.1 | API/code compatibility | __________ |
| 36 | 5.1 | Configuration/deployment | __________ |
| 37 | 5.1 | API/code compatibility | __________ |
| 38 | 5.1 | Configuration/deployment | __________ |
| 39 | 5.1 | Data/schema migration | __________ |
| 40 | 5.1 | API/code compatibility | __________ |
| 41 | 5.1 | API/code compatibility | __________ |
| 42 | 6.0 | Configuration/deployment | __________ |
| 43 | 6.0 | API/code compatibility | __________ |
| 44 | 6.0 | Configuration/deployment | __________ |
| 45 | 6.0 | Configuration/deployment | __________ |
| 46 | 6.0 | API/code compatibility | __________ |
| 47 | 6.0 | Configuration/deployment | __________ |
| 48 | 6.0 | API/code compatibility | __________ |
| 49 | 6.0 | API/code compatibility | __________ |
| 50 | 6.0 | API/code compatibility | __________ |

## Full review

### 01. Django 4.2 — `dj-824f9f77e31f43a1`

> The map_height and map_width attributes of BaseGeometryWidget are deprecated, use CSS to size map widgets instead.

**Suggestion:** UI/output behavior

**Why:** GIS map-widget sizing moves from attributes to CSS display rules.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L602-L603)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 02. Django 4.2 — `dj-58cf6129825ebaf1`

> The django.contrib.gis.gdal.GDALRaster class now supports pathlib.Path.

**Suggestion:** API/code compatibility

**Why:** Code constructing GDALRaster can now pass pathlib.Path.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L165-L166)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 03. Django 4.2 — `dj-0caed1893de9c4b8`

> Django 4.2 supports Python 3.8, 3.9, 3.10, 3.11, and 3.12 (as of 4.2.8). We highly recommend and only officially support the latest release of each series.

**Suggestion:** Configuration/deployment

**Why:** The Python runtime version must be checked against supported versions.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L26-L28)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 04. Django 4.2 — `dj-dc88a878dc11c36a`

> The makemigrations --check option no longer creates missing migration files.

**Suggestion:** Data/schema migration

**Why:** The migration check command no longer writes missing migration files.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L434-L435)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 05. Django 4.2 — `dj-6077a683265860f3`

> Upstream support for MariaDB 10.3 ends in May 2023. Django 4.2 supports MariaDB 10.4 and higher.

**Suggestion:** Configuration/deployment

**Why:** The deployed MariaDB version must be at least 10.4.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L387-L388)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 06. Django 4.2 — `dj-bc23b0212fced48b`

> Upstream support for PostgreSQL 11 ends in November 2023. Django 4.2 supports PostgreSQL 12 and higher.

**Suggestion:** Configuration/deployment

**Why:** The deployed PostgreSQL version must be at least 12.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L399-L400)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 07. Django 4.2 — `dj-44c4cba3d7b7318a`

> F() expressions that output BooleanField can now be negated using ~F() (inversion operator).

**Suggestion:** Data/schema migration

**Why:** Negated F expressions change ORM Boolean query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L296-L297)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 08. Django 4.2 — `dj-e9ae32e5f42dfcda`

> SimpleTestCase.assertFormsetError() is deprecated in favor of assertFormSetError().

**Suggestion:** API/code compatibility

**Why:** Tests should call assertFormSetError rather than the deprecated method name.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L605-L606)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 09. Django 4.2 — `dj-44a43369c03e7a92`

> The minimum supported version of asgiref is increased from 3.5.2 to 3.6.0.

**Suggestion:** Configuration/deployment

**Why:** The installed asgiref version must satisfy the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L450-L451)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 10. Django 4.2 — `dj-4c52455de1270249`

> The OpenLayers template widget no longer includes inline CSS (which also removes the former map_css block) to better comply with a strict Content Security Policy.

**Suggestion:** UI/output behavior

**Why:** The OpenLayers widget no longer renders inline CSS or its map_css block.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L171-L173)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 11. Django 4.2 — `dj-e5a5fc0033748206`

> django.contrib.postgres.fields.CITextField is deprecated in favor of TextField(db_collation="…") with a case-insensitive non-deterministic collation.

**Suggestion:** Data/schema migration

**Why:** CITextField replacement involves database collation and field schema.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L596-L598)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 12. Django 4.2 — `dj-05b48e3b6dae8378`

> The minimum supported version of redis-py is increased from 3.0.0 to 3.4.0.

**Suggestion:** Configuration/deployment

**Why:** The installed redis-py version must satisfy the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L468-L469)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 13. Django 4.2 — `dj-c38fc290d84fd733`

> The STATICFILES_STORAGE setting is deprecated in favor of STORAGES["staticfiles"].

**Suggestion:** Configuration/deployment

**Why:** Project static-file settings should move to STORAGES.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L617-L618)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 14. Django 4.2 — `dj-97fd457c2569ac8f`

> The undocumented negated parameter of the django.db.models.Exists expression is removed.

**Suggestion:** API/code compatibility

**Why:** Code constructing Exists cannot pass the removed negated parameter.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L442-L443)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 15. Django 5.0 — `dj-b45ac57dd7f8ec9f`

> The django.contrib.gis.admin.GeoModelAdmin and OSMGeoAdmin classes are removed.

**Suggestion:** API/code compatibility

**Why:** Admin integration code cannot import the removed GIS admin classes.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L703-L704)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 16. Django 5.0 — `dj-c0be835563299aef`

> The default iteration count for the PBKDF2 password hasher is increased from 600,000 to 720,000.

**Suggestion:** Configuration/deployment

**Why:** The default password-hasher work factor changes runtime security and cost.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L235-L236)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 17. Django 5.0 — `dj-44d9a2a03c899f6f`

> request is added to the signature of ModelAdmin.lookup_allowed. Support for ModelAdmin subclasses that do not accept this argument is deprecated.

**Suggestion:** API/code compatibility

**Why:** ModelAdmin.lookup_allowed subclasses should accept request.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L612-L614)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 18. Django 5.0 — `dj-9270e5c78d369543`

> The minimum supported version of docutils is increased to 0.19.

**Suggestion:** Configuration/deployment

**Why:** The installed docutils version must satisfy the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L590-L590)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 19. Django 5.0 — `dj-3d97572189fbd75f`

> The new django.shortcuts.aget_object_or_404 and django.shortcuts.aget_list_or_404 asynchronous shortcuts allow asynchronous getting objects.

**Suggestion:** API/code compatibility

**Why:** Async application code can use the new object lookup shortcuts.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L387-L389)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 20. Django 5.0 — `dj-7fcb7250012c1f73`

> Django 5.0 supports Python 3.10, 3.11, and 3.12. We highly recommend and only officially support the latest release of each series.

**Suggestion:** Configuration/deployment

**Why:** The deployed Python runtime must match the supported series.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L21-L22)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 21. Django 5.0 — `dj-8e82767edeb1773f`

> Passing nulls_first=False or nulls_last=False to Expression.asc() and Expression.desc() methods, and the OrderBy expression is no longer allowed.

**Suggestion:** API/code compatibility

**Why:** Code passing nulls_first=False or nulls_last=False must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L757-L759)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 22. Django 5.0 — `dj-fe18b0d5acb88cb3`

> FORMS_URLFIELD_ASSUME_HTTPS transitional setting is deprecated.

**Suggestion:** Configuration/deployment

**Why:** The transitional HTTPS form URL setting is deprecated.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L629-L629)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 23. Django 5.0 — `dj-779da1c74c29094f`

> Passing positional arguments name and violation_error_message to django.db.models.BaseConstraint is deprecated in favor of keyword-only arguments.

**Suggestion:** API/code compatibility

**Why:** BaseConstraint calls should use keyword arguments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L608-L610)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 24. Django 5.0 — `dj-9a068ca501ea1086`

> Integer fields are now validated as 64-bit integers on SQLite to match the behavior of sqlite3.

**Suggestion:** Data/schema migration

**Why:** SQLite integer-field validation now enforces 64-bit bounds.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L542-L543)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 25. Django 5.0 — `dj-44e31593a028e605`

> On MariaDB 10.7+, UUIDField is now created as UUID column rather than CHAR(32) column. See the migration guide above for more details on migrating-uuidfield.

**Suggestion:** Data/schema migration

**Why:** MariaDB UUIDField now uses a native UUID column, requiring schema review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L397-L399)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 26. Django 5.0 — `dj-7b4cacd834755d16`

> The minimum supported version of selenium is increased from 3.8.0 to 4.8.0.

**Suggestion:** Configuration/deployment

**Why:** The installed Selenium version must satisfy the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L571-L572)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 27. Django 5.0 — `dj-f8a9880442191e0a`

> The undocumented BaseForm._html_output() method is removed.

**Suggestion:** API/code compatibility

**Why:** Custom form code cannot call removed BaseForm._html_output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L706-L706)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 28. Django 5.0 — `dj-48030379118199c1`

> The CSRF_COOKIE_MASKED transitional setting is removed.

**Suggestion:** Configuration/deployment

**Why:** Project CSRF configuration cannot use the removed setting.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L716-L716)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 29. Django 5.0 — `dj-9fe89b7ded219b02`

> Filtering querysets against overflowing integer values now always returns an empty queryset. As a consequence, you may need to use ExpressionWrapper() to explicitly wrap arithmetic against integer fields in such cases.

**Suggestion:** Data/schema migration

**Why:** Overflowing integer filters now return empty querysets.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L592-L595)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 30. Django 5.0 — `dj-64702c3bf43faaa7`

> The undocumented django.utils.baseconv module is removed.

**Suggestion:** API/code compatibility

**Why:** Code importing the removed baseconv module must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L666-L666)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 31. Django 5.0 — `dj-c3306f93cfd4f491`

> The minimum supported version of asgiref is increased from 3.6.0 to 3.7.0.

**Suggestion:** Configuration/deployment

**Why:** The installed asgiref version must satisfy the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L568-L569)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 32. Django 5.1 — `dj-b011fb1c33111460`

> The new OGRGeometry.set_3d method allows addition and removal of the Z coordinate dimension.

**Suggestion:** API/code compatibility

**Why:** GIS code can call OGRGeometry.set_3d.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L164-L165)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 33. Django 5.1 — `dj-2def81586d7886cf`

> The minimum supported version of asgiref is increased from 3.7.0 to 3.8.1.

**Suggestion:** Configuration/deployment

**Why:** The installed asgiref version must satisfy the new minimum.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L401-L402)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 34. Django 5.1 — `dj-2ade41d8a4fe182e`

> Django 5.1 supports Python 3.10, 3.11, 3.12, and 3.13 (as of 5.1.3). We highly recommend and only officially support the latest release of each series.

**Suggestion:** Configuration/deployment

**Why:** The deployed Python runtime must match the supported series.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L21-L23)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 35. Django 5.1 — `dj-ec76bd9ebc875ab2`

> The django.contrib.gis.geoip2.GeoIP2.open() method is deprecated. Use the django.contrib.gis.geoip2.GeoIP2 constructor instead.

**Suggestion:** API/code compatibility

**Why:** Code calling GeoIP2.open should use the constructor.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L429-L430)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 36. Django 5.1 — `dj-870fd8b81d1c60b1`

> The DEFAULT_FILE_STORAGE and STATICFILES_STORAGE settings is removed.

**Suggestion:** Configuration/deployment

**Why:** Storage configuration cannot use the removed settings.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L492-L492)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 37. Django 5.1 — `dj-22df2f0be03ba748`

> Template engines now implement a check() method that is already registered with the check framework.

**Suggestion:** API/code compatibility

**Why:** Custom template engines can implement the check method.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L290-L291)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 38. Django 5.1 — `dj-1449ac4efdb41e55`

> Upstream support for MariaDB 10.4 ends in June 2024. Django 5.1 supports MariaDB 10.5 and higher.

**Suggestion:** Configuration/deployment

**Why:** The deployed MariaDB version must be at least 10.5.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L350-L351)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 39. Django 5.1 — `dj-860388c57c366700`

> django.contrib.gis.db.models.functions.BoundingCircle is now supported on SpatiaLite 5.1+.

**Suggestion:** Data/schema migration

**Why:** BoundingCircle adds a SpatiaLite database-query capability.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L142-L143)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 40. Django 5.1 — `dj-67c05ecb0bb507f8`

> django.contrib.gis.gdal.OGRGeometry, django.contrib.gis.gdal.Point, django.contrib.gis.gdal.LineString, django.contrib.gis.gdal.Polygon, and django.contrib.gis.gdal.GeometryCollection and its subclasses now support measured geometries via the new OGRGeometry.is_measured and m properties, and the OGRGeometry.set_measured method.

**Suggestion:** API/code compatibility

**Why:** GIS code can access measured-geometry properties and methods.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L167-L173)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 41. Django 5.1 — `dj-5ab216a837e6cb90`

> The django.core.files.storage.get_storage_class() function is removed.

**Suggestion:** API/code compatibility

**Why:** Code calling the removed get_storage_class function must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L494-L494)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 42. Django 6.0 — `dj-9bb0f2c834a0031c`

> The minimum supported version of asgiref is increased from 3.8.1 to 3.9.1.

**Suggestion:** Configuration/deployment

**Why:** The installed asgiref version must satisfy the new minimum.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L481-L482)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 43. Django 6.0 — `dj-18debaeeabea3576`

> The django.contrib.gis.geoip2.GeoIP2.coords() method is removed.

**Suggestion:** API/code compatibility

**Why:** GIS code cannot call removed GeoIP2.coords.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L613-L613)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 44. Django 6.0 — `dj-af61d9658f42921f`

> The default iteration count for the PBKDF2 password hasher is increased from 1,000,000 to 1,200,000.

**Suggestion:** Configuration/deployment

**Why:** The default password-hasher work factor changes runtime security and cost.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L177-L178)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 45. Django 6.0 — `dj-b60b8bb23b91aa11`

> The Django 5.2.x series is the last to support Python 3.10 and 3.11.

**Suggestion:** Configuration/deployment

**Why:** The deployed Python runtime must account for the support cutoff.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L24-L24)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 46. Django 6.0 — `dj-a2d70b512f065eb1`

> The DatabaseOperations.fetch_returned_insert_columns() method is removed and the fetch_returned_rows() method replacing fetch_returned_insert_rows() expects both a cursor and returning_params to be provided, just like fetch_returned_insert_columns() did.

**Suggestion:** API/code compatibility

**Why:** Custom database backend code must use the new method and arguments.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L375-L379)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 47. Django 6.0 — `dj-b5ceb2bf4ea05054`

> The DjangoDivFormRenderer and Jinja2DivFormRenderer transitional form renderers are removed.

**Suggestion:** Configuration/deployment

**Why:** Form renderer configuration cannot reference removed renderer classes.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L564-L565)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 48. Django 6.0 — `dj-4d594cd898fcd496`

> Support for calling format_html() without passing args or kwargs is removed.

**Suggestion:** API/code compatibility

**Why:** format_html callers must provide args or kwargs.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L572-L573)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 49. Django 6.0 — `dj-2a307aa97af70ff0`

> The ForeignObject.get_reverse_joining_columns() method is removed.

**Suggestion:** API/code compatibility

**Why:** Custom ForeignObject code cannot call the removed method.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L586-L586)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

### 50. Django 6.0 — `dj-cb3cdd693a08f81f`

> The setter for django.contrib.gis.gdal.OGRGeometry.coord_dim is removed.

**Suggestion:** API/code compatibility

**Why:** GIS code should call set_3d instead of setting coord_dim.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L620-L620)

**Bhargav's decision:** Confirm / Change to: __________   **Note:** __________

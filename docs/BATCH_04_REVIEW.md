# Batch 04 (Om): 50 draft label suggestions

> **DRAFT - AGENT SUGGESTIONS ONLY.** Assigned to Om Nathani for review. These 50 rows are not human-confirmed labels and must not enter model training until he confirms or corrects them.

Prepared: 2026-10-28. The batch uses pinned official Django release-note entries. It is for annotation, not a representative test set.

**Selection:** Eight entries each from feature releases 4.2, 5.0, 5.1, 5.2, and 6.0, plus ten patch-release entries. The sampler excluded all 150 reviewed IDs, incomplete flattened fragments, and obvious near-duplicates, then preferred varied sections and patch releases with a fixed hash order. Selection did not use class labels. The current 150-row aggregate is `data/processed/reviewed_labels.csv`.

**How to review:** Read the full source text and my reason, then confirm or change each label using [the guide](DATA_AND_LABELS.md). Reply with `Confirm all except: 03 -> Configuration/deployment; 40 -> API/code compatibility` if those are your corrections, or confirm a smaller range. Your confirmed decisions will be credited to Om Nathani in the local record. `UNCLEAR` is allowed for a genuinely mixed note, with a reason; do not force a class to fill a quota.

Draft counts: API/code compatibility: 25; Configuration/deployment: 7; Data/schema migration: 10; UI/output behavior: 8; UNCLEAR: 0. No row clearly merits `No targeted check stated` from its text alone.

## Quick index

| No. | Django | Suggested label | Your decision |
| ---: | --- | --- | --- |
| 01 | 4.2 | UI/output behavior | __________ |
| 02 | 4.2 | API/code compatibility | __________ |
| 03 | 4.2 | API/code compatibility | __________ |
| 04 | 4.2 | Data/schema migration | __________ |
| 05 | 4.2 | Data/schema migration | __________ |
| 06 | 4.2 | Configuration/deployment | __________ |
| 07 | 4.2 | Configuration/deployment | __________ |
| 08 | 4.2 | UI/output behavior | __________ |
| 09 | 5.0 | API/code compatibility | __________ |
| 10 | 5.0 | API/code compatibility | __________ |
| 11 | 5.0 | API/code compatibility | __________ |
| 12 | 5.0 | API/code compatibility | __________ |
| 13 | 5.0 | API/code compatibility | __________ |
| 14 | 5.0 | API/code compatibility | __________ |
| 15 | 5.0 | API/code compatibility | __________ |
| 16 | 5.0 | API/code compatibility | __________ |
| 17 | 5.1 | API/code compatibility | __________ |
| 18 | 5.1 | API/code compatibility | __________ |
| 19 | 5.1 | Configuration/deployment | __________ |
| 20 | 5.1 | UI/output behavior | __________ |
| 21 | 5.1 | API/code compatibility | __________ |
| 22 | 5.1 | API/code compatibility | __________ |
| 23 | 5.1 | Configuration/deployment | __________ |
| 24 | 5.1 | API/code compatibility | __________ |
| 25 | 5.2 | API/code compatibility | __________ |
| 26 | 5.2 | API/code compatibility | __________ |
| 27 | 5.2 | Data/schema migration | __________ |
| 28 | 5.2 | API/code compatibility | __________ |
| 29 | 5.2 | API/code compatibility | __________ |
| 30 | 5.2 | Data/schema migration | __________ |
| 31 | 5.2 | Configuration/deployment | __________ |
| 32 | 5.2 | API/code compatibility | __________ |
| 33 | 6.0 | Data/schema migration | __________ |
| 34 | 6.0 | UI/output behavior | __________ |
| 35 | 6.0 | Configuration/deployment | __________ |
| 36 | 6.0 | API/code compatibility | __________ |
| 37 | 6.0 | API/code compatibility | __________ |
| 38 | 6.0 | Configuration/deployment | __________ |
| 39 | 6.0 | UI/output behavior | __________ |
| 40 | 6.0 | UI/output behavior | __________ |
| 41 | 6.0.1 | API/code compatibility | __________ |
| 42 | 5.2.1 | API/code compatibility | __________ |
| 43 | 5.2.5 | Data/schema migration | __________ |
| 44 | 5.2.2 | Data/schema migration | __________ |
| 45 | 5.2.8 | API/code compatibility | __________ |
| 46 | 5.2.1 | UI/output behavior | __________ |
| 47 | 5.2.2 | Data/schema migration | __________ |
| 48 | 5.2.1 | Data/schema migration | __________ |
| 49 | 5.2.1 | Data/schema migration | __________ |
| 50 | 5.2.1 | UI/output behavior | __________ |

## Notes and reasons

### 01. Django 4.2 - `dj-85f9bf45589dc7f0`

> The autofocus HTML attribute in the admin search box is removed as it can be confusing for screen readers.

**Suggestion:** UI/output behavior

**Why:** The admin search box no longer renders with autofocus; check the visible form behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L431-L432)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 02. Django 4.2 - `dj-2f25f32a43f316f4`

> django.contrib.postgres.fields.CIText mixin is deprecated.

**Suggestion:** API/code compatibility

**Why:** Code importing or inheriting the deprecated CIText mixin needs review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L600-L600)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 03. Django 4.2 - `dj-a3554bb0e93400f9`

> django.contrib.staticfiles.storage.ManifestStaticFilesStorage now has experimental support for replacing paths to JavaScript modules in import and export statements with their hashed counterparts. If you want to try it, subclass ManifestStaticFilesStorage and set the support_js_module_import_aggregation attribute to True.

**Suggestion:** API/code compatibility

**Why:** The opt-in requires a ManifestStaticFilesStorage subclass and a named attribute in code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L209-L213)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 04. Django 4.2 - `dj-8dbfa8a114c4c41a`

> QuerySet.prefetch_related now supports django.db.models.Prefetch objects with sliced querysets.

**Suggestion:** Data/schema migration

**Why:** Prefetch with sliced querysets changes ORM data retrieval behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L279-L280)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 05. Django 4.2 - `dj-583ba5e4cbae7447`

> Migrations now support serialization of enum.Flag objects.

**Suggestion:** Data/schema migration

**Why:** Serialization of enum.Flag values is a migration-data behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L270-L270)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 06. Django 4.2 - `dj-ee8ad56ac42ae5df`

> The new "assume_role" option is now supported in OPTIONS on PostgreSQL to allow specifying the session role.

**Suggestion:** Configuration/deployment

**Why:** The PostgreSQL session role is set through database connection OPTIONS.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L222-L223)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 07. Django 4.2 - `dj-86c8ddcddbb7b9ae`

> Upstream support for MySQL 5.7 ends in October 2023. Django 4.2 supports MySQL 8 and higher.

**Suggestion:** Configuration/deployment

**Why:** MySQL 8 or later is a database deployment requirement.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L393-L394)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 08. Django 4.2 - `dj-e8edcfa8118ff3dd`

> The debug page now shows exception notes and fine-grained error locations on Python 3.11+.

**Suggestion:** UI/output behavior

**Why:** The development debug page displays exception notes and error locations differently.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L232-L233)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 09. Django 5.0 - `dj-62a0019778368b21`

> The django.contrib.gis.admin.OpenLayersWidget is removed.

**Suggestion:** API/code compatibility

**Why:** References to the removed OpenLayersWidget class must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L748-L748)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 10. Django 5.0 - `dj-d2e264b91074e4fb`

> The undocumented django.contrib.admin.helpers.checkbox is removed.

**Suggestion:** API/code compatibility

**Why:** Code using the removed admin.helpers.checkbox helper must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L540-L540)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 11. Django 5.0 - `dj-bf7f2d9a8f82d7eb`

> The django.db.models.enums.ChoicesMeta metaclass is renamed to ChoicesType.

**Suggestion:** API/code compatibility

**Why:** Imports or references to the renamed metaclass need review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L642-L643)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 12. Django 5.0 - `dj-9af1304b59dbc724`

> django.views.decorators.debug.sensitive_variables and django.views.decorators.debug.sensitive_post_parameters can now be used with asynchronous functions.

**Suggestion:** API/code compatibility

**Why:** The sensitive_variables and sensitive_post_parameters decorators now accept async functions.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L328-L330)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 13. Django 5.0 - `dj-07fee769eaae1964`

> The new django.db.models.aprefetch_related_objects function allows asynchronous prefetching of model instances.

**Suggestion:** API/code compatibility

**Why:** The new asynchronous prefetch function is an interface for application code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L391-L392)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 14. Django 5.0 - `dj-1faf5d1443fe8159`

> The new AdminSite.get_model_admin method returns an admin class for the given model class.

**Suggestion:** API/code compatibility

**Why:** The new AdminSite.get_model_admin method is a Python interface.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L223-L224)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 15. Django 5.0 - `dj-859dd9ff55a99b70`

> The new offset argument of django.core.validators.StepValueValidator allows specifying an offset for valid values.

**Suggestion:** API/code compatibility

**Why:** StepValueValidator gains an offset argument for code to pass.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L442-L444)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 16. Django 5.0 - `dj-3c588bb1fa8f22fa`

> QuerySet.update_or_create now supports the parameter create_defaults. As a consequence, any models that have a field named create_defaults that are used with an update_or_create() should specify the field in the lookup with create_defaults__exact.

**Suggestion:** API/code compatibility

**Why:** update_or_create callers using a create_defaults field need a new lookup spelling.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L493-L496)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 17. Django 5.1 - `dj-8dbeb41ca821e623`

> The check keyword argument of CheckConstraint is deprecated in favor of condition.

**Suggestion:** API/code compatibility

**Why:** CheckConstraint callers should replace the deprecated check keyword with condition.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L441-L442)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 18. Django 5.1 - `dj-864456b917259879`

> GeoIP2.city now exposes the accuracy_radius and region_name values. In addition, the dma_code and region values are now exposed as metro_code and region_code, but the previous keys are also retained for backward compatibility.

**Suggestion:** API/code compatibility

**Why:** GeoIP2.city return values gain keys; consuming code may use or inspect them.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L154-L157)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 19. Django 5.1 - `dj-e9d57652e1f54388`

> Upstream support for PostgreSQL 12 ends in November 2024. Django 5.1 supports PostgreSQL 13 and higher.

**Suggestion:** Configuration/deployment

**Why:** PostgreSQL 13 or later is a database deployment requirement.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L356-L357)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 20. Django 5.1 - `dj-eb5a216b1cc321e5`

> SimpleTestCase.assertURLEqual and django.test.SimpleTestCase.assertInHTML now add ": " to the msg_prefix. This is consistent with the behavior of other assertions.

**Suggestion:** UI/output behavior

**Why:** The output message from two test assertions gains a colon and space.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L378-L380)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 21. Django 5.1 - `dj-993e9162c8561f1e`

> django.contrib.sessions.backends.base.SessionBase and all built-in session engines now provide async API. The new asynchronous methods all have a prefixed names, e.g. aget(), akeys(), or acycle_key().

**Suggestion:** API/code compatibility

**Why:** Session engines gain named asynchronous methods for code to call.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L197-L199)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 22. Django 5.1 - `dj-14d381d4d287f26a`

> The SimpleTestCase.assertFormsetError() method is removed.

**Suggestion:** API/code compatibility

**Why:** Calls to the removed assertFormsetError method must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L482-L482)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 23. Django 5.1 - `dj-787851d13b60a5ba`

> LoginRequiredMiddleware respects the login_url and redirect_field_name values set via the django.contrib.auth.decorators.login_required decorator, but does not support setting login_url or redirect_field_name via the django.contrib.auth.mixins.LoginRequiredMixin.

**Suggestion:** Configuration/deployment

**Why:** The note describes which authentication redirect settings middleware respects.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L95-L99)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 24. Django 5.1 - `dj-7ec0704bb28f09f2`

> django.db.models.expressions.RowRange now accepts positive integers for the start argument and negative integers for the end argument.

**Suggestion:** API/code compatibility

**Why:** RowRange accepts additional numeric argument values in Python code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L255-L256)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 25. Django 5.2 - `dj-143f120d29d72b98`

> The new HttpRequest.get_preferred_type method can be used to query the preferred media type the client accepts.

**Suggestion:** API/code compatibility

**Why:** HttpRequest gains a method returning the client's preferred media type.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L334-L335)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 26. Django 5.2 - `dj-99db6b856a30068e`

> The makemigrations and migrate commands have a new Command.autodetector attribute for subclasses to override in order to use a custom autodetector class.

**Suggestion:** API/code compatibility

**Why:** A management-command subclass can override the new autodetector attribute.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L283-L285)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 27. Django 5.2 - `dj-ee99eee96eb85ab7`

> The new operation AlterConstraint is a no-op operation that alters constraints without dropping and recreating constraints in the database.

**Suggestion:** Data/schema migration

**Why:** AlterConstraint changes how a migration alters a database constraint.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L294-L295)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 28. Django 5.2 - `dj-9a669d4336b847cb`

> django.utils.safestring.SafeString now returns NotImplemented in __add__ for non-string right-hand side values. This aligns with the str addition behavior and allows __radd__ to be used if available.

**Suggestion:** API/code compatibility

**Why:** SafeString.__add__ now returns NotImplemented for a non-string value.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L383-L386)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 29. Django 5.2 - `dj-47e91bf7b32294d6`

> The password validator classes now have a new method get_error_message(), which can be overridden in subclasses to customize the error messages.

**Suggestion:** API/code compatibility

**Why:** Password-validator subclasses can override the new get_error_message method.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L185-L187)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 30. Django 5.2 - `dj-cc01b4964f593da0`

> The new django.db.models.functions.JSONArray database function accepts a list of field names or expressions and returns a JSON array containing those values.

**Suggestion:** Data/schema migration

**Why:** JSONArray changes the values returned by a database expression.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L320-L322)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 31. Django 5.2 - `dj-8d46c19101e65282`

> Oracle backends now support connection pools, by setting "pool" in the OPTIONS part of your database configuration.

**Suggestion:** Configuration/deployment

**Why:** Oracle connection pooling is enabled through database OPTIONS.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L215-L216)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 32. Django 5.2 - `dj-5c237fcaabf7f13f`

> The all argument for the django.contrib.staticfiles.finders.find() function is deprecated in favor of the find_all argument.

**Suggestion:** API/code compatibility

**Why:** Callers of staticfiles.find should replace all with find_all.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L480-L481)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 33. Django 6.0 - `dj-9f72b7b846547e50`

> The new django.db.models.AnyValue aggregate returns an arbitrary value from the non-null input values. This is supported on SQLite, MySQL, Oracle, and PostgreSQL 16+.

**Suggestion:** Data/schema migration

**Why:** AnyValue changes the values produced by an ORM aggregate query.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L307-L309)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 34. Django 6.0 - `dj-0147760521c98dd3`

> The Django Template Language now supports template partials, making it easier to encapsulate and reuse small named fragments within a template file. The new tags {% partialdef %} and {% partial %} define a partial and render it, respectively.

**Suggestion:** UI/output behavior

**Why:** Template partials change what fragments a template can render.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L81-L85)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 35. Django 6.0 - `dj-28ebbe91ba0f85e7`

> Upstream support for MariaDB 10.5 ends in June 2025. Django 6.0 supports MariaDB 10.6 and higher.

**Suggestion:** Configuration/deployment

**Why:** MariaDB 10.6 or later is a database deployment requirement.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L387-L388)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 36. Django 6.0 - `dj-1270fb8e2268e8e2`

> The get_prefetch_queryset() method of related managers and descriptors is removed.

**Suggestion:** API/code compatibility

**Why:** Code using the removed get_prefetch_queryset method needs review.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L595-L596)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 37. Django 6.0 - `dj-05392308b8db8af5`

> The PostgreSQL StringAgg class is deprecated in favor of the generally available django.db.models.StringAgg class.

**Suggestion:** API/code compatibility

**Why:** Imports or uses of PostgreSQL StringAgg should move to the general class.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L511-L512)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 38. Django 6.0 - `dj-0ede19711f34187e`

> Multiple Cookie headers are now supported for HTTP/2 requests when running with ASGI.

**Suggestion:** Configuration/deployment

**Why:** The change concerns HTTP/2 Cookie handling in an ASGI deployment.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L333-L334)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 39. Django 6.0 - `dj-e404be26e5b5904c`

> Message levels messages.DEBUG and messages.INFO now have distinct icons and CSS styling. Previously, both levels shared the same appearance as messages.SUCCESS. Given that ModelAdmin.message_user uses messages.INFO by default, set the level to messages.SUCCESS to keep the previous icon and styling.

**Suggestion:** UI/output behavior

**Why:** Admin message levels have different icons and CSS styling.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L168-L172)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 40. Django 6.0 - `dj-42c1a4a8e9dadaf5`

> The new BaseGeometryWidget.base_layer attribute allows specifying a JavaScript map base layer, enabling customization of map tile providers.

**Suggestion:** UI/output behavior

**Why:** The geometry widget's map base layer changes visible map tiles.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L190-L191)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 41. Django 6.0.1 - `dj-af36753c3de0efc4`

> Fixed a regression in Django 6.0 where django.urls.path routes defined using django.utils.translation.gettext_lazy failed to resolve correctly (36796).

**Suggestion:** API/code compatibility

**Why:** Code defining translated path routes is the affected interface.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L38-L40)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 42. Django 5.2.1 - `dj-4f7e7d1bde6bf560`

> Fixed a regression in Django 5.2 that caused improper values to be returned from QuerySet.values_list() when duplicate field names were specified (36288).

**Suggestion:** API/code compatibility

**Why:** values_list returned an incorrect value shape for duplicate field names.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L53-L55)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 43. Django 5.2.5 - `dj-0db04252c24ebb63`

> Fixed a regression in Django 5.2.1 that prevented the usage of UNNEST PostgreSQL strategy of QuerySet.bulk_create() with foreign keys (36502).

**Suggestion:** Data/schema migration

**Why:** The fix changes ORM bulk_create behavior for foreign keys.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.5.txt#L12-L14)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 44. Django 5.2.2 - `dj-ac4c0b147df26ca4`

> Fixed a regression in Django 5.2 that caused a crash when using QuerySet.prefetch_related() to prefetch a foreign key with a Prefetch queryset for a subclass of the foreign target (36432).

**Suggestion:** Data/schema migration

**Why:** The fix changes ORM prefetch behavior for a foreign-key relationship.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L61-L63)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 45. Django 5.2.8 - `dj-3a97d56b7824b9dd`

> QuerySet.filter, QuerySet.exclude, QuerySet.get, and Q were subject to SQL injection using a suitably crafted dictionary, with dictionary expansion, as the _connector argument.

**Suggestion:** API/code compatibility

**Why:** Untrusted dictionary expansion into named ORM methods is the code path to check.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.8.txt#L24-L26)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 46. Django 5.2.1 - `dj-8074ff66d177ca80`

> Fixed a regression in Django 5.2, introduced when fixing 2025-26699, where the wordwrap template filter did not preserve empty lines between paragraphs after wrapping text (36341).

**Suggestion:** UI/output behavior

**Why:** The wordwrap template filter changes the rendered text's blank lines.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L65-L67)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 47. Django 5.2.2 - `dj-18fb764d36310e70`

> Fixed a crash when using select_related against a ForeignObject originating from a model with a CompositePrimaryKey (36373).

**Suggestion:** Data/schema migration

**Why:** select_related with a composite primary key affects ORM data retrieval.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L27-L28)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 48. Django 5.2.1 - `dj-827b6fdbaaeaf250`

> Fixed a regression in Django 5.2 that caused a crash when using QuerySet.select_for_update(of=(…)) with values()/values_list() including expressions (36301).

**Suggestion:** Data/schema migration

**Why:** select_for_update with expressions changes ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L49-L51)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 49. Django 5.2.1 - `dj-f7e13b7d851a4c88`

> Fixed a regression in Django 5.2 that caused a crash when using update() on a QuerySet filtered against a related model and including references to annotations through values() (36360).

**Suggestion:** Data/schema migration

**Why:** The fix concerns ORM update queries with related-model filters and annotations.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L72-L74)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

### 50. Django 5.2.1 - `dj-2a56e41e477c0ad9`

> Fixed a regression in Django 5.2 where the password validation error message from MinimumLengthValidator was not translated when using non-English locales (36314).

**Suggestion:** UI/output behavior

**Why:** Password-validation error text is now translated for non-English locales.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L57-L59)

**Om's decision:** Confirm / Change to: __________   **Note:** __________

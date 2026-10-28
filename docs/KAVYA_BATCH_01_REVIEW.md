# Kavya batch 01: 50 human-confirmed decisions

> **REVIEW COMPLETE.** Kavya confirmed all 50 proposed decisions on 2026-10-28, including keeping rows 32, 36, and 46 as `UNCLEAR`. The 47 five-class labels may be used for later training; the three `UNCLEAR` rows remain review-only. The original pilot is untouched.

Review completed: 2026-10-28. The rows are new entries from official pinned Django release notes. This is an annotation batch, not a representative test set.

**Selection:** Five rows each from feature releases 4.2, 5.0, 5.1, 5.2, and 6.0; the other 25 come from patch releases 5.2.1-5.2.8 and 6.0.1. The sampler excluded all 50 pilot IDs and three visibly incomplete extracted fragments, preferred different source sections, then used a fixed hash order. It did not use labels to choose rows. The 6.0 rows must not be treated as an untouched final test after this review; freeze a new final evaluation split later.

**Review outcome:** Kavya read the complete suggestion sheet and confirmed every proposed decision. This is human-confirmed review with proposed labels visible, not blind independent annotation. The canonical reviewer record is the ignored local `data/annotations/kavya_batch_01_labels.csv`; a reviewer-name-free export is `data/processed/kavya_batch_01_reviewed_labels.csv`.

Guide: [Data and labeling guide](DATA_AND_LABELS.md). The five model labels are API/code compatibility, Configuration/deployment, Data/schema migration, UI/output behavior, and No targeted check stated. `UNCLEAR` is a separate review state.

Confirmed counts: API/code compatibility: 16; Configuration/deployment: 6; Data/schema migration: 13; UI/output behavior: 12; UNCLEAR: 3. No row in this batch clearly merits `No targeted check stated`; do not force that class to fill a quota.

## Quick index

| No. | Django | Confirmed label | Review status |
| ---: | --- | --- | --- |
| 01 | 4.2 | UI/output behavior | Confirmed |
| 02 | 4.2 | UI/output behavior | Confirmed |
| 03 | 4.2 | UI/output behavior | Confirmed |
| 04 | 4.2 | Configuration/deployment | Confirmed |
| 05 | 4.2 | API/code compatibility | Confirmed |
| 06 | 5.0 | API/code compatibility | Confirmed |
| 07 | 5.0 | Configuration/deployment | Confirmed |
| 08 | 5.0 | Data/schema migration | Confirmed |
| 09 | 5.0 | API/code compatibility | Confirmed |
| 10 | 5.0 | API/code compatibility | Confirmed |
| 11 | 5.1 | API/code compatibility | Confirmed |
| 12 | 5.1 | API/code compatibility | Confirmed |
| 13 | 5.1 | Configuration/deployment | Confirmed |
| 14 | 5.1 | Configuration/deployment | Confirmed |
| 15 | 5.1 | Data/schema migration | Confirmed |
| 16 | 5.2 | UI/output behavior | Confirmed |
| 17 | 5.2 | API/code compatibility | Confirmed |
| 18 | 5.2 | API/code compatibility | Confirmed |
| 19 | 5.2 | Configuration/deployment | Confirmed |
| 20 | 5.2 | UI/output behavior | Confirmed |
| 21 | 6.0 | UI/output behavior | Confirmed |
| 22 | 6.0 | Data/schema migration | Confirmed |
| 23 | 6.0 | API/code compatibility | Confirmed |
| 24 | 6.0 | UI/output behavior | Confirmed |
| 25 | 6.0 | API/code compatibility | Confirmed |
| 26 | 5.2.1 | UI/output behavior | Confirmed |
| 27 | 5.2.1 | API/code compatibility | Confirmed |
| 28 | 5.2.1 | Data/schema migration | Confirmed |
| 29 | 5.2.1 | Data/schema migration | Confirmed |
| 30 | 5.2.1 | Data/schema migration | Confirmed |
| 31 | 5.2.2 | Data/schema migration | Confirmed |
| 32 | 5.2.2 | UNCLEAR | Confirmed |
| 33 | 5.2.2 | UI/output behavior | Confirmed |
| 34 | 5.2.2 | UI/output behavior | Confirmed |
| 35 | 5.2.2 | Data/schema migration | Confirmed |
| 36 | 5.2.3 | UNCLEAR | Confirmed |
| 37 | 5.2.3 | API/code compatibility | Confirmed |
| 38 | 5.2.3 | Data/schema migration | Confirmed |
| 39 | 5.2.4 | Data/schema migration | Confirmed |
| 40 | 5.2.4 | Data/schema migration | Confirmed |
| 41 | 5.2.5 | Data/schema migration | Confirmed |
| 42 | 5.2.5 | Configuration/deployment | Confirmed |
| 43 | 5.2.6 | API/code compatibility | Confirmed |
| 44 | 5.2.6 | API/code compatibility | Confirmed |
| 45 | 5.2.7 | API/code compatibility | Confirmed |
| 46 | 5.2.7 | UNCLEAR | Confirmed |
| 47 | 5.2.8 | API/code compatibility | Confirmed |
| 48 | 5.2.8 | Data/schema migration | Confirmed |
| 49 | 6.0.1 | UI/output behavior | Confirmed |
| 50 | 6.0.1 | UI/output behavior | Confirmed |

## Notes and reasons

### 01. Django 4.2 - `dj-d3570ba37c8bc12b`

> The test --debug-sql option now formats SQL queries with sqlparse.

**Confirmed label:** UI/output behavior

**Why:** The --debug-sql option changes the format of command output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L321-L322)

**Kavya's decision:** Confirmed as shown.

### 02. Django 4.2 - `dj-e7b11a458905612e`

> The list of common passwords used by CommonPasswordValidator is updated to the most recent version.

**Confirmed label:** UI/output behavior

**Why:** The validator's updated password list can change the validation result shown to a user.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L359-L360)

**Kavya's decision:** Confirmed as shown.

### 03. Django 4.2 - `dj-b2c39bdcf4235a76`

> The light or dark color theme of the admin can now be toggled in the UI, as well as being set to follow the system setting.

**Confirmed label:** UI/output behavior

**Why:** The admin's visible light/dark theme can be toggled.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L122-L123)

**Kavya's decision:** Confirmed as shown.

### 04. Django 4.2 - `dj-6713095c15a87138`

> makemessages command now supports locales with private sub-tags such as nl_NL-x-informal.

**Confirmed label:** Configuration/deployment

**Why:** The makemessages command changes which locale identifiers can be used in localization setup.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L261-L262)

**Kavya's decision:** Confirmed as shown.

### 05. Django 4.2 - `dj-fbb7c1421766a652`

> The new robust argument for django.db.transaction.on_commit allows performing actions that can fail after a database transaction is successfully committed.

**Confirmed label:** API/code compatibility

**Why:** The transaction.on_commit call gains a robust argument that application code can use.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L285-L287)

**Kavya's decision:** Confirmed as shown.

### 06. Django 5.0 - `dj-c307f51e0535fea5`

> The DjangoDivFormRenderer and Jinja2DivFormRenderer transitional form renderers are deprecated.

**Confirmed label:** API/code compatibility

**Why:** Code using either deprecated form-renderer class should be reviewed.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L605-L606)

**Kavya's decision:** Confirmed as shown.

### 07. Django 5.0 - `dj-a252d1ef9f2fd2b9`

> The Django 4.2.x series is the last to support Python 3.8 and 3.9.

**Confirmed label:** Configuration/deployment

**Why:** Supported Python runtime versions affect the deployed environment.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L24-L24)

**Kavya's decision:** Confirmed as shown.

### 08. Django 5.0 - `dj-f3490d11c3475a05`

> QuerySet.prefetch_related now supports prefetching django.contrib.contenttypes.fields.GenericForeignKey with non-homogeneous set of results.

**Confirmed label:** Data/schema migration

**Why:** ORM prefetch behavior changes for GenericForeignKey results.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L254-L256)

**Kavya's decision:** Confirmed as shown.

### 09. Django 5.0 - `dj-8673a32b15b0dea4`

> DatabaseFeatures.supports_expression_defaults should be set to False if the database doesn't support using database functions as defaults.

**Confirmed label:** API/code compatibility

**Why:** Custom database-backend code must set the DatabaseFeatures attribute correctly.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L457-L458)

**Kavya's decision:** Confirmed as shown.

### 10. Django 5.0 - `dj-74cf99026e320f83`

> The django.contrib.sitemaps.ping_google() function and the ping_google management command are removed as the Google Sitemaps ping endpoint is deprecated and will be removed in January 2024.

**Confirmed label:** API/code compatibility

**Why:** Calls to the removed ping_google function or management command need review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L478-L480)

**Kavya's decision:** Confirmed as shown.

### 11. Django 5.1 - `dj-865fc2d64a44ed50`

> Support for passing positional arguments to Signer and TimestampSigner is removed.

**Confirmed label:** API/code compatibility

**Why:** Signer and TimestampSigner calls can no longer pass positional arguments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L489-L490)

**Kavya's decision:** Confirmed as shown.

### 12. Django 5.1 - `dj-194e281625231181`

> The django.test.RequestFactory, django.test.AsyncRequestFactory, django.test.Client, and django.test.AsyncClient classes now support the query_params parameter, which accepts a dictionary of query string keys and values. This allows setting query strings on any HTTP methods more easily.

**Confirmed label:** API/code compatibility

**Why:** Test code can pass a new query_params argument to the named request/client APIs.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L301-L305)

**Kavya's decision:** Confirmed as shown.

### 13. Django 5.1 - `dj-c29c4c6c6f12e4f5`

> "init_command" option is now supported in OPTIONS on SQLite to allow specifying pragma options to set upon connection.

**Confirmed label:** Configuration/deployment

**Why:** SQLite connection OPTIONS can now include an init_command setting.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L204-L206)

**Kavya's decision:** Confirmed as shown.

### 14. Django 5.1 - `dj-b9e44943fdc6c444`

> The default parallelism of the ScryptPasswordHasher is increased from 1 to 5, to follow OWASP recommendations.

**Confirmed label:** Configuration/deployment

**Why:** A changed password-hasher parallelism default affects runtime configuration and resource use.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L119-L120)

**Kavya's decision:** Confirmed as shown.

### 15. Django 5.1 - `dj-ff470db325ec04ae`

> django.contrib.postgres.indexes.BTreeIndex now supports the deduplicate_items parameter.

**Confirmed label:** Data/schema migration

**Why:** The BTreeIndex option concerns the database index definition.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L186-L187)

**Kavya's decision:** Confirmed as shown.

### 16. Django 5.2 - `dj-b3a66e64b763ddb5`

> The value of a django.db.models.URLField now renders as a link.

**Confirmed label:** UI/output behavior

**Why:** A URLField value is now displayed as a link.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L140-L140)

**Kavya's decision:** Confirmed as shown.

### 17. Django 5.2 - `dj-c6206bca65cdf600`

> The new django.core.mail.EmailMultiAlternatives.body_contains method returns a boolean indicating whether a provided text is contained in the email body and in all attached MIME type text/* alternatives.

**Confirmed label:** API/code compatibility

**Why:** Application code can call the new body_contains method and inspect its boolean result.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L237-L239)

**Kavya's decision:** Confirmed as shown.

### 18. Django 5.2 - `dj-7e273df3a515e3d4`

> django.utils.decorators.method_decorator now supports wrapping asynchronous view methods.

**Confirmed label:** API/code compatibility

**Why:** method_decorator can now wrap asynchronous view methods in code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L221-L222)

**Kavya's decision:** Confirmed as shown.

### 19. Django 5.2 - `dj-a3ee5613a0b29927`

> The minimum supported version of gettext is increased from 0.15 to 0.19.

**Confirmed label:** Configuration/deployment

**Why:** The minimum gettext version is an environment/dependency requirement.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L436-L436)

**Kavya's decision:** Confirmed as shown.

### 20. Django 5.2 - `dj-05e646fb4126cb97`

> The new django.forms.TelInput form widget is for entering telephone numbers and renders as &lt;input type="tel" ...>.

**Confirmed label:** UI/output behavior

**Why:** TelInput renders a different HTML input type for a form.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L257-L258)

**Kavya's decision:** Confirmed as shown.

### 21. Django 6.0 - `dj-c0f7b469ad475d3a`

> The querystring template tag now accepts multiple positional arguments, which must be mappings, such as django.http.QueryDict or dict.

**Confirmed label:** UI/output behavior

**Why:** A template tag's accepted arguments affect URL output in rendered templates; review this boundary with API/code.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L345-L347)

**Kavya's decision:** Confirmed as shown.

### 22. Django 6.0 - `dj-873e2269223ab9f9`

> Squashed migrations can now themselves be squashed before being transitioned to normal migrations.

**Confirmed label:** Data/schema migration

**Why:** The change concerns how squashed database migrations are handled.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L269-L270)

**Kavya's decision:** Confirmed as shown.

### 23. Django 6.0 - `dj-671dc25095b57eaa`

> Support for passing Python's legacy email email.mime.base.MIMEBase object to EmailMessage.attach() (or including one in the message's attachments list) is deprecated. For complex attachments requiring additional headers or parameters, switch to the modern email API's email.message.MIMEPart.

**Confirmed label:** API/code compatibility

**Why:** EmailMessage.attach callers using MIMEBase must move to MIMEPart.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L536-L541)

**Kavya's decision:** Confirmed as shown.

### 24. Django 6.0 - `dj-365b7a57281cc79a`

> The default scheme for forms.URLField has changed from "http" to "https".

**Confirmed label:** UI/output behavior

**Why:** The default URL scheme produced by a form field changes from http to https.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L575-L576)

**Kavya's decision:** Confirmed as shown.

### 25. Django 6.0 - `dj-877a59446c8810d4`

> The new Aggregate.allow_order_by class attribute determines whether the aggregate function allows passing an order_by keyword argument.

**Confirmed label:** API/code compatibility

**Why:** The Aggregate class attribute controls whether code may pass order_by.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L286-L287)

**Kavya's decision:** Confirmed as shown.

### 26. Django 5.2.1 - `dj-c919e8dfa06d3024`

> Fixed a regression in Django 5.2 that caused a crash when serializing email alternatives or attachments due to named tuple mismatches (36309).

**Confirmed label:** UI/output behavior

**Why:** The bug affected serialization of email alternatives and attachments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L69-L70)

**Kavya's decision:** Confirmed as shown.

### 27. Django 5.2.1 - `dj-71b5ff8aa21de072`

> django.utils.html.strip_tags now raises a SuspiciousOperation exception if it encounters an unusually large number of unclosed opening tags.

**Confirmed label:** API/code compatibility

**Why:** strip_tags now raises a named exception for certain inputs; callers may need to handle it.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L23-L24)

**Kavya's decision:** Confirmed as shown.

### 28. Django 5.2.1 - `dj-e606fe01e26e47a5`

> Fixed a bug in Django 5.2 that caused composite primary key introspection to wrongly identify IntegerField as AutoField on SQLite (36358).

**Confirmed label:** Data/schema migration

**Why:** Composite-primary-key introspection reported the wrong database field type.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L76-L78)

**Kavya's decision:** Confirmed as shown.

### 29. Django 5.2.1 - `dj-74a46ea71c7acbbc`

> Fixed a regression in Django 5.2 that caused unnecessary queries when prefetching nullable foreign key relationships (36290).

**Confirmed label:** Data/schema migration

**Why:** Prefetching a nullable foreign key changed the ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L33-L34)

**Kavya's decision:** Confirmed as shown.

### 30. Django 5.2.1 - `dj-d0b976ec9546869e`

> Fixed a regression in Django 5.2 that caused a crash of QuerySet.bulk_create() with nullable geometry fields on PostGIS (36289).

**Confirmed label:** Data/schema migration

**Why:** bulk_create with nullable geometry fields affects database writes.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L36-L38)

**Kavya's decision:** Confirmed as shown.

### 31. Django 5.2.2 - `dj-e44ca58068c6eaf7`

> Fixed a bug in Django 5.2 where calling QuerySet.in_bulk() with an id_list argument on models with a CompositePrimaryKey failed to observe database parameter limits (36416).

**Confirmed label:** Data/schema migration

**Why:** in_bulk with a composite primary key affects query limits and ORM data access.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L52-L54)

**Kavya's decision:** Confirmed as shown.

### 32. Django 5.2.2 - `dj-553e2d214321e914`

> Although this does not directly impact Django's security model, it poses risks when logs are consumed or interpreted by other tools. To fix this, the internal django.utils.log.log_response() function now escapes all positional formatting arguments using a safe encoding.

**Confirmed label:** UNCLEAR

**Why:** The note points to both log output and downstream log-consumer safety; the guide does not clearly rank those areas.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L19-L22)

**Kavya's decision:** Confirmed as shown.

### 33. Django 5.2.2 - `dj-541ed350a6e738ac`

> Fixed a bug in Django 5.2 where HttpRequest.get_preferred_type() did not account for media type parameters in Accept headers, reducing specificity in content negotiation (36411).

**Confirmed label:** UI/output behavior

**Why:** Accept-header handling changes the media type chosen for an HTTP response.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L56-L59)

**Kavya's decision:** Confirmed as shown.

### 34. Django 5.2.2 - `dj-10de6c2bdb15e0f5`

> Fixed a regression in Django 5.2 where admin's filter_horizontal buttons lacked type="button", causing them to intercept form submission when pressing the Enter key (36423).

**Confirmed label:** UI/output behavior

**Why:** Admin form buttons changed what happens when Enter submits a form.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L48-L50)

**Kavya's decision:** Confirmed as shown.

### 35. Django 5.2.2 - `dj-bf96fbc55535db84`

> Fixed a regression in Django 5.2 that caused a crash when using OuterRef in the filter argument of an Aggregate expression (36404).

**Confirmed label:** Data/schema migration

**Why:** OuterRef inside an Aggregate filter affects ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.2.txt#L41-L42)

**Kavya's decision:** Confirmed as shown.

### 36. Django 5.2.3 - `dj-995c215eb38f1d96`

> Fixed a log injection possibility by migrating remaining response logging to django.utils.log.log_response(), which safely escapes arguments such as the request path to prevent unsafe log output (2025-48432).

**Confirmed label:** UNCLEAR

**Why:** The note points to both response-log output and operational log safety; a reviewer should choose the first area.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.3.txt#L13-L15)

**Kavya's decision:** Confirmed as shown.

### 37. Django 5.2.3 - `dj-84348ed14b32c161`

> Fixed a regression in Django 5.2.2 where the q parameter was removed from the internal django.http.MediaType.params property (36446).

**Confirmed label:** API/code compatibility

**Why:** The internal MediaType.params property lost and regained the q parameter.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.3.txt#L21-L22)

**Kavya's decision:** Confirmed as shown.

### 38. Django 5.2.3 - `dj-957a60cba32b80bb`

> Fixed a regression in Django 5.2 that caused QuerySet.bulk_update to incorrectly convert None to JSON null instead of SQL NULL for JSONField (36419).

**Confirmed label:** Data/schema migration

**Why:** bulk_update changes whether None becomes JSON null or SQL NULL in stored data.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.3.txt#L17-L19)

**Kavya's decision:** Confirmed as shown.

### 39. Django 5.2.4 - `dj-0c6449b08f70ef20`

> Fixed a crash in Django 5.2 when performing an __in lookup involving a composite primary key and a subquery on backends that lack native support for tuple lookups (36464).

**Confirmed label:** Data/schema migration

**Why:** A composite-primary-key lookup with a subquery affects ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.4.txt#L20-L22)

**Kavya's decision:** Confirmed as shown.

### 40. Django 5.2.4 - `dj-dd6b62a0b3da89eb`

> Fixed a regression in Django 5.2.3 where Value(None, JSONField()) used in a django.db.models.expressions.When condition was incorrectly serialized as SQL NULL instead of JSON null (36453).

**Confirmed label:** Data/schema migration

**Why:** JSONField expression serialization changes SQL NULL versus JSON null semantics.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.4.txt#L16-L18)

**Kavya's decision:** Confirmed as shown.

### 41. Django 5.2.5 - `dj-5ea54f89b8c35e14`

> Fixed a crash in Django 5.2 when validating a model that uses GeneratedField or constraints composed of Q and Case lookups (36518).

**Confirmed label:** Data/schema migration

**Why:** GeneratedField and constraint validation concern model data rules.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.5.txt#L19-L21)

**Kavya's decision:** Confirmed as shown.

### 42. Django 5.2.5 - `dj-a2e4bfc6268a921b`

> Added compatibility for docutils 0.22 (36535).

**Confirmed label:** Configuration/deployment

**Why:** Compatibility with docutils 0.22 affects an installed dependency version.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.5.txt#L23-L23)

**Kavya's decision:** Confirmed as shown.

### 43. Django 5.2.6 - `dj-85f0f7d648a513a2`

> FilteredRelation was subject to SQL injection in column aliases, using a suitably crafted dictionary, with dictionary expansion, as the **kwargs passed to QuerySet.annotate or QuerySet.alias.

**Confirmed label:** API/code compatibility

**Why:** QuerySet.annotate/alias callers expanding an untrusted dictionary into kwargs need code review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.6.txt#L12-L14)

**Kavya's decision:** Confirmed as shown.

### 44. Django 5.2.6 - `dj-419ced0e3b3b5c9a`

> Fixed a bug where using QuerySet.values() or values_list() with a ForeignObject composed of multiple fields returned incorrect results instead of tuples of the referenced fields (36431).

**Confirmed label:** API/code compatibility

**Why:** values()/values_list() returned the wrong shape for ForeignObject results; consuming code should be checked.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.6.txt#L19-L21)

**Kavya's decision:** Confirmed as shown.

### 45. Django 5.2.7 - `dj-92551a1c0008a325`

> QuerySet.annotate, QuerySet.alias, QuerySet.aggregate, and QuerySet.extra methods were subject to SQL injection in column aliases, using a suitably crafted dictionary, with dictionary expansion, as the **kwargs passed to these methods (follow up to 2022-28346).

**Confirmed label:** API/code compatibility

**Why:** QuerySet callers expanding an untrusted dictionary into kwargs need code review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.7.txt#L14-L18)

**Kavya's decision:** Confirmed as shown.

### 46. Django 5.2.7 - `dj-761f5a147134517c`

> The django.utils.archive.extract() function, used by startapp --template and startproject --template, allowed partial directory-traversal via an archive with file paths sharing a common prefix with the target directory (follow up to 2021-3281).

**Confirmed label:** UNCLEAR

**Why:** The archive.extract function and project-template commands are both named; code use and project setup are plausible first checks.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.7.txt#L23-L26)

**Kavya's decision:** Confirmed as shown.

### 47. Django 5.2.8 - `dj-1d102276fe2b1fc1`

> Python's NFKC normalization is slow on Windows. As a consequence, django.http.HttpResponseRedirect, django.http.HttpResponsePermanentRedirect, and the shortcut redirect() were subject to a potential denial-of-service attack via certain inputs with a very large number of Unicode characters (follow up to 2025-27556).

**Confirmed label:** API/code compatibility

**Why:** The affected interfaces are redirect response classes and redirect(); review calls that accept large untrusted inputs.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.8.txt#L14-L19)

**Kavya's decision:** Confirmed as shown.

### 48. Django 5.2.8 - `dj-af54932e4defb838`

> Fixed a bug in Django 5.2 where QuerySet.first() and QuerySet.last() raised an error on querysets performing aggregation that selected all fields of a composite primary key.

**Confirmed label:** Data/schema migration

**Why:** first()/last() on aggregate queries with composite primary keys affects ORM data access.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.8.txt#L33-L35)

**Kavya's decision:** Confirmed as shown.

### 49. Django 6.0.1 - `dj-b134568af8ec0626`

> Fixed a bug where management command colorized help (introduced in Python 3.14) ignored the --no-color option and the DJANGO_COLORS setting (36376).

**Confirmed label:** UI/output behavior

**Why:** The change affects visible color in management-command help output.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L23-L25)

**Kavya's decision:** Confirmed as shown.

### 50. Django 6.0.1 - `dj-ad64d6f07ff6548f`

> Fixed a visual regression in Django 6.0 for admin form fields grouped under a &lt;fieldset> in Safari (36807).

**Confirmed label:** UI/output behavior

**Why:** The note explicitly describes a visual regression in admin form fields.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L31-L32)

**Kavya's decision:** Confirmed as shown.

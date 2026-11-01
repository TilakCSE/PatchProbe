# Tilak batch 02: 100 human-confirmed decisions

> **REVIEW COMPLETE.** Tilaksinh Chauhan confirmed all 100 proposed decisions on 2026-11-01, including five `UNCLEAR` states. Suggestions were visible during review.

Prepared: 2026-11-01. The rows are source-linked entries from pinned official Django release notes. This annotation batch is not a representative test set.

**Selection:** Nineteen entries each from feature releases 4.2, 5.0, 5.1, 5.2, and 6.0, plus five patch-release entries. All 200 reviewed IDs were excluded. The sampler filtered visibly incomplete flattened fragments and obvious near-duplicates, preferred different source sections and patch releases, and used a fixed hash order. It did not use class labels. Reviewers may still find extraction defects and should flag them rather than force a label.

**Review outcome:** Tilak confirmed every proposed decision. The named local record is ignored by Git; the public export is `data/processed/tilak_batch_02_reviewed_labels.csv`. This is human-confirmed review of visible suggestions, not blind independent annotation.

Guide: [Data and labeling guide](DATA_AND_LABELS.md). `UNCLEAR` is a review state, excluded from model training. `EXCLUDE` is a review instruction for an invalid source row, not a sixth model label.

Confirmed counts: API/code compatibility: 40; Configuration/deployment: 15; Data/schema migration: 19; UI/output behavior: 21; UNCLEAR: 5. No row clearly merits `No targeted check stated`; do not force it to fill a quota.

## Quick index

| No. | Django | Confirmed label | Status |
| ---: | --- | --- | --- |
| 001 | 4.2 | Configuration/deployment | Confirmed |
| 002 | 4.2 | API/code compatibility | Confirmed |
| 003 | 4.2 | UI/output behavior | Confirmed |
| 004 | 4.2 | Configuration/deployment | Confirmed |
| 005 | 4.2 | Data/schema migration | Confirmed |
| 006 | 4.2 | UI/output behavior | Confirmed |
| 007 | 4.2 | API/code compatibility | Confirmed |
| 008 | 4.2 | Data/schema migration | Confirmed |
| 009 | 4.2 | Data/schema migration | Confirmed |
| 010 | 4.2 | API/code compatibility | Confirmed |
| 011 | 4.2 | Configuration/deployment | Confirmed |
| 012 | 4.2 | Configuration/deployment | Confirmed |
| 013 | 4.2 | Data/schema migration | Confirmed |
| 014 | 4.2 | Data/schema migration | Confirmed |
| 015 | 4.2 | UI/output behavior | Confirmed |
| 016 | 4.2 | UI/output behavior | Confirmed |
| 017 | 4.2 | Data/schema migration | Confirmed |
| 018 | 4.2 | API/code compatibility | Confirmed |
| 019 | 4.2 | Data/schema migration | Confirmed |
| 020 | 5.0 | UI/output behavior | Confirmed |
| 021 | 5.0 | API/code compatibility | Confirmed |
| 022 | 5.0 | UI/output behavior | Confirmed |
| 023 | 5.0 | API/code compatibility | Confirmed |
| 024 | 5.0 | API/code compatibility | Confirmed |
| 025 | 5.0 | Configuration/deployment | Confirmed |
| 026 | 5.0 | Configuration/deployment | Confirmed |
| 027 | 5.0 | API/code compatibility | Confirmed |
| 028 | 5.0 | API/code compatibility | Confirmed |
| 029 | 5.0 | API/code compatibility | Confirmed |
| 030 | 5.0 | API/code compatibility | Confirmed |
| 031 | 5.0 | API/code compatibility | Confirmed |
| 032 | 5.0 | API/code compatibility | Confirmed |
| 033 | 5.0 | Configuration/deployment | Confirmed |
| 034 | 5.0 | Data/schema migration | Confirmed |
| 035 | 5.0 | UI/output behavior | Confirmed |
| 036 | 5.0 | API/code compatibility | Confirmed |
| 037 | 5.0 | Data/schema migration | Confirmed |
| 038 | 5.0 | API/code compatibility | Confirmed |
| 039 | 5.1 | API/code compatibility | Confirmed |
| 040 | 5.1 | API/code compatibility | Confirmed |
| 041 | 5.1 | API/code compatibility | Confirmed |
| 042 | 5.1 | UNCLEAR | Confirmed |
| 043 | 5.1 | UNCLEAR | Confirmed |
| 044 | 5.1 | UNCLEAR | Confirmed |
| 045 | 5.1 | UI/output behavior | Confirmed |
| 046 | 5.1 | UI/output behavior | Confirmed |
| 047 | 5.1 | UI/output behavior | Confirmed |
| 048 | 5.1 | API/code compatibility | Confirmed |
| 049 | 5.1 | API/code compatibility | Confirmed |
| 050 | 5.1 | Configuration/deployment | Confirmed |
| 051 | 5.1 | UI/output behavior | Confirmed |
| 052 | 5.1 | UI/output behavior | Confirmed |
| 053 | 5.1 | API/code compatibility | Confirmed |
| 054 | 5.1 | UI/output behavior | Confirmed |
| 055 | 5.1 | API/code compatibility | Confirmed |
| 056 | 5.1 | Data/schema migration | Confirmed |
| 057 | 5.1 | API/code compatibility | Confirmed |
| 058 | 5.2 | API/code compatibility | Confirmed |
| 059 | 5.2 | API/code compatibility | Confirmed |
| 060 | 5.2 | API/code compatibility | Confirmed |
| 061 | 5.2 | Configuration/deployment | Confirmed |
| 062 | 5.2 | Data/schema migration | Confirmed |
| 063 | 5.2 | API/code compatibility | Confirmed |
| 064 | 5.2 | UI/output behavior | Confirmed |
| 065 | 5.2 | UI/output behavior | Confirmed |
| 066 | 5.2 | API/code compatibility | Confirmed |
| 067 | 5.2 | UI/output behavior | Confirmed |
| 068 | 5.2 | Data/schema migration | Confirmed |
| 069 | 5.2 | UI/output behavior | Confirmed |
| 070 | 5.2 | API/code compatibility | Confirmed |
| 071 | 5.2 | Data/schema migration | Confirmed |
| 072 | 5.2 | Configuration/deployment | Confirmed |
| 073 | 5.2 | API/code compatibility | Confirmed |
| 074 | 5.2 | Data/schema migration | Confirmed |
| 075 | 5.2 | UI/output behavior | Confirmed |
| 076 | 5.2 | Configuration/deployment | Confirmed |
| 077 | 6.0 | Configuration/deployment | Confirmed |
| 078 | 6.0 | API/code compatibility | Confirmed |
| 079 | 6.0 | API/code compatibility | Confirmed |
| 080 | 6.0 | Configuration/deployment | Confirmed |
| 081 | 6.0 | API/code compatibility | Confirmed |
| 082 | 6.0 | API/code compatibility | Confirmed |
| 083 | 6.0 | API/code compatibility | Confirmed |
| 084 | 6.0 | UNCLEAR | Confirmed |
| 085 | 6.0 | UNCLEAR | Confirmed |
| 086 | 6.0 | API/code compatibility | Confirmed |
| 087 | 6.0 | UI/output behavior | Confirmed |
| 088 | 6.0 | API/code compatibility | Confirmed |
| 089 | 6.0 | API/code compatibility | Confirmed |
| 090 | 6.0 | UI/output behavior | Confirmed |
| 091 | 6.0 | Configuration/deployment | Confirmed |
| 092 | 6.0 | API/code compatibility | Confirmed |
| 093 | 6.0 | Configuration/deployment | Confirmed |
| 094 | 6.0 | API/code compatibility | Confirmed |
| 095 | 6.0 | Data/schema migration | Confirmed |
| 096 | 5.2.1 | Data/schema migration | Confirmed |
| 097 | 5.2.5 | Data/schema migration | Confirmed |
| 098 | 6.0.1 | Data/schema migration | Confirmed |
| 099 | 5.2.1 | Data/schema migration | Confirmed |
| 100 | 5.2.1 | UI/output behavior | Confirmed |

## Notes and reasons

### 001. Django 4.2 - `dj-c9f1d86b95decabb`

> The minimum supported version of argon2-cffi is increased from 19.1.0 to 19.2.0.

**Confirmed label:** Configuration/deployment

**Why:** argon2-cffi has a new minimum installed version.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L460-L461)

**Tilak's decision:** Confirmed as shown above.

### 002. Django 4.2 - `dj-bc6ecfae352920de`

> The new FromWKB() and FromWKT() functions allow creating geometries from Well-known binary (WKB) and Well-known text (WKT) representations.

**Confirmed label:** API/code compatibility

**Why:** Application code can call the new FromWKB and FromWKT functions.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L182-L185)

**Tilak's decision:** Confirmed as shown above.

### 003. Django 4.2 - `dj-b64c56240aa3d4d2`

> The admin's font stack now prefers system UI fonts and no longer requires downloading fonts. Additionally, CSS variables are available to more easily override the default font families.

**Confirmed label:** UI/output behavior

**Why:** The admin's fonts and CSS overrides change visible styling.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L125-L127)

**Tilak's decision:** Confirmed as shown above.

### 004. Django 4.2 - `dj-4a43b0aa07c74863`

> Django now supports psycopg version 3.1.8 or higher. To update your code, install the psycopg library, you don't need to change the ENGINE as django.db.backends.postgresql supports both libraries.

**Confirmed label:** Configuration/deployment

**Why:** The supported psycopg driver version is a deployment dependency.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L38-L41)

**Tilak's decision:** Confirmed as shown above.

### 005. Django 4.2 - `dj-7ba587321c7cea8c`

> The Meta.index_together option is deprecated in favor of the django.db.models.Options.indexes option.

**Confirmed label:** Data/schema migration

**Why:** Replacing index_together concerns the database index definition.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L491-L492)

**Tilak's decision:** Confirmed as shown above.

### 006. Django 4.2 - `dj-b0cece5dd42a4eea`

> The django-db-logger logger now logs transaction management queries (BEGIN, COMMIT, and ROLLBACK) at the DEBUG level.

**Confirmed label:** UI/output behavior

**Why:** Transaction statements now appear in DEBUG log output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L255-L256)

**Tilak's decision:** Confirmed as shown above.

### 007. Django 4.2 - `dj-7552789ddda7dc35`

> Model now provides asynchronous versions of some methods that use the database, using an a prefix: Model.adelete, Model.arefresh_from_db, and Model.asave.

**Confirmed label:** API/code compatibility

**Why:** Model gains named async methods for code to call.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L299-L301)

**Tilak's decision:** Confirmed as shown above.

### 008. Django 4.2 - `dj-dca902e4b419c816`

> The new makemigrations --update option merges model changes into the latest migration and optimizes the resulting operations.

**Confirmed label:** Data/schema migration

**Why:** makemigrations --update changes generated migration operations.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L264-L265)

**Tilak's decision:** Confirmed as shown above.

### 009. Django 4.2 - `dj-b95f515917eab967`

> JSONField and its associated lookups and aggregates used to allow passing JSON encoded string literals which caused ambiguity on whether string literals were already encoded from database backend's perspective.

**Confirmed label:** Data/schema migration

**Why:** Encoded JSON literals affect JSONField database value semantics.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L528-L530)

**Tilak's decision:** Confirmed as shown above.

### 010. Django 4.2 - `dj-597808d7d1899ca6`

> In order to avoid updating unnecessary columns, QuerySet.update_or_create now passes update_fields to the Model.save() calls. As a consequence, any fields modified in the custom save() methods should be added to the update_fields keyword argument before calling super(). See overriding-model-methods for more details.

**Confirmed label:** API/code compatibility

**Why:** Custom save methods must handle the update_fields argument correctly.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L405-L410)

**Tilak's decision:** Confirmed as shown above.

### 011. Django 4.2 - `dj-2341f64ca23aea16`

> The DEFAULT_FILE_STORAGE setting is deprecated in favor of STORAGES["default"].

**Confirmed label:** Configuration/deployment

**Why:** The file-storage setting name changes in project configuration.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L614-L615)

**Tilak's decision:** Confirmed as shown above.

### 012. Django 4.2 - `dj-d215f2a7e069be24`

> The new STORAGES setting allows configuring multiple custom file storage backends. It also controls storage engines for managing files (the "default" key) and static files (the "staticfiles" key).

**Confirmed label:** Configuration/deployment

**Why:** STORAGES configures file and static-file backend choices.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L108-L111)

**Tilak's decision:** Confirmed as shown above.

### 013. Django 4.2 - `dj-726eb907dae5be02`

> The arrayfield.overlap lookup now supports QuerySet.values() and values_list() as a right-hand side.

**Confirmed label:** Data/schema migration

**Why:** The array overlap lookup changes accepted ORM query inputs.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L197-L198)

**Tilak's decision:** Confirmed as shown above.

### 014. Django 4.2 - `dj-e2e1d6cefd3845f2`

> Also, the new django.db.migrations.operations.AlterModelTableComment operation allows changing table comments defined in the Meta.db_table_comment.

**Confirmed label:** Data/schema migration

**Why:** AlterModelTableComment is a database migration operation.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L85-L87)

**Tilak's decision:** Confirmed as shown above.

### 015. Django 4.2 - `dj-84715c40f992e27f`

> django.middleware.gzip.GZipMiddleware now includes a mitigation for the BREACH attack. It will add up to 100 random bytes to gzip responses to make BREACH attacks harder. Read more about the mitigation technique in the Heal The Breach (HTB) paper.

**Confirmed label:** UI/output behavior

**Why:** GZipMiddleware changes compressed HTTP response bytes.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L92-L95)

**Tilak's decision:** Confirmed as shown above.

### 016. Django 4.2 - `dj-6489551cc6a6453f`

> Added support and translations for the Central Kurdish (Sorani) language.

**Confirmed label:** UI/output behavior

**Why:** The new translation changes language shown in the interface.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L250-L250)

**Tilak's decision:** Confirmed as shown above.

### 017. Django 4.2 - `dj-e9848db3721fe466`

> inspectdb now uses display_size from DatabaseIntrospection.get_table_description() rather than internal_size for CharField.

**Confirmed label:** Data/schema migration

**Why:** inspectdb changes how a CharField is inferred from database metadata.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L380-L382)

**Tilak's decision:** Confirmed as shown above.

### 018. Django 4.2 - `dj-fde6932bcb0ca6fc`

> django.http.StreamingHttpResponse now supports async iterators when Django is served via ASGI.

**Confirmed label:** API/code compatibility

**Why:** StreamingHttpResponse can consume async iterators under ASGI.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L315-L316)

**Tilak's decision:** Confirmed as shown above.

### 019. Django 4.2 - `dj-53a26ce0817c6705`

> django.contrib.auth.forms.UserCreationForm now saves many-to-many form fields for a custom user model.

**Confirmed label:** Data/schema migration

**Why:** UserCreationForm now saves many-to-many values to persistent data.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L152-L153)

**Tilak's decision:** Confirmed as shown above.

### 020. Django 5.0 - `dj-86a1ecdd2043df42`

> Support and translations for the Uyghur language are now available.

**Confirmed label:** UI/output behavior

**Why:** The new translation changes user-visible language.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L353-L353)

**Tilak's decision:** Confirmed as shown above.

### 021. Django 5.0 - `dj-21e4ef44e3d007e5`

> Passing a response object and a form/formset name to SimpleTestCase.assertFormError() and assertFormSetError() is no longer allowed.

**Confirmed label:** API/code compatibility

**Why:** The two test assertion methods no longer accept those call arguments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L744-L746)

**Tilak's decision:** Confirmed as shown above.

### 022. Django 5.0 - `dj-e470f7f664ff2bf0`

> django.forms.BoundField.as_field_group renders fields with the "django/forms/field.html" template by default and can be customized on a per-project, per-field, or per-request basis. See reusable-field-group-templates.

**Confirmed label:** UI/output behavior

**Why:** BoundField.as_field_group changes the template used to render a field.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L112-L115)

**Tilak's decision:** Confirmed as shown above.

### 023. Django 5.0 - `dj-8319d6da9eb1f5ab`

> The new MessagesTestMixin.assertMessages assertion method allows testing django.contrib.messages added to a response.

**Confirmed label:** API/code compatibility

**Why:** Tests can call the new assertMessages assertion method.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L277-L279)

**Tilak's decision:** Confirmed as shown above.

### 024. Django 5.0 - `dj-e18113f343eaf133`

> The new django.forms.URLField.assume_scheme argument for django.forms.URLField allows specifying a default URL scheme.

**Confirmed label:** API/code compatibility

**Why:** URLField gains a named argument for form code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L341-L342)

**Tilak's decision:** Confirmed as shown above.

### 025. Django 5.0 - `dj-8e5670eefec63c29`

> The minimum supported version of colorama is increased to 0.4.6.

**Confirmed label:** Configuration/deployment

**Why:** colorama has a new minimum installed version.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L588-L588)

**Tilak's decision:** Confirmed as shown above.

### 026. Django 5.0 - `dj-6bd35b7b8592bfa9`

> Support for cx_Oracle is deprecated in favor of oracledb 1.3.2+ Python driver.

**Confirmed label:** Configuration/deployment

**Why:** The supported Oracle Python driver changes for deployment.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L634-L635)

**Tilak's decision:** Confirmed as shown above.

### 027. Django 5.0 - `dj-bfe7ac5e6607ea08`

> Under ASGI, http.disconnect events are now handled. This allows views to perform any necessary cleanup if a client disconnects before the response is generated. See async-handling-disconnect for more details.

**Confirmed label:** API/code compatibility

**Why:** Async view code can handle client disconnects for cleanup.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L292-L294)

**Tilak's decision:** Confirmed as shown above.

### 028. Django 5.0 - `dj-22c340c7b9814198`

> AuthenticationMiddleware now adds an HttpRequest.auser asynchronous method that returns the currently logged-in user.

**Confirmed label:** API/code compatibility

**Why:** HttpRequest gains the auser method for code to call.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L244-L245)

**Tilak's decision:** Confirmed as shown above.

### 029. Django 5.0 - `dj-01dbf017c6eeb1ea`

> django.test.AsyncClient now supports the follow parameter.

**Confirmed label:** API/code compatibility

**Why:** AsyncClient gains a follow parameter in test code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L433-L433)

**Tilak's decision:** Confirmed as shown above.

### 030. Django 5.0 - `dj-d2ce1f5ac552b9d6`

> Under the hood the provided choices are normalized into a list of 2-tuples as the canonical form whenever the choices value is updated. For more information, please check the model field reference on choices.

**Confirmed label:** API/code compatibility

**Why:** Updated choices are normalized into a new canonical Python value shape.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L202-L205)

**Tilak's decision:** Confirmed as shown above.

### 031. Django 5.0 - `dj-4f98d626fc69234a`

> The new create_defaults argument of QuerySet.update_or_create and QuerySet.aupdate_or_create methods allows specifying a different field values for the create operation.

**Confirmed label:** API/code compatibility

**Why:** update_or_create gains a create_defaults call argument.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L365-L367)

**Tilak's decision:** Confirmed as shown above.

### 032. Django 5.0 - `dj-73ce2c03d92cf9ad`

> File.open now passes all positional (*args) and keyword arguments (**kwargs) to Python's built-in open.

**Confirmed label:** API/code compatibility

**Why:** File.open forwards its positional and keyword call arguments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L335-L336)

**Tilak's decision:** Confirmed as shown above.

### 033. Django 5.0 - `dj-4e231316ad07dcad`

> Support for pre-releases of MySQL 8.0.x series is removed. Django 5.0 supports MySQL 8.0.11 and higher.

**Confirmed label:** Configuration/deployment

**Why:** MySQL 8.0.11 or later is required in the deployed database.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L487-L488)

**Tilak's decision:** Confirmed as shown above.

### 034. Django 5.0 - `dj-b273243d421ee60d`

> Running the makemigrations command will generate a migration containing a no-op AlterField operation.

**Confirmed label:** Data/schema migration

**Why:** makemigrations generates an AlterField operation, even if it is a no-op.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L531-L532)

**Tilak's decision:** Confirmed as shown above.

### 035. Django 5.0 - `dj-a69e50f7011856f0`

> The django.contrib.admin.AllValuesFieldListFilter, ChoicesFieldListFilter, RelatedFieldListFilter, and RelatedOnlyFieldListFilter admin filters now handle multi-valued query parameters.

**Confirmed label:** UI/output behavior

**Why:** Admin list filters now handle multi-value query parameters in the interface.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L216-L219)

**Tilak's decision:** Confirmed as shown above.

### 036. Django 5.0 - `dj-2946844b8483f1a1`

> The new GEOSGeometry.equals_identical method allows point-wise equivalence checking of geometries.

**Confirmed label:** API/code compatibility

**Why:** GEOSGeometry gains a named geometry-comparison method.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L271-L272)

**Tilak's decision:** Confirmed as shown above.

### 037. Django 5.0 - `dj-7f8247ead72eacfa`

> Serialization of functions decorated with functools.cache or functools.lru_cache is now supported without the need to write a custom serializer.

**Confirmed label:** Data/schema migration

**Why:** Cached functions can now be serialized into migrations.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L358-L360)

**Tilak's decision:** Confirmed as shown above.

### 038. Django 5.0 - `dj-120492989b4cda79`

> Following the release of Django 5.0, we suggest that third-party app authors drop support for all versions of Django prior to 4.2. At that time, you should be able to run your package's tests using python -Wd so that deprecation warnings appear. After making the deprecation warning fixes, your app should be compatible with Django 5.0.

**Confirmed label:** API/code compatibility

**Why:** Third-party app code should fix deprecations for Django 5.0 compatibility.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L29-L33)

**Tilak's decision:** Confirmed as shown above.

### 039. Django 5.1 - `dj-e148b6d9e48a48f3`

> OGRGeometry.centroid is now available on all supported geometry types.

**Confirmed label:** API/code compatibility

**Why:** OGRGeometry gains a centroid property for code to read.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L175-L176)

**Tilak's decision:** Confirmed as shown above.

### 040. Django 5.1 - `dj-1ea0b1ec665f6b36`

> Passing positional arguments to Model.save and Model.asave is deprecated in favor of keyword-only arguments.

**Confirmed label:** API/code compatibility

**Why:** Model.save and asave callers must move positional values to keywords.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L432-L433)

**Tilak's decision:** Confirmed as shown above.

### 041. Django 5.1 - `dj-c47bb20fb2a41fdb`

> The new Expression.constraint_validation_compatible attribute allows specifying that the expression should be ignored during a constraint validation.

**Confirmed label:** API/code compatibility

**Why:** Expression gains a Python attribute controlling validation behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L279-L281)

**Tilak's decision:** Confirmed as shown above.

### 042. Django 5.1 - `dj-647753226b554227`

> The new django.contrib.auth.middleware.LoginRequiredMiddleware redirects all unauthenticated requests to a login page. Views can allow unauthenticated requests by using the new django.contrib.auth.decorators.login_not_required decorator.

**Confirmed label:** UNCLEAR

**Why:** The note names both middleware redirect behavior and a view decorator; routing setup and code are plausible first checks.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L90-L93)

**Tilak's decision:** Confirmed as shown above.

### 043. Django 5.1 - `dj-59c73b0b265e0e49`

> django.contrib.sessions.backends.cached_db.SessionStore now handles exceptions when storing session information in the cache, logging proper error messages with their traceback via the newly added sessions logger.

**Confirmed label:** UNCLEAR

**Why:** The note changes session-cache storage handling and error-log output; both checks are explicit.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L192-L195)

**Tilak's decision:** Confirmed as shown above.

### 044. Django 5.1 - `dj-66f72e2ebbc08247`

> The new django.contrib.auth.forms.AdminUserCreationForm and the existing django.contrib.auth.forms.AdminPasswordChangeForm now support disabling password-based authentication by setting an unusable password on form save. This is now available in the admin when visiting the user creation and password change pages.

**Confirmed label:** UNCLEAR

**Why:** The form saves an unusable password and changes admin page behavior; data/auth state and UI checks both matter.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L122-L126)

**Tilak's decision:** Confirmed as shown above.

### 045. Django 5.1 - `dj-8e3ae4d2beee8433`

> The new Operation.category attribute allows specifying an operation category used by the makemigrations to display a meaningful symbol for the operation.

**Confirmed label:** UI/output behavior

**Why:** makemigrations now prints different symbols in command output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L244-L247)

**Tilak's decision:** Confirmed as shown above.

### 046. Django 5.1 - `dj-62afa19a6411cb13`

> In order to improve accessibility, the expandable widget used for ModelAdmin.fieldsets and InlineModelAdmin.fieldsets, when the fieldset has a name and use the collapse class, now includes &lt;details> and &lt;summary> elements.

**Confirmed label:** UI/output behavior

**Why:** The fieldset renders new details and summary HTML elements.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L369-L373)

**Tilak's decision:** Confirmed as shown above.

### 047. Django 5.1 - `dj-ca9fce341ec17d38`

> django.test.SimpleTestCase.assertContains, django.test.SimpleTestCase.assertNotContains, and django.test.SimpleTestCase.assertInHTML assertions now add haystacks to assertion error messages.

**Confirmed label:** UI/output behavior

**Why:** Assertion failure messages now include haystack text.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L296-L299)

**Tilak's decision:** Confirmed as shown above.

### 048. Django 5.1 - `dj-d599d9b309ff4e5a`

> The new django.core.validators.DomainNameValidator validates domain names, including internationalized domain names. The new django.core.validators.validate_domain_name function returns an instance of django.core.validators.DomainNameValidator.

**Confirmed label:** API/code compatibility

**Why:** Code can call the new domain-name validator class or function.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L321-L324)

**Tilak's decision:** Confirmed as shown above.

### 049. Django 5.1 - `dj-ebbe289df2de19a1`

> The TransactionTestCase.assertQuerysetEqual() method is removed.

**Confirmed label:** API/code compatibility

**Why:** Test code calling assertQuerysetEqual must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L484-L484)

**Tilak's decision:** Confirmed as shown above.

### 050. Django 5.1 - `dj-42ae7be519a47cbe`

> "pool" option is now supported in OPTIONS on PostgreSQL to allow using connection pools.

**Confirmed label:** Configuration/deployment

**Why:** The PostgreSQL connection pool is selected through database OPTIONS.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L211-L212)

**Tilak's decision:** Confirmed as shown above.

### 051. Django 5.1 - `dj-b14b9502d2cbd3eb`

> The makemigrations command now displays meaningful symbols for each operation to highlight operation categories.

**Confirmed label:** UI/output behavior

**Why:** makemigrations displays symbols for operation categories.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L237-L239)

**Tilak's decision:** Confirmed as shown above.

### 052. Django 5.1 - `dj-90191dc1142d59ab`

> In order to improve accessibility and enable screen readers to associate fieldsets with their help text, the form fieldset now includes the aria-describedby HTML attribute.

**Confirmed label:** UI/output behavior

**Why:** The form fieldset renders an aria-describedby attribute.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L230-L232)

**Tilak's decision:** Confirmed as shown above.

### 053. Django 5.1 - `dj-a6663c521e47bafb`

> Custom tags may now set extra data on the Parser object that will later be made available on the Template instance. Such data may be used, for example, by the template loader, or other template clients.

**Confirmed label:** API/code compatibility

**Why:** Custom template-tag code can pass data through Parser to Template.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L286-L288)

**Tilak's decision:** Confirmed as shown above.

### 054. Django 5.1 - `dj-8038b8b0b35ac963`

> ModelAdmin.list_display now supports using __ lookups to list fields from related models.

**Confirmed label:** UI/output behavior

**Why:** list_display can show related-model fields in the admin table.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L110-L111)

**Tilak's decision:** Confirmed as shown above.

### 055. Django 5.1 - `dj-abfc06ff06216ed9`

> FromWKB() and FromWKT() functions now support the optional srid argument (except for Oracle where it is ignored).

**Confirmed label:** API/code compatibility

**Why:** FromWKB and FromWKT gain an optional srid call argument.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L178-L181)

**Tilak's decision:** Confirmed as shown above.

### 056. Django 5.1 - `dj-6a8ff4ba985cbfab`

> QuerySet.order_by now supports ordering by annotation transforms such as JSONObject keys and ArrayAgg indices.

**Confirmed label:** Data/schema migration

**Why:** order_by changes supported ordering of ORM query results.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L263-L264)

**Tilak's decision:** Confirmed as shown above.

### 057. Django 5.1 - `dj-01d080c1626a83bf`

> GeoIP2.country now exposes the continent_code, continent_name, and is_in_european_union values.

**Confirmed label:** API/code compatibility

**Why:** GeoIP2.country exposes additional return-value keys.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L151-L152)

**Tilak's decision:** Confirmed as shown above.

### 058. Django 5.2 - `dj-245026eb59d3a39b`

> BaseDatabaseOperations.adapt_decimalfield_value() is now a no-op, simply returning the given value.

**Confirmed label:** API/code compatibility

**Why:** A database-backend method now returns its input unchanged.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L406-L407)

**Tilak's decision:** Confirmed as shown above.

### 059. Django 5.2 - `dj-2f1f40af9fddef5c`

> django.urls.reverse and django.urls.reverse_lazy now accept query and fragment keyword arguments, allowing the addition of a query string and/or fragment identifier in the generated URL, respectively.

**Confirmed label:** API/code compatibility

**Why:** reverse and reverse_lazy gain query and fragment keyword arguments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L376-L378)

**Tilak's decision:** Confirmed as shown above.

### 060. Django 5.2 - `dj-0896989ac8c3c94e`

> Built-in aggregate functions accepting only one argument (Avg, Count, Max, Min, StdDev, Sum, and Variance) now raise TypeError when called with an incorrect number of arguments.

**Confirmed label:** API/code compatibility

**Why:** Aggregate function calls now raise TypeError for wrong argument counts.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L468-L470)

**Tilak's decision:** Confirmed as shown above.

### 061. Django 5.2 - `dj-6a0c228821685d31`

> A new warning is displayed when running runserver, indicating that it is unsuitable for production. This warning can be suppressed by setting the DJANGO_RUNSERVER_HIDE_WARNING environment variable to "true".

**Confirmed label:** Configuration/deployment

**Why:** An environment variable controls the runserver warning.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L278-L281)

**Tilak's decision:** Confirmed as shown above.

### 062. Django 5.2 - `dj-f00d25a9f516c502`

> CharField.max_length is no longer required to be set on SQLite, which supports unlimited VARCHAR columns.

**Confirmed label:** Data/schema migration

**Why:** SQLite CharField schema no longer requires max_length.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L313-L315)

**Tilak's decision:** Confirmed as shown above.

### 063. Django 5.2 - `dj-437a0b96dc0778cd`

> Each serialization format now defines a Deserializer class, rather than a function, to improve extensibility when defining a custom serialization format.

**Confirmed label:** API/code compatibility

**Why:** Custom serializers now extend a Deserializer class rather than a function.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L350-L352)

**Tilak's decision:** Confirmed as shown above.

### 064. Django 5.2 - `dj-958df5e44fe7eaa8`

> All django.utils.feedgenerator.SyndicationFeed classes now support a stylesheets attribute. If specified, an &lt;? xml-stylesheet ?> processing instruction will be added to the top of the document for each stylesheet in the given list. See feed-stylesheets for more details.

**Confirmed label:** UI/output behavior

**Why:** A stylesheet processing instruction is added to feed output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L203-L206)

**Tilak's decision:** Confirmed as shown above.

### 065. Django 5.2 - `dj-32b33a0e1871342f`

> The new preserve_request argument for django.http.HttpResponseRedirect and django.http.HttpResponsePermanentRedirect determines whether the HTTP status codes 302/307 or 301/308 are used, respectively.

**Confirmed label:** UI/output behavior

**Why:** The redirect response can use different HTTP status codes.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L337-L341)

**Tilak's decision:** Confirmed as shown above.

### 066. Django 5.2 - `dj-c7068115d2ed4748`

> django.utils.html.format_html_join now supports taking an iterable of mappings, passing their contents as keyword arguments to django.utils.html.format_html.

**Confirmed label:** API/code compatibility

**Why:** format_html_join accepts mapping values passed as keyword arguments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L388-L390)

**Tilak's decision:** Confirmed as shown above.

### 067. Django 5.2 - `dj-4fb7e64520d2dffb`

> The admin/base.html template now has a new block extrabody for adding custom code before the closing &lt;/body> tag.

**Confirmed label:** UI/output behavior

**Why:** The admin template gains a block affecting rendered page content.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L136-L138)

**Tilak's decision:** Confirmed as shown above.

### 068. Django 5.2 - `dj-30c1ff70517f87c6`

> coveredby and covers lookup are now supported on MySQL.

**Confirmed label:** Data/schema migration

**Why:** MySQL now supports these spatial ORM lookups.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L198-L198)

**Tilak's decision:** Confirmed as shown above.

### 069. Django 5.2 - `dj-6be4e414a62b8ad8`

> An django.forms.BoundField.aria_describedby property is added to BoundField to ease use of this HTML attribute in templates.

**Confirmed label:** UI/output behavior

**Why:** BoundField exposes ARIA description text for rendered templates.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L264-L265)

**Tilak's decision:** Confirmed as shown above.

### 070. Django 5.2 - `dj-fa875e72fd1eea4e`

> The new django.template.Library.simple_block_tag decorator enables the creation of simple block tags, which can accept and use a section of the template.

**Confirmed label:** API/code compatibility

**Why:** Library gains a decorator for defining custom block tags.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L357-L359)

**Tilak's decision:** Confirmed as shown above.

### 071. Django 5.2 - `dj-078c223b0a181fcf`

> Data loaded from django.test.TransactionTestCase.fixtures and from migrations enabled with serialized_rollback=True are now available during TransactionTestCase.setUpClass().

**Confirmed label:** Data/schema migration

**Why:** Test fixture data becomes available earlier in setUpClass.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L368-L371)

**Tilak's decision:** Confirmed as shown above.

### 072. Django 5.2 - `dj-21c91c9037b5e764`

> MySQL connections now default to using the utf8mb4 character set, instead of utf8, which is an alias for the deprecated character set utf8mb3. utf8mb3 can be specified in the OPTIONS part of the DATABASES setting, if needed for legacy databases.

**Confirmed label:** Configuration/deployment

**Why:** The MySQL connection charset default and DATABASES option change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L425-L428)

**Tilak's decision:** Confirmed as shown above.

### 073. Django 5.2 - `dj-f8a40f7edb69080c`

> Support for subclasses of RemoteUserMiddleware that override process_request() without overriding aprocess_request() is deprecated.

**Confirmed label:** API/code compatibility

**Why:** RemoteUserMiddleware subclasses need an async override.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L493-L495)

**Tilak's decision:** Confirmed as shown above.

### 074. Django 5.2 - `dj-1c46ed5022e97f72`

> The new django.db.models.CompositePrimaryKey allows tables to be created with a primary key consisting of multiple fields.

**Confirmed label:** Data/schema migration

**Why:** CompositePrimaryKey changes the database primary-key schema.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L58-L59)

**Tilak's decision:** Confirmed as shown above.

### 075. Django 5.2 - `dj-b1cf4044c13415af`

> The model pages are now restricted to users with the corresponding view or change permissions.

**Confirmed label:** UI/output behavior

**Why:** Permissions now change which admindocs model pages are visible.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L149-L150)

**Tilak's decision:** Confirmed as shown above.

### 076. Django 5.2 - `dj-79e5d031414a7165`

> The django.template.context_processors.debug context processor is no longer included in the default project template.

**Confirmed label:** Configuration/deployment

**Why:** The default project template omits a context processor setting.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L446-L447)

**Tilak's decision:** Confirmed as shown above.

### 077. Django 6.0 - `dj-5a2ea893bde42a53`

> Model fields, indexes, and constraints from django.contrib.postgres now include system checks to verify that django.contrib.postgres is an installed app.

**Confirmed label:** Configuration/deployment

**Why:** The system check verifies django.contrib.postgres is installed.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L217-L219)

**Tilak's decision:** Confirmed as shown above.

### 078. Django 6.0 - `dj-7898dac145983c8b`

> Notably, the return type of the EmailMessage.message() method is now an instance of Python's email.message.EmailMessage. This supports the same API as the previous SafeMIMEText and SafeMIMEMultipart return types, but is not an instance of those now-deprecated classes.

**Confirmed label:** API/code compatibility

**Why:** EmailMessage.message returns a different Python object type.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L150-L154)

**Tilak's decision:** Confirmed as shown above.

### 079. Django 6.0 - `dj-4cd4d16d8e80e1e6`

> The get_joining_columns() method of ForeignObject and ForeignObjectRel is removed.

**Confirmed label:** API/code compatibility

**Why:** The removed ForeignObject method requires call-site review.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L583-L584)

**Tilak's decision:** Confirmed as shown above.

### 080. Django 6.0 - `dj-c86600580a2a6291`

> The URLIZE_ASSUME_HTTPS transitional setting is deprecated.

**Confirmed label:** Configuration/deployment

**Why:** The transitional HTTPS setting is deprecated.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L523-L523)

**Tilak's decision:** Confirmed as shown above.

### 081. Django 6.0 - `dj-b0abf963b55caeb3`

> The new GEOSGeometry.hasm property checks whether the geometry has the M dimension.

**Confirmed label:** API/code compatibility

**Why:** GEOSGeometry gains the hasm property for code to read.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L183-L184)

**Tilak's decision:** Confirmed as shown above.

### 082. Django 6.0 - `dj-fccc186303613cf1`

> Constraints now implement a check() method that is already registered with the check framework.

**Confirmed label:** API/code compatibility

**Why:** Constraints gain a registered check method.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L280-L281)

**Tilak's decision:** Confirmed as shown above.

### 083. Django 6.0 - `dj-9251157d15ef54ef`

> If the database supports UPDATE … RETURNING statements, backends can set DatabaseFeatures.can_return_rows_from_update=True.

**Confirmed label:** API/code compatibility

**Why:** Database backends can set a named DatabaseFeatures attribute.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L381-L382)

**Tilak's decision:** Confirmed as shown above.

### 084. Django 6.0 - `dj-4477e12e473786f4`

> In Django 6.0, DEFAULT_AUTO_FIELD now defaults to django.db.models.BigAutoField and the aforementioned lines in the project and app templates are removed.

**Confirmed label:** UNCLEAR

**Why:** A configuration default changes and can affect database primary-key schema; both checks are explicit.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L444-L446)

**Tilak's decision:** Confirmed as shown above.

### 085. Django 6.0 - `dj-7675e0e48b5d2cd6`

> Django now includes a built-in Tasks framework for running code outside the HTTP request–response cycle. This enables offloading work, such as sending emails or processing data, to background workers.

**Confirmed label:** UNCLEAR

**Why:** The new Tasks API and background worker deployment are both plausible first checks.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L101-L103)

**Tilak's decision:** Confirmed as shown above.

### 086. Django 6.0 - `dj-1e5ce06380134918`

> The new AdminSite.password_change_form attribute allows customizing the form used in the admin site password change view.

**Confirmed label:** API/code compatibility

**Why:** AdminSite gains an attribute for selecting a password-change form.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L165-L166)

**Tilak's decision:** Confirmed as shown above.

### 087. Django 6.0 - `dj-a4b7d37cb533d0a4`

> The querystring template tag now consistently prefixes the returned query string with a ?, ensuring reliable link generation behavior.

**Confirmed label:** UI/output behavior

**Why:** The querystring tag changes URLs rendered in links.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L342-L343)

**Tilak's decision:** Confirmed as shown above.

### 088. Django 6.0 - `dj-2e1d2abd3f648f2e`

> The new django.core.paginator.AsyncPaginator and django.core.paginator.AsyncPage provide async implementations of django.core.paginator.Paginator and django.core.paginator.Page respectively.

**Confirmed label:** API/code compatibility

**Why:** AsyncPaginator and AsyncPage are new classes for code to use.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L325-L328)

**Tilak's decision:** Confirmed as shown above.

### 089. Django 6.0 - `dj-55794410a09d9106`

> EmailMessage.attach() now accepts a email.message.MIMEPart object from Python's modern email API.

**Confirmed label:** API/code compatibility

**Why:** EmailMessage.attach accepts a new MIMEPart argument type.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L248-L250)

**Tilak's decision:** Confirmed as shown above.

### 090. Django 6.0 - `dj-a15e682a99d0ed08`

> django.contrib.staticfiles.storage.ManifestStaticFilesStorage now ensures consistent path ordering in manifest files, making them more reproducible and reducing unnecessary diffs.

**Confirmed label:** UI/output behavior

**Why:** The static-files manifest output now has stable path ordering.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L232-L234)

**Tilak's decision:** Confirmed as shown above.

### 091. Django 6.0 - `dj-b7dffeac71b02af5`

> The startproject and startapp commands now create the custom target directory if it doesn't exist.

**Confirmed label:** Configuration/deployment

**Why:** Project setup commands now create a missing target directory.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L260-L261)

**Tilak's decision:** Confirmed as shown above.

### 092. Django 6.0 - `dj-f1d77b81d9ec4f95`

> All parameters must be passed as keyword arguments when creating an EmailMessage or EmailMultiAlternatives instance, except for the first four (subject, body, from_email, and to), which may still be passed either as positional or keyword arguments.

**Confirmed label:** API/code compatibility

**Why:** EmailMessage constructors now restrict positional arguments.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L500-L503)

**Tilak's decision:** Confirmed as shown above.

### 093. Django 6.0 - `dj-5ccaf6e861ba495e`

> Built-in support for the Content Security Policy (CSP) standard is now available, making it easier to protect web applications against content injection attacks such as cross-site scripting (XSS). CSP allows declaring trusted sources of content by giving browsers strict rules about which scripts, styles, images, or other resources can be loaded.

**Confirmed label:** Configuration/deployment

**Why:** CSP trusted-source policy is an application security configuration.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L43-L47)

**Tilak's decision:** Confirmed as shown above.

### 094. Django 6.0 - `dj-e2e11e844245d968`

> The undocumented encoding property of django.core.mail.EmailMessage no longer supports Python legacy email.charset.Charset objects.

**Confirmed label:** API/code compatibility

**Why:** EmailMessage.encoding no longer accepts a legacy Charset object.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L420-L422)

**Tilak's decision:** Confirmed as shown above.

### 095. Django 6.0 - `dj-dcf0e14c4bba7df0`

> Serialization of deconstructible objects now supports keyword arguments with names that are not valid Python identifiers.

**Confirmed label:** Data/schema migration

**Why:** Migration serialization now supports unusual keyword names.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L274-L275)

**Tilak's decision:** Confirmed as shown above.

### 096. Django 5.2.1 - `dj-3b38f31e42c8f79c`

> Fixed a data corruption possibility in file_move_safe() when allow_overwrite=True, where leftover content from a previously larger file could remain after overwriting with a smaller one due to lack of truncation (36298).

**Confirmed label:** Data/schema migration

**Why:** The file overwrite fix prevents persistent file-content corruption.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L44-L47)

**Tilak's decision:** Confirmed as shown above.

### 097. Django 5.2.5 - `dj-49b2515cbe8ef124`

> Fixed a crash in Django 5.2 when filtering against a composite primary key using a tuple containing expressions (36522).

**Confirmed label:** Data/schema migration

**Why:** A composite-key filter changes ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.5.txt#L16-L17)

**Tilak's decision:** Confirmed as shown above.

### 098. Django 6.0.1 - `dj-485803ee534b9de7`

> Fixed a regression in Django 6.0 that caused django.db.models.query.QuerySet.bulk_create to crash when introspecting the connection on SQLite (36818).

**Confirmed label:** Data/schema migration

**Why:** bulk_create on SQLite changes ORM data-write behavior.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.1.txt#L27-L29)

**Tilak's decision:** Confirmed as shown above.

### 099. Django 5.2.1 - `dj-41502838e5207a6d`

> Fixed a regression in Django 5.2 that caused a crash when annotating aggregate expressions over query that uses explicit grouping by transforms followed by field references (36292).

**Confirmed label:** Data/schema migration

**Why:** Aggregate annotations and grouping change ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L29-L31)

**Tilak's decision:** Confirmed as shown above.

### 100. Django 5.2.1 - `dj-47264f3af3f7a71d`

> Fixed a regression in Django 5.2 that caused the object-tools block to be rendered twice when using custom admin templates with overridden blocks due to changes in the base admin page block structure (36331).

**Confirmed label:** UI/output behavior

**Why:** Custom admin templates no longer render object tools twice.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.1.txt#L61-L63)

**Tilak's decision:** Confirmed as shown above.

# Om batch 02: 100 human-confirmed decisions

> **REVIEW COMPLETE.** Om Nathani confirmed all 100 proposed decisions on 2026-11-01, including one `No targeted check stated` label. Suggestions were visible during review.

Prepared: 2026-11-01. Source: pinned official Django release notes. This is an annotation queue, not a representative test set.

**Selection:** 26 entries from Django 4.2, 32 from 5.0, 12 from 5.1, and 30 from 6.0. A fixed hash order selected entries after excluding 350 confirmed IDs, obvious near-duplicates, and visibly incomplete fragments. No 5.2 candidate passed the current near-duplicate check after the prior batches; too few patch-release candidates passed to support a balanced patch quota. The selection therefore uses four feature releases. Selection did not use labels.

**Review outcome:** Om confirmed every proposed decision. The ignored local record contains his name and exact timestamps; the shareable export is `data/processed/om_batch_02_reviewed_labels.csv`. The review was non-blind because suggestions were visible.

**Confirmed counts:** API/code compatibility: 53; Configuration/deployment: 11; Data/schema migration: 19; UI/output behavior: 16; No targeted check stated: 1; UNCLEAR: 0.

## Quick index

| No. | Django | Confirmed label | Status |
| ---: | --- | --- | --- |
| 001 | 4.2 | Data/schema migration | Confirmed |
| 002 | 4.2 | UI/output behavior | Confirmed |
| 003 | 4.2 | Data/schema migration | Confirmed |
| 004 | 4.2 | API/code compatibility | Confirmed |
| 005 | 4.2 | UI/output behavior | Confirmed |
| 006 | 4.2 | API/code compatibility | Confirmed |
| 007 | 4.2 | UI/output behavior | Confirmed |
| 008 | 4.2 | Data/schema migration | Confirmed |
| 009 | 4.2 | API/code compatibility | Confirmed |
| 010 | 4.2 | API/code compatibility | Confirmed |
| 011 | 4.2 | UI/output behavior | Confirmed |
| 012 | 4.2 | Configuration/deployment | Confirmed |
| 013 | 4.2 | No targeted check stated | Confirmed |
| 014 | 4.2 | API/code compatibility | Confirmed |
| 015 | 4.2 | UI/output behavior | Confirmed |
| 016 | 4.2 | Configuration/deployment | Confirmed |
| 017 | 4.2 | UI/output behavior | Confirmed |
| 018 | 4.2 | API/code compatibility | Confirmed |
| 019 | 4.2 | API/code compatibility | Confirmed |
| 020 | 4.2 | API/code compatibility | Confirmed |
| 021 | 4.2 | API/code compatibility | Confirmed |
| 022 | 4.2 | API/code compatibility | Confirmed |
| 023 | 4.2 | Configuration/deployment | Confirmed |
| 024 | 4.2 | API/code compatibility | Confirmed |
| 025 | 4.2 | API/code compatibility | Confirmed |
| 026 | 4.2 | API/code compatibility | Confirmed |
| 027 | 5.0 | API/code compatibility | Confirmed |
| 028 | 5.0 | API/code compatibility | Confirmed |
| 029 | 5.0 | Data/schema migration | Confirmed |
| 030 | 5.0 | UI/output behavior | Confirmed |
| 031 | 5.0 | Data/schema migration | Confirmed |
| 032 | 5.0 | API/code compatibility | Confirmed |
| 033 | 5.0 | UI/output behavior | Confirmed |
| 034 | 5.0 | UI/output behavior | Confirmed |
| 035 | 5.0 | UI/output behavior | Confirmed |
| 036 | 5.0 | API/code compatibility | Confirmed |
| 037 | 5.0 | API/code compatibility | Confirmed |
| 038 | 5.0 | Data/schema migration | Confirmed |
| 039 | 5.0 | UI/output behavior | Confirmed |
| 040 | 5.0 | UI/output behavior | Confirmed |
| 041 | 5.0 | Data/schema migration | Confirmed |
| 042 | 5.0 | Data/schema migration | Confirmed |
| 043 | 5.0 | Configuration/deployment | Confirmed |
| 044 | 5.0 | API/code compatibility | Confirmed |
| 045 | 5.0 | API/code compatibility | Confirmed |
| 046 | 5.0 | API/code compatibility | Confirmed |
| 047 | 5.0 | UI/output behavior | Confirmed |
| 048 | 5.0 | Configuration/deployment | Confirmed |
| 049 | 5.0 | API/code compatibility | Confirmed |
| 050 | 5.0 | Data/schema migration | Confirmed |
| 051 | 5.0 | API/code compatibility | Confirmed |
| 052 | 5.0 | API/code compatibility | Confirmed |
| 053 | 5.0 | API/code compatibility | Confirmed |
| 054 | 5.0 | API/code compatibility | Confirmed |
| 055 | 5.0 | Configuration/deployment | Confirmed |
| 056 | 5.0 | UI/output behavior | Confirmed |
| 057 | 5.0 | API/code compatibility | Confirmed |
| 058 | 5.0 | API/code compatibility | Confirmed |
| 059 | 5.1 | API/code compatibility | Confirmed |
| 060 | 5.1 | Data/schema migration | Confirmed |
| 061 | 5.1 | API/code compatibility | Confirmed |
| 062 | 5.1 | Data/schema migration | Confirmed |
| 063 | 5.1 | API/code compatibility | Confirmed |
| 064 | 5.1 | API/code compatibility | Confirmed |
| 065 | 5.1 | UI/output behavior | Confirmed |
| 066 | 5.1 | API/code compatibility | Confirmed |
| 067 | 5.1 | Configuration/deployment | Confirmed |
| 068 | 5.1 | API/code compatibility | Confirmed |
| 069 | 5.1 | API/code compatibility | Confirmed |
| 070 | 5.1 | API/code compatibility | Confirmed |
| 071 | 6.0 | API/code compatibility | Confirmed |
| 072 | 6.0 | Data/schema migration | Confirmed |
| 073 | 6.0 | Configuration/deployment | Confirmed |
| 074 | 6.0 | Configuration/deployment | Confirmed |
| 075 | 6.0 | Data/schema migration | Confirmed |
| 076 | 6.0 | UI/output behavior | Confirmed |
| 077 | 6.0 | API/code compatibility | Confirmed |
| 078 | 6.0 | Data/schema migration | Confirmed |
| 079 | 6.0 | API/code compatibility | Confirmed |
| 080 | 6.0 | Configuration/deployment | Confirmed |
| 081 | 6.0 | API/code compatibility | Confirmed |
| 082 | 6.0 | Data/schema migration | Confirmed |
| 083 | 6.0 | API/code compatibility | Confirmed |
| 084 | 6.0 | API/code compatibility | Confirmed |
| 085 | 6.0 | API/code compatibility | Confirmed |
| 086 | 6.0 | API/code compatibility | Confirmed |
| 087 | 6.0 | API/code compatibility | Confirmed |
| 088 | 6.0 | Data/schema migration | Confirmed |
| 089 | 6.0 | API/code compatibility | Confirmed |
| 090 | 6.0 | Data/schema migration | Confirmed |
| 091 | 6.0 | Configuration/deployment | Confirmed |
| 092 | 6.0 | API/code compatibility | Confirmed |
| 093 | 6.0 | Data/schema migration | Confirmed |
| 094 | 6.0 | API/code compatibility | Confirmed |
| 095 | 6.0 | API/code compatibility | Confirmed |
| 096 | 6.0 | Data/schema migration | Confirmed |
| 097 | 6.0 | API/code compatibility | Confirmed |
| 098 | 6.0 | API/code compatibility | Confirmed |
| 099 | 6.0 | API/code compatibility | Confirmed |
| 100 | 6.0 | API/code compatibility | Confirmed |

## Full review

### 001. Django 4.2 — `dj-6f728983f5370e48`

> The AlterIndexTogether migration operation is now officially supported only for pre-Django 4.2 migration files. For backward compatibility reasons, it's still part of the public API, and there's no plan to deprecate or remove it, but it should not be used for new migrations. Use django.db.migrations.operations.AddIndex and django.db.migrations.operations.RemoveIndex operations instead.

**Confirmed label:** Data/schema migration

**Why:** New migrations should use AddIndex or RemoveIndex instead of AlterIndexTogether.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L518-L523)

**Om's decision:** Confirmed as shown above.

### 002. Django 4.2 — `dj-0c341aa4a966631e`

> The new Sitemap.get_languages_for_item method allows customizing the list of languages for which the item is displayed.

**Confirmed label:** UI/output behavior

**Why:** Sitemap language selection changes which item versions appear in output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L203-L204)

**Om's decision:** Confirmed as shown above.

### 003. Django 4.2 — `dj-247d6288cba3acf2`

> During the deprecation period string literals will be attempted to be JSON decoded and a warning will be emitted on success that points at passing non-encoded forms instead.

**Confirmed label:** Data/schema migration

**Why:** JSONField string-literal decoding changes database lookup semantics.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L532-L534)

**Om's decision:** Confirmed as shown above.

### 004. Django 4.2 — `dj-158b098d136c4c7d`

> django.contrib.auth.forms.UserCreationForm now rejects usernames that differ only in case. If you need the previous behavior, use django.contrib.auth.forms.BaseUserCreationForm instead.

**Confirmed label:** API/code compatibility

**Why:** UserCreationForm validation rejects case-only username differences.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L453-L455)

**Om's decision:** Confirmed as shown above.

### 005. Django 4.2 — `dj-b84e4c6a57c3765c`

> The GeoJSON serializer now outputs the id key for serialized features, which defaults to the primary key of objects.

**Confirmed label:** UI/output behavior

**Why:** The GeoJSON serializer now emits an id key.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L161-L163)

**Om's decision:** Confirmed as shown above.

### 006. Django 4.2 — `dj-807a543efe4fca3f`

> The django.core.files.storage.get_storage_class() function is deprecated.

**Confirmed label:** API/code compatibility

**Why:** Code calling get_storage_class needs a replacement.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L620-L620)

**Om's decision:** Confirmed as shown above.

### 007. Django 4.2 — `dj-d7492c53c58c409b`

> The chosen options of django.contrib.admin.ModelAdmin.filter_horizontal and django.contrib.admin.ModelAdmin.filter_vertical widgets are now filterable.

**Confirmed label:** UI/output behavior

**Why:** Admin filter widgets now let users filter chosen options.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L133-L136)

**Om's decision:** Confirmed as shown above.

### 008. Django 4.2 — `dj-566b3d1813c8f14a`

> The new KT() expression represents the text value of a key, index, or path transform of django.db.models.JSONField.

**Confirmed label:** Data/schema migration

**Why:** KT changes JSONField key and path query expressions.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L289-L291)

**Om's decision:** Confirmed as shown above.

### 009. Django 4.2 — `dj-aad353564e51e60f`

> The new ManifestStaticFilesStorage.manifest_hash attribute provides a hash over all files in the manifest and changes whenever one of the files changes.

**Confirmed label:** API/code compatibility

**Why:** Code can read the new manifest_hash attribute.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L215-L217)

**Om's decision:** Confirmed as shown above.

### 010. Django 4.2 — `dj-02d40701c4400e4b`

> The private internal vendored copy of urllib.parse.urlsplit() now strips '\r', '\n', and '\t' (see 2022-0391 and 43882). This is to protect projects that may be incorrectly using the internal url_has_allowed_host_and_scheme() function, instead of using one of the documented functions for handling URL redirects. The Django functions were not affected.

**Confirmed label:** API/code compatibility

**Why:** Projects using the private URL validation helper may see different input handling.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L346-L351)

**Om's decision:** Confirmed as shown above.

### 011. Django 4.2 — `dj-2ecd3de8279bcc45`

> Session cookies are now treated as credentials and therefore hidden and replaced with stars (**********) in error reports.

**Confirmed label:** UI/output behavior

**Why:** Error reports now mask session cookie values.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L235-L236)

**Om's decision:** Confirmed as shown above.

### 012. Django 4.2 — `dj-189c548575bbdd11`

> The new django.core.files.storage.InMemoryStorage class provides a non-persistent storage useful for speeding up tests by avoiding disk access.

**Confirmed label:** Configuration/deployment

**Why:** Tests can configure the new nonpersistent storage backend.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L102-L103)

**Om's decision:** Confirmed as shown above.

### 013. Django 4.2 — `dj-71b9e7008cbacc1c`

> Support for psycopg2 is likely to be deprecated and removed at some point in the future.

**Confirmed label:** No targeted check stated

**Why:** This predicts a possible future psycopg2 deprecation but states no current behavior to verify.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L43-L44)

**Om's decision:** Confirmed as shown above.

### 014. Django 4.2 — `dj-b95c3d2bc0db65e9`

> django.forms.models.modelform_factory now respects the formfield_callback attribute of the form’s Meta.

**Confirmed label:** API/code compatibility

**Why:** Code using modelform_factory may observe its Meta callback being honored.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L244-L245)

**Om's decision:** Confirmed as shown above.

### 015. Django 4.2 — `dj-f50dadd1100f8cff`

> django.contrib.gis.forms.widgets.OpenLayersWidget is now based on OpenLayers 7.2.2 (previously 4.6.5).

**Confirmed label:** UI/output behavior

**Why:** The GIS form widget now uses a newer OpenLayers interface.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L175-L176)

**Om's decision:** Confirmed as shown above.

### 016. Django 4.2 — `dj-25bfae6588fad5b1`

> The minimum supported version of Pillow is increased from 6.2.0 to 6.2.1.

**Confirmed label:** Configuration/deployment

**Why:** The installed Pillow minimum version has increased.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L463-L463)

**Om's decision:** Confirmed as shown above.

### 017. Django 4.2 — `dj-e8ee23ceceff9a2b`

> {% blocktranslate asvar … %}<blocktranslate> result is now marked as safe for (HTML) output purposes.

**Confirmed label:** UI/output behavior

**Why:** Block translation output is now marked HTML-safe.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L428-L429)

**Om's decision:** Confirmed as shown above.

### 018. Django 4.2 — `dj-c27b19544e9e4d10`

> The alias argument for Expression.get_group_by_cols is removed.

**Confirmed label:** API/code compatibility

**Why:** Code passing alias to Expression.get_group_by_cols must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L437-L437)

**Om's decision:** Confirmed as shown above.

### 019. Django 4.2 — `dj-35e23ba0f05bc8ea`

> The undocumented django.http.multipartparser.parse_header() function is removed. Use django.utils.http.parse_header_parameters() instead.

**Confirmed label:** API/code compatibility

**Why:** Code calling the removed parse_header helper must use its replacement.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L425-L426)

**Om's decision:** Confirmed as shown above.

### 020. Django 4.2 — `dj-ae38608ab5422555`

> Related managers now provide asynchronous versions of methods that change a set of related objects, using an a prefix: RelatedManager.aadd, RelatedManager.aclear, RelatedManager.aremove, and RelatedManager.aset.

**Confirmed label:** API/code compatibility

**Why:** Code can call new asynchronous related-manager methods.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L303-L306)

**Om's decision:** Confirmed as shown above.

### 021. Django 4.2 — `dj-efba58cf37e55725`

> The is_summary argument of the undocumented Query.add_annotation() method is removed.

**Confirmed label:** API/code compatibility

**Why:** Code passing is_summary to Query.add_annotation must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L445-L446)

**Om's decision:** Confirmed as shown above.

### 022. Django 4.2 — `dj-36e8ecc6dcd90b7d`

> Passing positional arguments to Signer and TimestampSigner is deprecated in favor of keyword-only arguments.

**Confirmed label:** API/code compatibility

**Why:** Signer and TimestampSigner calls should use keyword arguments.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L611-L612)

**Om's decision:** Confirmed as shown above.

### 023. Django 4.2 — `dj-2597548c67d06ef9`

> The minimum supported version of jinja2 is increased from 2.9.2 to 2.11.0.

**Confirmed label:** Configuration/deployment

**Why:** The installed Jinja2 minimum version has increased.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L465-L466)

**Om's decision:** Confirmed as shown above.

### 024. Django 4.2 — `dj-dbebcd23fca3f4a1`

> Manually instantiated WSGIRequest objects must be provided a file-like object for wsgi.input. Previously, Django was more lax than the expected behavior as specified by the WSGI specification.

**Confirmed label:** API/code compatibility

**Why:** Manual WSGIRequest construction must pass a file-like wsgi.input.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L471-L473)

**Om's decision:** Confirmed as shown above.

### 025. Django 4.2 — `dj-b967fb53adb3486f`

> Registering lookups on django.db.models.Field instances is now supported.

**Confirmed label:** API/code compatibility

**Why:** Custom code can register lookups on Field instances.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L282-L283)

**Om's decision:** Confirmed as shown above.

### 026. Django 4.2 — `dj-375657786332b92a`

> TransactionTestCase.assertQuerysetEqual() is deprecated in favor of assertQuerySetEqual().

**Confirmed label:** API/code compatibility

**Why:** Tests should call assertQuerySetEqual instead of its deprecated spelling.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L608-L609)

**Om's decision:** Confirmed as shown above.

### 027. Django 5.0 — `dj-a8ecca31d0580322`

> The django.contrib.auth.hashers.CryptPasswordHasher is removed.

**Confirmed label:** API/code compatibility

**Why:** Code importing the removed password hasher must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L750-L750)

**Om's decision:** Confirmed as shown above.

### 028. Django 5.0 — `dj-589f9ca085068d7e`

> The get_prefetch_queryset() method of related managers and descriptors is deprecated. Starting with Django 6.0, get_prefetcher() and prefetch_related_objects() will no longer fallback to get_prefetch_queryset(). Subclasses should implement get_prefetch_querysets() instead.

**Confirmed label:** API/code compatibility

**Why:** Custom related managers should implement get_prefetch_querysets.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L647-L651)

**Om's decision:** Confirmed as shown above.

### 029. Django 5.0 — `dj-e6d2a6c833af72b5`

> django.db.models.functions.Now database function now uses LOCALTIMESTAMP instead of CURRENT_TIMESTAMP on Oracle.

**Confirmed label:** Data/schema migration

**Why:** Now() produces different Oracle timestamp query semantics.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L551-L552)

**Om's decision:** Confirmed as shown above.

### 030. Django 5.0 — `dj-8897681fa857d0ab`

> Form fields now include the aria-describedby HTML attribute to enable screen readers to associate form fields with their help text.

**Confirmed label:** UI/output behavior

**Why:** Rendered form fields now include aria-describedby for help text.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L346-L347)

**Om's decision:** Confirmed as shown above.

### 031. Django 5.0 — `dj-7c3feb578ccf090a`

> QuerySet.aiterator now supports previous calls to prefetch_related().

**Confirmed label:** Data/schema migration

**Why:** aiterator now supports prefetch-related ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L394-L395)

**Om's decision:** Confirmed as shown above.

### 032. Django 5.0 — `dj-6eec489d605286c7`

> The undocumented ability to pass errors=None to SimpleTestCase.assertFormError() and assertFormsetError() is removed.

**Confirmed label:** API/code compatibility

**Why:** Tests passing errors=None to these assertion helpers must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L724-L725)

**Om's decision:** Confirmed as shown above.

### 033. Django 5.0 — `dj-a3442b75bc4b9b8d`

> The ability to return a str, rather than a SafeString, when rendering an ErrorDict and ErrorList is removed.

**Confirmed label:** UI/output behavior

**Why:** ErrorDict and ErrorList render with a SafeString result.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L708-L709)

**Om's decision:** Confirmed as shown above.

### 034. Django 5.0 — `dj-661274fe22148fac`

> The "django/forms/default.html" and "django/forms/formsets/default.html" templates are removed.

**Confirmed label:** UI/output behavior

**Why:** The removed form templates affect rendered form output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L752-L753)

**Om's decision:** Confirmed as shown above.

### 035. Django 5.0 — `dj-da9a226c0649ef26`

> The default form and formset rendering style is changed to the div-based.

**Confirmed label:** UI/output behavior

**Why:** Default form and formset output is now div-based.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L755-L755)

**Om's decision:** Confirmed as shown above.

### 036. Django 5.0 — `dj-2e4b699be6798b14`

> The ForeignObject.get_reverse_joining_columns() method is deprecated.

**Confirmed label:** API/code compatibility

**Why:** Custom ForeignObject code should stop using get_reverse_joining_columns.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L622-L622)

**Om's decision:** Confirmed as shown above.

### 037. Django 5.0 — `dj-880feb4a7ac42c10`

> The name argument of django.utils.functional.cached_property() is removed.

**Confirmed label:** API/code compatibility

**Why:** Code passing name to cached_property must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L718-L719)

**Om's decision:** Confirmed as shown above.

### 038. Django 5.0 — `dj-ef90dd5bb066df97`

> The force_insert argument of Model.save now allows specifying a tuple of parent classes that must be forced to be inserted.

**Confirmed label:** Data/schema migration

**Why:** Model.save force_insert changes how parent rows are inserted.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L376-L378)

**Om's decision:** Confirmed as shown above.

### 039. Django 5.0 — `dj-db035fa36e528f70`

> django.core.exceptions.BadRequest is raised for non-UTF-8 encoded requests with the application/x-www-form-urlencoded content type. See 1866 for more details.

**Confirmed label:** UI/output behavior

**Why:** Non-UTF-8 form requests now produce a BadRequest response.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L584-L586)

**Om's decision:** Confirmed as shown above.

### 040. Django 5.0 — `dj-f4534eaf6d77cba2`

> AdminSite.site_header is now rendered in a <div> tag instead of <h1>. Screen reader users rely on heading elements for navigation within a page. Having two <h1> elements was confusing and the site header wasn't helpful as it is repeated on all pages.

**Confirmed label:** UI/output behavior

**Why:** The admin site header now renders as a div rather than h1.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L554-L557)

**Om's decision:** Confirmed as shown above.

### 041. Django 5.0 — `dj-bee0973da9d4ddaf`

> The new UniqueConstraint.nulls_distinct attribute allows customizing the treatment of NULL values on PostgreSQL 15+.

**Confirmed label:** Data/schema migration

**Why:** UniqueConstraint changes database NULL uniqueness behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L384-L385)

**Om's decision:** Confirmed as shown above.

### 042. Django 5.0 — `dj-6708ed64e9d7a838`

> The django.contrib.postgres.aggregates.ArrayAgg, JSONBAgg, and StringAgg aggregates no longer return [], [], and '', respectively, when there are no rows.

**Confirmed label:** Data/schema migration

**Why:** The aggregates now return different values for empty result sets.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L679-L681)

**Om's decision:** Confirmed as shown above.

### 043. Django 5.0 — `dj-01a5b71f0dad9a9b`

> django.contrib.sessions.serializers.PickleSerializer is removed.

**Confirmed label:** Configuration/deployment

**Why:** Session serializer configuration cannot reference removed PickleSerializer.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L727-L727)

**Om's decision:** Confirmed as shown above.

### 044. Django 5.0 — `dj-239bce880672c352`

> The undocumented Query.annotation_select_mask attribute is changed from a set of strings to an ordered list of strings.

**Confirmed label:** API/code compatibility

**Why:** Custom code reading Query.annotation_select_mask sees an ordered list.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L545-L546)

**Om's decision:** Confirmed as shown above.

### 045. Django 5.0 — `dj-38b70045f734b662`

> The django.utils.timezone.utc alias to datetime.timezone.utc is removed.

**Confirmed label:** API/code compatibility

**Why:** Code importing the removed timezone.utc alias must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L741-L742)

**Om's decision:** Confirmed as shown above.

### 046. Django 5.0 — `dj-9c92b70589a65d6d`

> The undocumented django.utils.datetime_safe module is removed.

**Confirmed label:** API/code compatibility

**Why:** Code importing the undocumented datetime_safe module must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L668-L668)

**Om's decision:** Confirmed as shown above.

### 047. Django 5.0 — `dj-ace6d835c35868a9`

> The default sitemap protocol for sitemaps built outside the context of a request is changed from 'http' to 'https'.

**Confirmed label:** UI/output behavior

**Why:** Generated sitemap URLs now default to HTTPS outside a request.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L673-L674)

**Om's decision:** Confirmed as shown above.

### 048. Django 5.0 — `dj-e0670c482bfef827`

> The USE_DEPRECATED_PYTZ transitional setting is removed.

**Confirmed label:** Configuration/deployment

**Why:** The removed USE_DEPRECATED_PYTZ setting requires configuration review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L685-L685)

**Om's decision:** Confirmed as shown above.

### 049. Django 5.0 — `dj-48f3b4fdc9d9460a`

> created=True is required in the signature of RemoteUserBackend.configure_user() subclasses.

**Confirmed label:** API/code compatibility

**Why:** RemoteUserBackend subclasses need a created parameter in configure_user.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L734-L735)

**Om's decision:** Confirmed as shown above.

### 050. Django 5.0 — `dj-4cc0ee36bc7b1c13`

> ImageField.update_dimension_fields() is no longer called on the post_init signal if width_field and height_field are not set.

**Confirmed label:** Data/schema migration

**Why:** ImageField no longer refreshes dimension fields on post_init in this case.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L548-L549)

**Om's decision:** Confirmed as shown above.

### 051. Django 5.0 — `dj-e4448c40f7dbb17d`

> Executing SQL queries before the app registry has been fully populated now raises RuntimeWarning.

**Confirmed label:** API/code compatibility

**Why:** Startup code that queries before app registry readiness now triggers a warning.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L581-L582)

**Om's decision:** Confirmed as shown above.

### 052. Django 5.0 — `dj-31dd107a823c507c`

> The opclasses argument of django.contrib.postgres.constraints.ExclusionConstraint is removed.

**Confirmed label:** API/code compatibility

**Why:** Constraint construction code cannot pass opclasses.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L721-L722)

**Om's decision:** Confirmed as shown above.

### 053. Django 5.0 — `dj-c670b5dfa0525855`

> The extra_tests argument for DiscoverRunner.build_suite() and DiscoverRunner.run_tests() is removed.

**Confirmed label:** API/code compatibility

**Why:** Custom test-runner calls cannot pass extra_tests.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L676-L677)

**Om's decision:** Confirmed as shown above.

### 054. Django 5.0 — `dj-d88b574be9d0b1c8`

> The Prefetch.get_current_queryset() method is deprecated.

**Confirmed label:** API/code compatibility

**Why:** Code using Prefetch.get_current_queryset should migrate.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L645-L645)

**Om's decision:** Confirmed as shown above.

### 055. Django 5.0 — `dj-5e86b39c4b8b2f4a`

> Django now supports oracledb version 1.3.2 or higher. Support for cx_Oracle is deprecated as of this release and will be removed in Django 6.0.

**Confirmed label:** Configuration/deployment

**Why:** Oracle driver dependency support changes at deployment.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L401-L403)

**Om's decision:** Confirmed as shown above.

### 056. Django 5.0 — `dj-a42acb81a5f215c2`

> Support for logging out via GET requests in the django.contrib.auth.views.LogoutView and django.contrib.auth.views.logout_then_login() is removed.

**Confirmed label:** UI/output behavior

**Why:** GET requests can no longer log users out through these views.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L737-L739)

**Om's decision:** Confirmed as shown above.

### 057. Django 5.0 — `dj-4f7f9791274fb4aa`

> The instance argument of the undocumented BaseModelFormSet.save_existing() method is renamed to obj.

**Confirmed label:** API/code compatibility

**Why:** Custom formset code must use the renamed obj parameter.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L537-L538)

**Om's decision:** Confirmed as shown above.

### 058. Django 5.0 — `dj-7852ce1821e9197e`

> Support for calling format_html() without passing args or kwargs is deprecated.

**Confirmed label:** API/code compatibility

**Why:** format_html calls need args or kwargs.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L631-L632)

**Om's decision:** Confirmed as shown above.

### 059. Django 5.1 — `dj-817e6d6119452636`

> Setting django.contrib.gis.gdal.OGRGeometry.coord_dim is deprecated. Use django.contrib.gis.gdal.OGRGeometry.set_3d instead.

**Confirmed label:** API/code compatibility

**Why:** GIS code should call set_3d instead of setting coord_dim.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L435-L436)

**Om's decision:** Confirmed as shown above.

### 060. Django 5.1 — `dj-40ba2b6ea6db1d1b`

> ImageField.update_dimension_fields(force=True) is no longer called after saving the image to storage. If your storage backend resizes images, the width_field and height_field will not match the width and height of the image.

**Confirmed label:** Data/schema migration

**Why:** Stored image dimensions can now differ after a resizing storage backend runs.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L396-L399)

**Om's decision:** Confirmed as shown above.

### 061. Django 5.1 — `dj-b88d18efb2fdeb5f`

> The map_width and map_height attributes of BaseGeometryWidget are removed.

**Confirmed label:** API/code compatibility

**Why:** Custom geometry-widget code cannot use removed sizing attributes.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L479-L480)

**Om's decision:** Confirmed as shown above.

### 062. Django 5.1 — `dj-5e68ad7061defe42`

> F() and OuterRef() expressions that output django.db.models.CharField, django.db.models.EmailField, django.db.models.SlugField, django.db.models.URLField, django.db.models.TextField, or django.contrib.postgres.fields.ArrayField can now be sliced.

**Confirmed label:** Data/schema migration

**Why:** Sliced F and OuterRef expressions change ORM query capabilities.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L266-L272)

**Om's decision:** Confirmed as shown above.

### 063. Django 5.1 — `dj-8ae42d878e28495b`

> django.contrib.auth.decorators.login_required, django.contrib.auth.decorators.permission_required, and django.contrib.auth.decorators.user_passes_test decorators now support wrapping asynchronous view functions.

**Confirmed label:** API/code compatibility

**Why:** Authentication decorators can wrap async view code.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L128-L131)

**Om's decision:** Confirmed as shown above.

### 064. Django 5.1 — `dj-8a3ba11c168afb27`

> django.contrib.gis.measure.Area now supports the ha unit.

**Confirmed label:** API/code compatibility

**Why:** GIS code can use the ha area unit.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L159-L159)

**Om's decision:** Confirmed as shown above.

### 065. Django 5.1 — `dj-0cef0c8c7053b673`

> In order to improve accessibility, the admin's footer is now rendered in a <footer> tag instead of a <div>, and also moved below the <div id="main"> element.

**Confirmed label:** UI/output behavior

**Why:** The admin footer moves and renders as a footer element.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L365-L367)

**Om's decision:** Confirmed as shown above.

### 066. Django 5.1 — `dj-df4d5a7c23a9e302`

> The undocumented django.utils.itercompat.is_iterable() function and the django.utils.itercompat module are deprecated. Use isinstance(..., collections.abc.Iterable) instead.

**Confirmed label:** API/code compatibility

**Why:** Code using the deprecated is_iterable helper should use Iterable checks.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L422-L424)

**Om's decision:** Confirmed as shown above.

### 067. Django 5.1 — `dj-72e698d90314db7d`

> The undocumented OS_OPEN_FLAGS property of django.core.files.storage.FileSystemStorage is deprecated. To allow overwriting files in storage, set the new django.core.files.storage.FileSystemStorage.allow_overwrite option to True instead.

**Confirmed label:** Configuration/deployment

**Why:** Storage overwrite behavior should use the new allow_overwrite option.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L444-L448)

**Om's decision:** Confirmed as shown above.

### 068. Django 5.1 — `dj-8463536403d3cb76`

> The get_cache_name() method of FieldCacheMixin is deprecated in favor of the cache_name cached property.

**Confirmed label:** API/code compatibility

**Why:** FieldCacheMixin code should use cache_name instead.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L450-L451)

**Om's decision:** Confirmed as shown above.

### 069. Django 5.1 — `dj-6706f6476c2cb5de`

> The undocumented django.urls.converters.get_converter() function is removed.

**Confirmed label:** API/code compatibility

**Why:** Code importing the removed get_converter helper must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L387-L388)

**Om's decision:** Confirmed as shown above.

### 070. Django 5.1 — `dj-2f172ab89266816d`

> To improve performance, the delete_selected admin action now uses QuerySet.bulk_create() when creating multiple LogEntry objects. As a result, pre_save and post_save signals for LogEntry are not sent when multiple objects are deleted via this admin action.

**Confirmed label:** API/code compatibility

**Why:** LogEntry signal handlers no longer run for bulk admin deletion.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L404-L407)

**Om's decision:** Confirmed as shown above.

### 071. Django 6.0 — `dj-76b9e6bb6bb3f0a2`

> Support for passing positional arguments to BaseConstraint is removed.

**Confirmed label:** API/code compatibility

**Why:** BaseConstraint construction can no longer use positional arguments.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L562-L562)

**Om's decision:** Confirmed as shown above.

### 072. Django 6.0 — `dj-47a2756fb3f4ee95`

> The new geom_type lookup and GeometryType() database function allow filtering geometries by their types.

**Confirmed label:** Data/schema migration

**Why:** GIS geometry-type filtering changes database query capabilities.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L199-L201)

**Om's decision:** Confirmed as shown above.

### 073. Django 6.0 — `dj-b6078dcb80c0e591`

> Backends are configured via the TASKS setting. The two built-in backends included in this release are primarily intended for development and testing.

**Confirmed label:** Configuration/deployment

**Why:** The TASKS setting selects a task backend.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L128-L130)

**Om's decision:** Confirmed as shown above.

### 074. Django 6.0 — `dj-f16308c7379c0325`

> The default protocol in urlize and urlizetrunc will change from HTTP to HTTPS in Django 7.0. Set the transitional setting URLIZE_ASSUME_HTTPS to True to opt into assuming HTTPS during the Django 6.x release cycle.

**Confirmed label:** Configuration/deployment

**Why:** Projects can opt in through the URLIZE_ASSUME_HTTPS setting.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L518-L521)

**Om's decision:** Confirmed as shown above.

### 075. Django 6.0 — `dj-84b21cb3fd2b1d24`

> The new django.db.models.StringAgg aggregate returns the input values concatenated into a string, separated by the delimiter string. This aggregate was previously supported only for PostgreSQL.

**Confirmed label:** Data/schema migration

**Why:** StringAgg changes database aggregation output.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L289-L291)

**Om's decision:** Confirmed as shown above.

### 076. Django 6.0 — `dj-f73e89d3037f1432`

> The Font Awesome Free icon set (version 6.7.2) is now used for the admin interface icons.

**Confirmed label:** UI/output behavior

**Why:** Admin interface icons now use a different icon set.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L162-L163)

**Om's decision:** Confirmed as shown above.

### 077. Django 6.0 — `dj-68fb2b2ff5586f4c`

> DatabaseOperations.return_insert_columns() and DatabaseOperations.fetch_returned_insert_rows() methods are renamed to returning_columns() and fetch_returned_rows(), respectively, to denote they can be used in the context of UPDATE … RETURNING statements as well as INSERT … RETURNING.

**Confirmed label:** API/code compatibility

**Why:** Custom database backend methods must use their new names.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L369-L373)

**Om's decision:** Confirmed as shown above.

### 078. Django 6.0 — `dj-22b8903434e0c035`

> The CreateExtension, BloomExtension, BtreeGinExtension, BtreeGistExtension, CITextExtension, CryptoExtension, HStoreExtension, TrigramExtension, and UnaccentExtension operations now support the optional hints parameter. This allows providing database hints to database routers to assist them in making routing decisions.

**Confirmed label:** Data/schema migration

**Why:** Extension migration operations gain database-router hints.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L221-L227)

**Om's decision:** Confirmed as shown above.

### 079. Django 6.0 — `dj-8d942a948add1013`

> The django.contrib.gis.geoip2.GeoIP2.open() method is removed.

**Confirmed label:** API/code compatibility

**Why:** Code calling GeoIP2.open must change.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L615-L615)

**Om's decision:** Confirmed as shown above.

### 080. Django 6.0 — `dj-e690ee59ffbf0335`

> The FORMS_URLFIELD_ASSUME_HTTPS transitional setting is removed.

**Confirmed label:** Configuration/deployment

**Why:** The transitional HTTPS URL-field setting is removed.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L578-L578)

**Om's decision:** Confirmed as shown above.

### 081. Django 6.0 — `dj-a8ff4cfcee097fc0`

> The check keyword argument of CheckConstraint is removed.

**Confirmed label:** API/code compatibility

**Why:** CheckConstraint construction cannot use the check keyword.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L622-L622)

**Om's decision:** Confirmed as shown above.

### 082. Django 6.0 — `dj-c7e42f17836b563b`

> The new django.contrib.gis.db.models.functions.Rotate database function rotates a geometry by a specified angle around the origin or a specified point.

**Confirmed label:** Data/schema migration

**Why:** The Rotate function changes GIS database query output.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L186-L188)

**Om's decision:** Confirmed as shown above.

### 083. Django 6.0 — `dj-508fbea6d133ba38`

> The ChoicesMeta alias to django.db.models.enums.ChoicesType is removed.

**Confirmed label:** API/code compatibility

**Why:** Code importing ChoicesMeta must use ChoicesType.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L590-L591)

**Om's decision:** Confirmed as shown above.

### 084. Django 6.0 — `dj-13ee2fca07b4793f`

> The django.db.models.sql.datastructures.Join no longer falls back to get_joining_columns().

**Confirmed label:** API/code compatibility

**Why:** Custom Join code cannot rely on get_joining_columns fallback.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L580-L581)

**Om's decision:** Confirmed as shown above.

### 085. Django 6.0 — `dj-652b270e573047a4`

> The PostgreSQL OrderableAggMixin is deprecated in favor of the order_by attribute now available on the django.db.models.Aggregate class.

**Confirmed label:** API/code compatibility

**Why:** Custom aggregates should move from OrderableAggMixin to order_by.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L514-L516)

**Om's decision:** Confirmed as shown above.

### 086. Django 6.0 — `dj-64c67d52aa79238e`

> The django.db.models.Model.save method now raises a specialized Model.NotUpdated exception, when a forced update results in no affected rows, instead of a generic django.db.DatabaseError.

**Confirmed label:** API/code compatibility

**Why:** Callers catching DatabaseError should handle Model.NotUpdated.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L293-L296)

**Om's decision:** Confirmed as shown above.

### 087. Django 6.0 — `dj-b974c5c55bfa8513`

> get_prefetcher() and prefetch_related_objects() no longer fall back to get_prefetch_queryset().

**Confirmed label:** API/code compatibility

**Why:** Custom prefetch code must implement the newer queryset method.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L598-L599)

**Om's decision:** Confirmed as shown above.

### 088. Django 6.0 — `dj-477c1c6fd8c7c1cb`

> Using a ForeignObject with multiple from_fields in Model indexes, constraints, or unique_together now emits a system check error.

**Confirmed label:** Data/schema migration

**Why:** Model indexes and constraints using this ForeignObject pattern now fail a system check.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L318-L320)

**Om's decision:** Confirmed as shown above.

### 089. Django 6.0 — `dj-697f07701d01409a`

> The django.core.mail.SafeMIMEText and SafeMIMEMultipart classes are deprecated.

**Confirmed label:** API/code compatibility

**Why:** Code importing deprecated SafeMIME classes needs review.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L547-L548)

**Om's decision:** Confirmed as shown above.

### 090. Django 6.0 — `dj-d1c88d3e201ce457`

> QuerySet.raw now supports models with a django.db.models.CompositePrimaryKey.

**Confirmed label:** Data/schema migration

**Why:** QuerySet.raw can now work with composite primary-key models.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L298-L299)

**Om's decision:** Confirmed as shown above.

### 091. Django 6.0 — `dj-b1dfa1b71eb65777`

> Django handles task creation and queuing, but does not provide a worker mechanism to run tasks. Execution must be managed by external infrastructure, such as a separate process or service.

**Confirmed label:** Configuration/deployment

**Why:** Background task execution requires an external worker service.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L132-L134)

**Om's decision:** Confirmed as shown above.

### 092. Django 6.0 — `dj-47fe8a934ad0a89d`

> request is required in the signature of ModelAdmin.lookup_allowed() subclasses.

**Confirmed label:** API/code compatibility

**Why:** ModelAdmin.lookup_allowed subclass signatures must accept request.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L569-L570)

**Om's decision:** Confirmed as shown above.

### 093. Django 6.0 — `dj-f8d4af7d6cedb5a9`

> django.db.models.GeneratedField\s and fields assigned expressions are now refreshed from the database after django.db.models.Model.save on backends that support the RETURNING clause (SQLite, PostgreSQL, and Oracle). On backends that don't support it (MySQL and MariaDB), the fields are marked as deferred to trigger a refresh on subsequent accesses.

**Confirmed label:** Data/schema migration

**Why:** Generated fields refresh from the database differently after save.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L311-L316)

**Om's decision:** Confirmed as shown above.

### 094. Django 6.0 — `dj-1ba22f7269cc3677`

> The OS_OPEN_FLAGS attribute of django.core.files.storage.FileSystemStorage is removed.

**Confirmed label:** API/code compatibility

**Why:** Storage subclass code using OS_OPEN_FLAGS must change.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L626-L627)

**Om's decision:** Confirmed as shown above.

### 095. Django 6.0 — `dj-9344267d8d9fb7b2`

> The django.core.mail.BadHeaderError exception is deprecated. Python's modern email raises a !ValueError for email headers containing prohibited characters.

**Confirmed label:** API/code compatibility

**Why:** Email header validation now raises ValueError rather than BadHeaderError.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L543-L545)

**Om's decision:** Confirmed as shown above.

### 096. Django 6.0 — `dj-13fc4d1e9aa9b579`

> Subqueries returning a django.db.models.CompositePrimaryKey can now be used as the target of lookups other than __in, such as __exact.

**Confirmed label:** Data/schema migration

**Why:** Composite-key subqueries now work with additional ORM lookups.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L301-L302)

**Om's decision:** Confirmed as shown above.

### 097. Django 6.0 — `dj-f4bd9253207b140f`

> Support for passing positional arguments to Model.save() and Model.asave() is removed.

**Confirmed label:** API/code compatibility

**Why:** Model.save and asave calls can no longer use positional arguments.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L617-L618)

**Om's decision:** Confirmed as shown above.

### 098. Django 6.0 — `dj-3e69e69fdd8a2f4f`

> The get_cache_name() method of FieldCacheMixin is removed.

**Confirmed label:** API/code compatibility

**Why:** FieldCacheMixin callers cannot use get_cache_name.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L624-L624)

**Om's decision:** Confirmed as shown above.

### 099. Django 6.0 — `dj-ee5016f30f930317`

> The undocumented django.core.mail.forbid_multi_line_headers() and django.core.mail.message.sanitize_address() functions are deprecated.

**Confirmed label:** API/code compatibility

**Why:** Code calling deprecated mail header helpers needs review.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L550-L551)

**Om's decision:** Confirmed as shown above.

### 100. Django 6.0 — `dj-aa76780f5fb84d24`

> Support for the orphans argument being larger than or equal to the per_page argument of django.core.paginator.Paginator and django.core.paginator.AsyncPaginator is deprecated.

**Confirmed label:** API/code compatibility

**Why:** Paginator construction must avoid this deprecated orphans value.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L530-L532)

**Om's decision:** Confirmed as shown above.

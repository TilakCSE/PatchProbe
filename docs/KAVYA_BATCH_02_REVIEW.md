# Kavya batch 02: 50 human-confirmed decisions

> **REVIEW COMPLETE.** Kavya Jariwala confirmed all 50 proposed decisions on 2026-11-01, including two `UNCLEAR` states and one `No targeted check stated` label. Suggestions were visible during review.

Prepared: 2026-11-01. Source: pinned official Django release notes. This is an annotation queue, not a representative test set.

**Selection:** Ten entries each from feature releases 4.2, 5.0, 5.1, 5.2, and 6.0, selected by fixed hash order after excluding the 300 confirmed IDs, obvious near-duplicates, and visibly incomplete extraction fragments. Only two patch-release candidates remained after filtering, so no patch-release quota was used. Selection did not use labels.

**Review outcome:** Kavya confirmed every proposed decision. The ignored local record contains her name and exact timestamps; the shareable export is `data/processed/kavya_batch_02_reviewed_labels.csv`. The review was non-blind because suggestions were visible.

**Confirmed counts:** API/code compatibility: 17; Configuration/deployment: 5; Data/schema migration: 13; UI/output behavior: 12; No targeted check stated: 1; UNCLEAR: 2.

## Quick index

| No. | Django | Confirmed label | Status |
| ---: | --- | --- | --- |
| 01 | 4.2 | Data/schema migration | Confirmed |
| 02 | 4.2 | API/code compatibility | Confirmed |
| 03 | 4.2 | Data/schema migration | Confirmed |
| 04 | 4.2 | Configuration/deployment | Confirmed |
| 05 | 4.2 | Configuration/deployment | Confirmed |
| 06 | 4.2 | Data/schema migration | Confirmed |
| 07 | 4.2 | Data/schema migration | Confirmed |
| 08 | 4.2 | Data/schema migration | Confirmed |
| 09 | 4.2 | API/code compatibility | Confirmed |
| 10 | 4.2 | UNCLEAR | Confirmed |
| 11 | 5.0 | API/code compatibility | Confirmed |
| 12 | 5.0 | API/code compatibility | Confirmed |
| 13 | 5.0 | Data/schema migration | Confirmed |
| 14 | 5.0 | UI/output behavior | Confirmed |
| 15 | 5.0 | API/code compatibility | Confirmed |
| 16 | 5.0 | UI/output behavior | Confirmed |
| 17 | 5.0 | UI/output behavior | Confirmed |
| 18 | 5.0 | UI/output behavior | Confirmed |
| 19 | 5.0 | UI/output behavior | Confirmed |
| 20 | 5.0 | UI/output behavior | Confirmed |
| 21 | 5.1 | UI/output behavior | Confirmed |
| 22 | 5.1 | API/code compatibility | Confirmed |
| 23 | 5.1 | API/code compatibility | Confirmed |
| 24 | 5.1 | Configuration/deployment | Confirmed |
| 25 | 5.1 | API/code compatibility | Confirmed |
| 26 | 5.1 | API/code compatibility | Confirmed |
| 27 | 5.1 | UI/output behavior | Confirmed |
| 28 | 5.1 | Data/schema migration | Confirmed |
| 29 | 5.1 | UI/output behavior | Confirmed |
| 30 | 5.1 | No targeted check stated | Confirmed |
| 31 | 5.2 | UI/output behavior | Confirmed |
| 32 | 5.2 | API/code compatibility | Confirmed |
| 33 | 5.2 | Data/schema migration | Confirmed |
| 34 | 5.2 | API/code compatibility | Confirmed |
| 35 | 5.2 | API/code compatibility | Confirmed |
| 36 | 5.2 | UI/output behavior | Confirmed |
| 37 | 5.2 | API/code compatibility | Confirmed |
| 38 | 5.2 | UI/output behavior | Confirmed |
| 39 | 5.2 | Data/schema migration | Confirmed |
| 40 | 5.2 | API/code compatibility | Confirmed |
| 41 | 6.0 | Configuration/deployment | Confirmed |
| 42 | 6.0 | API/code compatibility | Confirmed |
| 43 | 6.0 | Data/schema migration | Confirmed |
| 44 | 6.0 | Data/schema migration | Confirmed |
| 45 | 6.0 | UNCLEAR | Confirmed |
| 46 | 6.0 | Data/schema migration | Confirmed |
| 47 | 6.0 | Data/schema migration | Confirmed |
| 48 | 6.0 | API/code compatibility | Confirmed |
| 49 | 6.0 | Configuration/deployment | Confirmed |
| 50 | 6.0 | API/code compatibility | Confirmed |

## Full review

### 01. Django 4.2 — `dj-f824bf3a3944f413`

> The new isempty lookup and IsEmpty() expression allow filtering empty geometries on PostGIS.

**Confirmed label:** Data/schema migration

**Why:** The PostGIS geometry lookup changes database filtering behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L178-L180)

**Kavya's decision:** Confirmed as shown above.

### 02. Django 4.2 — `dj-6bae94dcaebcd2a9`

> django.contrib.auth.hashers.SHA1PasswordHasher, django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher, and django.contrib.auth.hashers.UnsaltedMD5PasswordHasher are deprecated.

**Confirmed label:** API/code compatibility

**Why:** Code using the named password hasher classes needs review before their removal.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L584-L586)

**Kavya's decision:** Confirmed as shown above.

### 03. Django 4.2 — `dj-c858d71194dc6344`

> From Django 5.1+ string literals will be implicitly interpreted as JSON string literals.

**Confirmed label:** Data/schema migration

**Why:** The interpretation of string literals in JSONField queries changes.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L558-L559)

**Kavya's decision:** Confirmed as shown above.

### 04. Django 4.2 — `dj-969d0b9a076e69f4`

> django.core.mail.backends.smtp.EmailBackend now verifies a hostname and certificates. If you need the previous behavior that is less restrictive and not recommended, subclass EmailBackend and override the ssl_context property.

**Confirmed label:** Configuration/deployment

**Why:** SMTP TLS certificate and hostname verification affects mail deployment settings.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L477-L481)

**Kavya's decision:** Confirmed as shown above.

### 05. Django 4.2 — `dj-54153a76463b3b37`

> The old DEFAULT_FILE_STORAGE and STATICFILES_STORAGE settings are deprecated as of this release.

**Confirmed label:** Configuration/deployment

**Why:** Project storage settings are deprecated and need configuration review.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L113-L114)

**Kavya's decision:** Confirmed as shown above.

### 06. Django 4.2 — `dj-1c4f005aef07ce59`

> Running the makemigrations command will generate a migration containing a django.db.migrations.operations.RenameIndex operation which will rename the existing index. Next, consider squashing migrations to remove index_together from historical migrations.

**Confirmed label:** Data/schema migration

**Why:** makemigrations generates an index-rename database migration.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L513-L516)

**Kavya's decision:** Confirmed as shown above.

### 07. Django 4.2 — `dj-e4f5d721aac5caaa`

> QuerySet now extensively supports filtering against window-functions with the exception of disjunctive filter lookups against window functions when performing aggregation.

**Confirmed label:** Data/schema migration

**Why:** QuerySet filtering against window functions changes ORM query behavior.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L275-L277)

**Kavya's decision:** Confirmed as shown above.

### 08. Django 4.2 — `dj-35efb274752736bb`

> ModelAdmin.list_editable now uses atomic transactions when making edits.

**Confirmed label:** Data/schema migration

**Why:** Admin list edits now use database transactions.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L141-L142)

**Kavya's decision:** Confirmed as shown above.

### 09. Django 4.2 — `dj-3ae3f8d8fbcae259`

> The new django.contrib.auth.forms.BaseUserCreationForm is now the recommended base class for customizing the user creation form.

**Confirmed label:** API/code compatibility

**Why:** Custom user-creation form code can use the new base class.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L155-L156)

**Kavya's decision:** Confirmed as shown above.

### 10. Django 4.2 — `dj-a372fb10c1a5ba9f`

> Be aware that psycopg 3 introduces some breaking changes over psycopg2. As a consequence, you may need to make some changes to account for differences from psycopg2.

**Confirmed label:** UNCLEAR

**Why:** The note says psycopg 3 may need changes but does not identify whether code or environment is the first check.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/4.2.txt#L46-L48)

**Kavya's decision:** Confirmed as shown above.

### 11. Django 5.0 — `dj-1d1cc12dd80ecbde`

> The usage of QuerySet.iterator() on a queryset that prefetches related objects without providing the chunk_size argument is no longer allowed.

**Confirmed label:** API/code compatibility

**Why:** Code calling QuerySet.iterator with prefetching must pass chunk_size.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L729-L730)

**Kavya's decision:** Confirmed as shown above.

### 12. Django 5.0 — `dj-8ce56f7bc0e1e176`

> The new asynchronous functions are now provided, using an a prefix: django.contrib.auth.aauthenticate, django.contrib.auth.aget_user, django.contrib.auth.alogin, django.contrib.auth.alogout, and django.contrib.auth.aupdate_session_auth_hash.

**Confirmed label:** API/code compatibility

**Why:** Authentication code can call the new asynchronous functions.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L238-L242)

**Kavya's decision:** Confirmed as shown above.

### 13. Django 5.0 — `dj-2a2504481cb55e2f`

> QuerySet.bulk_create and QuerySet.abulk_create methods now set the primary key on each model instance when the update_conflicts parameter is enabled (if the database supports it).

**Confirmed label:** Data/schema migration

**Why:** bulk_create now sets primary keys on updated model instances.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L380-L382)

**Kavya's decision:** Confirmed as shown above.

### 14. Django 5.0 — `dj-30284ac0af51693d`

> In order to improve accessibility, the admin's main content area and header content area are now rendered in a <main> and <header> tag instead of <div>.

**Confirmed label:** UI/output behavior

**Why:** The admin page renders different HTML landmark elements.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L559-L561)

**Kavya's decision:** Confirmed as shown above.

### 15. Django 5.0 — `dj-4e8981b2affad1f3`

> The get_joining_columns() method of ForeignObject and ForeignObjectRel is deprecated. Starting with Django 6.0, django.db.models.sql.datastructures.Join will no longer fallback to get_joining_columns(). Subclasses should implement get_joining_fields() instead.

**Confirmed label:** API/code compatibility

**Why:** ForeignObject subclasses should implement get_joining_fields instead.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L616-L620)

**Kavya's decision:** Confirmed as shown above.

### 16. Django 5.0 — `dj-06931b2138b789d1`

> django.test.runner.DiscoverRunner now allows showing the duration of the slowest tests using the test --durations option (available on Python 3.12+).

**Confirmed label:** UI/output behavior

**Why:** The test runner can now display durations in command output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L435-L437)

**Kavya's decision:** Confirmed as shown above.

### 17. Django 5.0 — `dj-d2ad21e5e9c9e759`

> Django 5.0 introduces the concept of a field group, and field group templates. This simplifies rendering of the related elements of a Django form field such as its label, widget, help text, and errors.

**Confirmed label:** UI/output behavior

**Why:** Form field groups change the rendered label, widget, help text, and error layout.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L51-L53)

**Kavya's decision:** Confirmed as shown above.

### 18. Django 5.0 — `dj-903892e91fbbdf46`

> Properties in ModelAdmin.list_display now support boolean attribute.

**Confirmed label:** UI/output behavior

**Why:** Boolean properties change what the admin list displays.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L226-L227)

**Kavya's decision:** Confirmed as shown above.

### 19. Django 5.0 — `dj-9b3355212fd7071c`

> The new escapeseq template filter applies escape to each element of a sequence.

**Confirmed label:** UI/output behavior

**Why:** The template filter changes rendered escaping of sequence elements.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L421-L422)

**Kavya's decision:** Confirmed as shown above.

### 20. Django 5.0 — `dj-a7a05b13ba669b83`

> Facet counts are now shown for applied filters in the admin changelist when toggled on via the UI. This behavior can be changed via the new ModelAdmin.show_facets attribute. For more information see facet-filters.

**Confirmed label:** UI/output behavior

**Why:** Facet counts appear in the admin changelist UI.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.0.txt#L43-L46)

**Kavya's decision:** Confirmed as shown above.

### 21. Django 5.1 — `dj-78db149ac73235f6`

> In order to improve accessibility, the admin's changelist filter is now rendered in a <nav> tag instead of a <div>.

**Confirmed label:** UI/output behavior

**Why:** The admin filter now renders as a nav element for accessibility.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L362-L363)

**Kavya's decision:** Confirmed as shown above.

### 22. Django 5.1 — `dj-17b4f11820f27d11`

> The BaseUserManager.make_random_password() method is removed.

**Confirmed label:** API/code compatibility

**Why:** Calls to the removed make_random_password method must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L462-L462)

**Kavya's decision:** Confirmed as shown above.

### 23. Django 5.1 — `dj-1acff56c1773bc8c`

> Overriding existing converters with django.urls.register_converter() is deprecated.

**Confirmed label:** API/code compatibility

**Why:** URL converter registration code can no longer override an existing converter.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L438-L439)

**Kavya's decision:** Confirmed as shown above.

### 24. Django 5.1 — `dj-3e47da618609b0d5`

> To enable this, add "django.contrib.auth.middleware.LoginRequiredMiddleware" to your MIDDLEWARE setting.

**Confirmed label:** Configuration/deployment

**Why:** Enabling the authentication middleware requires changing MIDDLEWARE settings.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L101-L102)

**Kavya's decision:** Confirmed as shown above.

### 25. Django 5.1 — `dj-1c5e24a9cfe0a326`

> The new OGRGeometry.is_3d attribute allows checking if a geometry has a Z coordinate dimension.

**Confirmed label:** API/code compatibility

**Why:** Application code can use the new OGRGeometry.is_3d attribute.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L161-L162)

**Kavya's decision:** Confirmed as shown above.

### 26. Django 5.1 — `dj-79eb1883fab34181`

> In order to enforce test isolation, database connections inside threads are no longer allowed in django.test.SimpleTestCase.

**Confirmed label:** API/code compatibility

**Why:** SimpleTestCase code that opens database connections in threads must change.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L315-L316)

**Kavya's decision:** Confirmed as shown above.

### 27. Django 5.1 — `dj-e49806d270ecd476`

> ReadOnlyPasswordHashWidget now includes a button to reset the user's password, which replaces the link previously embedded in the ReadOnlyPasswordHashField's help text, improving the overall accessibility of the django.contrib.auth.forms.UserChangeForm.

**Confirmed label:** UI/output behavior

**Why:** The password reset control changes from a link to a button in the form UI.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L133-L137)

**Kavya's decision:** Confirmed as shown above.

### 28. Django 5.1 — `dj-6a7e2370f3ed08f8`

> The new exclusion argument of django.db.models.expressions.RowRange and django.db.models.expressions.ValueRange allows excluding rows, groups, and ties from the window frames.

**Confirmed label:** Data/schema migration

**Why:** RowRange and ValueRange change window-frame query semantics.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L258-L261)

**Kavya's decision:** Confirmed as shown above.

### 29. Django 5.1 — `dj-fdc27c605a9d4a70`

> django.utils.text.Truncator used by truncatechars_html and truncatewords_html template filters now uses html.parser.HTMLParser subclasses. This results in a more robust and faster operation, but there may be small differences in the output.

**Confirmed label:** UI/output behavior

**Why:** HTML truncation template filters can produce slightly different output.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L382-L385)

**Kavya's decision:** Confirmed as shown above.

### 30. Django 5.1 — `dj-5626831568da00fe`

> The JavaScript file collapse.js is removed since it is no longer needed in the Django admin site.

**Confirmed label:** No targeted check stated

**Why:** The note only says an admin JavaScript asset is removed because it is no longer needed; it states no downstream behavior to check.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.1.txt#L375-L376)

**Kavya's decision:** Confirmed as shown above.

### 31. Django 5.2 — `dj-a8c1b6f87d962c4f`

> The new field_id argument for django.forms.ErrorList allows an HTML id attribute to be added in the error template. See ErrorList.field_id for details.

**Confirmed label:** UI/output behavior

**Why:** ErrorList can render an HTML id attribute in its error template.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L260-L262)

**Kavya's decision:** Confirmed as shown above.

### 32. Django 5.2 — `dj-5850f125d681b2a5`

> HttpRequest.accepted_types is now sorted by the client's preference, based on the request's Accept header.

**Confirmed label:** API/code compatibility

**Why:** Code reading HttpRequest.accepted_types now receives client-preference order.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L438-L439)

**Kavya's decision:** Confirmed as shown above.

### 33. Django 5.2 — `dj-7741b101ec4e75e1`

> Added support for validation of model constraints which use a django.db.models.GeneratedField.

**Confirmed label:** Data/schema migration

**Why:** GeneratedField constraints change model data validation.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L306-L307)

**Kavya's decision:** Confirmed as shown above.

### 34. Django 5.2 — `dj-4ca20b754cc8ee08`

> GDAL now supports curved geometries CurvePolygon, CompoundCurve, CircularString, MultiSurface, and MultiCurve via the new OGRGeometry.has_curve property, and the OGRGeometry.get_linear_geometry and OGRGeometry.get_curve_geometry methods.

**Confirmed label:** API/code compatibility

**Why:** GIS code can use the new geometry property and conversion methods.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L192-L196)

**Kavya's decision:** Confirmed as shown above.

### 35. Django 5.2 — `dj-7fc7222da0694303`

> The new HttpResponse.text property provides the string representation of HttpResponse.content.

**Confirmed label:** API/code compatibility

**Why:** Code can read the new HttpResponse.text property.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L331-L332)

**Kavya's decision:** Confirmed as shown above.

### 36. Django 5.2 — `dj-6a5cb941514e779d`

> To improve accessibility for screen reader users aria-describedby is used to associate form fields with their error messages. See how form errors are displayed for details.

**Confirmed label:** UI/output behavior

**Why:** Form errors now render an aria-describedby link for screen readers.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L267-L269)

**Kavya's decision:** Confirmed as shown above.

### 37. Django 5.2 — `dj-782bfadf691be97f`

> The attributes UniqueConstraint.violation_error_code and UniqueConstraint.violation_error_message are now always used when provided. Previously, they were ignored if UniqueConstraint.fields was set without a UniqueConstraint.condition.

**Confirmed label:** API/code compatibility

**Why:** ValidationError code and message from UniqueConstraint change for callers.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L441-L444)

**Kavya's decision:** Confirmed as shown above.

### 38. Django 5.2 — `dj-e33b7e94b40f4f42`

> The new django.forms.SearchInput form widget is for entering search queries and renders as <input type="search" ...>.

**Confirmed label:** UI/output behavior

**Why:** SearchInput renders an input type=search element.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L254-L255)

**Kavya's decision:** Confirmed as shown above.

### 39. Django 5.2 — `dj-7fb97a2d908a0908`

> QuerySet.explain now supports the memory and serialize options on PostgreSQL 17+.

**Confirmed label:** Data/schema migration

**Why:** QuerySet.explain changes PostgreSQL query-plan output options.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L317-L318)

**Kavya's decision:** Confirmed as shown above.

### 40. Django 5.2 — `dj-64f742cd2026db8c`

> The new Expression.allows_composite_expressions attribute specifies that the expression allows composite expressions, for example, to support composite primary keys.

**Confirmed label:** API/code compatibility

**Why:** Custom Expression code can set allows_composite_expressions.

[Official source](https://github.com/django/django/blob/47fe39af56ecd0ad73b9c7562511015e96b91b80/docs/releases/5.2.txt#L324-L326)

**Kavya's decision:** Confirmed as shown above.

### 41. Django 6.0 — `dj-890331f0fb995b6f`

> CSP policies can now be enforced or monitored directly using built-in tools: headers are added via the django.middleware.csp.ContentSecurityPolicyMiddleware, nonces are supported through the django.template.context_processors.csp context processor, and policies are configured using the SECURE_CSP and SECURE_CSP_REPORT_ONLY settings.

**Confirmed label:** Configuration/deployment

**Why:** CSP policies, middleware, and settings require security configuration review.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L49-L54)

**Kavya's decision:** Confirmed as shown above.

### 42. Django 6.0 — `dj-f9641451ada49d39`

> django.urls.register_converter() no longer allows overriding existing converters.

**Confirmed label:** API/code compatibility

**Why:** Code registering URL converters must stop overriding existing converters.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L604-L605)

**Kavya's decision:** Confirmed as shown above.

### 43. Django 6.0 — `dj-dd4b42a02b7c9633`

> Using a percent sign in a column alias or annotation is deprecated.

**Confirmed label:** Data/schema migration

**Why:** Column aliases and ORM annotations using percent signs need query review.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L534-L534)

**Kavya's decision:** Confirmed as shown above.

### 44. Django 6.0 — `dj-207fee4ac69b9eaf`

> The new Lexeme expression for full text search provides fine-grained control over search terms. Lexeme objects automatically escape their input and support logical combination operators (&, |, ~), prefix matching, and term weighting.

**Confirmed label:** Data/schema migration

**Why:** Lexeme changes full-text search expression and query behavior.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L211-L215)

**Kavya's decision:** Confirmed as shown above.

### 45. Django 6.0 — `dj-04307ab49df421a8`

> The framework provides task definition, validation, queuing, and result handling. Django guarantees consistent behavior for creating and managing tasks, while the responsibility for running them continues to belong to external worker processes.

**Confirmed label:** UNCLEAR

**Why:** The task framework spans task-definition code and external workers; the note does not establish one first check.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L105-L108)

**Kavya's decision:** Confirmed as shown above.

### 46. Django 6.0 — `dj-51390d1401074e25`

> The new order_by argument for django.db.models.Aggregate allows specifying the ordering of the elements in the result.

**Confirmed label:** Data/schema migration

**Why:** Aggregate order_by changes the ordering of query results.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L283-L284)

**Kavya's decision:** Confirmed as shown above.

### 47. Django 6.0 — `dj-1dc9543670ee5c6f`

> coveredby and isvalid lookups, django.contrib.gis.db.models.Collect aggregation, and django.contrib.gis.db.models.functions.GeoHash and django.contrib.gis.db.models.functions.IsValid database functions are now supported on MariaDB 12.0.1+.

**Confirmed label:** Data/schema migration

**Why:** The new GIS lookups and functions affect MariaDB database queries.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L193-L197)

**Kavya's decision:** Confirmed as shown above.

### 48. Django 6.0 — `dj-9dbfdcdf4cc51eb9`

> Email handling in Django now uses Python's modern email API, introduced in Python 3.6. This API, centered around the email.message.EmailMessage class, offers a cleaner and Unicode-friendly interface for composing and sending emails. It replaces use of Python's older legacy (Compat32) API, which relied on lower-level MIME classes (from email.mime) and required more manual handling of message structure and encoding.

**Confirmed label:** API/code compatibility

**Why:** Email integration code may need review for the modern email API.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L142-L148)

**Kavya's decision:** Confirmed as shown above.

### 49. Django 6.0 — `dj-8333d59629961b52`

> If you haven't dealt with this warning by now, add DEFAULT_AUTO_FIELD = 'django.db.models.AutoField' to your project's settings, or default_auto_field = 'django.db.models.AutoField' to an app's AppConfig, as needed.

**Confirmed label:** Configuration/deployment

**Why:** The note explicitly tells projects to update DEFAULT_AUTO_FIELD configuration.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L452-L455)

**Kavya's decision:** Confirmed as shown above.

### 50. Django 6.0 — `dj-a98cf2e001856ed1`

> As the internal implementations of django.core.mail.EmailMessage and django.core.mail.EmailMultiAlternatives have changed significantly, closely examine any custom subclasses that rely on overriding undocumented, internal underscore methods.

**Confirmed label:** API/code compatibility

**Why:** Custom EmailMessage subclasses overriding internal methods need code review.

[Official source](https://github.com/django/django/blob/85eb963c5297fb285aecf4a90c97141a1b9c5bee/docs/releases/6.0.txt#L424-L427)

**Kavya's decision:** Confirmed as shown above.

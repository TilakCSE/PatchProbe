"""Focused checks for extraction and provenance; no gold labels are invented."""

from __future__ import annotations

import sys
import unittest
from collections import Counter
from dataclasses import replace
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from patchprobe.ingest import (  # noqa: E402
    PILOT_RELEASES,
    clean_rst,
    deduplicate_exact,
    parse_release_notes,
    select_pilot,
)


REVISION = "a" * 40


class IngestTests(unittest.TestCase):
    def test_rst_roles_and_inline_code_are_readable(self) -> None:
        raw = "* :meth:`User.check() <django.auth.User.check>` now returns ``False``."
        self.assertEqual(clean_rst(raw), "User.check() now returns False.")
        self.assertEqual(
            clean_rst("* :meth:`.File.open` passes ``*args`` and ``**kwargs`` to :func:`python:open`."),
            "File.open passes *args and **kwargs to open.",
        )
        self.assertNotIn("``", clean_rst("* Use the format ``:role:`link text <link>``` for custom links."))

    def test_blocks_skip_titles_directives_and_literal_code(self) -> None:
        source = """========================
Django 5.2 release notes
========================

Welcome to Django 5.2!

Bugfixes
========

* Fixed a regression in :class:`Example` that changed the output of a view.

* Fixed a bug in the ORM query compiler that returned incorrect rows for joins.

  The problem affected applications with multiple related tables.

.. code-block:: python

    print('ignore this code')

This paragraph describes the change to a public API used by integration code::

    print('ignore literal code')

Backwards incompatible changes
==============================

* The configured middleware ordering now changes the response for requests.
"""
        entries = parse_release_notes(source, "5.2", REVISION)
        self.assertEqual(len(entries), 4)
        self.assertEqual(entries[0].section_path, "Bugfixes")
        self.assertIn("multiple related tables", entries[1].text)
        self.assertIn("#L12-L14", entries[1].source_url)
        self.assertNotIn("print", " ".join(entry.text for entry in entries))
        self.assertEqual(entries[-1].section_path, "Backwards incompatible changes")
        self.assertTrue(all(entry.source_revision == REVISION for entry in entries))

    def test_exact_dedup_and_deterministic_unlabeled_pilot(self) -> None:
        source = """Django 5.2 release notes
========================

Bugfixes
========

* Fixed a regression in the database adapter that returned incorrect values.

* Fixed a regression in the database adapter that returned incorrect values.

* Corrected the output of a rendering function for unusual inputs in forms.
"""
        entries = parse_release_notes(source, "5.2", REVISION)
        kept, removed = deduplicate_exact(entries)
        self.assertEqual(removed, 1)
        self.assertEqual(len(kept), 2)
        self.assertEqual(set(kept[0].row()), {
            "entry_id", "release", "source_url", "source_revision",
            "section_path", "raw_text", "text",
        })
        self.assertNotIn("label", kept[0].row())

    def test_pilot_balances_feature_releases_and_distinct_sections(self) -> None:
        base = parse_release_notes(
            "Django 5.2 release notes\n========================\n\nBugfixes\n========\n\n"
            "* Fixed a regression in the database adapter that returned incorrect values.\n",
            "5.2",
            REVISION,
        )[0]
        candidates = [
            replace(
                base,
                entry_id=f"{release}-{index}",
                release=release,
                section_path=f"Family {index % 3} > Section {index}",
            )
            for release in PILOT_RELEASES
            for index in range(12)
        ]
        pilot = select_pilot(candidates, 50)
        self.assertEqual(Counter(row.release for row in pilot), {release: 10 for release in PILOT_RELEASES})
        for release in PILOT_RELEASES:
            self.assertEqual(len({row.section_path for row in pilot if row.release == release}), 10)
        self.assertEqual([row.entry_id for row in pilot], [row.entry_id for row in select_pilot(list(reversed(candidates)), 50)])
        self.assertEqual([row.release for row in pilot[:5]], list(PILOT_RELEASES))


if __name__ == "__main__":
    unittest.main()

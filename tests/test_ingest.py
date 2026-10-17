"""Focused checks for extraction and provenance; no gold labels are invented."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from patchprobe.ingest import (  # noqa: E402
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
        self.assertEqual(select_pilot(kept, 2), select_pilot(kept, 2))
        self.assertEqual(set(kept[0].row()), {
            "entry_id", "release", "source_url", "source_revision",
            "section_path", "raw_text", "text",
        })
        self.assertNotIn("label", kept[0].row())


if __name__ == "__main__":
    unittest.main()

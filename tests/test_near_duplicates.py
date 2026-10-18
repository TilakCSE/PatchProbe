"""Check that the leakage audit flags close cross-release notes without auto-exclusion."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_near_duplicates.py"
SPEC = importlib.util.spec_from_file_location("audit_near_duplicates", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class NearDuplicateAuditTests(unittest.TestCase):
    def test_cross_release_similarity_and_same_release_exclusion(self) -> None:
        rows = [
            {"entry_id": "a", "release": "5.0", "text": "The widget.render method is deprecated and should be replaced."},
            {"entry_id": "b", "release": "6.0", "text": "The widget.render method is removed and should be replaced."},
            {"entry_id": "c", "release": "5.0", "text": "The widget.render method is deprecated and should be replaced."},
            {"entry_id": "d", "release": "6.0", "text": "The database migration now requires a new column."},
        ]
        pairs = MODULE.find_pairs(rows, threshold=0.70)
        self.assertTrue(any({pair["left_id"], pair["right_id"]} == {"a", "b"} for pair in pairs))
        self.assertFalse(any({pair["left_id"], pair["right_id"]} == {"a", "c"} for pair in pairs))
        self.assertFalse(any({pair["left_id"], pair["right_id"]} == {"a", "d"} for pair in pairs))

    def test_invalid_threshold_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "threshold"):
            MODULE.find_pairs([], threshold=0)


if __name__ == "__main__":
    unittest.main()

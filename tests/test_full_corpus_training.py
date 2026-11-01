"""Focused checks for the declared near-duplicate exclusion policy."""

from patchprobe.model import Example

from scripts.train_full_corpus import filter_cross_split_pairs, split_chronological


def row(entry_id: str, release: str) -> Example:
    return Example(entry_id, release, "https://example.org", "A release note.", "API/code compatibility")


def pair(left: str, right: str) -> dict[str, str]:
    return {"left_id": left, "right_id": right}


def test_cross_split_policy_preserves_train_and_dev_before_test():
    splits = {
        "train": [row("train", "1")],
        "dev": [row("dev", "2")],
        "test": [row("test", "3"), row("clean", "3")],
    }
    kept, excluded = filter_cross_split_pairs(
        splits, [pair("train", "dev"), pair("dev", "test")]
    )
    assert [r.entry_id for r in kept["train"]] == ["train"]
    assert kept["dev"] == []
    assert [r.entry_id for r in kept["test"]] == ["clean"]
    assert excluded == {
        "dev": "cross_split_near_duplicate",
        "test": "cross_split_near_duplicate",
    }


def test_within_split_and_unlabeled_pairs_do_not_remove_rows():
    splits = {
        "train": [row("one", "1")],
        "dev": [row("two", "2")],
        "test": [row("three", "3"), row("four", "3")],
    }
    kept, excluded = filter_cross_split_pairs(
        splits, [pair("three", "four"), pair("unlabeled", "one")]
    )
    assert excluded == {}
    assert kept == splits


def test_chronological_split_has_disjoint_release_families():
    examples = [
        row("a", "4.2"), row("b", "5.0"), row("c", "5.1"),
        row("d", "5.2.8"), row("e", "6.0"), row("f", "6.0.1"),
    ]
    splits = split_chronological(examples)
    assert [r.entry_id for r in splits["train"]] == ["a", "b", "c"]
    assert [r.entry_id for r in splits["dev"]] == ["d"]
    assert [r.entry_id for r in splits["test"]] == ["e", "f"]

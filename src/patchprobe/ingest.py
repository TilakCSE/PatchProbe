"""Reproducible extraction of candidate entries from Django release-note RST.

The extractor deliberately produces *unlabeled* examples.  It does not infer
regression-check labels from headings or wording.
"""

from __future__ import annotations

import hashlib
import re
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path


# Annotated tags 5.2.8 and 6.0.1 resolve to these immutable *commit* IDs.
SOURCE_GROUPS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "5.2.8",
        "47fe39af56ecd0ad73b9c7562511015e96b91b80",
        ("4.2", "5.0", "5.1", "5.2", "5.2.1", "5.2.2", "5.2.3", "5.2.4", "5.2.5", "5.2.6", "5.2.7", "5.2.8"),
    ),
    (
        "6.0.1",
        "85eb963c5297fb285aecf4a90c97141a1b9c5bee",
        ("6.0", "6.0.1"),
    ),
)
PILOT_RELEASES = ("4.2", "5.0", "5.1", "5.2", "6.0")

FIELDNAMES = (
    "entry_id",
    "release",
    "source_url",
    "source_revision",
    "section_path",
    "raw_text",
    "text",
)

_HEADING_RANK = {"=": 0, "-": 1, "~": 2, "^": 3, '"': 4, "'": 5}
_BULLET = re.compile(r"^\s*(?:[*+-]|#\.|\d+\.)\s+")
_ROLE = re.compile(r":(?:[\w.]+:)?[\w.]+:`([^`]+)`")
_LINK = re.compile(r"`([^`<>]+)\s*<[^`<>]+>`_{0,2}")
_SPACE = re.compile(r"\s+")


@dataclass(frozen=True)
class Entry:
    entry_id: str
    release: str
    source_url: str
    source_revision: str
    section_path: str
    raw_text: str
    text: str

    def row(self) -> dict[str, str]:
        return asdict(self)


def raw_url(revision: str, release: str) -> str:
    return f"https://raw.githubusercontent.com/django/django/{revision}/docs/releases/{release}.txt"


def source_url(revision: str, release: str, start_line: int, end_line: int) -> str:
    return (
        f"https://github.com/django/django/blob/{revision}/docs/releases/"
        f"{release}.txt#L{start_line}-L{end_line}"
    )


def fetch_release(revision: str, release: str, cache_root: Path, offline: bool = False) -> str:
    """Read pinned upstream source, caching exact bytes outside version control."""
    cache_path = cache_root / revision / f"{release}.txt"
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8")
    if offline:
        raise FileNotFoundError(f"Offline source missing: {cache_path}")

    request = urllib.request.Request(
        raw_url(revision, release),
        headers={"User-Agent": "PatchProbe-educational-ingest/0.1"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not fetch Django {release} at {revision}: {exc}") from exc
    text = payload.decode("utf-8")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_bytes(payload)
    return text


def clean_rst(raw: str) -> str:
    """Remove common inline RST markup without losing code identifiers."""
    text = _BULLET.sub("", raw.strip())
    text = _SPACE.sub(" ", text)
    code_spans: list[str] = []

    def protect_code(match: re.Match[str]) -> str:
        code_spans.append(match.group(1))
        return f"\ue000{len(code_spans) - 1}\ue001"

    text = re.sub(r"``([^`]+)``", protect_code, text)

    def replace_role(match: re.Match[str]) -> str:
        content = match.group(1)
        display = content.split(" <", 1)[0].lstrip("~.")
        return display.removeprefix("python:")

    text = _ROLE.sub(replace_role, text)
    text = _LINK.sub(r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`_{1,2}", r"\1", text)
    text = re.sub(r"\ue000(\d+)\ue001", lambda match: code_spans[int(match.group(1))], text)
    text = text.replace("``", "")
    return _SPACE.sub(" ", text).strip()


def _heading_at(lines: list[str], index: int) -> tuple[str, int] | None:
    if index + 1 >= len(lines):
        return None
    title, rule = lines[index].strip(), lines[index + 1].strip()
    if not title or not rule or len(rule) < max(3, len(title)):
        return None
    char = rule[0]
    if char not in _HEADING_RANK or any(symbol != char for symbol in rule):
        return None
    return title, _HEADING_RANK[char]


def _eligible(text: str, section_path: str) -> bool:
    if not section_path or len(text) < 45:
        return False
    if text.startswith((".. ", ":", "$ ")):
        return False
    first = section_path.split(" > ", 1)[0].lower()
    if first in {"references", "contributors", "acknowledgments"}:
        return False
    if re.match(r"^(?:see |for more |for details |this section |the following |read the )", text, re.I):
        return False
    return True


def parse_release_notes(source: str, release: str, revision: str) -> list[Entry]:
    """Extract substantive bullets and prose blocks, retaining line-level provenance.

    This is a conservative, deterministic RST block parser.  It omits directive
    bodies and literal code blocks.  The output still needs human review before
    it can become a labeled training set.
    """
    lines = source.splitlines()
    entries: list[Entry] = []
    headings: list[tuple[int, str]] = []
    block: list[str] = []
    block_start = 0
    block_end = 0
    block_section = ""
    skip_directive = False
    skip_literal = False

    def flush() -> None:
        nonlocal block, block_start, block_end, block_section, skip_literal
        if not block:
            return
        raw = "\n".join(block).strip()
        text = clean_rst(raw)
        if _eligible(text, block_section):
            digest = hashlib.sha256(
                f"{revision}\0{release}\0{block_start}\0{raw}".encode("utf-8")
            ).hexdigest()[:16]
            entries.append(
                Entry(
                    entry_id=f"dj-{digest}",
                    release=release,
                    source_url=source_url(revision, release, block_start, block_end),
                    source_revision=revision,
                    section_path=block_section,
                    raw_text=raw,
                    text=text,
                )
            )
        skip_literal = raw.endswith("::")
        block = []

    index = 0
    while index < len(lines):
        heading = _heading_at(lines, index)
        if heading:
            flush()
            title, rank = heading
            if not re.fullmatch(r"Django \d+(?:\.\d+)* release notes", title):
                while headings and headings[-1][0] >= rank:
                    headings.pop()
                headings.append((rank, title))
            skip_directive = False
            skip_literal = False
            index += 2
            continue

        line = lines[index]
        stripped = line.strip()
        if skip_directive or skip_literal:
            if not stripped or line[:1].isspace():
                index += 1
                continue
            skip_directive = skip_literal = False

        if line.startswith(".. "):
            flush()
            skip_directive = True
            index += 1
            continue
        if not stripped:
            # A paragraph indented under a list item belongs to that item.
            # A nested list item starts a new candidate instead.
            if block and _BULLET.match(block[0]) and not block[-1].rstrip().endswith("::"):
                lookahead = index + 1
                while lookahead < len(lines) and not lines[lookahead].strip():
                    lookahead += 1
                if (
                    lookahead < len(lines)
                    and lines[lookahead][:1].isspace()
                    and not _BULLET.match(lines[lookahead])
                    and not lines[lookahead].lstrip().startswith(".. ")
                ):
                    block.append("")
                    index += 1
                    continue
            flush()
            index += 1
            continue
        if line.startswith("    ") and not block:
            index += 1
            continue

        bullet = bool(_BULLET.match(line))
        if block and bullet:
            flush()
        elif block and _BULLET.match(block[0]) and not line[:1].isspace():
            flush()
        if not block:
            block_start = index + 1
            block_section = " > ".join(title for _, title in headings)
        block.append(line)
        block_end = index + 1
        index += 1
    flush()
    return entries


def deduplicate_exact(entries: list[Entry]) -> tuple[list[Entry], int]:
    """Keep first occurrence of identical model text across source releases."""
    seen: set[str] = set()
    kept: list[Entry] = []
    for entry in entries:
        key = _SPACE.sub(" ", entry.text).casefold()
        if key in seen:
            continue
        seen.add(key)
        kept.append(entry)
    return kept, len(entries) - len(kept)


def select_pilot(entries: list[Entry], size: int = 50) -> list[Entry]:
    """Select equal feature-release coverage, spreading sections and families."""
    if size < 0 or size % len(PILOT_RELEASES):
        raise ValueError(f"size must be a nonnegative multiple of {len(PILOT_RELEASES)}")
    quota = size // len(PILOT_RELEASES)
    by_release: dict[str, list[Entry]] = {release: [] for release in PILOT_RELEASES}
    for entry in entries:
        # Bullets usually state a complete change without relying on the
        # preceding paragraph.  Prose remains in the full candidate corpus.
        if entry.release in by_release and _BULLET.match(entry.raw_text) and 70 <= len(entry.text) <= 700:
            by_release[entry.release].append(entry)

    selected: dict[str, list[Entry]] = {}
    for release, rows in by_release.items():
        if len(rows) < quota:
            raise ValueError(f"Only {len(rows)} eligible {release} entries; requested {quota}")
        remaining = rows.copy()
        chosen: list[Entry] = []
        used_paths: set[str] = set()
        family_counts: dict[str, int] = {}
        while len(chosen) < quota:
            fresh = [row for row in remaining if row.section_path not in used_paths]
            pool = fresh or remaining

            def ranking(row: Entry) -> tuple[int, str]:
                family = row.section_path.split(" > ", 1)[0]
                stable = hashlib.sha256(f"pilot-v2:{release}:{row.entry_id}".encode()).hexdigest()
                return family_counts.get(family, 0), stable

            winner = min(pool, key=ranking)
            chosen.append(winner)
            remaining.remove(winner)
            used_paths.add(winner.section_path)
            family = winner.section_path.split(" > ", 1)[0]
            family_counts[family] = family_counts.get(family, 0) + 1
        selected[release] = chosen

    # Interleave releases so the annotator sees varied notes from the start.
    return [selected[release][index] for index in range(quota) for release in PILOT_RELEASES]

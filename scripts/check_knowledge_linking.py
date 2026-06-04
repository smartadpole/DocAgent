#!/usr/bin/env python3
"""Check minimal knowledge graph links for concepts and articles."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


LINK_RE = re.compile(r"\[\[([^\]|#]+)")
CHECK_DIRS = ("concepts", "articles")
ENTRY_FILES = {
    "concepts": {"INDEX.md", "README.md", "concepts/README.md"},
    "articles": {"INDEX.md", "README.md", "articles/README.md"},
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_markdown(repo: Path) -> list[Path]:
    return [
        path
        for path in repo.rglob("*.md")
        if ".git" not in path.parts and not any(part.endswith("_files") for part in path.parts)
    ]


def aliases_for(path: Path, repo: Path) -> set[str]:
    rel = path.relative_to(repo).as_posix()
    without_suffix = rel.removesuffix(".md")
    aliases = {rel, without_suffix}
    if path.name != "README.md":
        aliases.add(path.stem)
    return aliases


def links_in(text: str) -> set[str]:
    return {match.strip() for match in LINK_RE.findall(text)}


def build_link_index(repo: Path) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    all_md = iter_markdown(repo)
    alias_to_path: dict[str, Path] = {}
    for path in all_md:
        for alias in aliases_for(path, repo):
            alias_to_path.setdefault(alias, path)

    outgoing: dict[str, set[str]] = {}
    incoming: dict[str, set[str]] = defaultdict(set)
    for path in all_md:
        rel = path.relative_to(repo).as_posix()
        resolved: set[str] = set()
        for target in links_in(read_text(path)):
            target_path = alias_to_path.get(target)
            if target_path is None:
                continue
            target_rel = target_path.relative_to(repo).as_posix()
            resolved.add(target_rel)
            incoming[target_rel].add(rel)
        outgoing[rel] = resolved
    return outgoing, incoming


def is_checked_page(path: Path, repo: Path) -> bool:
    rel = path.relative_to(repo).as_posix()
    if path.name == "README.md":
        return False
    return any(rel.startswith(f"{directory}/") for directory in CHECK_DIRS)


def source_kind(rel: str) -> str | None:
    for directory in CHECK_DIRS:
        if rel.startswith(f"{directory}/"):
            return directory
    return None


def check_page(
    rel: str,
    outgoing: dict[str, set[str]],
    incoming: dict[str, set[str]],
    errors: list[str],
) -> None:
    kind = source_kind(rel)
    if kind is None:
        return

    own_outgoing = {target for target in outgoing.get(rel, set()) if target != rel}
    non_log_incoming = {source for source in incoming.get(rel, set()) if source != rel and source != "log.md"}
    entry_incoming = non_log_incoming & ENTRY_FILES[kind]
    knowledge_incoming = {
        source
        for source in non_log_incoming
        if source.startswith("concepts/")
        or source.startswith("articles/")
        or source.startswith("governance/")
        or source.startswith("skills/")
        or source.startswith("templates/")
    }

    if not own_outgoing:
        errors.append(f"{rel}: missing outgoing wikilink to existing knowledge page")
    if not non_log_incoming:
        errors.append(f"{rel}: missing non-log backlink; log.md cannot be the only discovery path")
    if not (entry_incoming or knowledge_incoming):
        entries = ", ".join(sorted(ENTRY_FILES[kind]))
        errors.append(f"{rel}: missing entry or knowledge backlink from {entries} or a related knowledge page")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    outgoing, incoming = build_link_index(repo)
    errors: list[str] = []

    for path in iter_markdown(repo):
        if not is_checked_page(path, repo):
            continue
        rel = path.relative_to(repo).as_posix()
        check_page(rel, outgoing, incoming, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OK: knowledge linking graph has entry, backlink, and outgoing-link coverage")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

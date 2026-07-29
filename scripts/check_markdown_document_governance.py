#!/usr/bin/env python3
"""Check wiki Markdown profile wiring and deterministic reader-table hazards."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PAGE_TABLE_HEADER_RE = re.compile(r"^\|\s*页面\s*\|")
PAGE_TABLE_SEPARATOR_RE = re.compile(r"^\|\s*:?-{3,}:?\s*\|")
PAGE_TABLE_LINK_CELL_RE = re.compile(
    r"^\|\s*\[\[([^\]|#\\\n]+)(?:#[^\]\\|\n]+)?(?:\\\|([^\]\n]+))?\]\]\s*\|"
)
PAGE_TABLE_UNESCAPED_ALIAS_RE = re.compile(
    r"^\|\s*\[\[([^\]|#\\\n]+)(?:#[^\]|\n]+)?\|([^\]\n]+)\]\]\s*\|"
)
SCAN_EXCLUDED_DIRS = {".git", ".obsidian", "archive", "assets", "raw", "views"}

REQUIRED_FILES = (
    "governance/markdown-document-governance-profile.v1.md",
    "governance/knowledge-linking-rules.md",
    "governance/instruction-adherence.md",
    "AGENTS.md",
    "INDEX.md",
    "scripts/check_all.py",
)

PROFILE_TERMS = (
    "profile_id:",
    "dialect: obsidian-vault",
    "primary_renderer: obsidian",
    "internal_link_style: wikilink",
    "generated_paths:",
    "validation_commands:",
    "markdown-document-governance",
)


def read(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required Markdown profile file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def iter_reader_markdown(repo: Path) -> list[Path]:
    return [
        path
        for path in repo.rglob("*.md")
        if not any(part in SCAN_EXCLUDED_DIRS for part in path.relative_to(repo).parts)
    ]


def check_page_table_links(rel: str, text: str, errors: list[str]) -> None:
    in_page_table = False
    for number, line in enumerate(text.splitlines(), start=1):
        if PAGE_TABLE_HEADER_RE.match(line):
            in_page_table = True
            continue
        if not in_page_table:
            continue
        if not line.startswith("|"):
            in_page_table = False
            continue
        if PAGE_TABLE_SEPARATOR_RE.match(line):
            continue
        malformed = PAGE_TABLE_UNESCAPED_ALIAS_RE.match(line)
        if malformed and "/" in malformed.group(1):
            target = malformed.group(1).strip()
            errors.append(
                f"{rel}:{number}: unescaped wikilink alias separator for [[{target}]]; "
                f"write [[{target}\\|页面标题]]"
            )
            continue
        match = PAGE_TABLE_LINK_CELL_RE.match(line)
        if not match:
            continue
        target = match.group(1).strip()
        alias = (match.group(2) or "").strip()
        if "/" in target and (not alias or alias == target):
            errors.append(
                f"{rel}:{number}: reader-facing `页面` table exposes qualified path "
                f"[[{target}]]; add a concise semantic alias"
            )


def run_fixtures(errors: list[str]) -> None:
    unescaped: list[str] = []
    check_page_table_links(
        "fixture-unescaped.md",
        "| 页面 | 职责 |\n| --- | --- |\n| [[projects/design/README|设计方案]] | owner |\n",
        unescaped,
    )
    if not unescaped:
        errors.append("fixture: unescaped table alias was not rejected")

    long_path: list[str] = []
    check_page_table_links(
        "fixture-long-path.md",
        "| 页面 | 职责 |\n| --- | --- |\n| [[projects/design/README]] | owner |\n",
        long_path,
    )
    if not long_path:
        errors.append("fixture: qualified path without alias was not rejected")

    valid: list[str] = []
    check_page_table_links(
        "fixture-valid.md",
        "| 页面 | 职责 |\n| --- | --- |\n| [[projects/design/README\\|设计方案]] | owner |\n",
        valid,
    )
    if valid:
        errors.append(f"fixture: valid escaped alias was rejected: {valid[0]}")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    texts = {rel: read(repo, rel, errors) for rel in REQUIRED_FILES}
    profile = texts.get("governance/markdown-document-governance-profile.v1.md", "")
    for term in PROFILE_TERMS:
        if profile and term not in profile:
            errors.append(
                "governance/markdown-document-governance-profile.v1.md: "
                f"missing profile term {term!r}"
            )
    if texts.get("scripts/check_all.py") and "markdown-document-governance" not in texts["scripts/check_all.py"]:
        errors.append("scripts/check_all.py: missing markdown-document-governance check")

    run_fixtures(errors)
    for path in iter_reader_markdown(repo):
        check_page_table_links(
            path.relative_to(repo).as_posix(),
            path.read_text(encoding="utf-8"),
            errors,
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} Markdown document-governance issue(s)", file=sys.stderr)
        return 1
    print("OK: wiki Markdown profile wiring and reader-table regression fixtures checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

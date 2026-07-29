#!/usr/bin/env python3
"""Check knowledge-linking skill wiring."""

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
    "skills/knowledge-linking/SKILL.md",
    "skills/knowledge-linking/TRANSFER.md",
    "governance/knowledge-linking-rules.md",
    "skills/README.md",
    "INDEX.md",
    "governance/response-mode-routing.md",
    "scripts/check_all.py",
)

SKILL_TERMS = (
    "分层落位",
    "关系画像",
    "主入口",
    "上位",
    "邻接",
    "反向回链",
    "log",
    "sensor",
    "knowledge-linking",
)

TRANSFER_TERMS = (
    "## 能力目标",
    "## 可以吸收",
    "## 只能抽象吸收",
    "## 禁止复制",
    "## 目标工程结构自检",
    "## 验证要求",
)

ROUTING_TERMS = (
    "knowledge-linking",
    "知识关联",
)


def iter_reader_markdown(repo: Path) -> list[Path]:
    return [
        path
        for path in repo.rglob("*.md")
        if not any(part in SCAN_EXCLUDED_DIRS for part in path.relative_to(repo).parts)
    ]


def check_readable_page_table_links_for_text(
    rel: str,
    text: str,
    errors: list[str],
) -> None:
    """Require semantic labels for qualified paths in reader-facing page tables."""
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
                f"{rel}:{number}: reader-facing `页面` table uses an unescaped wikilink alias "
                f"separator for [[{target}]]; write [[{target}\\|页面标题]] so Markdown does not split the cell"
            )
            continue
        match = PAGE_TABLE_LINK_CELL_RE.match(line)
        if not match:
            continue
        target = match.group(1).strip()
        alias = (match.group(2) or "").strip()
        if "/" not in target or (alias and alias != target):
            continue
        errors.append(
            f"{rel}:{number}: reader-facing `页面` table exposes qualified path "
            f"[[{target}]]; add a concise semantic alias such as [[{target}\\|页面标题]]"
        )


def check_readable_page_table_links(repo: Path, errors: list[str]) -> None:
    for path in iter_reader_markdown(repo):
        rel = path.relative_to(repo).as_posix()
        check_readable_page_table_links_for_text(
            rel,
            path.read_text(encoding="utf-8"),
            errors,
        )


def read(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required knowledge-linking file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing knowledge-linking term {term!r}")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        read(repo, rel, errors)

    skill = read(repo, "skills/knowledge-linking/SKILL.md", errors)
    transfer = read(repo, "skills/knowledge-linking/TRANSFER.md", errors)
    governance = read(repo, "governance/knowledge-linking-rules.md", errors)
    routing = read(repo, "governance/response-mode-routing.md", errors)
    readme = read(repo, "skills/README.md", errors)
    index = read(repo, "INDEX.md", errors)
    check_all = read(repo, "scripts/check_all.py", errors)

    if skill:
        require_terms("skills/knowledge-linking/SKILL.md", skill, SKILL_TERMS, errors)
    if transfer:
        require_terms("skills/knowledge-linking/TRANSFER.md", transfer, TRANSFER_TERMS, errors)
    if governance:
        require_terms("governance/knowledge-linking-rules.md", governance, ("knowledge-linking", "有效链接", "单一信息源", "关系画像", "禁止项"), errors)
    if routing:
        require_terms("governance/response-mode-routing.md", routing, ROUTING_TERMS, errors)
    for rel, text in (("skills/README.md", readme), ("INDEX.md", index)):
        if text and "[[skills/knowledge-linking/SKILL]]" not in text:
            errors.append(f"{rel}: missing knowledge-linking entry")
    if check_all and "knowledge-linking" not in check_all:
        errors.append("scripts/check_all.py: missing knowledge-linking check")
    check_readable_page_table_links(repo, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} knowledge-linking issue(s)", file=sys.stderr)
        return 1

    print("OK: knowledge-linking wiring and readable page-table link labels checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

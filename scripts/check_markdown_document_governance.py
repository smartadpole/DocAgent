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
TABLE_UNESCAPED_ALIAS_RE = re.compile(
    r"\[\[([^\]|#\\\n]+)(?:#[^\]|\n]+)?\|([^\]\n]+)\]\]"
)
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"`+[^`\n]*`+")
PREFIX_WIKILINK_RE = re.compile(r"(?<![\w`])([A-Za-z][A-Za-z0-9_-]*)/\[\[")
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
    "所有读者正文表格",
    "路径前缀粘连",
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


def iter_reader_lines(text: str) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    in_frontmatter = False
    fence_char = ""
    for number, line in enumerate(text.splitlines(), start=1):
        if number == 1 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
            continue
        fence = FENCE_RE.match(line)
        if fence:
            marker_char = fence.group(1)[0]
            if not fence_char:
                fence_char = marker_char
            elif marker_char == fence_char:
                fence_char = ""
            continue
        if fence_char:
            continue
        lines.append((number, INLINE_CODE_RE.sub("", line)))
    return lines


def check_render_hazards(rel: str, text: str, errors: list[str]) -> None:
    in_page_table = False
    for number, line in iter_reader_lines(text):
        stripped = line.lstrip()
        in_table_row = stripped.startswith("|")
        if in_table_row:
            for malformed in TABLE_UNESCAPED_ALIAS_RE.finditer(line):
                target = malformed.group(1).strip()
                alias = malformed.group(2).strip()
                errors.append(
                    f"{rel}:{number}: Markdown table uses an unescaped wikilink alias "
                    f"separator in [[{target}|{alias}]]; write [[{target}\\|{alias}]]"
                )

        if PAGE_TABLE_HEADER_RE.match(stripped):
            in_page_table = True
            continue
        if not in_page_table:
            prefix = PREFIX_WIKILINK_RE.search(line)
            if prefix:
                errors.append(
                    f"{rel}:{number}: project/path prefix is attached directly to a wikilink "
                    f"as {prefix.group(1)}/[[...]]"
                )
            continue
        if not in_table_row:
            in_page_table = False
        elif not PAGE_TABLE_SEPARATOR_RE.match(line):
            match = PAGE_TABLE_LINK_CELL_RE.match(line)
            if match:
                target = match.group(1).strip()
                alias = (match.group(2) or "").strip()
                if "/" in target and (not alias or alias == target):
                    errors.append(
                        f"{rel}:{number}: reader-facing `页面` table exposes qualified path "
                        f"[[{target}]]; add a concise semantic alias"
                    )

        prefix = PREFIX_WIKILINK_RE.search(line)
        if prefix:
            errors.append(
                f"{rel}:{number}: project/path prefix is attached directly to a wikilink "
                f"as {prefix.group(1)}/[[...]]"
            )


def run_fixtures(errors: list[str]) -> None:
    unescaped: list[str] = []
    check_render_hazards(
        "fixture-unescaped.md",
        "| Owner | 职责 |\n| --- | --- |\n| [[projects/design/README|设计方案]] | owner |\n",
        unescaped,
    )
    if not unescaped:
        errors.append("fixture: unescaped table alias was not rejected")

    long_path: list[str] = []
    check_render_hazards(
        "fixture-long-path.md",
        "| 页面 | 职责 |\n| --- | --- |\n| [[projects/design/README]] | owner |\n",
        long_path,
    )
    if not long_path:
        errors.append("fixture: qualified path without alias was not rejected")

    prefix: list[str] = []
    check_render_hazards(
        "fixture-prefix.md",
        "wiki/[[projects/design/README\\|设计方案]]\n",
        prefix,
    )
    if not prefix:
        errors.append("fixture: attached project/wikilink prefix was not rejected")

    examples: list[str] = []
    check_render_hazards(
        "fixture-examples.md",
        "```markdown\n| [[projects/design/README|设计方案]] |\n```\n"
        "`wiki/[[projects/design/README|设计方案]]`\n",
        examples,
    )
    if examples:
        errors.append(f"fixture: fenced/inline syntax example was rejected: {examples[0]}")

    valid: list[str] = []
    check_render_hazards(
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
        check_render_hazards(
            path.relative_to(repo).as_posix(),
            path.read_text(encoding="utf-8"),
            errors,
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} Markdown document-governance issue(s)", file=sys.stderr)
        return 1
    print(
        "OK: wiki Markdown profile wiring and context-aware table/path-prefix "
        "regression fixtures checked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

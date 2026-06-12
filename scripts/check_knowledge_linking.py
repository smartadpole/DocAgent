#!/usr/bin/env python3
"""Check knowledge-linking skill wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "skills/knowledge-linking/SKILL.md",
    "skills/knowledge-linking/TRANSFER.md",
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
    routing = read(repo, "governance/response-mode-routing.md", errors)
    readme = read(repo, "skills/README.md", errors)
    index = read(repo, "INDEX.md", errors)
    check_all = read(repo, "scripts/check_all.py", errors)

    if skill:
        require_terms("skills/knowledge-linking/SKILL.md", skill, SKILL_TERMS, errors)
    if transfer:
        require_terms("skills/knowledge-linking/TRANSFER.md", transfer, TRANSFER_TERMS, errors)
    if routing:
        require_terms("governance/response-mode-routing.md", routing, ROUTING_TERMS, errors)
    for rel, text in (("skills/README.md", readme), ("INDEX.md", index)):
        if text and "[[skills/knowledge-linking/SKILL]]" not in text:
            errors.append(f"{rel}: missing knowledge-linking entry")
    if check_all and "knowledge-linking" not in check_all:
        errors.append("scripts/check_all.py: missing knowledge-linking check")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} knowledge-linking issue(s)", file=sys.stderr)
        return 1

    print("OK: knowledge-linking wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

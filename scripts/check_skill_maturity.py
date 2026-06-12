#!/usr/bin/env python3
"""Check skill maturity wiring, template fields, and local skill entries."""

from __future__ import annotations

import re
import sys
from pathlib import Path


README_TERMS = (
    "## 技能成熟度模型",
    "证据信号",
    "README entry",
    "template",
    "governance",
    "sensor",
    "TRANSFER",
    "evidence boundary",
    "skill-maturity",
)
TEMPLATE_TERMS = (
    "maturity:",
    "evidence_signals:",
    "transfer_ready:",
    "sensor:",
    "## 成熟度与证据信号",
    "evidence boundary",
)
CHECK_ALL_TERMS = ("skill-maturity", "check_skill_maturity.py")
WORKFLOW_TERMS = ("skill-maturity", "技能成熟度")
AGENT_TERMS = ("skill-maturity", "专项 sensor")
STATUS_TERMS = ("skill-maturity", "技能成熟度")
SKILL_REQUIRED_TERMS = ("## 定位", "## 输出格式", "## 禁止项")
SKILL_WORKFLOW_TERMS = ("## 工作流", "## 响应模式", "## 工作链还原")
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)


def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required skill maturity file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing skill maturity term {term!r}")


def check_skill_frontmatter(rel: str, text: str, errors: list[str]) -> None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"{rel}: missing YAML frontmatter")
        return
    frontmatter = match.group("body")
    for key in ("name:", "description:"):
        if key not in frontmatter:
            errors.append(f"{rel}: missing frontmatter field {key}")


def check_skill_files(repo: Path, readme: str, errors: list[str]) -> None:
    skill_files = sorted((repo / "skills").glob("*/SKILL.md"))
    if not skill_files:
        errors.append("skills/: no project skill files found")
        return

    for path in skill_files:
        rel = path.relative_to(repo).as_posix()
        text = path.read_text(encoding="utf-8")
        check_skill_frontmatter(rel, text, errors)
        require_terms(rel, text, SKILL_REQUIRED_TERMS, errors)
        if not any(term in text for term in SKILL_WORKFLOW_TERMS):
            errors.append(f"{rel}: missing workflow or response-mode section")
        wikilink = f"[[{path.relative_to(repo).with_suffix('').as_posix()}]]"
        if wikilink not in readme:
            errors.append(f"skills/README.md: missing skill entry {wikilink}")


def check_skill_maturity(repo: Path) -> list[str]:
    errors: list[str] = []
    readme = read_text(repo, "skills/README.md", errors)
    template = read_text(repo, "templates/skill-template.md", errors)
    check_all = read_text(repo, "scripts/check_all.py", errors)
    workflow = read_text(repo, "governance/WORKFLOW.md", errors)
    agents = read_text(repo, "AGENTS.md", errors)
    codex_agents = read_text(repo, ".codex/AGENTS.md", errors)
    status = read_text(repo, "projects/status.md", errors)

    if readme:
        require_terms("skills/README.md", readme, README_TERMS, errors)
        check_skill_files(repo, readme, errors)
    if template:
        require_terms("templates/skill-template.md", template, TEMPLATE_TERMS, errors)
    if check_all:
        require_terms("scripts/check_all.py", check_all, CHECK_ALL_TERMS, errors)
    for rel, text in (
        ("governance/WORKFLOW.md", workflow),
        ("AGENTS.md", agents),
        (".codex/AGENTS.md", codex_agents),
        ("projects/status.md", status),
    ):
        if text:
            if rel == "governance/WORKFLOW.md":
                required_terms = WORKFLOW_TERMS
            elif rel == "projects/status.md":
                required_terms = STATUS_TERMS
            else:
                required_terms = AGENT_TERMS
            require_terms(rel, text, required_terms, errors)

    return errors


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors = check_skill_maturity(repo)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} skill maturity issue(s)", file=sys.stderr)
        return 1
    print("OK: skill maturity entries, template fields, and sensor wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

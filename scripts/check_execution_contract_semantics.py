#!/usr/bin/env python3
"""Check execution-contract semantic guardrail wiring."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "governance/execution-contract-semantics.md",
    "governance/instruction-adherence.md",
    "governance/README.md",
    "INDEX.md",
    "AGENTS.md",
    "governance/WORKFLOW.md",
    "governance/POLICY.md",
    "projects/development/plan/work-item-system-model.md",
    "projects/development/plan/task-design-model.md",
    "projects/development/plan/test-acceptance-planning-model.md",
    "projects/development/reports/README.md",
    "scripts/check_all.py",
)

SEMANTICS_TERMS = (
    "# 执行合同语义",
    "执行合同语义污染",
    "裁决必须单值",
    "裁决不单值",
    "上层规则下沉",
    "非目标变潜在任务",
    "伪 optional",
    "证据层级回流",
    "辅助证据改写问题本体",
    "非目标只命名不展开",
    "scripts/check_execution_contract_semantics.py",
)

ENTRY_TERMS = (
    "execution-contract-semantics",
    "执行合同语义",
)

REQUIRED_TERM_BY_FILE = {
    "governance/README.md": ENTRY_TERMS,
    "INDEX.md": ENTRY_TERMS,
    "AGENTS.md": ENTRY_TERMS,
    "governance/WORKFLOW.md": ("execution-contract-semantics",),
    "governance/POLICY.md": ENTRY_TERMS,
    "governance/instruction-adherence.md": ENTRY_TERMS,
    "projects/development/plan/test-acceptance-planning-model.md": ENTRY_TERMS,
    "scripts/check_all.py": ("execution-contract-semantics", "check_execution_contract_semantics.py"),
}

FORBIDDEN_EXECUTION_PATTERNS = (
    r"默认不需要[^。\n]*(?:但|如果|若|如需)",
    r"(?:可选|视情况|后续可能|optional)[^。\n]*(?:关闭|裁决|done|验收)",
    r"非目标[^。\n]*(?:后续如何|归谁|怎么测|不作为关闭条件)",
)


def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required execution-contract semantics file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing execution-contract semantics term {term}")


def strip_wikilinks(text: str) -> str:
    return re.sub(r"\[\[[^\]]+\]\]", "", text)


def iter_contract_files(repo: Path) -> list[Path]:
    specs = (
        ("projects/development/issues", "issue-*.md"),
        ("projects/development/execution/tasks", "TASK-*.md"),
        ("projects/development/acceptance/plans", "AP-*.md"),
    )
    paths: list[Path] = []
    for root_rel, pattern in specs:
        root = repo / root_rel
        if root.exists():
            paths.extend(sorted(root.glob(pattern)))
    return paths


def reject_execution_pollution(repo: Path, errors: list[str]) -> None:
    for path in iter_contract_files(repo):
        rel = path.relative_to(repo).as_posix()
        text = strip_wikilinks(path.read_text(encoding="utf-8"))
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pattern in FORBIDDEN_EXECUTION_PATTERNS:
                if re.search(pattern, line, flags=re.IGNORECASE):
                    errors.append(
                        f"{rel}:{line_no}: execution contract must be single-valued; pattern {pattern}"
                    )


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (repo / rel).exists():
            errors.append(f"{rel}: required execution-contract semantics file is missing")

    semantics = read_text(repo, "governance/execution-contract-semantics.md", errors)
    if semantics:
        require_terms("governance/execution-contract-semantics.md", semantics, SEMANTICS_TERMS, errors)

    for rel, terms in REQUIRED_TERM_BY_FILE.items():
        text = read_text(repo, rel, errors)
        if text:
            require_terms(rel, text, terms, errors)

    reject_execution_pollution(repo, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} execution-contract semantics issue(s)", file=sys.stderr)
        return 1
    print("OK: execution-contract semantic guardrails checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

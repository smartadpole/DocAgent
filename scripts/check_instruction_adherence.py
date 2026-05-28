#!/usr/bin/env python3
"""Check instruction-adherence governance wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "governance/instruction-adherence.md",
    "governance/harness-feedback-ledger.md",
    "governance/harness-evolution.md",
    "governance/response-mode-routing.md",
    "AGENTS.md",
    ".codex/AGENTS.md",
    "governance/README.md",
    "governance/WORKFLOW.md",
    "governance/POLICY.md",
    "scripts/check_all.py",
    "scripts/check_harness_feedback_ledger.py",
)

INSTRUCTION_PAGE_TERMS = (
    "truth_scope: instruction_adherence_execution_coverage",
    "## 边界",
    "## Rule Coverage Ladder",
    "## 触发矩阵",
    "## 当前 sensor 覆盖",
    "## 提交闭环防漏",
    "## 规则瘦身判定",
    "## 收尾证明",
    "execution-contract-semantics",
    "check_instruction_adherence.py",
    "check_harness_feedback_ledger.py",
)
ENTRY_TERMS = ("instruction-adherence", "触发器", "sensor")
AGENTS_TERMS = ("instruction-adherence", "触发器", "最终证明")
CODEX_TERMS = ("instruction-adherence", "scripts/check_all.py --only")
LEDGER_TERMS = (
    "wiki 独立治理 sensor 拆分",
    "规则不能只停在自然语言",
    "instruction-adherence",
)
CHECK_ALL_TERMS = (
    "instruction-adherence",
    "scripts/check_instruction_adherence.py",
    "harness-feedback-ledger",
    "scripts/check_harness_feedback_ledger.py",
)


def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required instruction-adherence file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing instruction-adherence term {term}")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (repo / rel).exists():
            errors.append(f"{rel}: required instruction-adherence file is missing")

    instruction = read_text(repo, "governance/instruction-adherence.md", errors)
    governance_readme = read_text(repo, "governance/README.md", errors)
    agents = read_text(repo, "AGENTS.md", errors)
    codex_agents = read_text(repo, ".codex/AGENTS.md", errors)
    ledger = read_text(repo, "governance/harness-feedback-ledger.md", errors)
    check_all = read_text(repo, "scripts/check_all.py", errors)

    if instruction:
        require_terms("governance/instruction-adherence.md", instruction, INSTRUCTION_PAGE_TERMS, errors)
    if governance_readme:
        require_terms("governance/README.md", governance_readme, ENTRY_TERMS, errors)
    if agents:
        require_terms("AGENTS.md", agents, AGENTS_TERMS, errors)
    if codex_agents:
        require_terms(".codex/AGENTS.md", codex_agents, CODEX_TERMS, errors)
    if ledger:
        require_terms("governance/harness-feedback-ledger.md", ledger, LEDGER_TERMS, errors)
    if check_all:
        require_terms("scripts/check_all.py", check_all, CHECK_ALL_TERMS, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} instruction-adherence issue(s)", file=sys.stderr)
        return 1

    print("OK: instruction-adherence triggers, ledger, and sensors checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

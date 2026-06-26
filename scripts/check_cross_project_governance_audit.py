#!/usr/bin/env python3
"""Validate cross-project governance audit contracts and sensor wiring."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "skills/cross-project-governance-audit/SKILL.md",
    "skills/cross-project-governance-audit/TRANSFER.md",
    "templates/cross-project-governance-audit-contract-template.md",
    "governance/agent-governance-strategy.md",
    "skills/README.md",
    "templates/README.md",
    "scripts/check_all.py",
)

REQUIRED_TERMS = {
    "skills/cross-project-governance-audit/SKILL.md": (
        "cross-project-governance-audit",
        "Cross-Project",
        "Project Governance Audit",
        "YYYY-MM-DD",
        "YYYY-MM",
        "git remote -v",
        "source-depth",
        "handoff-ready",
        "skill-transfer",
        "Transfer Manifest",
        "non-reference",
        "verification-loop",
        "no runtime validation",
        "true-gap / recognition-gap / signal-only-gap",
    ),
    "templates/cross-project-governance-audit-contract-template.md": (
        "Cross-Project Governance Audit Contract Template",
        "CPGA-YYYY-MM-DD",
        "YYYY-MM",
        "Source Depth",
        "git remote -v",
        "git fetch --all --prune",
        "Drift Report",
        "true-gap",
        "recognition-gap",
        "signal-only-gap",
        "handoff-ready",
        "verification-loop",
        "Transfer Manifest",
        "non-reference",
        "no runtime validation",
        "行动 owner",
        "检查方式",
        "完成口径",
        "上层抽象",
        "举一反三",
    ),
    "governance/agent-governance-strategy.md": (
        "Cross-Project Governance Audit",
        "cross-project-governance-audit",
        "Project Governance Audit",
        "YYYY-MM-DD",
        "YYYY-MM",
        "git remote -v",
        "source-depth",
        "handoff-ready",
        "skill-transfer",
        "Transfer Manifest",
        "non-reference",
        "verification-loop",
        "no runtime validation",
        "true-gap / recognition-gap / signal-only-gap",
    ),
    "skills/cross-project-governance-audit/TRANSFER.md": (
        "能力目标",
        "可以吸收",
        "只能抽象吸收",
        "禁止复制",
        "目标工程结构自检",
        "验证要求",
        "source-depth",
        "handoff-ready",
        "no runtime validation",
    ),
    "scripts/check_all.py": (
        "cross-project-governance-audit",
        "check_cross_project_governance_audit.py",
    ),
}


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing cross-project governance audit file: {rel}")

    for rel, terms in REQUIRED_TERMS.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel} missing cross-project governance audit term: {term}")

    if errors:
        print("Cross-project governance audit validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Cross-project governance audit validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

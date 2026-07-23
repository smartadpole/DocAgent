#!/usr/bin/env python3
"""Check comprehensive wiki governance-system rectification wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "governance/wiki-governance-system-contract.v1.md",
    "templates/governance-system-upgrade-contract-template.md",
    "governance/acknowledgebase-topic-system-adoption.v1.md",
    "governance/agent-system-maturity.md",
    "governance/agent-orchestration.md",
    "governance/harness-evolution.md",
    "governance/harness-feedback-ledger.md",
    "governance/WORKFLOW.md",
    "projects/memory/README.md",
    "projects/memory/shared.md",
    "skills/README.md",
    ".codex/AGENTS.md",
)

CONTRACT_TERMS = (
    "Wiki Governance System Contract",
    "agent",
    "workflow",
    "memory",
    "harness",
    "skill",
    "evaluation",
    "governance",
    "template",
    "topic",
    "migration",
    "owner landing",
    "agent behavior",
    "sensor / evaluator",
    "closeout proof",
    "不完成条件",
    "structure-only",
    "insufficient-evidence",
)

TEMPLATE_TERMS = (
    "Governance System Upgrade Contract Template",
    "Source Coverage",
    "Ability Extraction",
    "System Layer Landing",
    "Sensor / Evaluator",
    "Persistence Routing",
    "Closeout Proof",
    "Goodhart guard",
)

ENTRYPOINT_TERMS = {
    ".codex/AGENTS.md": (
        "wiki-governance-system-contract.v1",
        "governance-system-rectification",
    ),
    "governance/WORKFLOW.md": (
        "wiki-governance-system-contract.v1",
        "Governance System Upgrade Contract",
        "governance-system-rectification",
    ),
    "governance/README.md": (
        "wiki-governance-system-contract.v1",
        "治理体系全面整改",
    ),
    "INDEX.md": (
        "wiki-governance-system-contract.v1",
        "治理体系全面整改",
    ),
    "README.md": (
        "wiki-governance-system-contract.v1",
        "治理体系全面整改",
    ),
    "templates/README.md": (
        "governance-system-upgrade-contract-template",
        "Governance System Upgrade Contract",
    ),
    "skills/README.md": (
        "Governance System Capability Pack",
        "wiki-governance-system-contract.v1",
    ),
    "projects/memory/README.md": (
        "wiki-governance-system-contract.v1",
        "acknowledgebase-topic-system-adoption.v1",
    ),
    "projects/memory/shared.md": (
        "wiki-governance-system-contract.v1",
        "acknowledgebase-topic-system-adoption.v1",
    ),
    "governance/agent-orchestration.md": (
        "Governance System Run Capsule",
        "wiki-governance-system-contract.v1",
    ),
    "governance/harness-evolution.md": (
        "治理体系全面整改",
        "wiki-governance-system-contract.v1",
    ),
    "governance/harness-feedback-ledger.md": (
        "逐 topic 清单不等于治理体系完成",
        "governance-system-rectification",
    ),
    "scripts/check_all.py": (
        "governance-system-rectification",
        "check_governance_system_rectification.py",
    ),
}


def read(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: missing file")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing required term {term!r}")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        read(repo, rel, errors)

    contract = read(repo, "governance/wiki-governance-system-contract.v1.md", errors)
    if contract:
        require_terms("governance/wiki-governance-system-contract.v1.md", contract, CONTRACT_TERMS, errors)

    template = read(repo, "templates/governance-system-upgrade-contract-template.md", errors)
    if template:
        require_terms("templates/governance-system-upgrade-contract-template.md", template, TEMPLATE_TERMS, errors)

    for rel, terms in ENTRYPOINT_TERMS.items():
        text = read(repo, rel, errors)
        if text:
            require_terms(rel, text, terms, errors)

    if errors:
        print("FAILED: governance system rectification wiring issues found", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("OK: governance system contract, owner landing, template, ledger, and sensor wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

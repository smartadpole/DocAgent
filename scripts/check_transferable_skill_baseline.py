#!/usr/bin/env python3
"""Validate transferable skill baseline adoption manifest and wiring."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MANIFEST = "skills/transferable-skill-governance/matrix-adoption-2026-06-26-agent-evidence-v12.md"

REQUIRED_FILES = (
    MANIFEST,
    "skills/README.md",
    "skills/transferable-skill-governance/SKILL.md",
    "skills/transferable-skill-governance/TRANSFER.md",
    "skills/cross-project-skill-adoption-prompt/SKILL.md",
    "skills/cross-project-skill-adoption-prompt/TRANSFER.md",
    "templates/skill-transfer-manifest-template.md",
    "scripts/check_skill_maturity.py",
    "scripts/check_all.py",
    "README.md",
    "INDEX.md",
    "governance/README.md",
    "projects/status.md",
)

MANIFEST_TERMS = (
    "source_snapshot_generated_at: 2026-06-26 11:39",
    "source_revision: 308bc64",
    "scoring_schema_version: agent-evidence-v12",
    "local_source_of_truth",
    "allowed_write_scope",
    "required_profile",
    "validation_command",
    "blocked_when_missing",
    "exceptions",
    "recognize",
    "complete",
    "upgrade",
    "merge",
    "adapt",
    "defer",
    "reject",
    "Goal Contract",
    "Loop Engineering",
    "Public HTML Publish",
    "documentation-maintenance",
    "issue-analysis",
    "topic-visual-presentation",
    "knowledge-linking",
    "research-capability",
    "frontier-technology-intake",
    "cross-project-governance-audit",
    "cross-project-skill-adoption-prompt",
    "transferable-skill-governance",
    "Agent System Capability Package",
    "work-item-auto-decomposition",
    "project-bound",
    "true-gap",
    "recognition-gap",
    "signal-only-gap",
    "sensor 只证明结构",
    "insufficient-evidence",
)

ENTRY_TERMS = {
    "skills/README.md": (
        "matrix-adoption-2026-06-26-agent-evidence-v12",
        "transferable-skill-baseline",
        "本工程 baseline conformance",
    ),
    "README.md": ("matrix-adoption-2026-06-26-agent-evidence-v12", "transferable-skill-baseline"),
    "INDEX.md": ("matrix-adoption-2026-06-26-agent-evidence-v12", "transferable-skill-baseline"),
    "governance/README.md": ("matrix-adoption-2026-06-26-agent-evidence-v12", "transferable-skill-baseline"),
    "projects/status.md": ("transferable-skill-baseline", "matrix-adoption-2026-06-26"),
    "scripts/check_all.py": ("transferable-skill-baseline", "check_transferable_skill_baseline.py"),
    "skills/transferable-skill-governance/SKILL.md": (
        "matrix-adoption-2026-06-26-agent-evidence-v12",
        "repo-native",
    ),
    "skills/transferable-skill-governance/TRANSFER.md": (
        "Matrix adoption manifest",
        "local_source_of_truth",
    ),
    "skills/cross-project-skill-adoption-prompt/SKILL.md": (
        "source-depth",
        "Transfer Manifest",
        "Matrix Recognition Capsule",
    ),
    "skills/cross-project-skill-adoption-prompt/TRANSFER.md": (
        "Matrix Recognition Capsule",
        "insufficient-evidence",
    ),
    "templates/skill-transfer-manifest-template.md": (
        "local_source_of_truth",
        "blocked_when_missing",
        "任务书基线",
    ),
}


def read_text(rel: str, errors: list[str]) -> str:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing transferable skill baseline file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel} missing transferable skill baseline term: {term}")


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        read_text(rel, errors)

    manifest = read_text(MANIFEST, errors)
    if manifest:
        require_terms(MANIFEST, manifest, MANIFEST_TERMS, errors)

    for rel, terms in ENTRY_TERMS.items():
        text = read_text(rel, errors)
        if text:
            require_terms(rel, text, terms, errors)

    if errors:
        print("Transferable skill baseline validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Transferable skill baseline validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

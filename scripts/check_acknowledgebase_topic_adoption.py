#!/usr/bin/env python3
"""Check AcknowledgeBase topic-to-system adoption coverage."""

from __future__ import annotations

import sys
from pathlib import Path


MANIFEST = "governance/acknowledgebase-topic-system-adoption.v1.md"

SOURCE_TOPICS = (
    "projects/design/topics/README.md",
    "projects/design/topics/universal-agent-harness-baseline.md",
    "projects/design/topics/agent-harness-memory-evaluation-and-migration.md",
    "projects/design/topics/agent-harness-memory-evaluation-and-migration/README.md",
    "projects/design/topics/agent-harness-memory-evaluation-and-migration/goal-orchestration-governance.md",
    "projects/design/topics/agent-harness-memory-evaluation-and-migration/cross-repository-governance-acceptance.md",
    "projects/design/topics/agent-harness-memory-evaluation-and-migration/process-knowledge-persistence.md",
    "projects/design/topics/collaborative-code-and-work-item-id-governance.md",
    "projects/design/topics/cross-project-log-architecture.md",
    "projects/design/topics/design-topic-file-governance.md",
    "projects/design/topics/dialogue-knowledge-persistence-system.md",
    "projects/design/topics/dialogue-work-state-capture-and-retrieval.md",
    "projects/design/topics/dialogue-work-state-capture-loop-contract.md",
    "projects/design/topics/dialogue-work-state-capture-phase-one-pilot.md",
    "projects/design/topics/execution-process-record-system.md",
    "projects/design/topics/personal-capability-system-architecture.md",
    "skills/topic-visual-presentation/SKILL.md",
    "projects/design/topics/research-operating-system-design.md",
    "projects/design/topics/retrospective-archive-storage-structure.md",
    "projects/design/topics/skill-maturity-integrated-scoring-loop-contract.md",
    "projects/design/topics/skill-maturity-scoring-evolution.md",
    "projects/design/topics/technical-research-capability-upgrade.md",
    "projects/design/topics/topic-placement-and-state-routing.md",
)

REQUIRED_MANIFEST_TERMS = (
    "ability adoption",
    "source_topic",
    "capability extraction",
    "wiki system layers",
    "wiki owner landing",
    "agent-system action",
    "validation",
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
    "not copied",
    "structure-only",
    "insufficient-evidence",
)

ENTRYPOINT_TERMS = {
    "INDEX.md": ("acknowledgebase-topic-system-adoption.v1", "逐 topic"),
    "governance/README.md": ("acknowledgebase-topic-system-adoption.v1", "逐 topic"),
    "governance/agent-system-maturity.md": (
        "acknowledgebase-topic-system-adoption.v1",
        "ability adoption",
    ),
    "governance/agent-system-cross-project-alignment.v1.md": (
        "acknowledgebase-topic-system-adoption.v1",
        "source topic",
    ),
    "projects/design/topics/agent-workflow-memory-harness-skill-landing.md": (
        "acknowledgebase-topic-system-adoption.v1",
        "逐 topic",
    ),
    ".codex/AGENTS.md": ("acknowledge-topic-adoption", "acknowledgebase-topic-system-adoption.v1"),
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

    manifest = read(repo, MANIFEST, errors)
    if manifest:
        require_terms(MANIFEST, manifest, REQUIRED_MANIFEST_TERMS, errors)
        for source_topic in SOURCE_TOPICS:
            if source_topic not in manifest:
                errors.append(f"{MANIFEST}: missing source topic {source_topic!r}")

    for rel, terms in ENTRYPOINT_TERMS.items():
        text = read(repo, rel, errors)
        if text:
            require_terms(rel, text, terms, errors)

    check_all = read(repo, "scripts/check_all.py", errors)
    if check_all:
        require_terms(
            "scripts/check_all.py",
            check_all,
            ("acknowledge-topic-adoption", "check_acknowledgebase_topic_adoption.py"),
            errors,
        )

    if errors:
        print("FAILED: AcknowledgeBase topic adoption issues found", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("OK: AcknowledgeBase topic adoption manifest, entrypoints, and source coverage checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

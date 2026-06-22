#!/usr/bin/env python3
"""Check Loop Engineering skill, templates, entrypoints, and gate wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "skills/loop-engineering/SKILL.md",
    "skills/loop-engineering/TRANSFER.md",
    "templates/loop-contract-template.md",
    "templates/run-capsule-template.md",
    "scripts/check_all.py",
    "AGENTS.md",
    "README.md",
    "INDEX.md",
    "governance/README.md",
    "skills/README.md",
    "templates/README.md",
)

SKILL_TERMS = (
    "Loop Engineering",
    "Discovery source",
    "Run queue",
    "Evaluator oracle",
    "Persistent state",
    "Scheduler / trigger",
    "Budget / stop",
    "Worker",
    "Subproject Git preflight",
    "Execution posture",
    "Process record",
    "Reuse decision",
    "orchestrator-only",
    "software-development",
    "不新建平行",
    "evidence boundary",
)

TRANSFER_TERMS = (
    "## 能力目标",
    "## 可以吸收",
    "## 只能抽象吸收",
    "## 禁止复制",
    "## 目标工程结构自检",
    "## 验证要求",
    "Loop Contract",
    "Run Capsule",
    "禁止复制 AcknowledgeBase",
)

LOOP_TEMPLATE_TERMS = (
    "## Discovery Source",
    "## Trigger / Schedule",
    "## Run Queue And State",
    "## Agent Topology",
    "## Subproject Git Preflight",
    "## Worker Ownership",
    "## Evaluator Oracle",
    "## Persistence Routing",
    "## Software Development Landing",
    "## Budget And Safety",
    "## Next-run Decision",
    "Process Record",
    "Reuse entry proof",
    "Retrospective trigger decision",
    "orchestrator-only",
    "queued / running / passed / partial / blocked / failed / skipped",
    "baseline fail + candidate pass",
    "stop / rerun / retry-after / split / escalate / wait-human / schedule-next",
    "禁止新建平行看板",
)

RUN_CAPSULE_TERMS = (
    "Parent Loop Contract",
    "Run id",
    "Input discovery item",
    "State transition",
    "Next-run recommendation",
    "Worker 回传是否齐全",
    "Subproject Git Preflight",
    "Process Record",
    "Reuse entry proof",
    "Retrospective trigger decision",
    "orchestrator-only",
)

ENTRY_TERMS = {
    "AGENTS.md": ("Loop Engineering", "skills/loop-engineering/SKILL", "templates/loop-contract-template"),
    "README.md": ("Loop Engineering", "skills/loop-engineering/SKILL", "templates/loop-contract-template"),
    "INDEX.md": ("Loop Engineering", "skills/loop-engineering/SKILL", "templates/loop-contract-template"),
    "governance/README.md": ("Loop Engineering", "skills/loop-engineering/SKILL", "templates/loop-contract-template"),
    "skills/README.md": ("skills/loop-engineering/SKILL",),
    "templates/README.md": ("templates/loop-contract-template", "templates/run-capsule-template"),
    "scripts/check_all.py": ("loop-engineering", "scripts/check_loop_engineering.py"),
}


def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required Loop Engineering file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing Loop Engineering term {term}")


def check_loop_engineering(repo: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (repo / rel).exists():
            errors.append(f"{rel}: required Loop Engineering file is missing")

    require_terms("skills/loop-engineering/SKILL.md", read_text(repo, "skills/loop-engineering/SKILL.md", errors), SKILL_TERMS, errors)
    require_terms("skills/loop-engineering/TRANSFER.md", read_text(repo, "skills/loop-engineering/TRANSFER.md", errors), TRANSFER_TERMS, errors)
    require_terms("templates/loop-contract-template.md", read_text(repo, "templates/loop-contract-template.md", errors), LOOP_TEMPLATE_TERMS, errors)
    require_terms("templates/run-capsule-template.md", read_text(repo, "templates/run-capsule-template.md", errors), RUN_CAPSULE_TERMS, errors)

    for rel, terms in ENTRY_TERMS.items():
        require_terms(rel, read_text(repo, rel, errors), terms, errors)

    return errors


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors = check_loop_engineering(repo)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} Loop Engineering issue(s)", file=sys.stderr)
        return 1
    print("OK: Loop Engineering skill, templates, entrypoints, and gate wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

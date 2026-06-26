#!/usr/bin/env python3
"""L5 validation for the wiki Agent Harness contract."""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FILES = (
    "governance/agent-governance-strategy.md",
    "governance/state-constraint-reasoning.md",
    "governance/agent-orchestration.md",
    "templates/goal-contract-template.md",
    "templates/run-capsule-template.md",
    "templates/loop-contract-template.md",
    "projects/development/reports/2026-06-22-agent-harness-l5-validation.md",
)

REPORT_TERMS = (
    "L5 final proof",
    "Goal Contract dry-run",
    "Run Capsule dry-run",
    "Subproject Git Preflight live readback",
    "Harness Evolution correction route",
    "不能上推",
    "0\t0",
)

# Cross-Project Governance Audit depth terms are intentionally kept in a
# sensor layer so matrix/depth checks do not rely only on governance prose.
CROSS_PROJECT_GOVERNANCE_AUDIT_DEPTH_TERMS = (
    "证据计划",
    "深度等级",
    "触发优先级",
    "完整产物",
    "行动 owner",
    "检查方式",
    "完成口径",
    "上层抽象",
    "举一反三",
)


@dataclass(frozen=True)
class GoalSample:
    evidence_layers: set[str]
    required_layers: set[str]

    def closeout(self) -> str:
        return "passed" if self.required_layers <= self.evidence_layers else "partial"


@dataclass(frozen=True)
class WorkerSample:
    worker_claims_done: bool
    evaluator_result: str | None

    def closeout(self) -> str:
        if self.worker_claims_done and self.evaluator_result is None:
            return "blocked"
        return self.evaluator_result or "partial"


def run(repo: Path, command: tuple[str, ...]) -> str:
    result = subprocess.run(command, cwd=repo, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(command)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing L5 validation term {term}")


def check_goal_dry_run(errors: list[str]) -> None:
    sample = GoalSample(
        evidence_layers={"local validation", "sensor", "git readback"},
        required_layers={"local validation", "service-side validation", "end-to-end validation"},
    )
    if sample.closeout() != "partial":
        errors.append("Goal Contract dry-run: local-only evidence must not close service/end-to-end scope")


def check_run_capsule_dry_run(errors: list[str]) -> None:
    blocked = WorkerSample(worker_claims_done=True, evaluator_result=None)
    passed = WorkerSample(worker_claims_done=True, evaluator_result="passed")
    if blocked.closeout() != "blocked":
        errors.append("Run Capsule dry-run: worker self-closure without evaluator must be blocked")
    if passed.closeout() != "passed":
        errors.append("Run Capsule dry-run: evaluator pass should close representative sample")


def check_git_preflight(repo: Path, errors: list[str]) -> None:
    branch = run(repo, ("git", "branch", "--show-current"))
    upstream = run(repo, ("git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"))
    remotes = run(repo, ("git", "remote", "-v"))
    ahead_behind = run(repo, ("git", "rev-list", "--left-right", "--count", "HEAD...@{u}"))
    _status = run(repo, ("git", "status", "--short"))

    if not branch:
        errors.append("Subproject Git Preflight live readback: branch is empty")
    if "/" not in upstream:
        errors.append("Subproject Git Preflight live readback: upstream is not configured")
    if "origin" not in remotes:
        errors.append("Subproject Git Preflight live readback: origin remote is missing")
    parts = ahead_behind.split()
    if len(parts) != 2 or not all(part.isdigit() for part in parts):
        errors.append("Subproject Git Preflight live readback: ahead/behind is not parseable")


def check_report(repo: Path, errors: list[str]) -> None:
    rel = "projects/development/reports/2026-06-22-agent-harness-l5-validation.md"
    text = (repo / rel).read_text(encoding="utf-8")
    require_terms(rel, text, REPORT_TERMS, errors)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (repo / rel).exists():
            errors.append(f"{rel}: required L5 validation file is missing")

    if not errors:
        check_goal_dry_run(errors)
        check_run_capsule_dry_run(errors)
        check_git_preflight(repo, errors)
        check_report(repo, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} Agent Harness L5 validation issue(s)", file=sys.stderr)
        return 1
    print("OK: Agent Harness L5 dry-runs, git preflight, report, and final-proof wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

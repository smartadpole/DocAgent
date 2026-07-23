#!/usr/bin/env python3
"""Check local Agent System Maturity wiring and honest evidence boundaries."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_OWNER_TERMS = (
    "Agent System Capability Package",
    "agent-system-cross-project-alignment.v1",
    "skill",
    "runtime",
    "harness",
    "memory",
    "evaluation",
    "governance",
    "migration",
    "Matrix Recognition Capsule",
    "true-gap",
    "recognition-gap",
    "signal-only-gap",
    "Goodhart guard",
    "external readback",
    "insufficient-evidence",
    "agent_intelligence_score",
    "Persistence Decision",
    "Worker findings",
)

REQUIRED_ALIGNMENT_TERMS = (
    "Cross-Project Agent Intelligence Alignment Map",
    "Source Coverage",
    "source archetype",
    "capability pack",
    "controller / production control-plane project",
    "subproject / implementation repo",
    "runtime-service / ops-agent",
    "data-model / evaluation project",
    "knowledge-base / domain-governance project",
    "lightweight repo",
    "agent-finalizer",
    "external-write-boundary",
    "acceptance-governance",
    "performance-bandwidth-analysis",
    "runtime-config-switch",
    "customer-group-db-readback",
    "Agent System Capability Package",
    "source freshness",
    "L5 blocked-boundary proof",
    "per-dialogue / run trace",
    "structure-only",
    "insufficient-evidence",
    "not copied",
    "blocked-by-orchestrator-readback",
)

DIMENSIONS = (
    "intent_modeling",
    "mode_selection",
    "tool_and_runtime_use",
    "context_and_memory_use",
    "decomposition_and_orchestration",
    "evidence_judgment",
    "recovery_and_learning",
    "user_alignment",
)

SYSTEM_LAYERS = ("skill", "runtime", "harness", "memory", "evaluation", "governance", "migration")

ENTRYPOINT_TERMS = {
    "README.md": ("[[agent-system-maturity]]", "Agent System Capability Package"),
    "INDEX.md": ("[[agent-system-maturity]]", "[[agent-system-cross-project-alignment.v1]]"),
    "governance/README.md": ("[[agent-system-maturity]]", "[[agent-system-cross-project-alignment.v1]]"),
    "templates/README.md": ("agent-intelligence-evaluation-template", "positive / negative behavior corpus"),
    "skills/README.md": ("work-item-auto-decomposition", "项目 / 领域绑定"),
    "AGENTS.md": ("本地是否存在 AcknowledgeBase", "对应 topic 必须 `updated`", "upstream_write_authorization", "Persistence Decision", "conformance"),
    ".codex/AGENTS.md": ("agent-system-maturity", "work-item-auto-decomposition"),
}

AGENT_INTELLIGENCE_TEMPLATE_TERMS = (
    "Agent Intelligence Evaluation",
    "positive / negative behavior corpus",
    "intent_modeling",
    "mode_selection",
    "tool_and_runtime_use",
    "context_and_memory_use",
    "decomposition_and_orchestration",
    "evidence_judgment",
    "recovery_and_learning",
    "user_alignment",
    "evaluator provenance",
    "Goodhart Guard",
    "agent_intelligence_score",
    "negative evidence review",
    "external readback",
)


def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: missing file")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing required term {term!r}")


def check_snapshot(repo: Path, errors: list[str]) -> None:
    rel = "governance/agent-system-maturity-snapshot.v1.json"
    text = read_text(repo, rel, errors)
    if not text:
        return
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"{rel}: invalid JSON: {exc}")
        return

    if data.get("schema_version") != "agent-system-maturity-snapshot-v1":
        errors.append(f"{rel}: unexpected schema_version")

    system = data.get("system", {})
    for layer in SYSTEM_LAYERS:
        entry = system.get(layer)
        if not isinstance(entry, dict):
            errors.append(f"{rel}: missing system layer {layer!r}")
            continue
        for field in ("verdict", "status", "proof", "non_upgrade_boundary"):
            if field not in entry:
                errors.append(f"{rel}: system layer {layer!r} missing {field!r}")

    intelligence = data.get("intelligence", {})
    if intelligence.get("intelligence_observed") != "insufficient-evidence":
        errors.append(f"{rel}: Phase 1A intelligence_observed must stay insufficient-evidence")
    if intelligence.get("agent_intelligence_score") is not None:
        errors.append(f"{rel}: agent_intelligence_score must stay null until behavior evidence is scored")

    dimension_scores = intelligence.get("dimension_scores", {})
    for dimension in DIMENSIONS:
        score = dimension_scores.get(dimension)
        if not isinstance(score, dict):
            errors.append(f"{rel}: missing intelligence dimension {dimension!r}")
            continue
        if score.get("status") != "insufficient-evidence":
            errors.append(f"{rel}: dimension {dimension!r} must be insufficient-evidence in Phase 1A")
        if score.get("score") is not None:
            errors.append(f"{rel}: dimension {dimension!r} score must be null")
        if not score.get("missing_evidence"):
            errors.append(f"{rel}: dimension {dimension!r} missing_evidence is empty")
        if "cap_reason" not in score:
            errors.append(f"{rel}: dimension {dimension!r} missing cap_reason")

    provenance = intelligence.get("evaluator_provenance", {})
    if provenance.get("negative_evidence_reviewed") is not False:
        errors.append(f"{rel}: negative_evidence_reviewed must be false until review is actually done")
    if "governance/agent-system-cross-project-alignment.v1.md" not in provenance.get("input_refs", []):
        errors.append(f"{rel}: evaluator_provenance.input_refs missing cross-project alignment map")
    external = data.get("external_readback", {})
    if external.get("status") != "blocked-by-orchestrator-readback":
        errors.append(f"{rel}: external_readback.status must state orchestrator-blocked readback")
    if not external.get("goodhart_guard"):
        errors.append(f"{rel}: missing goodhart_guard")
    if "no structure-only alignment promoted to behavior intelligence" not in external.get("goodhart_guard", []):
        errors.append(f"{rel}: missing structure-only Goodhart guard")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    owner = read_text(repo, "governance/agent-system-maturity.md", errors)
    if owner:
        require_terms("governance/agent-system-maturity.md", owner, REQUIRED_OWNER_TERMS, errors)
        require_terms(
            "governance/agent-system-maturity.md",
            owner,
            ("agent-intelligence-evaluation-template", "positive / negative behavior corpus"),
            errors,
        )

    alignment = read_text(repo, "governance/agent-system-cross-project-alignment.v1.md", errors)
    if alignment:
        require_terms(
            "governance/agent-system-cross-project-alignment.v1.md",
            alignment,
            REQUIRED_ALIGNMENT_TERMS,
            errors,
        )

    for rel, terms in ENTRYPOINT_TERMS.items():
        text = read_text(repo, rel, errors)
        if text:
            require_terms(rel, text, terms, errors)

    intelligence_template = read_text(repo, "templates/agent-intelligence-evaluation-template.md", errors)
    if intelligence_template:
        require_terms(
            "templates/agent-intelligence-evaluation-template.md",
            intelligence_template,
            AGENT_INTELLIGENCE_TEMPLATE_TERMS,
            errors,
        )

    check_snapshot(repo, errors)

    if errors:
        print("FAILED: agent system maturity wiring issues found", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("OK: agent system maturity owner, snapshot, and entrypoints checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

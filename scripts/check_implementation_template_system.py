#!/usr/bin/env python3
"""Check wiki implementation-project template system wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "projects/design/topics/implementation-engineering-template-system.md",
    "projects/design/topics/agent-workflow-memory-harness-skill-landing.md",
    "templates/implementation-project-profile-template.md",
)

TOPIC_INDEX_TERMS = (
    "implementation-engineering-template-system",
    "agent-workflow-memory-harness-skill-landing",
    "实现类工程合集",
    "Project Profile Overlay",
    "Capability Pack",
    "Agent / Workflow / Memory / Harness / Skill",
)

IMPLEMENTATION_TOPIC_TERMS = (
    "所有实现类工程的合集与模板",
    "主控 / controller",
    "子工程 / implementation repo",
    "runtime-service",
    "模板母体",
    "Template Kernel",
    "Capability Pack",
    "knowledge-base-profile",
    "ops-agent-profile",
    "Adoption Matrix",
    "required_packs",
    "forbidden_packs",
    "project_bound_facts",
    "Subproject Git Preflight",
    "Implementation Project Profile",
    "Project Profile Overlay",
    "Capability Packs",
    "Owner Topology Compatibility",
    "owner_topology_role",
    "owner_independence_gate",
    "responsibility_scope",
    "clone_instantiation_mode",
    "mother_seed_policy",
    "research_depth_default",
    "source_deidentification_rule",
    "agent_system_layers",
    "Topic 到系统层落地",
    "Universal Agent Harness Baseline",
    "Research Operating System",
    "topic placement",
    "不能上推",
)

LANDING_TOPIC_TERMS = (
    "Agent / Workflow / Memory / Harness / Skill",
    "系统矩阵",
    "agent",
    "workflow",
    "memory",
    "harness",
    "skill",
    "evaluation",
    "topic",
    "migration",
    "Topic 吸收裁决",
    "dialogue persistence",
    "insufficient-evidence",
)

PROFILE_TEMPLATE_TERMS = (
    "project_role",
    "profile_overlay",
    "required_capability_packs",
    "forbidden_capability_packs",
    "Template-Facing Boundary",
    "Template Kernel",
    "Project Profile Overlay",
    "Capability Packs",
    "Owner Topology Boundary",
    "Clone Instantiation",
    "owner_topology_role",
    "owner_independence_gate",
    "responsibility_scope",
    "core_workflows",
    "primary_facts_and_evidence",
    "clone_instantiation_mode",
    "mother_seed_policy",
    "identity_rewrite_required",
    "current_state_reset",
    "privacy_currentness_boundary",
    "research_depth_default",
    "Adoption Matrix",
    "required_packs",
    "optional_packs",
    "forbidden_packs",
    "project_bound_facts",
    "source_deidentification_rule",
    "Owner Surfaces",
    "Agent System Layers",
    "Control Plane",
    "Implementation Boundaries",
    "Subproject Git Preflight",
    "Evidence Contract",
    "Template Adoption",
    "Closeout Proof",
    "blocked_for_done",
    "not_blocked_for_implementation",
)

ENTRYPOINT_TERMS = {
    "templates/README.md": ("implementation-project-profile-template", "实现类工程 Profile"),
    "skills/README.md": ("implementation-project-profile-template", "实现类工程合集"),
    "governance/agent-system-maturity.md": (
        "implementation-engineering-template-system",
        "implementation-project-profile-template",
        "所有实现类工程",
    ),
    "governance/agent-system-cross-project-alignment.v1.md": (
        "implementation-engineering-template-system",
        "agent-workflow-memory-harness-skill-landing",
        "AcknowledgeBase topic",
    ),
    "AGENTS.md": ("实现类工程合集", "implementation-project-profile-template"),
    ".codex/AGENTS.md": ("implementation-template-system", "implementation-project-profile-template"),
    "INDEX.md": ("implementation-engineering-template-system", "implementation-project-profile-template"),
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

    topic_index = read(repo, "projects/design/topics/README.md", errors)
    if topic_index:
        require_terms("projects/design/topics/README.md", topic_index, TOPIC_INDEX_TERMS, errors)

    implementation_topic = read(repo, "projects/design/topics/implementation-engineering-template-system.md", errors)
    if implementation_topic:
        require_terms(
            "projects/design/topics/implementation-engineering-template-system.md",
            implementation_topic,
            IMPLEMENTATION_TOPIC_TERMS,
            errors,
        )

    landing_topic = read(repo, "projects/design/topics/agent-workflow-memory-harness-skill-landing.md", errors)
    if landing_topic:
        require_terms(
            "projects/design/topics/agent-workflow-memory-harness-skill-landing.md",
            landing_topic,
            LANDING_TOPIC_TERMS,
            errors,
        )

    profile = read(repo, "templates/implementation-project-profile-template.md", errors)
    if profile:
        require_terms("templates/implementation-project-profile-template.md", profile, PROFILE_TEMPLATE_TERMS, errors)

    for rel, terms in ENTRYPOINT_TERMS.items():
        text = read(repo, rel, errors)
        if text:
            require_terms(rel, text, terms, errors)

    if errors:
        print("FAILED: implementation template system wiring issues found", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("OK: implementation template system owner, profile, entrypoints, and topic landing checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

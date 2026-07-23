#!/usr/bin/env python3
"""Check production-grade agent control-plane hardening wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_TERMS: dict[str, tuple[str, ...]] = {
    "governance/agent-orchestration.md": (
        "Production-Grade Control Plane Hardening",
        "agent-finalizer",
        "external-write-boundary",
        "acceptance-governance",
        "long-task-progress",
        "production readback",
        "performance evidence ledger",
        "runtime config switch",
        "DB / service-side readback",
    ),
    "governance/agent-system-cross-project-alignment.v1.md": (
        "Registered Source Archetype Capability Absorption",
        "source archetype",
        "capability pack",
        "controller / production control-plane project",
        "subproject / implementation repo",
        "runtime-service / ops-agent",
        "data-model / evaluation project",
        "knowledge-base / domain-governance project",
        "lightweight repo",
        "local-operations-diagnostics",
        "owner-first memory",
        "evaluation-scheme-design",
        "admission / lease / heartbeat",
        "tool-specific thin adapter",
        "minimum viable governance profile",
        "Production Control-Plane Delta Decision",
        "performance-bandwidth-analysis",
        "runtime-config-switch",
        "agent-finalizer",
        "external-write-boundary",
        "acceptance-governance",
        "long-task-progress",
        "production readback",
        "DB readback",
        "不新增通用业务 skill",
    ),
    "governance/wiki-governance-system-contract.v1.md": (
        "实战控制面吸收要求",
        "注册表全工程吸收要求",
        "registry-driven",
        "每一行",
        "performance-bandwidth-analysis",
        "runtime-config-switch",
        "agent-control-plane-hardening",
        "DB readback",
        "不新增通用 skill",
    ),
    "skills/performance-bandwidth-analysis/SKILL.md": (
        "Performance Bandwidth Analysis",
        "timing ledger",
        "coverage matrix",
        "production",
        "service-side readback",
        "不可上推",
    ),
    "skills/performance-bandwidth-analysis/TRANSFER.md": (
        "## 可以吸收",
        "## 只能抽象吸收",
        "## 禁止复制",
        "## 目标工程结构自检",
    ),
    "skills/runtime-config-switch/SKILL.md": (
        "Runtime Config Switch",
        "live service",
        "default path proof",
        "service registry",
        "rollback",
    ),
    "skills/runtime-config-switch/TRANSFER.md": (
        "## 可以吸收",
        "## 只能抽象吸收",
        "## 禁止复制",
        "## 目标工程结构自检",
    ),
    "skills/README.md": (
        "performance-bandwidth-analysis",
        "runtime-config-switch",
        "agent-finalizer / external-write-boundary / acceptance-governance / long-task-progress",
        "registry-driven 全工程逐行吸收边界",
    ),
    "skills/cross-project-governance-audit/SKILL.md": (
        "举一反三",
        "source registry",
        "逐工程审计",
        "system-layer capability",
        "project-bound fact",
    ),
    "scripts/check_all.py": (
        "agent-control-plane-hardening",
        "check_agent_control_plane_hardening.py",
    ),
}


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel, terms in REQUIRED_TERMS.items():
        path = repo / rel
        if not path.exists():
            errors.append(f"{rel}: missing required file")
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel}: missing required term {term!r}")

    if errors:
        print("FAILED: agent control-plane hardening wiring issues found", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("OK: agent control-plane hardening owners, skills, transfer guards, and sensor wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

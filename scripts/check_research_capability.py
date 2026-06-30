#!/usr/bin/env python3
"""Validate research-capability aggregate wiring."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "skills/research-capability/SKILL.md",
    "skills/research-capability/TRANSFER.md",
    "skills/research-capability/reference/research-method-route-map.md",
    "skills/technology-research/SKILL.md",
    "skills/technology-research/TRANSFER.md",
    "governance/research-capability-rules.md",
    "templates/technology-research-contract-template.md",
    "templates/technology-research-report-template.md",
    "templates/technology-research-evidence-matrix-template.md",
    "templates/technology-research-adoption-contract-template.md",
    "templates/research-intake-template.md",
    "skills/README.md",
    "README.md",
    "INDEX.md",
)

REQUIRED_TERMS = {
    "skills/research-capability/SKILL.md": (
        "聚合入口",
        "technology-research",
        "证据等级",
        "行动等级",
        "当前性审计",
        "不平铺外部 13 个子项",
        "So-What",
        "counter-evidence",
        "deal-breaker",
        "decision output",
        "更新机制",
        "深度等级",
        "Path ROOT",
        "行动 owner",
        "完成口径",
        "持久化",
        "Frontier Technology Intake",
        "Frontier Tech Intake",
        "Research Intake",
        "source package",
        "A3 compensation",
        "knowledge-linking",
        "research-method-route-map",
    ),
    "skills/research-capability/reference/research-method-route-map.md": (
        "Research Method Route Map",
        "R0 线索",
        "R4 尽调 / 接入",
        "子项路由",
        "结构化判断",
        "竞争情报",
        "尽职调查",
        "科研方法",
        "战略前瞻",
        "溯源入口",
        "反证面",
        "风险门",
        "行动兑现",
    ),
    "skills/technology-research/SKILL.md": (
        "So-What",
        "counter-evidence",
        "deal-breaker",
        "decision output",
        "刷新触发",
        "R0",
        "R4",
        "溯源入口",
    ),
    "skills/research-capability/TRANSFER.md": (
        "能力目标",
        "可以吸收",
        "只能抽象吸收",
        "禁止复制",
        "目标工程结构自检",
        "验证要求",
        "Frontier Technology Intake",
        "source package",
        "A3 compensation",
        "不复制",
    ),
    "templates/research-intake-template.md": (
        "Research Intake Template",
        "Intake Contract",
        "frontier_tech_intake",
        "Frontier Tech Intake",
        "Frontier Tech Intake source",
        "source_type",
        "access_boundary",
        "capture_method",
        "extraction_quality",
        "Intelligence Contract",
        "parser_agent",
        "evaluator_oracle",
        "evidence_level",
        "evidence level",
        "Decision Asset Gate",
        "So-What",
        "counter-evidence",
        "deal-breaker",
        "decision_output",
        "staleness / update trigger",
        "refresh trigger / update mechanism",
        "depth_level",
        "深度等级",
        "Path ROOT",
        "行动 owner",
        "检查方式",
        "完成口径",
        "A3 Compensation",
        "Writeback",
        "refresh_trigger",
    ),
    "governance/research-capability-rules.md": (
        "证据等级",
        "行动等级",
        "必须查证当前事实",
        "沉淀落位",
    ),
    "skills/README.md": (
        "research-capability",
        "technology-research",
    ),
    "README.md": (
        "research-capability",
        "technology-research",
    ),
    "INDEX.md": (
        "research-capability",
        "technology-research",
    ),
}


def main() -> int:
    errors: list[str] = []
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing research-capability file: {rel_path}")

    for rel_path, terms in REQUIRED_TERMS.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel_path} missing research-capability term: {term}")

    if errors:
        print("Research capability validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Research capability validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

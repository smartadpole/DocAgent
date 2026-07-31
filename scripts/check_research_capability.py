#!/usr/bin/env python3
"""Validate research-capability wiring and executable research contracts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ".codex/research-capability-profile.md"
FIXTURE_ROOT = ROOT / "scripts/fixtures/research-capability"
CONTRACT_REVISION = "research-contract.v1"

REQUIRED_FILES = (
    PROFILE,
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

POSITIVE_FIXTURES = (
    "positive-r3-trial.v1.json",
    "positive-evidence-delta-adopt.v1.json",
)

NEGATIVE_FIXTURES = (
    "negative-r3-without-source-plan.v1.json",
    "negative-adopt-without-validation.v1.json",
    "negative-production-adopt-without-runtime.v1.json",
    "negative-evidence-delta-without-reopen.v1.json",
)

REQUIRED_TERMS = {
    PROFILE: (
        "research_level: strong-template-kernel",
        "contract_revision: research-contract.v1",
        "upstream_owner: AcknowledgeBase",
        "R2+ Source Plan checkpoint",
        "Evidence Delta Re-open",
        "evaluation loop",
        "second upstream truth source",
    ),
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
        "strong-template-kernel",
        "Source Plan checkpoint",
        "coverage matrix",
        "Evidence Delta Re-open",
        "Research Case Packet",
        "Revision Brief",
        "Delta Source Plan",
        "outcome review",
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
        "Source Plan checkpoint",
        "coverage matrix",
        "Evidence Delta Re-open",
        "Revision Brief",
        "Delta Source Plan",
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
        "Source Plan checkpoint",
        "coverage matrix",
        "Evidence Delta Re-open",
        "Revision Brief",
        "Delta Source Plan",
        "outcome review",
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
        "Strong Template Kernel",
        "R2+ Source Plan",
        "Evidence Delta Re-open",
        "验证与评价循环",
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


def require_non_empty(mapping: dict, fields: tuple[str, ...], code: str, errors: list[str]) -> None:
    for field in fields:
        value = mapping.get(field)
        if value in (None, "", [], {}):
            errors.append(f"{code}:{field}")


def validate_case(case: dict) -> list[str]:
    """Return stable error codes for one structured research contract."""
    errors: list[str] = []
    depth = case.get("depth")
    action_level = case.get("action_level")
    claim_scope = case.get("claim_scope")
    source_plan = case.get("source_plan") or {}
    coverage = case.get("coverage_matrix") or []
    evidence_delta = case.get("evidence_delta") or {}
    validation = case.get("validation") or {}
    evaluation = case.get("evaluation") or {}

    require_non_empty(
        case,
        (
            "case_id",
            "contract_revision",
            "research_level",
            "depth",
            "claim_scope",
            "action_level",
            "so_what",
            "decision_output",
            "deal_breakers",
        ),
        "CONTRACT_REQUIRED",
        errors,
    )
    if case.get("research_level") != "strong-template-kernel":
        errors.append("PROFILE_NOT_STRONG_TEMPLATE_KERNEL")
    if case.get("contract_revision") != CONTRACT_REVISION:
        errors.append("CONTRACT_REVISION_INVALID")
    if depth not in {"R0", "R1", "R2", "R3", "R4"}:
        errors.append("DEPTH_INVALID")
    if action_level not in {"Adopt", "Trial", "Assess", "Hold", "Blocked"}:
        errors.append("ACTION_LEVEL_INVALID")
    if claim_scope not in {
        "knowledge",
        "design",
        "implementation",
        "production",
        "procurement",
        "compliance",
    }:
        errors.append("CLAIM_SCOPE_INVALID")

    if depth in {"R2", "R3", "R4"}:
        if source_plan.get("checkpoint") != "pass":
            errors.append("R2_SOURCE_PLAN_CHECKPOINT")
        require_non_empty(
            source_plan,
            (
                "required_l1",
                "coverage_target",
                "contradiction_plan",
                "access_boundary",
                "stop_condition",
                "owner",
            ),
            "R2_SOURCE_PLAN_REQUIRED",
            errors,
        )
        if not coverage:
            errors.append("R2_COVERAGE_MATRIX_REQUIRED")

    for index, row in enumerate(coverage):
        require_non_empty(
            row,
            ("question_id", "status", "supporting_evidence", "counter_evidence"),
            f"COVERAGE_ROW_{index}",
            errors,
        )
        if row.get("status") not in {"covered", "partial", "blocked"}:
            errors.append(f"COVERAGE_ROW_{index}:invalid_status")

    if evidence_delta.get("triggered"):
        if evidence_delta.get("materiality") not in {
            "duplicate",
            "clarification",
            "conclusion-changing",
            "architecture-changing",
        }:
            errors.append("EVIDENCE_DELTA_MATERIALITY")
        require_non_empty(
            evidence_delta,
            ("external_verification", "new_counter_evidence", "propagation_results"),
            "EVIDENCE_DELTA_REOPEN",
            errors,
        )
        if evidence_delta.get("conclusion_recomputed") is not True:
            errors.append("EVIDENCE_DELTA_REOPEN:conclusion_recomputed")

    evidence_levels = set(case.get("evidence_levels") or [])
    if action_level == "Adopt":
        if "L1" not in evidence_levels:
            errors.append("ADOPT_L1_REQUIRED")
        if validation.get("local_validation") is not True:
            errors.append("ADOPT_LOCAL_VALIDATION_REQUIRED")
        if claim_scope == "production" and validation.get("runtime_readback") is not True:
            errors.append("ADOPT_RUNTIME_READBACK_REQUIRED")
        if evaluation.get("outcome_review") != "passed":
            errors.append("ADOPT_OUTCOME_REVIEW_REQUIRED")
        if any(row.get("status") != "covered" for row in coverage):
            errors.append("ADOPT_COVERAGE_INCOMPLETE")

    require_non_empty(
        evaluation,
        ("deterministic_validator", "evaluator_provenance", "outcome_review", "next_run_decision"),
        "EVALUATION_REQUIRED",
        errors,
    )
    if evaluation.get("evaluator_provenance") == "builder-self":
        errors.append("INDEPENDENT_EVALUATOR_REQUIRED")
    if evaluation.get("outcome_review") not in {"passed", "failed", "unproven"}:
        errors.append("OUTCOME_REVIEW_INVALID")
    if evaluation.get("outcome_review") == "failed":
        require_non_empty(
            evaluation,
            ("revision_brief", "delta_source_plan"),
            "REVISION_LOOP_REQUIRED",
            errors,
        )

    return sorted(set(errors))


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def validate_fixtures(errors: list[str]) -> None:
    for name in POSITIVE_FIXTURES:
        path = FIXTURE_ROOT / name
        if not path.exists():
            errors.append(f"missing positive research fixture: {path.relative_to(ROOT)}")
            continue
        case_errors = validate_case(load_json(path))
        if case_errors:
            errors.append(f"positive fixture {name} failed: {', '.join(case_errors)}")

    for name in NEGATIVE_FIXTURES:
        path = FIXTURE_ROOT / name
        if not path.exists():
            errors.append(f"missing negative research fixture: {path.relative_to(ROOT)}")
            continue
        case = load_json(path)
        expected = set(case.pop("expected_errors", []))
        actual = set(validate_case(case))
        missing = sorted(expected - actual)
        if missing:
            errors.append(f"negative fixture {name} missed errors: {', '.join(missing)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        default=[],
        help="Validate a structured research-case JSON file; may be repeated.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.case:
        failed = False
        for raw_path in args.case:
            path = Path(raw_path)
            case_errors = validate_case(load_json(path))
            if case_errors:
                failed = True
                print(f"Research contract invalid: {path}")
                for error in case_errors:
                    print(f"- {error}")
            else:
                print(f"Research contract valid: {path}")
        return 1 if failed else 0

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

    validate_fixtures(errors)

    if errors:
        print("Research capability validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Research capability wiring and structured contract fixtures passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

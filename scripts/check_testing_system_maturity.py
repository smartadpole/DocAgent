#!/usr/bin/env python3
"""Check testing, acceptance, and release guardrail wiring."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "concepts/software-testing-acceptance-release.md",
    "projects/development/plan/test-acceptance-planning-model.md",
    "projects/development/acceptance/README.md",
    "projects/development/acceptance/plans/README.md",
    "projects/development/reports/README.md",
    "templates/development-acceptance-plan-template.md",
    "templates/development-test-report-template.md",
    "scripts/check_all.py",
)

CONCEPT_REQUIRED_TERMS = (
    "环境是证据面，不是荣誉阶梯",
    "环境命名应抽象成角色",
    "开发环境",
    "CI 环境",
    "集成环境",
    "预发 / 灰度环境",
    "生产环境",
    "外部依赖 / 读回源",
)

PLANNING_TERMS = (
    "## 成熟度升级：从规则到系统",
    "AP 覆盖审计",
    "环境路由一致性检查",
    "非功能测试矩阵",
    "fixture / oracle 台账",
    "人工确认覆盖表",
    "发布 runbook / rollback checklist",
    "测试质量指标",
    "规则存在但没有 sensor / 模板字段 / 报告字段承接",
)

ACCEPTANCE_TERMS = (
    "## 覆盖审计入口",
    "AP 覆盖",
    "用例覆盖",
    "非功能覆盖",
    "fixture / oracle 覆盖",
    "人工确认覆盖",
    "发布覆盖",
    "scripts/check_testing_system_maturity.py",
)

PLANS_TERMS = (
    "## AP 覆盖审计",
    "L2",
    "L3",
    "AP 缺失",
    "目标事项未回链",
    "报告没有计划来源",
    "release checklist",
)

REPORTS_TERMS = (
    "计划来源",
    "## 测试质量指标",
    "AP 覆盖率",
    "复验失败率",
    "逃逸缺陷",
    "回归守卫入驻率",
    "环境上推违规",
    "## 数据、fixture 和 oracle 治理",
    "没有 oracle 的执行结果只能写成观察",
)

TEMPLATE_TERMS = (
    "target_items",
    "报告落点",
    "## Fixture / Oracle",
    "## 人工确认",
    "## 上推边界",
)

CHECK_ALL_TERMS = (
    "testing-system-maturity",
    "scripts/check_testing_system_maturity.py",
)


def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required testing-system-maturity file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing testing-system-maturity term {term}")


def strip_wikilinks(text: str) -> str:
    return re.sub(r"\[\[[^\]]+\]\]", "", text)


def check_ap_files(repo: Path, errors: list[str]) -> None:
    ap_root = repo / "projects/development/acceptance/plans"
    if not ap_root.exists():
        errors.append("projects/development/acceptance/plans: missing AP root")
        return

    for path in sorted(ap_root.glob("AP-*.md")):
        rel = path.relative_to(repo).as_posix()
        text = path.read_text(encoding="utf-8")
        for term in ("target_items:", "报告落点", "## 上推边界"):
            if term not in text:
                errors.append(f"{rel}: AP must declare {term}")
        if re.search(r"默认不需要[^。\n]*(?:但|如果|若|如需)", strip_wikilinks(text)):
            errors.append(f"{rel}: AP environment route must be single-valued")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (repo / rel).exists():
            errors.append(f"{rel}: required testing-system-maturity file is missing")

    file_terms = {
        "concepts/software-testing-acceptance-release.md": CONCEPT_REQUIRED_TERMS,
        "projects/development/plan/test-acceptance-planning-model.md": PLANNING_TERMS,
        "projects/development/acceptance/README.md": ACCEPTANCE_TERMS,
        "projects/development/acceptance/plans/README.md": PLANS_TERMS,
        "projects/development/reports/README.md": REPORTS_TERMS,
        "templates/development-acceptance-plan-template.md": TEMPLATE_TERMS,
        "scripts/check_all.py": CHECK_ALL_TERMS,
    }
    for rel, terms in file_terms.items():
        text = read_text(repo, rel, errors)
        if text:
            require_terms(rel, text, terms, errors)

    report_template = read_text(repo, "templates/development-test-report-template.md", errors)
    if report_template:
        require_terms(
            "templates/development-test-report-template.md",
            report_template,
            ("计划来源 / AP", "fixture / oracle", "不上推边界 / 禁止上推边界"),
            errors,
        )

    check_ap_files(repo, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} testing-system-maturity issue(s)", file=sys.stderr)
        return 1
    print("OK: testing system maturity wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Check work-item governance wiring for the wiki.

The check intentionally validates structure first: required files, exact matrix
columns, template field labels, required sections, and entrypoint links. A small
set of phrase checks remains for conceptual invariants that are hard to express
as a markdown structure.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "projects/development/plan/README.md",
    "projects/development/plan/work-item-system-model.md",
    "projects/development/plan/task-design-model.md",
    "projects/development/execution/execution-packages/README.md",
    "projects/development/execution/tasks/README.md",
    "projects/development/execution/developer-execution-workflow.md",
    "projects/development/issues/README.md",
    "projects/development/reports/README.md",
    "projects/service-registry.md",
    "templates/development-work-item-matrix-template.md",
    "templates/development-execution-package-template.md",
    "templates/development-task-template.md",
    "templates/development-issue-template.md",
    "templates/development-test-report-template.md",
    "templates/service-registry-template.md",
    "templates/code-handoff-template.md",
    "templates/developer-task-brief-template.md",
)

CONCEPT_TERMS: dict[str, tuple[str, ...]] = {
    "projects/development/plan/work-item-system-model.md": (
        "Gate -> FP -> EP -> TASK",
        "Issue 是案件档案",
        "报告是每次庭审记录",
        "服务台账",
    ),
    "projects/development/plan/task-design-model.md": (
        "状态化交付合同",
        "Done Contract",
    ),
    "projects/development/issues/README.md": (
        "Issue 是案件档案",
        "报告是每次庭审记录",
        "latest valid report",
    ),
    "projects/development/reports/README.md": (
        "Issue 是案件档案",
        "报告是每次庭审记录",
        "local validation",
        "service-side validation",
        "end-to-end validation",
    ),
    "projects/service-registry.md": (
        "UI / API",
        "config_path_key",
        "config_restore",
        "ui_api_contract",
    ),
    "projects/development/execution/developer-execution-workflow.md": (
        "Gate / FP / EP / TASK",
        "只读上下文模式",
        "受控回写模式",
        "无写权限回传模式",
    ),
}

REQUIRED_HEADINGS: dict[str, tuple[str, ...]] = {
    "projects/development/plan/README.md": (
        "## 维护者入口顺序",
        "## 目录职责",
        "## 维护规则",
    ),
    "projects/development/plan/work-item-system-model.md": (
        "## 总体链路",
        "## 事项类型",
        "## 关系节点覆盖",
        "## EP 和 TASK 分工",
        "## Issue 与报告分工",
        "## 关系矩阵",
        "## 关闭守卫",
    ),
    "projects/development/plan/task-design-model.md": (
        "## 设计决策",
        "## 标准结构",
        "## 状态填充规则",
    ),
    "projects/development/execution/developer-execution-workflow.md": (
        "## 主控和实现工程协作边界",
        "## 最短使用方式",
        "## 单功能开发闭环",
        "## 代码工程回传包",
        "## 写权限模式",
    ),
    "projects/development/issues/README.md": (
        "## Issue 与报告分工",
        "## 创建边界",
        "## 维护规则",
    ),
    "projects/development/reports/README.md": (
        "## 报告规则",
        "## 验收执行包触发矩阵",
        "## 最小报告骨架",
    ),
}

MATRIX_COLUMNS = (
    "上游需求 / 目标",
    "Gate",
    "功能点 / 候选项",
    "EP",
    "TASK",
    "子工程增量",
    "关系类型",
    "主责模块",
    "当前状态",
    "输出物",
    "关闭证据",
    "回归守卫",
    "关系节点覆盖",
    "反馈回写",
    "未确认项",
    "备注",
)

TEMPLATE_FIELDS: dict[str, tuple[str, ...]] = {
    "templates/development-execution-package-template.md": (
        "上游需求 / 目标",
        "父 Gate",
        "父 FP",
        "主责模块",
        "risk",
        "issue",
        "test / 报告",
        "验收",
        "issue-trigger",
        "local validation",
        "service-side validation",
        "end-to-end validation",
        "不上推边界",
        "service registry",
    ),
    "templates/development-task-template.md": (
        "父 EP",
        "上游 Gate / FP",
        "目标",
        "范围",
        "不做项",
        "local validation",
        "service-side validation",
        "end-to-end validation",
        "issue-trigger",
        "回归守卫",
        "service registry",
    ),
    "templates/development-issue-template.md": (
        "用户可见症状",
        "复现路径",
        "根因边界",
        "EP",
        "TASK",
        "最新有效报告",
        "未验证边界",
        "关闭结论",
    ),
    "templates/development-test-report-template.md": (
        "上游 EP / TASK / FP / Gate / ISSUE",
        "验收执行包类型",
        "local validation",
        "service-side validation",
        "end-to-end validation",
        "本轮独立取证动作",
        "服务组 / 服务台账证据",
        "不上推边界 / 禁止上推边界",
        "回归守卫入驻",
    ),
    "templates/service-registry-template.md": (
        "service_id",
        "components",
        "config_profile",
        "config_path_key",
        "config_restore",
        "ui_api_contract",
        "health_check",
        "last_verified_at",
    ),
    "templates/code-handoff-template.md": (
        "对应 Gate",
        "对应 FP / 候选 ID",
        "对应 EP",
        "对应 TASK",
        "对应 ISSUE / issue-trigger",
        "父 EP Done Contract 对齐",
        "TASK Done Contract 完成情况",
        "服务台账 / UI API / 配置回写",
        "关闭判断和不上推边界",
    ),
    "templates/developer-task-brief-template.md": (
        "对应 Gate",
        "功能点 / 候选项",
        "父 EP",
        "TASK",
        "ISSUE / issue-trigger",
        "父 EP Done Contract",
        "TASK Done Contract",
        "服务台账 / UI API / 配置要求",
        "不上推边界",
    ),
}

ENTRYPOINT_LINKS: dict[str, tuple[str, ...]] = {
    "README.md": (
        "[[projects/development/plan/work-item-system-model]]",
        "[[projects/service-registry]]",
    ),
    "INDEX.md": (
        "[[projects/development/plan/work-item-system-model]]",
        "[[projects/development/plan/task-design-model]]",
        "[[projects/development/execution/execution-packages/README]]",
        "[[projects/development/execution/tasks/README]]",
        "[[projects/development/issues/README]]",
    ),
    "projects/README.md": (
        "[[projects/development/plan/work-item-system-model]]",
        "[[projects/development/plan/task-design-model]]",
        "[[projects/development/execution/execution-packages/README]]",
        "[[projects/development/execution/tasks/README]]",
        "[[projects/development/issues/README]]",
    ),
    "templates/README.md": (
        "[[templates/development-execution-package-template]]",
        "[[templates/development-task-template]]",
        "[[templates/development-issue-template]]",
        "[[templates/code-handoff-template]]",
        "[[templates/developer-task-brief-template]]",
    ),
    "governance/WORKFLOW.md": (
        "projects/development/plan/README.md#维护者入口顺序",
        "python3 scripts/check_all.py --only work-item-matrix",
    ),
}

STRICT_TERMS: dict[str, tuple[str, ...]] = {
    "AGENTS.md": ("Gate -> FP -> EP -> TASK", "work-item-matrix", "Issue 案件"),
    "governance/POLICY.md": ("Gate -> FP -> EP -> TASK", "Issue 是案件档案", "服务台账"),
}

FORBIDDEN_MAIN_LOOP_PHRASES = (
    "TODO / FP",
    "TODO / Gate",
    "TODO / FP / Gate",
    "TODO / 测试报告",
    "TODO / worklog",
    "测试报告 / TODO / FP",
    "不关闭 TODO",
    "关闭 TODO",
    "TODO 状态",
    "TODO / FP / Gate / release",
    "需求 / TODO / FP / Gate",
    "处理本库 TODO / FP",
    "相关 TODO / FP / Gate",
    "实现 / 测试 -> TODO",
    "设计、TODO 或测试报告",
    "设计、TODO、测试报告",
    "设计、TODO、测试报告或服务台账",
    "设计包、功能点、TODO",
    "影响 TODO 关闭",
    "关联 TODO",
    "来源 TODO / 候选项",
    "功能点成为最小执行单位",
    "以功能点作为最小执行单位",
)

FORBIDDEN_SCAN_FILES = (
    "AGENTS.md",
    "governance/BRAIN.md",
    "governance/POLICY.md",
    "governance/WORKFLOW.md",
    "governance/response-mode-routing.md",
    "projects/development/execution/engineering-feedback-loop.md",
    "projects/development/execution/worklog.md",
    "projects/decisions.md",
    "projects/trace.md",
    "templates/development-feature-point-template.md",
    "templates/development-gate-template.md",
    "templates/skill-template.md",
)


def read_text(repo: Path, rel_path: str, errors: list[str]) -> str:
    path = repo / rel_path
    if not path.exists():
        errors.append(f"{rel_path}: missing file")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(repo: Path, rel_path: str, terms: tuple[str, ...], errors: list[str]) -> None:
    text = read_text(repo, rel_path, errors)
    if not text:
        return
    for term in terms:
        if term not in text:
            errors.append(f"{rel_path}: missing required term {term!r}")


def require_headings(repo: Path, rel_path: str, headings: tuple[str, ...], errors: list[str]) -> None:
    text = read_text(repo, rel_path, errors)
    if not text:
        return
    for heading in headings:
        if not re.search(rf"^{re.escape(heading)}\s*$", text, flags=re.MULTILINE):
            errors.append(f"{rel_path}: missing heading {heading!r}")


def require_template_fields(repo: Path, rel_path: str, fields: tuple[str, ...], errors: list[str]) -> None:
    text = read_text(repo, rel_path, errors)
    if not text:
        return
    for field in fields:
        bullet_pattern = rf"^\s*-\s+`?{re.escape(field)}`?："
        if not re.search(bullet_pattern, text, flags=re.MULTILINE):
            errors.append(f"{rel_path}: missing template field {field!r}")


def parse_first_table_header(text: str, required_first_column: str) -> list[str]:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and required_first_column in stripped:
            return [part.strip() for part in stripped.strip("|").split("|")]
    return []


def require_matrix_columns(repo: Path, errors: list[str]) -> None:
    rel_path = "templates/development-work-item-matrix-template.md"
    text = read_text(repo, rel_path, errors)
    if not text:
        return
    header = parse_first_table_header(text, "上游需求 / 目标")
    if not header:
        errors.append(f"{rel_path}: missing matrix header row")
        return
    if tuple(header) != MATRIX_COLUMNS:
        errors.append(
            f"{rel_path}: matrix columns changed; expected {MATRIX_COLUMNS!r}, got {tuple(header)!r}"
        )


def require_table_columns(repo: Path, rel_path: str, first_column: str, columns: tuple[str, ...], errors: list[str]) -> None:
    text = read_text(repo, rel_path, errors)
    if not text:
        return
    header = parse_first_table_header(text, first_column)
    if not header:
        errors.append(f"{rel_path}: missing table header with first column {first_column!r}")
        return
    missing = [column for column in columns if column not in header]
    if missing:
        errors.append(f"{rel_path}: table missing column(s): {', '.join(missing)}")


def forbid_legacy_main_loop_phrases(repo: Path, errors: list[str]) -> None:
    for rel_path in FORBIDDEN_SCAN_FILES:
        text = read_text(repo, rel_path, errors)
        if not text:
            continue
        for phrase in FORBIDDEN_MAIN_LOOP_PHRASES:
            if phrase in text:
                errors.append(f"{rel_path}: legacy TODO/FP main-loop phrase remains: {phrase!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Run strict entrypoint checks.")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel_path in REQUIRED_FILES:
        read_text(repo, rel_path, errors)

    for rel_path, terms in CONCEPT_TERMS.items():
        require_terms(repo, rel_path, terms, errors)

    for rel_path, headings in REQUIRED_HEADINGS.items():
        require_headings(repo, rel_path, headings, errors)

    for rel_path, fields in TEMPLATE_FIELDS.items():
        require_template_fields(repo, rel_path, fields, errors)

    require_matrix_columns(repo, errors)
    require_table_columns(
        repo,
        "projects/development/reports/README.md",
        "触发信号",
        ("触发信号", "必须启动的验收执行包", "最小证据链", "不足时状态上限"),
        errors,
    )
    require_table_columns(
        repo,
        "projects/development/execution/developer-execution-workflow.md",
        "协作环节",
        ("协作环节", "主控系统职责", "实现工程职责", "禁止事项"),
        errors,
    )
    forbid_legacy_main_loop_phrases(repo, errors)

    if args.strict:
        for rel_path, links in ENTRYPOINT_LINKS.items():
            require_terms(repo, rel_path, links, errors)
        for rel_path, terms in STRICT_TERMS.items():
            require_terms(repo, rel_path, terms, errors)

    if errors:
        print("FAILED: work item governance structural issues found", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("OK: work item governance structure looks consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

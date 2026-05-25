#!/usr/bin/env python3
"""Check work-item governance wiring for the wiki."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = (
    "projects/development/plan/work-item-system-model.md",
    "projects/development/plan/task-design-model.md",
    "projects/development/execution/execution-packages/README.md",
    "projects/development/execution/tasks/README.md",
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
    "projects/development/execution/developer-execution-workflow.md",
)

REQUIRED_TERMS: dict[str, tuple[str, ...]] = {
    "projects/development/plan/work-item-system-model.md": (
        "Gate -> FP -> EP -> TASK",
        "risk:",
        "test:",
        "验收:",
        "issue-trigger:",
        "Issue 是案件档案",
        "报告是每次庭审记录",
        "服务台账",
    ),
    "projects/development/plan/task-design-model.md": (
        "父级 EP",
        "状态化交付合同",
        "Done Contract",
        "issue-trigger",
        "回归守卫",
    ),
    "projects/development/execution/execution-packages/README.md": (
        "EP 是 Execution Package",
        "父 EP",
        "TASK",
        "risk",
        "issue",
        "test",
        "验收",
    ),
    "projects/development/execution/tasks/README.md": (
        "父级 EP",
        "状态化交付合同",
        "Done Contract",
        "issue-trigger",
        "回归守卫",
    ),
    "projects/development/issues/README.md": (
        "原始现象",
        "Issue 是案件档案",
        "报告是每次庭审记录",
        "latest valid report",
        "issue-trigger",
    ),
    "projects/development/reports/README.md": (
        "Issue 是案件档案",
        "报告是每次庭审记录",
        "local validation",
        "service-side validation",
        "end-to-end validation",
        "服务组",
    ),
    "projects/service-registry.md": (
        "UI / API",
        "config_path_key",
        "config_restore",
        "ui_api_contract",
        "服务组",
    ),
    "templates/development-work-item-matrix-template.md": (
        "Gate -> FP -> EP -> TASK",
        "EP",
        "TASK",
        "关系节点覆盖",
        "issue-trigger",
    ),
    "templates/development-execution-package-template.md": (
        "父 Gate",
        "父 FP",
        "包内 TASK",
        "Done Contract",
        "issue-trigger",
    ),
    "templates/development-task-template.md": (
        "父 EP",
        "Done Contract",
        "关系校准",
        "issue-trigger",
        "回归守卫",
    ),
    "templates/development-issue-template.md": (
        "原始现象",
        "分层事实",
        "最新有效报告",
        "关闭裁决",
    ),
    "templates/development-test-report-template.md": (
        "上游 EP / TASK / FP / Gate / ISSUE",
        "验收执行包类型",
        "独立取证",
        "服务台账",
        "不上推边界",
    ),
    "templates/service-registry-template.md": (
        "config_path_key",
        "config_restore",
        "ui_api_contract",
        "UI / API",
    ),
    "templates/code-handoff-template.md": (
        "对应 EP",
        "对应 TASK",
        "对应 ISSUE / issue-trigger",
        "TASK Done Contract",
        "服务台账",
        "不上推边界",
    ),
    "templates/developer-task-brief-template.md": (
        "父 EP",
        "TASK",
        "ISSUE / issue-trigger",
        "TASK Done Contract",
        "服务台账",
        "不上推边界",
    ),
    "projects/development/execution/developer-execution-workflow.md": (
        "Gate / FP / EP / TASK",
        "父 EP",
        "TASK Done Contract",
        "服务台账",
        "上推边界",
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

ENTRYPOINT_TERMS: dict[str, tuple[str, ...]] = {
    "AGENTS.md": ("Gate -> FP -> EP -> TASK", "work-item-matrix", "Issue 案件"),
    "governance/WORKFLOW.md": ("work-item-matrix", "EP 执行包", "TASK 任务", "已发生 Issue"),
    "governance/POLICY.md": ("Gate -> FP -> EP -> TASK", "Issue 是案件档案", "服务台账"),
    "README.md": ("Gate、FP、EP、TASK", "服务台账"),
    "INDEX.md": ("EP 执行包", "TASK 任务", "Issue 案件"),
    "projects/README.md": ("EP 执行包", "TASK 任务", "Issue 案件"),
    "projects/STRUCTURE.md": ("execution-packages", "issues/", "task-design-model.md"),
    "templates/README.md": ("development-execution-package-template", "development-task-template", "development-issue-template"),
}


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Run strict wiring checks.")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel_path in REQUIRED_FILES:
        read_text(repo, rel_path, errors)

    for rel_path, terms in REQUIRED_TERMS.items():
        require_terms(repo, rel_path, terms, errors)

    matrix = read_text(repo, "templates/development-work-item-matrix-template.md", errors)
    for column in MATRIX_COLUMNS:
        if column not in matrix:
            errors.append(f"templates/development-work-item-matrix-template.md: missing matrix column {column!r}")

    if args.strict:
        for rel_path, terms in ENTRYPOINT_TERMS.items():
            require_terms(repo, rel_path, terms, errors)

    if errors:
        print("FAILED: work item governance wiring issues found", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("OK: work item governance wiring looks consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

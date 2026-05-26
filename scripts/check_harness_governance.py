#!/usr/bin/env python3
"""Check Agent Harness routing and feedback-sensor wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "governance/response-mode-routing.md",
    "governance/instruction-adherence.md",
    "governance/execution-contract-semantics.md",
    "governance/harness-evolution.md",
    "governance/harness-feedback-ledger.md",
    "concepts/harness-engineering.md",
    "concepts/codex-goals.md",
    "templates/goal-contract-template.md",
    "templates/development-acceptance-plan-template.md",
    "templates/harness-adoption-template.md",
    "templates/harness-episode-package-template.md",
    "templates/harness-evolution-review-template.md",
    ".codex/AGENTS.md",
    "scripts/check_all.py",
    "scripts/check_testing_system_maturity.py",
    "scripts/check_execution_contract_semantics.py",
    "AGENTS.md",
    "governance/WORKFLOW.md",
    "governance/POLICY.md",
    "skills/issue-analysis/SKILL.md",
)

ENTRYPOINT_REFERENCES = (
    "README.md",
    "INDEX.md",
    "governance/README.md",
    "projects/README.md",
    "projects/STRUCTURE.md",
    "skills/README.md",
    "templates/README.md",
)

RESPONSE_MODES = (
    "快速诊断",
    "知识沉淀",
    "Issue 分析 + 沉淀",
    "验收关闭",
    "规则升级",
    "子工程实现 / 回传",
    "批处理",
)

ROUTING_REQUIRED_TERMS = (
    "confirmed / likely / possible / blocked",
    "先给最小可信 checkpoint",
    "读取预算",
    "输出节奏",
    "禁止项",
    "Harness 维护检查",
    "Goal Contract",
    "工作阶段",
    "sensor",
    "scripts/check_harness_governance.py",
    "scripts/check_all.py",
    "--only",
    "harness-evolution",
    "harness-feedback-ledger",
    "期望最终状态防跑偏",
    "验证面 / 证据边界防漂移",
    "预算 / 阻塞停止条件防无限探索",
    "响应模式判断之后、正式长时执行之前",
    "主控和子工程之间的长任务回传",
)

TEMPLATE_REQUIRED_SECTIONS = (
    "## 单一信息源",
    "## 写权限和边界",
    "## 响应模式路由",
    "## Goal Contract",
    "## 验证层级",
    "## Handoff 和回写",
    "## Feedback Sensors",
    "## 规则反哺",
)

EPISODE_TEMPLATE_REQUIRED_SECTIONS = (
    "## Goal Contract",
    "## 首次 Checkpoint",
    "## 执行轨迹",
    "## 证据边界",
    "## Harness 反馈",
)

EVOLUTION_TEMPLATE_REQUIRED_SECTIONS = (
    "## 统计窗口",
    "## Episode 样本",
    "## 趋势判断",
    "## 晋升 / 降级决策",
    "## Sensor Backlog",
)

ISSUE_SKILL_REQUIRED_TERMS = (
    "### 0. 先判响应模式",
    "是否需要升级",
    "不默认新建 issue",
)

CHECK_ALL_REQUIRED_TERMS = (
    "--only",
    "harness-governance",
    "testing-system-maturity",
    "execution-contract-semantics",
    "git-diff-whitespace",
    "git-staged-diff-whitespace",
)

H5_EVOLUTION_REQUIRED_TERMS = (
    "## H5 定义",
    "## Episode 数据",
    "## 规则晋升",
    "## 降级和删除",
    "## 工作节奏",
    "harness-feedback-ledger",
)

H5_LEDGER_REQUIRED_TERMS = (
    "## Episode Ledger",
    "## Sensor Backlog",
    "## Rule Promotion Queue",
    "## Rule Prune Queue",
    "DocCustomeranalysis Harness 反哺",
)

CODEX_ADAPTER_REQUIRED_TERMS = (
    "response-mode-routing",
    "instruction-adherence",
    "execution-contract-semantics",
    "harness-evolution",
    "harness-feedback-ledger",
    "Goal Contract",
    "scripts/check_all.py --only",
)

GOAL_CONTRACT_TEMPLATE_REQUIRED_SECTIONS = (
    "## 适用性判断",
    "## 完成契约",
    "## 迭代和停止",
    "## 证据审计",
    "## 主控 / 子工程分工",
)

GOAL_CONTRACT_TEMPLATE_REQUIRED_TERMS = (
    "防止任务跑偏",
    "防止证据漂移",
    "防止无限探索",
    "原始目标 / 用户最新目标",
    "完成判定",
    "探索分支上限",
    "阻塞后汇报格式",
    "辅助证据",
    "明确不足以闭环的证据",
    "health、日志、子工程自述或中间态误当成真正闭环",
    "响应模式判断之后、正式长时执行之前",
    "复杂 bug 复现、性能优化、迁移、跨轮调研、反复验证的修复、主控和子工程之间的长任务回传",
)


def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required harness file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def has_link_or_term(text: str, stem: str) -> bool:
    return stem in text or stem.replace("-", " ") in text


def check_required_files(repo: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (repo / rel).exists():
            errors.append(f"{rel}: required harness file is missing")
    return errors


def check_response_mode_routing(repo: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(repo, "governance/response-mode-routing.md", errors)
    if not text:
        return errors

    for mode in RESPONSE_MODES:
        if mode not in text:
            errors.append(f"governance/response-mode-routing.md: missing response mode {mode}")
    for term in ROUTING_REQUIRED_TERMS:
        if term not in text:
            errors.append(f"governance/response-mode-routing.md: missing harness routing term {term}")

    nonblank_lines = [line for line in text.splitlines() if line.strip()]
    if len(nonblank_lines) > 180:
        errors.append(
            "governance/response-mode-routing.md: routing page is too large; "
            "move details into WORKFLOW, skills, templates, or scripts"
        )
    return errors


def check_entrypoint_wiring(repo: Path) -> list[str]:
    errors: list[str] = []
    for rel in ENTRYPOINT_REFERENCES:
        text = read_text(repo, rel, errors)
        if not text:
            continue
        for stem in ("response-mode-routing", "harness-evolution"):
            if not has_link_or_term(text, stem):
                errors.append(f"{rel}: must link to {stem}")
    return errors


def check_rule_and_skill_wiring(repo: Path) -> list[str]:
    errors: list[str] = []
    agents = read_text(repo, "AGENTS.md", errors)
    workflow = read_text(repo, "governance/WORKFLOW.md", errors)
    policy = read_text(repo, "governance/POLICY.md", errors)
    skill = read_text(repo, "skills/issue-analysis/SKILL.md", errors)

    if agents:
        for term in ("每轮动手前先按", "快速诊断", "显式告诉用户", "harness-feedback-ledger"):
            if term not in agents:
                errors.append(f"AGENTS.md: missing response routing or H5 guard {term}")
        if "| 模式 |" in agents:
            errors.append("AGENTS.md: must stay a short guard, not duplicate the response mode table")

    if workflow:
        for term in ("### 0.0 响应模式路由", "模式切换要显式说明", "scripts/check_all.py", "Harness episode"):
            if term not in workflow:
                errors.append(f"governance/WORKFLOW.md: missing response workflow or H5 term {term}")

    if policy:
        for term in ("不得用同一套重治理动作覆盖所有问题", "快速诊断模式默认不写项目状态", "episode"):
            if term not in policy:
                errors.append(f"governance/POLICY.md: missing response policy or H5 guard {term}")

    if skill:
        for term in ISSUE_SKILL_REQUIRED_TERMS:
            if term not in skill:
                errors.append(f"skills/issue-analysis/SKILL.md: missing issue-analysis routing term {term}")

    return errors


def check_concept_and_template(repo: Path) -> list[str]:
    errors: list[str] = []
    concept = read_text(repo, "concepts/harness-engineering.md", errors)
    template = read_text(repo, "templates/harness-adoption-template.md", errors)
    goal_template = read_text(repo, "templates/goal-contract-template.md", errors)
    episode_template = read_text(repo, "templates/harness-episode-package-template.md", errors)
    evolution_template = read_text(repo, "templates/harness-evolution-review-template.md", errors)

    if concept:
        for term in ("Agent = Model + Harness", "Scripts / Sensors", "harness-evolution", "goal-contract-template"):
            if term not in concept:
                errors.append(f"concepts/harness-engineering.md: missing harness concept term {term}")

    if template:
        for section in TEMPLATE_REQUIRED_SECTIONS:
            if section not in template:
                errors.append(f"templates/harness-adoption-template.md: missing section {section}")
    if goal_template:
        for section in GOAL_CONTRACT_TEMPLATE_REQUIRED_SECTIONS:
            if section not in goal_template:
                errors.append(f"templates/goal-contract-template.md: missing section {section}")
        for term in GOAL_CONTRACT_TEMPLATE_REQUIRED_TERMS:
            if term not in goal_template:
                errors.append(f"templates/goal-contract-template.md: missing Goal Contract term {term}")
    if episode_template:
        for section in EPISODE_TEMPLATE_REQUIRED_SECTIONS:
            if section not in episode_template:
                errors.append(f"templates/harness-episode-package-template.md: missing section {section}")
    if evolution_template:
        for section in EVOLUTION_TEMPLATE_REQUIRED_SECTIONS:
            if section not in evolution_template:
                errors.append(f"templates/harness-evolution-review-template.md: missing section {section}")
    return errors


def check_quality_gate_script(repo: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(repo, "scripts/check_all.py", errors)
    if text:
        for term in CHECK_ALL_REQUIRED_TERMS:
            if term not in text:
                errors.append(f"scripts/check_all.py: missing staged work-phase gate term {term}")
    return errors


def check_h5_evolution(repo: Path) -> list[str]:
    errors: list[str] = []
    evolution = read_text(repo, "governance/harness-evolution.md", errors)
    ledger = read_text(repo, "governance/harness-feedback-ledger.md", errors)
    codex_adapter = read_text(repo, ".codex/AGENTS.md", errors)

    if evolution:
        for term in H5_EVOLUTION_REQUIRED_TERMS:
            if term not in evolution:
                errors.append(f"governance/harness-evolution.md: missing H5 term {term}")
    if ledger:
        for term in H5_LEDGER_REQUIRED_TERMS:
            if term not in ledger:
                errors.append(f"governance/harness-feedback-ledger.md: missing H5 ledger term {term}")
    if codex_adapter:
        for term in CODEX_ADAPTER_REQUIRED_TERMS:
            if term not in codex_adapter:
                errors.append(f".codex/AGENTS.md: missing Codex adapter term {term}")
    return errors


def check_instruction_and_semantics_wiring(repo: Path) -> list[str]:
    errors: list[str] = []
    instruction = read_text(repo, "governance/instruction-adherence.md", errors)
    semantics = read_text(repo, "governance/execution-contract-semantics.md", errors)

    if instruction:
        for term in ("Rule Coverage Ladder", "触发矩阵", "L5", "最终回复证明", "execution-contract-semantics"):
            if term not in instruction:
                errors.append(f"governance/instruction-adherence.md: missing instruction adherence term {term}")
    if semantics:
        for term in ("执行合同语义污染", "裁决必须单值", "非目标变潜在任务", "伪 optional", "证据层级回流"):
            if term not in semantics:
                errors.append(f"governance/execution-contract-semantics.md: missing semantics term {term}")
    return errors


def check_harness_governance(repo: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(check_required_files(repo))
    errors.extend(check_response_mode_routing(repo))
    errors.extend(check_entrypoint_wiring(repo))
    errors.extend(check_rule_and_skill_wiring(repo))
    errors.extend(check_concept_and_template(repo))
    errors.extend(check_quality_gate_script(repo))
    errors.extend(check_h5_evolution(repo))
    errors.extend(check_instruction_and_semantics_wiring(repo))
    return errors


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors = check_harness_governance(repo)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} harness governance issue(s)", file=sys.stderr)
        return 1
    print("OK: harness governance routing, H5 ledger, templates, and sensors checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

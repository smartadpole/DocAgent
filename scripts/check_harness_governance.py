#!/usr/bin/env python3
"""Check Agent Harness routing and feedback-sensor wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "governance/response-mode-routing.md",
    "governance/agent-governance-strategy.md",
    "governance/proactive-dialogue-system.md",
    "governance/instruction-adherence.md",
    "governance/execution-contract-semantics.md",
    "governance/harness-evolution.md",
    "governance/harness-feedback-ledger.md",
    "concepts/harness-engineering.md",
    "concepts/codex-goals.md",
    "templates/goal-contract-template.md",
    "templates/guided-discovery-session-template.md",
    "templates/development-acceptance-plan-template.md",
    "templates/harness-adoption-template.md",
    "templates/harness-episode-package-template.md",
    "templates/harness-evolution-review-template.md",
    "scripts/check_all.py",
    "scripts/check_testing_system_maturity.py",
    "scripts/check_execution_contract_semantics.py",
    "AGENTS.md",
    "governance/WORKFLOW.md",
    "governance/POLICY.md",
    "skills/issue-analysis/SKILL.md",
    "concepts/project-retrospective.md",
    "concepts/software-development-project-retrospective.md",
    "concepts/agent-work-retrospective.md",
    "projects/retrospectives/README.md",
    "templates/project-retrospective-template.md",
    "skills/historical-dialogue-retrospective/SKILL.md",
    "skills/cross-project-skill-adoption-prompt/SKILL.md",
    "skills/cross-project-skill-adoption-prompt/examples/retrospective-transfer-taskbook-golden.md",
    "skills/historical-dialogue-retrospective/TRANSFER.md",
    "templates/skill-transfer-manifest-template.md",
)

AGENT_STRATEGY_REQUIRED_TERMS = (
    "Log Eligibility",
    "Artifactization Eligibility",
    "Check Budget",
    "Rule Upgrade Budget",
    "P0",
    "P1",
    "P2",
    "P3",
    "提交税",
    "语义门",
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
    "引导式设计",
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
    "proactive-dialogue-system",
    "场景包",
    "置信度",
    "性能预算",
)

PROACTIVE_DIALOGUE_REQUIRED_TERMS = (
    "## 策略定位",
    "## 目标",
    "## 双层架构",
    "## 场景包",
    "## 触发信号",
    "## 决策模型",
    "## 上下文自动判定",
    "## 提问协议",
    "## 引导阶段",
    "## 通用问题库",
    "## 知识库问题包",
    "## 软件研发问题包：角色 × 环节矩阵",
    "## 其他场景问题包",
    "## 性能预算",
    "## 产物路由",
    "## 完成标准",
    "## 无感交流等级",
    "通用主动对话内核",
    "场景化问题包",
    "场景包",
    "置信度",
    "可直接判断",
    "可先假设",
    "必须现在问",
    "可归为待确认",
    "当前 blocked",
    "产品意图",
    "核心场景",
    "验收标准",
    "输入采集层",
    "对话所得",
    "agent 思考结果",
    "每轮产物化落地判定",
    "本轮无新增可沉淀信息",
    "读取预算",
    "问题预算",
    "检查预算",
    "产物大小预算",
    "commit hash",
)

GUIDED_DISCOVERY_TEMPLATE_REQUIRED_SECTIONS = (
    "## 基本信息",
    "## 当前理解",
    "## 场景问题包",
    "## 本轮关键假设",
    "## 本轮只问的问题",
    "## 回答吸收",
    "## 阶段产物",
    "## 性能预算",
    "## 路由",
    "## 产物化与提交闭环",
    "## 收尾",
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

SHARED_AGENT_ENTRY_REQUIRED_TERMS = (
    "项目级 agent 规则正文只维护根目录 `AGENTS.md` 一份",
    "CLAUDE.md",
    ".codex/AGENTS.md",
    "thin Codex adapter",
    "不承接第二份规则正文",
    "@../AGENTS.md",
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

RETROSPECTIVE_SYSTEM_REQUIRED_TERMS = (
    "复盘系统",
    "行动分流",
    "harness-feedback-ledger",
    "harness-evolution",
    "不替代",
)

RETROSPECTIVE_ARCHIVE_REQUIRED_TERMS = (
    "系统运行闭环",
    "轻量 checkpoint",
    "标准复盘",
    "深度复盘",
    "行动分流",
    "治理自演进关系",
    "不在复盘目录形成平行看板",
)

RETROSPECTIVE_TEMPLATE_REQUIRED_SECTIONS = (
    "## 复盘对象",
    "## 原始目标",
    "## 实际结果",
    "## 关键事实",
    "### 证据地图",
    "## 交付链回看",
    "## 偏差与原因",
    "## Agent 工作回看",
    "## 改进行动",
    "## 沉淀路由",
    "## 治理自演进判断",
    "## 未验证边界",
)

HISTORICAL_RETROSPECTIVE_SKILL_REQUIRED_TERMS = (
    "触发场景",
    "响应模式",
    "证据源分层",
    "框定复盘对象",
    "还原工作链",
    "判断 agent 偏差",
    "判断效率和质量",
    "输出改进路由",
    "质量自检",
    "不把 [[log]] 当原始真相源",
)

SKILL_TRANSFER_PROMPT_REQUIRED_TERMS = (
    "源能力覆盖矩阵",
    "生成思考循环",
    "执行合同判定",
    "源能力抽取",
    "模块展开",
    "失败模式审查",
    "Golden regression",
    "所有已沉淀 skill / 能力主题",
    "任意技能主题",
    "主题专属模块",
    "可执行任务书",
    "任务书优先",
    "对照样稿质量门",
    "Golden Baseline",
    "Baseline 对比评分",
    "generated >= baseline",
    "模式污染防线",
    "通用迁移提示词",
    "只有一个产物",
    "最终交付",
    "逐项可执行",
)

RETROSPECTIVE_TRANSFER_REQUIRED_TERMS = (
    "复盘体系迁移的最小模块清单",
    "字段级任务书展开要求",
    "Golden regression 样例",
    "推荐提示词骨架",
    "可执行任务书",
    "通用版生成规则",
    "优于示例的判定标准",
    "最终交付",
    "方法入口",
    "档案入口",
    "行动分流机制",
    "治理自演进关系",
)

RETROSPECTIVE_TRANSFER_GOLDEN_REQUIRED_TERMS = (
    "请升级本工程的完整复盘体系",
    "复盘体系的目标",
    "## 一、复盘体系参考资料",
    "## 二、吸收边界",
    "## 三、请在目标工程中完成的设计",
    "## 四、需要建立的复盘体系模块",
    "目标：让人和 agent 知道什么场景应该复盘",
    "必须写入：",
    "禁止只写一句",
    "不要把测试报告当复盘",
    "不要把 Issue 关闭当复盘完成",
    "不要只凭 log 做历史对话复盘",
    "## 五、需要更新的入口",
    "## 六、最终交付",
    "最终回复中请说明",
    "Regression Requirements",
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


def check_agent_governance_strategy(repo: Path) -> list[str]:
    errors: list[str] = []
    strategy = read_text(repo, "governance/agent-governance-strategy.md", errors)
    if strategy:
        for term in AGENT_STRATEGY_REQUIRED_TERMS:
            if term not in strategy:
                errors.append(f"governance/agent-governance-strategy.md: missing strategy term {term}")

    for rel in (
        "README.md",
        "INDEX.md",
        "governance/README.md",
        "concepts/agent-governance.md",
        "AGENTS.md",
        "governance/WORKFLOW.md",
        "governance/POLICY.md",
        "governance/instruction-adherence.md",
        "governance/log-writing-rules.md",
        "governance/harness-feedback-ledger.md",
    ):
        text = read_text(repo, rel, errors)
        if text and "agent-governance-strategy" not in text:
            errors.append(f"{rel}: missing agent-governance-strategy wiring")

    for rel in (
        "AGENTS.md",
        "governance/WORKFLOW.md",
        "governance/POLICY.md",
        "governance/instruction-adherence.md",
        "governance/log-writing-rules.md",
    ):
        text = read_text(repo, rel, errors)
        if text and "log eligibility" not in text:
            errors.append(f"{rel}: missing log eligibility gate")
    return errors


def check_proactive_dialogue(repo: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(repo, "governance/proactive-dialogue-system.md", errors)
    template = read_text(repo, "templates/guided-discovery-session-template.md", errors)
    workflow = read_text(repo, "governance/WORKFLOW.md", errors)
    policy = read_text(repo, "governance/POLICY.md", errors)
    agents = read_text(repo, "AGENTS.md", errors)
    templates_readme = read_text(repo, "templates/README.md", errors)
    index = read_text(repo, "INDEX.md", errors)
    ledger = read_text(repo, "governance/harness-feedback-ledger.md", errors)

    if text:
        for term in PROACTIVE_DIALOGUE_REQUIRED_TERMS:
            if term not in text:
                errors.append(f"governance/proactive-dialogue-system.md: missing proactive dialogue term {term}")
    if template:
        for section in GUIDED_DISCOVERY_TEMPLATE_REQUIRED_SECTIONS:
            if section not in template:
                errors.append(f"templates/guided-discovery-session-template.md: missing section {section}")
    for rel, doc in (
        ("governance/WORKFLOW.md", workflow),
        ("governance/POLICY.md", policy),
        ("AGENTS.md", agents),
        ("templates/README.md", templates_readme),
        ("INDEX.md", index),
        ("governance/harness-feedback-ledger.md", ledger),
    ):
        if doc and "proactive-dialogue-system" not in doc:
            errors.append(f"{rel}: missing proactive-dialogue-system wiring")
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
        for term in ("引导式设计", "性能预算"):
            if term not in agents:
                errors.append(f"AGENTS.md: missing proactive dialogue or performance guard {term}")
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
    agents = read_text(repo, "AGENTS.md", errors)

    if evolution:
        for term in H5_EVOLUTION_REQUIRED_TERMS:
            if term not in evolution:
                errors.append(f"governance/harness-evolution.md: missing H5 term {term}")
    if ledger:
        for term in H5_LEDGER_REQUIRED_TERMS:
            if term not in ledger:
                errors.append(f"governance/harness-feedback-ledger.md: missing H5 ledger term {term}")
    if (repo / ".codex/AGENTS.md").exists():
        errors.append(".codex/AGENTS.md: duplicate project-level rule entry; merge into root AGENTS.md")
    if agents:
        for term in SHARED_AGENT_ENTRY_REQUIRED_TERMS:
            if term not in agents:
                errors.append(f"AGENTS.md: missing shared agent entry term {term}")
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


def check_retrospective_system(repo: Path) -> list[str]:
    errors: list[str] = []
    concept = read_text(repo, "concepts/project-retrospective.md", errors)
    software = read_text(repo, "concepts/software-development-project-retrospective.md", errors)
    agent = read_text(repo, "concepts/agent-work-retrospective.md", errors)
    archive = read_text(repo, "projects/retrospectives/README.md", errors)
    template = read_text(repo, "templates/project-retrospective-template.md", errors)
    skill = read_text(repo, "skills/historical-dialogue-retrospective/SKILL.md", errors)

    if concept:
        for term in RETROSPECTIVE_SYSTEM_REQUIRED_TERMS:
            if term not in concept:
                errors.append(f"concepts/project-retrospective.md: missing retrospective system term {term}")
    if software:
        for term in ("交付链检查点", "Gate / FP / EP / TASK / risk / issue / AP / report", "不要把测试报告当复盘"):
            if term not in software:
                errors.append(f"concepts/software-development-project-retrospective.md: missing delivery-chain term {term}")
    if agent:
        for term in ("目标理解", "阶段判断", "上下文读取", "工具使用", "验证质量", "收尾提交质量"):
            if term not in agent:
                errors.append(f"concepts/agent-work-retrospective.md: missing agent-retrospective term {term}")
    if archive:
        for term in RETROSPECTIVE_ARCHIVE_REQUIRED_TERMS:
            if term not in archive:
                errors.append(f"projects/retrospectives/README.md: missing archive term {term}")
    if template:
        for section in RETROSPECTIVE_TEMPLATE_REQUIRED_SECTIONS:
            if section not in template:
                errors.append(f"templates/project-retrospective-template.md: missing section {section}")
    if skill:
        for term in HISTORICAL_RETROSPECTIVE_SKILL_REQUIRED_TERMS:
            if term not in skill:
                errors.append(f"skills/historical-dialogue-retrospective/SKILL.md: missing skill term {term}")
    for rel in ("README.md", "INDEX.md", "AGENTS.md", "governance/WORKFLOW.md", "skills/README.md", "templates/README.md"):
        text = read_text(repo, rel, errors)
        if text and "retrospective" not in text and "复盘" not in text:
            errors.append(f"{rel}: missing retrospective system wiring")
    return errors


def check_skill_transfer_prompt_system(repo: Path) -> list[str]:
    errors: list[str] = []
    meta_skill = read_text(repo, "skills/cross-project-skill-adoption-prompt/SKILL.md", errors)
    retrospective_transfer = read_text(repo, "skills/historical-dialogue-retrospective/TRANSFER.md", errors)
    retrospective_golden = read_text(
        repo,
        "skills/cross-project-skill-adoption-prompt/examples/retrospective-transfer-taskbook-golden.md",
        errors,
    )
    ledger = read_text(repo, "governance/harness-feedback-ledger.md", errors)

    if meta_skill:
        for term in SKILL_TRANSFER_PROMPT_REQUIRED_TERMS:
            if term not in meta_skill:
                errors.append(f"skills/cross-project-skill-adoption-prompt/SKILL.md: missing transfer-prompt term {term}")
    if retrospective_transfer:
        for term in RETROSPECTIVE_TRANSFER_REQUIRED_TERMS:
            if term not in retrospective_transfer:
                errors.append(f"skills/historical-dialogue-retrospective/TRANSFER.md: missing retrospective transfer term {term}")
    if retrospective_golden:
        for term in RETROSPECTIVE_TRANSFER_GOLDEN_REQUIRED_TERMS:
            if term not in retrospective_golden:
                errors.append(
                    "skills/cross-project-skill-adoption-prompt/examples/"
                    f"retrospective-transfer-taskbook-golden.md: missing golden term {term}"
                )
    if ledger and "跨工程迁移提示词任务书形态检查" not in ledger:
        errors.append("governance/harness-feedback-ledger.md: missing skill-transfer prompt shape sensor backlog")
    if ledger and "跨工程迁移提示词产物回归检查" not in ledger:
        errors.append("governance/harness-feedback-ledger.md: missing skill-transfer prompt golden regression sensor")
    return errors


def check_harness_governance(repo: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(check_required_files(repo))
    errors.extend(check_response_mode_routing(repo))
    errors.extend(check_entrypoint_wiring(repo))
    errors.extend(check_agent_governance_strategy(repo))
    errors.extend(check_proactive_dialogue(repo))
    errors.extend(check_rule_and_skill_wiring(repo))
    errors.extend(check_concept_and_template(repo))
    errors.extend(check_quality_gate_script(repo))
    errors.extend(check_h5_evolution(repo))
    errors.extend(check_instruction_and_semantics_wiring(repo))
    errors.extend(check_retrospective_system(repo))
    errors.extend(check_skill_transfer_prompt_system(repo))
    return errors


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors = check_harness_governance(repo)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} harness governance issue(s)", file=sys.stderr)
        return 1
    print("OK: harness governance routing, H5 ledger, retrospectives, templates, and sensors checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

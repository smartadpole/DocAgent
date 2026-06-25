#!/usr/bin/env python3
"""Check retrospective system wiring, templates, and skill coverage."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "concepts/project-retrospective.md",
    "concepts/software-development-project-retrospective.md",
    "concepts/agent-work-retrospective.md",
    "projects/retrospectives/README.md",
    "templates/project-retrospective-template.md",
    "skills/retrospective-capability/SKILL.md",
    "skills/retrospective-capability/TRANSFER.md",
    "skills/delivery-retrospective/SKILL.md",
    "skills/delivery-retrospective/TRANSFER.md",
    "skills/historical-dialogue-retrospective/SKILL.md",
)

ENTRYPOINT_REFERENCES: dict[str, tuple[str, ...]] = {
    "README.md": (
        "projects/retrospectives/README",
        "concepts/project-retrospective",
        "templates/project-retrospective-template",
        "skills/retrospective-capability/SKILL",
        "skills/delivery-retrospective/SKILL",
        "skills/historical-dialogue-retrospective/SKILL",
    ),
    "INDEX.md": (
        "projects/retrospectives/README",
        "concepts/project-retrospective",
        "templates/project-retrospective-template",
        "skills/retrospective-capability/SKILL",
        "skills/delivery-retrospective/SKILL",
        "skills/historical-dialogue-retrospective/SKILL",
    ),
    "AGENTS.md": (
        "projects/retrospectives/README",
        "concepts/project-retrospective",
        "skills/retrospective-capability/SKILL",
        "skills/historical-dialogue-retrospective/SKILL",
    ),
    ".codex/AGENTS.md": (
        "projects/retrospectives/README",
        "concepts/project-retrospective",
        "skills/retrospective-capability/SKILL",
        "skills/historical-dialogue-retrospective/SKILL",
        "retrospective-system",
    ),
    "governance/README.md": (
        "projects/retrospectives/README",
        "concepts/project-retrospective",
        "skills/retrospective-capability/SKILL",
        "harness-feedback-ledger",
    ),
    "governance/WORKFLOW.md": (
        "projects/retrospectives/README",
        "concepts/project-retrospective",
        "templates/project-retrospective-template",
        "skills/retrospective-capability/SKILL",
        "skills/delivery-retrospective/SKILL",
        "skills/historical-dialogue-retrospective/SKILL",
        "retrospective-system",
    ),
    "governance/POLICY.md": (
        "projects/retrospectives/README",
        "harness-feedback-ledger",
    ),
    "governance/response-mode-routing.md": (
        "projects/retrospectives/",
        "skills/retrospective-capability/SKILL",
        "skills/delivery-retrospective/SKILL",
        "skills/historical-dialogue-retrospective/SKILL",
    ),
    "projects/README.md": ("projects/retrospectives/README",),
    "projects/STRUCTURE.md": (
        "projects/retrospectives/README",
        "concepts/project-retrospective",
    ),
    "projects/incidents/README.md": ("projects/retrospectives/README",),
    "projects/development/reports/README.md": ("projects/retrospectives/README",),
    "concepts/README.md": (
        "concepts/project-retrospective",
        "concepts/software-development-project-retrospective",
        "concepts/agent-work-retrospective",
        "skills/retrospective-capability/SKILL",
    ),
    "templates/README.md": ("templates/project-retrospective-template",),
    "skills/README.md": (
        "skills/retrospective-capability/SKILL",
        "skills/delivery-retrospective/SKILL",
        "skills/historical-dialogue-retrospective/SKILL",
    ),
}

RETROSPECTIVE_INDEX_REQUIRED_TERMS = (
    "这页负责什么",
    "这页不负责什么",
    "文件落位",
    "复盘粒度",
    "当前复盘索引",
    "共性主题",
    "行动项分流",
    "沉淀路由",
    "维护说明",
    "系统运行闭环",
    "显式复盘请求",
    "自动触发关系",
    "上轮行动兑现回检",
    "no-op / 轻量复盘 checkpoint 只适用于自动触发判断",
    "projects/retrospectives/",
    "templates/project-retrospective-template",
    "skills/retrospective-capability/SKILL",
    "skills/delivery-retrospective/SKILL",
    "skills/historical-dialogue-retrospective/SKILL",
)

PROJECT_RETROSPECTIVE_REQUIRED_TERMS = (
    "长期价值",
    "文件落位",
    "复盘层级",
    "启动判断与路由",
    "复盘粒度",
    "最小产出",
    "改进行动跟踪",
    "治理自演进",
    "复盘系统",
    "retrospective-capability",
    "delivery-retrospective",
    "log",
    "Issue",
    "事故",
    "memory",
    "trace",
)

SOFTWARE_RETROSPECTIVE_REQUIRED_TERMS = (
    "需求是否清楚",
    "设计是否支撑实现和验收",
    "Gate / FP / EP / TASK",
    "risk、issue、AP、report",
    "测试、验收、发布证据",
    "运行质量",
    "服务台账",
    "协作治理",
    "delivery-retrospective",
)

AGENT_RETROSPECTIVE_REQUIRED_TERMS = (
    "目标理解",
    "阶段判断",
    "上下文读取",
    "工具使用",
    "执行策略",
    "验证质量",
    "沟通节奏",
    "权限和边界控制",
    "沉淀路由",
    "收尾和提交质量",
    "harness-feedback-ledger",
    "retrospective-capability",
)

TEMPLATE_REQUIRED_SECTIONS = (
    "## 复盘对象",
    "## 原始目标",
    "## 实际结果",
    "## 关键事实",
    "## 首轮目标与用户纠偏锚点",
    "## 上轮行动兑现回检",
    "## 偏差与原因",
    "## 保留做法",
    "## 改进行动",
    "## 沉淀路由",
    "## 上层抽象与举一反三",
    "## 治理自演进判断",
    "## 未验证边界",
)

TEMPLATE_REQUIRED_TERMS = (
    "project: <project-id>",
    "证据地图",
    "原始 session / rollout",
    "git diff / commit",
    "## 可选回看模块",
    "只保留和复盘对象相关的模块",
    "### 软件研发交付链回看（适用时）",
    "### Agent 工作回看（适用时）",
)

RETROSPECTIVE_CAPABILITY_REQUIRED_TERMS = (
    "复盘能力总技能",
    "统一复盘合同",
    "子项路由",
    "上轮行动兑现回检",
    "no-op / 轻量复盘 checkpoint / 标准复盘 / 深度复盘",
    "显式复盘请求",
    "深度复盘",
    "首轮目标",
    "用户纠偏序列",
    "行动分流",
    "不把测试报告当复盘",
)

DELIVERY_SKILL_REQUIRED_TERMS = (
    "项目交付与软件研发链复盘子技能",
    "需求 -> 设计 -> 拆解 -> 实现 -> 测试验收 -> 发布运行",
    "证据读取顺序",
    "交付链回看",
    "上轮行动兑现回检",
    "需求偏差",
    "设计偏差",
    "验证偏差",
    "不把测试报告当复盘",
)

SKILL_REQUIRED_TERMS = (
    "触发场景",
    "自动触发矩阵",
    "显式深度历史复盘",
    "响应模式",
    "证据源分层",
    "复盘对象框定",
    "工作链还原",
    "Agent 偏差分类",
    "效率和质量判断",
    "Workflow 改进路由",
    "输出格式",
    "禁止项",
    "当前对话上下文",
    "原始 session / rollout",
    "git diff / commit",
    "检查 / 测试输出",
    "memory",
    "最终回复 / handoff",
    "首轮目标",
    "用户纠偏序列",
    "上层抽象与举一反三",
    "不因一次偏差直接新增硬规则",
)

def read_text(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required retrospective file is missing")
        return ""
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        errors.append(f"{rel}: required retrospective file is empty")
    return text


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing retrospective term {term}")


def check_required_files(repo: Path, errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        read_text(repo, rel, errors)


def check_retrospective_content(repo: Path, errors: list[str]) -> None:
    require_terms(
        "projects/retrospectives/README.md",
        read_text(repo, "projects/retrospectives/README.md", errors),
        RETROSPECTIVE_INDEX_REQUIRED_TERMS,
        errors,
    )
    require_terms(
        "concepts/project-retrospective.md",
        read_text(repo, "concepts/project-retrospective.md", errors),
        PROJECT_RETROSPECTIVE_REQUIRED_TERMS,
        errors,
    )
    require_terms(
        "concepts/software-development-project-retrospective.md",
        read_text(repo, "concepts/software-development-project-retrospective.md", errors),
        SOFTWARE_RETROSPECTIVE_REQUIRED_TERMS,
        errors,
    )
    require_terms(
        "concepts/agent-work-retrospective.md",
        read_text(repo, "concepts/agent-work-retrospective.md", errors),
        AGENT_RETROSPECTIVE_REQUIRED_TERMS,
        errors,
    )
    require_terms(
        "templates/project-retrospective-template.md",
        read_text(repo, "templates/project-retrospective-template.md", errors),
        TEMPLATE_REQUIRED_SECTIONS,
        errors,
    )
    require_terms(
        "templates/project-retrospective-template.md",
        read_text(repo, "templates/project-retrospective-template.md", errors),
        TEMPLATE_REQUIRED_TERMS,
        errors,
    )
    require_terms(
        "skills/retrospective-capability/SKILL.md",
        read_text(repo, "skills/retrospective-capability/SKILL.md", errors),
        RETROSPECTIVE_CAPABILITY_REQUIRED_TERMS,
        errors,
    )
    require_terms(
        "skills/delivery-retrospective/SKILL.md",
        read_text(repo, "skills/delivery-retrospective/SKILL.md", errors),
        DELIVERY_SKILL_REQUIRED_TERMS,
        errors,
    )
    require_terms(
        "skills/historical-dialogue-retrospective/SKILL.md",
        read_text(repo, "skills/historical-dialogue-retrospective/SKILL.md", errors),
        SKILL_REQUIRED_TERMS,
        errors,
    )


def check_entrypoint_wiring(repo: Path, errors: list[str]) -> None:
    for rel, required_links in ENTRYPOINT_REFERENCES.items():
        text = read_text(repo, rel, errors)
        if not text:
            continue
        missing = [link for link in required_links if link not in text]
        if missing:
            errors.append(f"{rel}: missing retrospective entrypoint link(s): {', '.join(missing)}")


def check_no_parallel_action_board(repo: Path, errors: list[str]) -> None:
    text = read_text(repo, "projects/retrospectives/README.md", errors)
    required_routes = (
        "projects/development/issues/README",
        "projects/incidents/README",
        "projects/development/risks/README",
        "projects/development/acceptance/README",
        "projects/development/reports/README",
        "projects/meetings/README",
        "projects/decisions",
        "projects/memory/README",
        "projects/trace",
        "harness-feedback-ledger",
        "scripts/check_all.py",
    )
    for route in required_routes:
        if route not in text:
            errors.append(f"projects/retrospectives/README.md: missing action route {route}")
    if "平行看板" not in text:
        errors.append("projects/retrospectives/README.md: must forbid parallel action boards")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    check_required_files(repo, errors)
    check_retrospective_content(repo, errors)
    check_entrypoint_wiring(repo, errors)
    check_no_parallel_action_board(repo, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} retrospective system issue(s)", file=sys.stderr)
        return 1

    print("OK: retrospective system wiring, template, and skill checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

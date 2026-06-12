#!/usr/bin/env python3
"""Generate the cross-project skill maturity HTML lens."""

from __future__ import annotations

import html
import json
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Union


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "views" / "current" / "governance" / "skill-maturity-matrix.html"
DIAGNOSTICS_OUTPUT = ROOT / "views" / "current" / "governance" / "skill-maturity-diagnostics.md"
DATA_OUTPUT = ROOT / "views" / "current" / "governance" / "skill-maturity-matrix.data.json"


@dataclass(frozen=True)
class Project:
    key: str
    label: str
    role: str
    path: Path
    registry_level: str


@dataclass(frozen=True)
class Evidence:
    score: int
    note: str
    hits: List[Path]
    signals: List[str]


PROJECTS = [
    Project("ack", "AcknowledgeBase", "治理中控 / 源能力", ROOT, "L3+ reference"),
    Project("wiki", "Software/wiki", "模板源", Path("/Users/hai/Documents/Software/wiki"), "L3 reference"),
    Project("doccust", "DocCustomeranalysis", "主控", Path("/Users/hai/Documents/Code/DocCustomeranalysis"), "L3 assessed"),
    Project("docfilm", "DocFilmCommunity", "主控", Path("/Users/hai/Documents/Code/DocFilmCommunity"), "L2 assessed"),
    Project("fetch", "fetch-adapter", "子工程", Path("/Users/hai/Documents/Code/Customer/fetch-adapter"), "L2 unenrolled"),
    Project("train", "train_platform", "子工程", Path("/Users/hai/Documents/Code/train_platform"), "L1-L2 unenrolled"),
    Project("prefect", "prefect", "子工程", Path("/Users/hai/Documents/Code/prefect"), "L1 unenrolled"),
    Project("customer", "customeranalysis", "子工程", Path("/Users/hai/Documents/Code/customeranalysis"), "special unenrolled"),
    Project("life", "LifeOS", "生活系统 / 下游强化源", Path("/Users/hai/Documents/Life"), "out-of-registry reference"),
    Project("docerp", "DocERP", "主控候选", Path("/Users/hai/Documents/Code/DocERP"), "observed"),
    Project("h100", "H100", "软件专题工程", Path("/Users/hai/Documents/Software/H100"), "observed"),
    Project("17lang", "17lang", "实现工程", Path("/Users/hai/Documents/Code/17lang"), "observed"),
]


ALIASES: Dict[str, List[str]] = {
    "problem-focused-visual-presentation": ["problem-focused-lens", "visual-presentation", "lens"],
    "historical-dialogue-retrospective": ["retrospective", "system-harness-review"],
    "issue-analysis": ["issue-incident-analysis", "incident-analysis"],
    "cross-project-governance-audit": ["harness-governance", "governance-audit", "agent-harness"],
    "goal-contract": ["codex-goals", "goals", "goal-mode", "harness-goal-governance", "long-term-goal-contract"],
    "knowledge-linking": ["knowledge-linking"],
    "technology-research-router": ["technology-research"],
    "technical-topic-research": ["technical-topic"],
    "open-source-project-research": ["open-source-project"],
    "industry-ai-research": ["industry-ai"],
    "cross-project-skill-adoption-prompt": ["skill-adoption", "skill-transfer"],
}

SKILL_DISPLAY_NAMES = {
    "cross-project-governance-audit": "跨工程治理审计",
    "cross-project-skill-adoption-prompt": "跨工程技能迁移提示词",
    "goal-contract": "Goal Contract / 长时任务完成契约",
    "historical-dialogue-retrospective": "历史对话复盘",
    "industry-ai-research": "行业 / AI 调研",
    "issue-analysis": "Issue / 事故分析",
    "knowledge-linking": "知识关联",
    "open-source-project-research": "开源工程调研",
    "problem-focused-visual-presentation": "问题聚焦式图文呈现",
    "technical-topic-research": "技术专题调研",
    "technology-research-router": "技术调研路由",
    "agents-md-sync": "Agent 规则同步",
    "backlog-management": "Backlog 批处理",
    "customer-group-db-readback": "客群 DB 读回",
    "customer-pipeline-docs": "客群管线文档入口",
    "customeranalysis-docs": "customeranalysis 文档入口",
    "document-changes": "文档变更检查",
    "film-community-docs": "Film Community 文档入口",
    "inbox-triage": "Inbox 整理",
    "life-decision-review": "生活决策复盘",
    "life-matter-routing": "生活事项路由",
    "weekly-review": "周报",
    "work-item-auto-decomposition": "事项自动拆解",
    "write-docs": "文档写作",
}

GROUP_DEFINITIONS: Dict[str, Dict[str, Union[str, int]]] = {
    "research-capability": {
        "display_name": "调研 / 研究能力",
        "description": "面向技术专题、开源工程、行业 / AI 赛道和产品 / 公司 / PoC 的研究能力总项。总表按一项呈现，细分路由、技术专题、开源工程、行业 AI 等子项在详情中展开。",
        "sort_order": 10,
    },
    "retrospective-capability": {
        "display_name": "复盘 / 回顾改进",
        "description": "面向历史对话、当前工作流、Harness episode、项目复盘和系统改进的复盘能力总项。总表按一项呈现，细分历史对话复盘、系统 harness review 等子项在详情中展开。",
        "sort_order": 20,
    },
    "project-context-entry": {
        "display_name": "项目上下文入口",
        "description": "面向具体工程的上下文加载、主控文档读取、handoff / TODO / FP 对齐和实现仓库接入能力。它通常是下游工程本地能力，不一定应反哺成通用源技能。",
        "sort_order": 120,
        "capability_scope": "project-bound",
        "scope_note": "绑定具体工程上下文入口和交接结构，不能按通用技能直接迁移。",
    },
    "documentation-maintenance": {
        "display_name": "文档与 Agent 规则维护",
        "description": "面向代码变更后的文档更新、AGENTS.md / agent 规则同步、写作文档和 PR 前文档新鲜度检查的维护能力。",
        "sort_order": 130,
        "capability_scope": "general",
    },
    "lifeos-management": {
        "display_name": "生活系统管理",
        "description": "LifeOS 侧面向生活事项路由、inbox 整理、周报和生活决策复盘的领域技能总项。它作为下游主题能力展示，不默认上推为软件工程通用技能。",
        "sort_order": 140,
        "capability_scope": "project-bound",
        "scope_note": "绑定 LifeOS 生活域，不默认上推为软件工程通用技能。",
    },
}

GROUP_BY_SKILL = {
    "technology-research-router": "research-capability",
    "technical-topic-research": "research-capability",
    "open-source-project-research": "research-capability",
    "industry-ai-research": "research-capability",
    "historical-dialogue-retrospective": "retrospective-capability",
    "customer-pipeline-docs": "project-context-entry",
    "customeranalysis-docs": "project-context-entry",
    "film-community-docs": "project-context-entry",
    "document-changes": "documentation-maintenance",
    "write-docs": "documentation-maintenance",
    "agents-md-sync": "documentation-maintenance",
    "life-matter-routing": "lifeos-management",
    "inbox-triage": "lifeos-management",
    "weekly-review": "lifeos-management",
    "life-decision-review": "lifeos-management",
}

PROJECT_BOUND_SKILLS = {
    "backlog-management": "绑定特定 issue backlog、仓库队列和维护策略，迁移时只能抽取批处理方法。",
    "customer-group-db-readback": "绑定客群业务表、数据库写入合同和验收口径，迁移时只能抽取读回验证方法。",
    "work-item-auto-decomposition": "绑定主控 Gate / FP / EP / TASK 事项模型，迁移前必须先抽象事项系统。",
}

SCOPE_LABELS = {
    "general": "通用 / 可迁移",
    "project-bound": "项目 / 领域绑定",
}

SCOPE_DESCRIPTIONS = {
    "general": "方法、治理契约或呈现流程可以跨工程复用；迁移重点是触发条件、事实源分层、流程、输出格式、验证和禁止项。",
    "project-bound": "能力绑定具体项目、业务对象、数据合同、运行环境或领域语义；矩阵只展示成熟度，跨工程反哺时只能抽象方法，不复制项目事实。",
}

SCOPE_SORT_ORDER = {
    "general": 0,
    "project-bound": 1,
}

SUPPLEMENTAL_CAPABILITIES: List[Dict[str, Union[str, List[str]]]] = [
    {
        "name": "goal-contract",
        "display_name": SKILL_DISPLAY_NAMES["goal-contract"],
        "path": "templates/goal-contract-template.md",
        "source_paths": [
            "AcknowledgeBase:templates/goal-contract-template.md",
            "AcknowledgeBase:concepts/codex-goals.md",
            "Software/wiki:templates/goal-contract-template.md",
            "Software/wiki:concepts/codex-goals.md",
        ],
        "source_projects": ["AcknowledgeBase", "Software/wiki"],
        "origin_projects": ["AcknowledgeBase", "Software/wiki"],
        "aliases": ["Codex Goals", "Goal Contract"],
        "description": "长时任务的线程级完成契约。用于终点明确但路径需要多轮探索的修复、迁移、调研、验收或主控 / 子工程回传，固定期望最终状态、验证面 / 证据边界、允许范围和阻塞停止条件；它不是普通 skill，也不替代验收关闭。",
        "has_transfer": "no",
        "has_source": "yes",
        "capability_type": "governance-contract",
    },
]


STATUS_LABELS = {
    "leader": "领先",
    "mature": "成熟",
    "adopted": "接入",
    "partial": "局部",
    "none": "未见",
    "blocked": "阻塞",
}

STATUS_SCORES = {
    "leader": 5,
    "mature": 4,
    "adopted": 3,
    "partial": 2,
    "none": 0,
    "blocked": -1,
}

SKILL_FILE_PATTERNS = [
    "skills/**/SKILL.md",
    ".codex/skills/**/SKILL.md",
    ".claude/skills/**/SKILL.md",
    ".agents/skills/**/SKILL.md",
]


def run(cmd: List[str], cwd: Path = ROOT) -> str:
    try:
        return subprocess.check_output(cmd, cwd=cwd, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def canonical_skill_name(value: str) -> str:
    normalized = normalize(value)
    for canonical, aliases in ALIASES.items():
        if normalized == normalize(canonical) or normalized in {normalize(alias) for alias in aliases}:
            return canonical
    return normalized


def humanize_skill_name(value: str) -> str:
    return value.replace("-", " ")


def display_name_for_skill(value: str) -> str:
    return SKILL_DISPLAY_NAMES.get(value, humanize_skill_name(value))


def group_name_for_skill(value: str) -> str:
    return GROUP_BY_SKILL.get(value, value)


def capability_scope_for_skill(value: str) -> str:
    group_name = group_name_for_skill(value)
    group_def = GROUP_DEFINITIONS.get(group_name)
    if group_def and group_def.get("capability_scope"):
        return str(group_def["capability_scope"])
    if value in PROJECT_BOUND_SKILLS:
        return "project-bound"
    return "general"


def scope_note_for_skill(value: str) -> str:
    group_name = group_name_for_skill(value)
    group_def = GROUP_DEFINITIONS.get(group_name)
    if group_def and group_def.get("scope_note"):
        return str(group_def["scope_note"])
    return PROJECT_BOUND_SKILLS.get(value, SCOPE_DESCRIPTIONS[capability_scope_for_skill(value)])


def origin_projects_for(source_occurrences: List[Dict[str, str]], occurrences: List[Dict[str, str]]) -> List[str]:
    if source_occurrences:
        return sorted({item["project_label"] for item in source_occurrences})
    return sorted({item["project_label"] for item in occurrences})


def read_skill_occurrences() -> List[Dict[str, str]]:
    occurrences = []
    for project in PROJECTS:
        if not project.path.exists():
            continue
        for pattern in SKILL_FILE_PATTERNS:
            for skill_path in sorted(project.path.glob(pattern)):
                if not skill_path.is_file():
                    continue
                text = skill_path.read_text(encoding="utf-8", errors="ignore")
                name_match = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
                desc_match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
                raw_name = name_match.group(1).strip() if name_match else skill_path.parent.name
                canonical = canonical_skill_name(raw_name)
                rel_path = str(skill_path.relative_to(project.path))
                occurrences.append(
                    {
                        "name": canonical,
                        "raw_name": raw_name,
                        "display_name": SKILL_DISPLAY_NAMES.get(canonical, humanize_skill_name(canonical)),
                        "path": rel_path,
                        "full_path": str(skill_path),
                        "project_key": project.key,
                        "project_label": project.label,
                        "description": desc_match.group(1).strip() if desc_match else "",
                        "has_transfer": "yes" if (skill_path.parent / "TRANSFER.md").exists() else "no",
                    }
                )
    return occurrences


def read_skill_manifest() -> List[Dict[str, Union[str, List[str]]]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for occurrence in read_skill_occurrences():
        grouped[occurrence["name"]].append(occurrence)

    raw_rows: List[Dict[str, Union[str, List[str]]]] = []
    for name, occurrences in grouped.items():
        source_occurrences = [item for item in occurrences if item["project_key"] == "ack"]
        description_source = source_occurrences[0] if source_occurrences else max(
            occurrences,
            key=lambda item: len(item["description"]),
        )
        aliases = sorted({item["raw_name"] for item in occurrences if canonical_skill_name(item["raw_name"]) == name})
        source_projects = sorted({item["project_label"] for item in occurrences})
        source_paths = [
            f"{item['project_label']}:{item['path']}"
            for item in sorted(occurrences, key=lambda item: (item["project_label"], item["path"]))
        ]
        raw_rows.append(
            {
                "name": name,
                "display_name": display_name_for_skill(name),
                "path": source_paths[0] if source_paths else "",
                "source_paths": source_paths,
                "source_projects": source_projects,
                "origin_projects": origin_projects_for(source_occurrences, occurrences),
                "aliases": aliases,
                "description": description_source["description"],
                "has_transfer": "yes" if any(item["has_transfer"] == "yes" for item in occurrences) else "no",
                "has_source": "yes" if source_occurrences else "no",
                "member_names": [name],
                "member_display_names": [display_name_for_skill(name)],
                "member_count": "1",
                "sort_order": "100",
                "capability_scope": capability_scope_for_skill(name),
                "scope_note": scope_note_for_skill(name),
            }
        )

    existing_names = {str(row["name"]) for row in raw_rows}
    for capability in SUPPLEMENTAL_CAPABILITIES:
        if str(capability["name"]) not in existing_names:
            raw_rows.append(
                {
                    **capability,
                    "member_names": [str(capability["name"])],
                    "member_display_names": [str(capability["display_name"])],
                    "member_count": "1",
                    "sort_order": "90",
                    "capability_scope": "general",
                    "scope_note": "治理契约类能力，不绑定单一项目业务事实；迁移时应保持完成契约和验收边界分离。",
                }
            )

    capability_groups: Dict[str, Dict[str, Union[str, List[str]]]] = {}
    for row in raw_rows:
        name = str(row["name"])
        group_name = group_name_for_skill(name)
        group_def = GROUP_DEFINITIONS.get(group_name)
        if group_name not in capability_groups:
            capability_groups[group_name] = {
                "name": group_name,
                "display_name": str(group_def["display_name"]) if group_def else str(row["display_name"]),
                "description": str(group_def["description"]) if group_def else str(row["description"]),
                "path": str(row.get("path", "")),
                "source_paths": [],
                "source_projects": [],
                "origin_projects": [],
                "aliases": [],
                "has_transfer": "no",
                "has_source": "no",
                "member_names": [],
                "member_display_names": [],
                "member_count": "0",
                "sort_order": str(group_def["sort_order"]) if group_def else str(row.get("sort_order", "100")),
                "capability_scope": str(group_def.get("capability_scope", row.get("capability_scope", "general"))) if group_def else str(row.get("capability_scope", "general")),
                "scope_note": str(group_def.get("scope_note", row.get("scope_note", ""))) if group_def else str(row.get("scope_note", "")),
            }
        group = capability_groups[group_name]
        if row.get("capability_scope") == "project-bound":
            group["capability_scope"] = "project-bound"
        if row.get("scope_note"):
            group["scope_note"] = str(row["scope_note"])
        group["source_paths"] = sorted({*group["source_paths"], *row.get("source_paths", [])})  # type: ignore[arg-type]
        group["source_projects"] = sorted({*group["source_projects"], *row.get("source_projects", [])})  # type: ignore[arg-type]
        group["origin_projects"] = sorted({*group["origin_projects"], *row.get("origin_projects", row.get("source_projects", []))})  # type: ignore[arg-type]
        group["aliases"] = sorted(
            {
                *group["aliases"],  # type: ignore[arg-type]
                name,
                str(row["display_name"]),
                *ALIASES.get(name, []),
                *[str(alias) for alias in row.get("aliases", [])],
            }
        )
        group["member_names"] = sorted({*group["member_names"], *row.get("member_names", [name])})  # type: ignore[arg-type]
        group["member_display_names"] = sorted({*group["member_display_names"], *row.get("member_display_names", [str(row["display_name"])])})  # type: ignore[arg-type]
        group["member_count"] = str(len(group["member_names"]))  # type: ignore[arg-type]
        if row.get("has_transfer") == "yes":
            group["has_transfer"] = "yes"
        if row.get("has_source") == "yes":
            group["has_source"] = "yes"

    return sorted(
        capability_groups.values(),
        key=lambda item: (int(str(item.get("sort_order", "100"))), str(item["display_name"])),
    )


def iter_candidate_files(project: Project) -> Iterable[Path]:
    if not project.path.exists():
        return []
    patterns = SKILL_FILE_PATTERNS + [
        "governance/*.md",
        "rules/*.md",
        ".codex/context/*.md",
        "logs/system/*.md",
        "views/README.md",
        "views/lens-registry.md",
        "views/current/**/*.html",
        "concepts/*goal*.md",
        "articles/*goal*.md",
        "templates/*harness*.md",
        "templates/*lens*.md",
        "templates/*research*.md",
        "templates/*issue*.md",
        "templates/*goal*.md",
        "templates/*contract*.md",
        "templates/README.md",
        "AGENTS.md",
        "README.md",
        "INDEX.md",
        ".codex/agents/**/*.md",
        ".agents/rules/**/*.md",
        "docs/handoffs/README.md",
        "docs/handoffs/**/TASK_EXECUTION_MODE.md",
        "projects/development/execution/**/*.md",
        "scripts/check_*.py",
        "tools/check_*.py",
        "automation/scripts/check_*.py",
    ]
    files: List[Path] = []
    for pattern in patterns:
        files.extend(project.path.glob(pattern))
    return sorted(set(p for p in files if p.is_file()))


def skill_terms(skill: Union[str, Dict[str, Union[str, List[str]]]]) -> List[str]:
    if isinstance(skill, dict):
        name = str(skill["name"])
        terms = [name] + ALIASES.get(name, []) + [str(alias) for alias in skill.get("aliases", [])]
    else:
        name = skill
        terms = [name] + ALIASES.get(name, [])
    normalized_terms = [normalize(term) for term in terms]
    return sorted({term for term in normalized_terms if term})


def skill_entry_terms(path: Path, project: Project) -> List[str]:
    rel = path.relative_to(project.path)
    if path.name != "SKILL.md" or len(rel.parts) < 2:
        return []
    return [normalize(rel.parts[-2]), normalize(str(rel))]


def evidence_for(project: Project, skill: Union[str, Dict[str, Union[str, List[str]]]]) -> List[Path]:
    skill_name = str(skill["name"]) if isinstance(skill, dict) else skill
    terms = skill_terms(skill)
    hits = []
    for path in iter_candidate_files(project):
        rel = normalize(str(path.relative_to(project.path)))
        if any(term in rel for term in terms):
            hits.append(path)
            continue
        if skill_name in {"cross-project-governance-audit", "historical-dialogue-retrospective"}:
            if any(token in rel for token in ["harness", "retrospective", "governance"]):
                hits.append(path)
        elif skill_name == "issue-analysis" and any(token in rel for token in ["issue", "incident"]):
            hits.append(path)
        elif skill_name in {"technology-research-router", "technical-topic-research", "open-source-project-research", "industry-ai-research"}:
            if any(token in rel for token in ["technology", "technical", "research", "source-project", "industry-ai"]):
                hits.append(path)
        elif skill_name == "goal-contract":
            goal_markers = [
                "Goal Contract",
                "goal-contract-template",
                "Long-term Goal Contract",
                "Codex Goals",
                "harness-goal-governance",
                "长时任务完成契约",
            ]
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")[:120_000]
            except OSError:
                text = ""
            if any(marker in text for marker in goal_markers):
                hits.append(path)
    return sorted(set(hits))


def score_evidence(project: Project, skill: Dict[str, Union[str, List[str]]], hits: List[Path]) -> Evidence:
    if not project.path.exists():
        return Evidence(score=-1, note="本机路径当前不可读。", hits=[], signals=[])
    if not hits:
        return Evidence(score=0, note="未在常见 skill / governance / sensor 路径发现等价能力。", hits=[], signals=[])

    skill_name = str(skill["name"])
    terms = skill_terms(skill)
    rels = [p.relative_to(project.path) for p in hits]
    rel_texts = [normalize(str(rel)) for rel in rels]
    score = 0
    signals: List[str] = []

    skill_entries = [
        p for p in hits
        if p.name == "SKILL.md"
        and any(term in entry_term for entry_term in skill_entry_terms(p, project) for term in terms)
    ]
    if skill_entries:
        score += 8
        signals.append("skill")

    transfer_files = []
    for skill_path in skill_entries:
        transfer = skill_path.parent / "TRANSFER.md"
        if transfer.exists():
            transfer_files.append(transfer)
    if transfer_files:
        score += 3
        signals.append("TRANSFER")

    sensor_hits = [
        rel for rel, rel_text in zip(rels, rel_texts)
        if (
            ("scripts" in rel.parts or "tools" in rel.parts or "automation" in rel.parts)
            and rel.name.startswith("check_")
            and any(term in rel_text for term in terms)
        )
    ]
    if sensor_hits:
        score += 3
        signals.append("sensor")

    view_hits = [rel for rel, rel_text in zip(rels, rel_texts) if rel.parts and rel.parts[0] == "views" and any(term in rel_text for term in terms)]
    if view_hits:
        score += 3
        signals.append("views")

    governance_hits = [
        rel for rel in rels
        if (rel.parts and rel.parts[0] in {"governance", "rules"}) or rel.parts[:2] == (".codex", "context")
    ]
    if governance_hits:
        score += 2
        signals.append("governance")

    template_hits = [rel for rel in rels if rel.parts and rel.parts[0] == "templates"]
    if template_hits:
        score += 1
        signals.append("template")

    if skill_name == "goal-contract":
        goal_path_hits = [
            rel_text for rel_text in rel_texts
            if any(
                token in rel_text
                for token in ["goal-contract", "codex-goals", "harness-goal-governance", "long-term-goal-contract"]
            )
        ]
        if goal_path_hits:
            score += 4
            signals.append("goal-contract")

    content_chars = 0
    for path in hits[:8]:
        try:
            content_chars += min(path.stat().st_size, 80_000)
        except OSError:
            pass
    if content_chars >= 50_000:
        score += 3
        signals.append("large-body")
    elif content_chars >= 18_000:
        score += 2
        signals.append("body")
    elif content_chars >= 6_000:
        score += 1
        signals.append("small-body")

    if not signals:
        score = max(score, 1)
        signals.append("trace")

    signal_text = "、".join(signals)
    note = f"动态重扫得分 {score}；证据信号：{signal_text}。"
    return Evidence(score=score, note=note, hits=hits[:5], signals=signals)


def status_for(score: int, max_score: int) -> str:
    if score < 0:
        return "blocked"
    if score == 0:
        return "none"
    if max_score >= 8 and score == max_score:
        return "leader"
    if max_score >= 8 and score >= max(8, int(max_score * 0.75)):
        return "mature"
    if score >= 8:
        return "adopted"
    return "partial"


def evidence_fingerprint(signals: List[str]) -> tuple[str, ...]:
    """Comparable evidence shape for one project under one skill theme."""
    expanded = set(signals)
    if "large-body" in expanded:
        expanded.update({"body", "small-body"})
    elif "body" in expanded:
        expanded.add("small-body")
    return tuple(sorted(expanded))


def build_context() -> Dict[str, Any]:
    skills = read_skill_manifest()
    total_member_count = sum(int(str(skill.get("member_count", "1"))) for skill in skills)
    scope_counts = {
        scope: sum(1 for skill in skills if str(skill.get("capability_scope", "general")) == scope)
        for scope in SCOPE_LABELS
    }
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    source_revision = run(["git", "rev-parse", "--short", "HEAD"]) or "working-tree"

    matrix = []
    for skill in skills:
        scored_cells = []
        for project in PROJECTS:
            hits = evidence_for(project, skill)
            evidence = score_evidence(project, skill, hits)
            scored_cells.append({"project": project, "evidence": evidence})

        max_score = max((cell["evidence"].score for cell in scored_cells), default=0)
        positive_fingerprint = sorted(
            {
                signal
                for cell in scored_cells
                if cell["evidence"].score > 0
                for signal in cell["evidence"].signals
            }
        )
        top_cells = [
            cell for cell in scored_cells
            if cell["evidence"].score == max_score and cell["evidence"].score > 0
        ]
        leader_candidate_projects = {
            cell["project"].label
            for cell in top_cells
            if set(evidence_fingerprint(cell["evidence"].signals)).issuperset(positive_fingerprint)
        }
        leader_gap = max_score > 0 and not leader_candidate_projects
        cells = []
        leading_projects = []
        mature_projects = []
        coverage_score = 0
        for cell in scored_cells:
            evidence = cell["evidence"]
            status = status_for(evidence.score, max_score)
            leader_rule_note = ""
            if cell["project"].label in leader_candidate_projects:
                status = "leader"
            elif status == "leader":
                status = "mature"
                leader_rule_note = "最高分但未覆盖同技能下其他工程的独特证据信号，按互补优秀处理为成熟；需补齐全体证据信号并集后才能标为领先。"
            coverage_score += max(STATUS_SCORES[status], 0)
            if status == "leader":
                leading_projects.append(cell["project"].label)
            if status in {"leader", "mature"}:
                mature_projects.append(cell["project"].label)
            cells.append(
                {
                    "project": cell["project"],
                    "status": status,
                    "note": evidence.note,
                    "hits": evidence.hits,
                    "signals": evidence.signals,
                    "fingerprint": list(evidence_fingerprint(evidence.signals)),
                    "leader_rule_note": leader_rule_note,
                    "score": evidence.score,
                }
            )
        matrix.append(
            {
                "skill": skill,
                "cells": cells,
                "leading_projects": leading_projects,
                "mature_projects": mature_projects,
                "score": coverage_score,
                "max_score": max_score,
                "top_projects": [cell["project"].label for cell in top_cells],
                "leader_gap": leader_gap,
                "required_leader_fingerprint": positive_fingerprint,
            }
        )

    return {
        "skills": skills,
        "total_member_count": total_member_count,
        "scope_counts": scope_counts,
        "generated": generated,
        "source_revision": source_revision,
        "matrix": matrix,
    }


def render_html(context: Dict[str, Any]) -> str:
    skills = context["skills"]
    total_member_count = context["total_member_count"]
    scope_counts = context["scope_counts"]
    generated = context["generated"]
    source_revision = context["source_revision"]
    matrix = context["matrix"]

    compact_cards_by_scope: Dict[str, List[str]] = defaultdict(list)
    overview_rows_by_scope: Dict[str, List[str]] = defaultdict(list)
    for row in matrix:
        skill = row["skill"]
        scope = str(skill.get("capability_scope", "general"))
        scope_label = SCOPE_LABELS.get(scope, scope)
        scope_note = str(skill.get("scope_note", SCOPE_DESCRIPTIONS.get(scope, "")))
        origin_projects = [str(project) for project in skill.get("origin_projects", skill["source_projects"])]
        found_projects = [str(project) for project in skill["source_projects"]]
        source_projects = "、".join(found_projects)
        source_roots = "、".join(origin_projects)
        source_paths = "；".join(str(path) for path in skill["source_paths"][:6])
        member_display_names = [str(item) for item in skill.get("member_display_names", [skill["display_name"]])]
        member_text = "、".join(member_display_names)
        member_count = str(skill.get("member_count", len(member_display_names)))
        leaders = row["leading_projects"]
        mature_projects = [p for p in row["mature_projects"] if p not in leaders]
        adopted = [c["project"].label for c in row["cells"] if c["status"] == "adopted"]
        partial = [c["project"].label for c in row["cells"] if c["status"] == "partial"]
        missing_count = sum(1 for c in row["cells"] if c["status"] == "none")
        if row.get("leader_gap"):
            next_step = "当前没有工程覆盖同技能下全体独特证据信号；先做互补差异对齐，覆盖并集后才标记领先。"
        elif leaders and set(leaders).issubset(set(origin_projects)):
            next_step = "源头当前领先；下一步是按目标工程结构迁移或补齐缺口。"
        elif leaders:
            next_step = "复核领先工程的可复用增量，抽象后反哺源能力 / TRANSFER / sensor。"
        else:
            next_step = "先补可检测的 skill / governance / TRANSFER / sensor / views 证据。"
        compact_cards_by_scope[scope].append(
            "<article class=\"skill-card\">"
            f"<div class=\"skill-card-head\"><div><code>{html.escape(skill['name'])}</code>"
            f"<p>{html.escape(skill['description'])}</p></div>"
            f"<span class=\"score\">{row['max_score']}</span></div>"
            f"<p class=\"scope-meta scope-{html.escape(scope)}\"><strong>{html.escape(scope_label)}</strong><span>{html.escape(scope_note)}</span></p>"
            f"<p class=\"source-meta\"><strong>源头</strong>{html.escape(source_roots if source_roots else '暂无')}<span>发现于：{html.escape(source_projects if source_projects else '暂无')}</span><span>子项：{html.escape(member_text)}（{html.escape(member_count)}）</span></p>"
            "<div class=\"compact-grid\">"
            f"<div><strong>领先</strong><span>{html.escape('、'.join(leaders) if leaders else '暂无')}</span></div>"
            f"<div><strong>成熟</strong><span>{html.escape('、'.join(mature_projects) if mature_projects else '暂无')}</span></div>"
            f"<div><strong>已接入</strong><span>{html.escape('、'.join(adopted[:5]) if adopted else '暂无')}</span></div>"
            f"<div><strong>局部 / 缺口</strong><span>{html.escape('、'.join(partial[:4]) if partial else '暂无局部')}；{missing_count} 个未见</span></div>"
            "</div>"
            f"<p class=\"next-step\">{html.escape(next_step)}</p>"
            f"<p class=\"source-line\">source roots: {html.escape(source_roots)} · found in: {html.escape(source_projects)} · TRANSFER: {html.escape(str(skill['has_transfer']))} · max score: {row['max_score']} · paths: {html.escape(source_paths)}</p>"
            "</article>"
        )
        overview_cells = "\n".join(
            f"<td class=\"heat-cell heat-{c['status']}{' heat-source' if c['project'].label in origin_projects else ''}\" title=\"{html.escape(c['project'].label + ': ' + c['note'] + ('；' + c['leader_rule_note'] if c.get('leader_rule_note') else '') + ('；源头工程。' if c['project'].label in origin_projects else ''))}\"><span>{STATUS_LABELS[c['status']]}<small>{c['score']}</small></span></td>"
            for c in row["cells"]
        )
        subitem_text = f"子项：{member_count}"
        overview_rows_by_scope[scope].append(
            "<tr>"
            f"<th title=\"{html.escape(skill['name'] + ' · 源头：' + (source_roots if source_roots else '暂无') + ' · 领先：' + ('、'.join(leaders) if leaders else '暂无'))}\"><code>{html.escape(skill['display_name'])}</code><span>{html.escape(subitem_text)}</span></th>"
            f"{overview_cells}</tr>"
        )

    project_cards = "\n".join(
        f"<article><strong>{html.escape(p.label)}</strong><span>{html.escape(p.registry_level)}</span>"
        f"<p>{html.escape(str(p.path))}</p></article>"
        for p in PROJECTS
    )

    def render_matrix_section(scope: str) -> str:
        rows = "".join(overview_rows_by_scope.get(scope, []))
        if not rows:
            return ""
        return (
            "<section>"
            f"<h2>{html.escape(SCOPE_LABELS[scope])}技能 / 能力 x 工程矩阵</h2>"
            f"<p class=\"section-note\">{html.escape(SCOPE_DESCRIPTIONS[scope])}</p>"
            "<div class=\"overview-shell\">"
            "<table class=\"overview-matrix\">"
            f"<thead><tr><th>技能 / 能力</th>{''.join(f'<th><span>{html.escape(p.label)}</span></th>' for p in PROJECTS)}</tr></thead>"
            f"<tbody>{rows}</tbody>"
            "</table>"
            "</div>"
            "<p class=\"overview-note\">格子底色显示成熟度，深色内边框和底部斜纹显示源头工程；第一列只保留能力名和子项数量。数字是该工程在该技能主题或治理能力下的证据信号分，不代表目标工程运行验收。</p>"
            "</section>"
        )

    def render_detail_section(scope: str) -> str:
        cards = "".join(compact_cards_by_scope.get(scope, []))
        if not cards:
            return ""
        return (
            "<section>"
            f"<h2>{html.escape(SCOPE_LABELS[scope])}技能 / 能力详情</h2>"
            f"<p class=\"section-note\">{html.escape(SCOPE_DESCRIPTIONS[scope])}</p>"
            f"<div class=\"skill-card-list\">{cards}</div>"
            "</section>"
        )

    matrix_sections = "\n".join(render_matrix_section(scope) for scope in sorted(SCOPE_LABELS, key=SCOPE_SORT_ORDER.get))
    detail_sections = "\n".join(render_detail_section(scope) for scope in sorted(SCOPE_LABELS, key=SCOPE_SORT_ORDER.get))

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>跨工程技能与治理能力成熟度矩阵</title>
  <meta name="lens_id" content="lens-skill-maturity-matrix-current">
  <meta name="focus_object" content="grouped general skills, governance capabilities, and project-bound domain skills across AcknowledgeBase and registered projects">
  <meta name="lens_type" content="knowledge">
  <meta name="generated_at" content="{html.escape(generated)}">
  <meta name="source_revision" content="{html.escape(source_revision)}">
  <meta name="source_pages" content="skills/README.md; projects/governance/registry.md; views/lens-registry.md">
  <meta name="source_scope" content="all discovered project skill files grouped into skill themes, split into general transferable capabilities and project/domain-bound capabilities, plus supplemental governance capability rows and local transfer, governance, sensor, template, view, and selected log evidence">
  <meta name="evidence_boundary" content="confirmed local skill-file discovery plus supplemental governance capability discovery and content-volume signals; detailed skills are grouped into larger themes and split by transferability scope; no runtime validation">
  <meta name="context_frame" content="cross-project grouped skill-theme and governance capability catalog with source roots, subitems, maturity ranking, and project-bound capability separation; source project participates in the same ranking as downstream projects">
  <meta name="output_mode" content="html_report / print_view">
  <meta name="visual_structure" content="overview matrix / compact skill cards / project cards">
  <meta name="export_profile" content="A4 landscape PDF and PNG generated from same canonical HTML">
  <meta name="print_profile" content="@page A4 landscape; repeat header; preserve sticky columns as regular table">
  <meta name="equivalence_profile" content="HTML / PDF / PNG use same source pack and same canonical HTML / source / manifest render pipeline">
  <meta name="default_auto_exports" content="PDF and PNG generated to views/.exports/ when this persistent HTML lens is updated">
  <meta name="conversation_png_preview" content="final response should display the generated PNG preview">
  <style>
    :root {{
      color-scheme: light;
      --ink: #1c2430;
      --muted: #647181;
      --line: #d8e0e8;
      --panel: #ffffff;
      --paper: #f5f7fa;
      --blue: #005fd8;
      --green: #008f3a;
      --amber: #d66a00;
      --red: #d10035;
      --violet: #5a2bc2;
      --teal: #008578;
      --gray: #2f3b4a;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--paper); color: var(--ink); line-height: 1.55; }}
    a {{ color: var(--blue); text-underline-offset: 3px; }}
    .wrap {{ width: min(1440px, calc(100vw - 36px)); margin: 0 auto; }}
    header {{ border-bottom: 1px solid var(--line); background: linear-gradient(180deg, #eef5f7 0%, #f8fafc 100%); }}
    .hero {{ min-height: 42vh; padding: 42px 0 28px; display: grid; gap: 22px; align-content: end; }}
    .eyebrow {{ color: var(--teal); font-size: 13px; font-weight: 800; }}
    h1 {{ max-width: 980px; margin: 0; font-size: clamp(34px, 5vw, 60px); line-height: 1.05; letter-spacing: 0; }}
    .subtitle {{ max-width: 980px; margin: 0; color: #344153; font-size: 18px; }}
    .meta-row {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 4px; }}
    .pill {{ display: inline-flex; align-items: center; min-height: 30px; padding: 4px 10px; border-radius: 999px; background: #e6edf3; color: #344153; font-size: 12px; font-weight: 700; }}
    main {{ padding: 30px 0 64px; }}
    section {{ margin: 0 0 30px; }}
    h2 {{ margin: 0 0 14px; font-size: 23px; letter-spacing: 0; }}
    .section-note {{ margin: -6px 0 12px; color: var(--muted); font-size: 13px; }}
    .cards {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
    .card, article {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 16px; box-shadow: 0 6px 18px rgba(28, 36, 48, 0.05); }}
    .card strong {{ display: block; font-size: 28px; line-height: 1; margin-bottom: 8px; }}
    .legend-groups {{ display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(280px, 0.8fr) minmax(320px, 1fr); gap: 12px; }}
    .legend-box {{ border: 1px solid var(--line); border-radius: 8px; background: var(--panel); padding: 12px; }}
    .legend-title {{ display: block; margin: 0 0 8px; color: #273549; font-size: 12px; font-weight: 900; }}
    .legend {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .status {{ display: inline-flex; align-items: center; justify-content: center; min-width: 46px; min-height: 24px; padding: 2px 8px; border-radius: 999px; color: white; font-size: 12px; font-weight: 800; }}
    .leader {{ background: var(--violet); }}
    .mature {{ background: var(--green); }}
    .adopted {{ background: var(--blue); }}
    .partial {{ background: var(--amber); }}
    .none {{ background: var(--gray); }}
    .blocked {{ background: var(--red); }}
    .overview-shell {{ overflow: auto; border: 1px solid var(--line); border-radius: 8px; background: var(--panel); }}
    .overview-matrix {{ min-width: 1180px; width: 100%; border-collapse: separate; border-spacing: 0; }}
    .overview-matrix th, .overview-matrix td {{ border-right: 2px solid #f8fafc; border-bottom: 2px solid #f8fafc; padding: 0; text-align: center; vertical-align: middle; }}
    .overview-matrix thead th {{ position: sticky; top: 0; z-index: 2; background: #dfe8f1; color: #172033; font-size: 12px; padding: 10px 8px; }}
    .overview-matrix thead th span {{ display: block; min-width: 74px; }}
    .overview-matrix tbody th {{ position: sticky; left: 0; z-index: 1; width: 260px; min-width: 260px; text-align: left; background: #eef2f6; padding: 10px 12px; }}
    .overview-matrix tbody th code {{ display: block; color: #172033; font-size: 13px; line-height: 1.35; white-space: normal; }}
    .overview-matrix tbody th span {{ display: block; margin-top: 4px; color: var(--muted); font-size: 11px; font-weight: 600; }}
    .heat-cell {{ position: relative; min-width: 76px; height: 44px; color: white; text-shadow: 0 1px 1px rgba(0, 0, 0, 0.24); overflow: hidden; }}
    .heat-cell span {{ display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 44px; font-size: 13px; font-weight: 900; letter-spacing: 0; }}
    .heat-cell small {{ margin-top: 1px; font-size: 10px; font-weight: 800; opacity: 0.88; }}
    .heat-source::before {{ content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 7px; background: repeating-linear-gradient(135deg, rgba(255,255,255,0.82) 0 4px, rgba(23,32,51,0.72) 4px 8px); opacity: 0.95; pointer-events: none; }}
    .heat-source::after {{ content: ""; position: absolute; inset: 4px; border: 2px solid rgba(23,32,51,0.9); border-radius: 4px; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.44); pointer-events: none; }}
    .source-sample {{ position: relative; display: inline-flex; align-items: center; justify-content: center; width: 70px; height: 28px; border-radius: 6px; background: #005fd8; color: white; font-size: 11px; font-weight: 900; overflow: hidden; text-shadow: 0 1px 1px rgba(0,0,0,0.24); }}
    .source-sample::before {{ content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 7px; background: repeating-linear-gradient(135deg, rgba(255,255,255,0.82) 0 4px, rgba(23,32,51,0.72) 4px 8px); }}
    .source-sample::after {{ content: ""; position: absolute; inset: 4px; border: 2px solid rgba(23,32,51,0.9); border-radius: 4px; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.44); }}
    .marker-row {{ display: flex; gap: 10px; align-items: center; color: var(--muted); font-size: 12px; }}
    .scope-row {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; color: var(--muted); font-size: 12px; }}
    .scope-pill {{ display: inline-flex; align-items: center; min-height: 24px; padding: 2px 8px; border-radius: 999px; background: #e7eef6; color: #27415f; font-weight: 900; }}
    .scope-pill.bound {{ background: #fff1df; color: #7a3a00; border: 1px solid #e6a35a; }}
    .heat-leader {{ background: #5a2bc2 !important; }}
    .heat-mature {{ background: #008f3a !important; }}
    .heat-adopted {{ background: #005fd8 !important; }}
    .heat-partial {{ background: #d66a00 !important; }}
    .heat-none {{ background: #2f3b4a !important; }}
    .heat-blocked {{ background: #d10035 !important; }}
    .overview-note {{ margin: 8px 0 0; color: var(--muted); font-size: 12px; }}
    .skill-card-list {{ display: grid; gap: 12px; }}
    .skill-card {{ padding: 14px; }}
    .skill-card-head {{ display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 12px; align-items: start; margin-bottom: 12px; }}
    .skill-card code {{ color: #172033; font-size: 14px; font-weight: 800; white-space: normal; }}
    .skill-card p {{ margin: 5px 0 0; color: var(--muted); font-size: 12px; }}
    .scope-meta {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: -4px 0 8px !important; color: var(--muted) !important; }}
    .scope-meta strong {{ display: inline-flex; min-height: 24px; align-items: center; padding: 2px 8px; border-radius: 999px; background: #e7eef6; color: #27415f; font-size: 12px; }}
    .scope-project-bound strong {{ background: #fff1df; color: #7a3a00; border: 1px solid #e6a35a; }}
    .scope-meta span {{ display: inline-flex; min-height: 24px; align-items: center; color: var(--muted); font-size: 12px; }}
    .source-meta {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: -4px 0 12px !important; color: #263244 !important; }}
    .source-meta strong {{ display: inline-flex; min-height: 24px; align-items: center; padding: 2px 8px; border-radius: 999px; background: #e7eef6; color: #27415f; font-size: 12px; }}
    .source-meta span {{ display: inline-flex; min-height: 24px; align-items: center; color: var(--muted); font-size: 12px; }}
    .score {{ display: inline-flex; align-items: center; justify-content: center; min-width: 42px; min-height: 34px; border-radius: 8px; background: #e7eef6; color: #27415f; font-weight: 900; }}
    .compact-grid {{ display: grid; grid-template-columns: 1.1fr 1fr 1fr 0.8fr; gap: 10px; }}
    .compact-grid div {{ min-height: 74px; border: 1px solid var(--line); border-radius: 8px; padding: 10px; background: #fbfcfe; }}
    .compact-grid strong {{ display: block; margin-bottom: 5px; font-size: 12px; color: #2d3a4a; }}
    .compact-grid span {{ color: #253244; font-size: 13px; }}
    .next-step {{ border-left: 4px solid var(--teal); padding-left: 10px; color: #253244 !important; }}
    .source-line {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    table {{ border-collapse: separate; border-spacing: 0; width: 100%; }}
    th, td {{ vertical-align: top; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 10px; background: var(--panel); }}
    .project-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
    article strong {{ display: block; font-size: 16px; }}
    article span {{ display: block; margin-top: 4px; color: var(--blue); font-weight: 700; font-size: 12px; }}
    article p {{ margin: 8px 0 0; color: var(--muted); font-size: 12px; word-break: break-word; }}
    .boundary {{ border-left: 5px solid var(--amber); }}
    .source-list {{ color: var(--muted); font-size: 13px; }}
    @media (max-width: 900px) {{
      .cards, .project-grid, .compact-grid, .legend-groups {{ grid-template-columns: 1fr; }}
      .wrap {{ width: min(100vw - 20px, 1440px); }}
      h1 {{ font-size: 34px; }}
    }}
    @media print {{
      @page {{ size: A4 landscape; margin: 10mm; }}
      body {{ background: white; }}
      .wrap {{ width: 100%; }}
      .hero {{ min-height: 0; padding: 0 0 12px; }}
      table, .overview-matrix {{ min-width: 0; font-size: 9px; }}
      th, td {{ padding: 5px; }}
      thead th, .overview-matrix tbody th {{ position: static; }}
      .cards, .project-grid {{ grid-template-columns: repeat(4, 1fr); }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap hero">
      <div class="eyebrow">Skill and governance capability maturity lens · 每三天刷新</div>
      <h1>跨工程技能与治理能力成熟度矩阵</h1>
      <p class="subtitle">每次刷新都会重新发现所有工程里的 skill 项，并把复盘、调研、文档维护、项目上下文入口等同主题能力归并成大项；细分子项在详情卡展开。通用 / 可迁移能力和项目 / 领域绑定能力分表呈现，避免把客群 DB 读回这类数据合同型技能误读成通用技能。</p>
      <div class="meta-row">
        <span class="pill">生成：{html.escape(generated)}</span>
        <span class="pill">源版本：{html.escape(source_revision)}</span>
        <span class="pill">汇总大项：{len(skills)}</span>
        <span class="pill">通用：{scope_counts['general']}</span>
        <span class="pill">项目 / 领域绑定：{scope_counts['project-bound']}</span>
        <span class="pill">底层细项：{total_member_count}</span>
        <span class="pill">工程数：{len(PROJECTS)}</span>
      </div>
    </div>
  </header>
  <main class="wrap">
    <section class="cards">
      <div class="card"><strong>{len(skills)}</strong><span>本轮汇总技能 / 能力大项</span></div>
      <div class="card"><strong>{scope_counts['general']}</strong><span>通用 / 可迁移大项</span></div>
      <div class="card"><strong>{scope_counts['project-bound']}</strong><span>项目 / 领域绑定大项</span></div>
      <div class="card"><strong>{sum(1 for s in skills if s['has_transfer'] == 'yes')}</strong><span>大项含 TRANSFER.md</span></div>
    </section>

    <section>
      <h2>图例</h2>
      <div class="legend-groups">
        <div class="legend-box">
          <strong class="legend-title">成熟度颜色</strong>
          <div class="legend">
            {''.join(f'<span class="status {k}">{v}</span>' for k, v in STATUS_LABELS.items())}
          </div>
        </div>
        <div class="legend-box">
          <strong class="legend-title">源头标记</strong>
          <div class="marker-row"><span class="source-sample">源头</span><span>深色内边框 + 底部斜纹表示该工程是此能力源头；成熟度仍由底色决定。</span></div>
        </div>
        <div class="legend-box">
          <strong class="legend-title">分类口径</strong>
          <div class="scope-row"><span class="scope-pill">通用 / 可迁移</span><span>迁移方法与守卫。</span><span class="scope-pill bound">项目 / 领域绑定</span><span>只抽象方法，不复制项目事实。</span></div>
        </div>
      </div>
    </section>

    <section class="card">
      <h2>行动诊断与结构化数据</h2>
      <p>HTML 只保留鸟瞰矩阵。逐工程、逐技能的分差、缺失信号和建议修改方向写入 <a href="./skill-maturity-diagnostics.md">skill-maturity-diagnostics.md</a>；同一轮扫描的结构化数据写入 <a href="./skill-maturity-matrix.data.json">skill-maturity-matrix.data.json</a>。三份产物由同一个生成脚本同步重写，避免总览、诊断和数据漂移。领先不是简单最高分：必须覆盖同一技能下全体工程已经出现的独特证据信号。</p>
    </section>

    {matrix_sections}

    {detail_sections}

    <section>
      <h2>工程范围</h2>
      <div class="project-grid">{project_cards}</div>
    </section>

    <section class="card boundary">
      <h2>证据边界</h2>
      <p>confirmed：本机文件存在、技能或能力入口可读、注册表已记录。dynamic catalog：每次刷新重新发现所有工程的 skill 文件，先按同主题归并成大项，再按通用 / 可迁移与项目 / 领域绑定分表呈现，并追加少量补充治理能力行。relative ranking：按同名 / 别名 skill 或治理能力、TRANSFER、sensor、views、template、governance 和正文体量信号计算相对成熟度；只有覆盖同一技能下全体工程独特证据信号并集的最高分工程才能标为领先；源头工程用边框和底部纹理标记。blocked：路径不可读。</p>
      <p>本页不直接修改子工程，不裁定子工程状态，也不表示可从下游原样复制。任何“领先”或“成熟”都只是本轮信号强弱；通用能力可迁移的是触发、事实源、流程、输出、验证和守卫，项目 / 领域绑定能力只能抽象方法，不能复制业务表、服务名、运行 ID、本地路径、项目状态或一次性 handoff。</p>
      <p class="source-list">主要来源：skills/README.md、projects/governance/registry.md、所有工程 skill / TRANSFER / governance / sensor / views / template 路径，以及补充治理能力清单。生成脚本：scripts/update_skill_maturity_matrix.py。同步产物：views/current/governance/skill-maturity-diagnostics.md、views/current/governance/skill-maturity-matrix.data.json。</p>
    </section>
  </main>
</body>
</html>
"""


def project_ref(path: Path, project: Project) -> str:
    try:
        return f"{project.label}:{path.relative_to(project.path).as_posix()}"
    except ValueError:
        return str(path)


def relative_output(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def cell_diagnostic(row: Dict[str, Any], cell: Dict[str, Any]) -> Dict[str, Any]:
    skill = row["skill"]
    project = cell["project"]
    leaders = [leader for leader in row["cells"] if leader["status"] == "leader"]
    leader_gap = bool(row.get("leader_gap"))
    top_cells = [
        item for item in row["cells"]
        if item["score"] == row["max_score"] and item["score"] > 0
    ]
    comparison_cells = leaders if leaders else top_cells
    leader_signals = [str(signal) for signal in row.get("required_leader_fingerprint", [])]
    current_signals = sorted(cell.get("signals", []))
    current_fingerprint = list(evidence_fingerprint(current_signals))
    missing_signals = [signal for signal in leader_signals if signal not in current_fingerprint]
    score_gap = max(row["max_score"] - cell["score"], 0)
    status = cell["status"]
    scope = str(skill.get("capability_scope", "general"))

    if status == "leader":
        missing_signals = []
        direction = "保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。"
    elif leader_gap and cell["score"] == row["max_score"] and cell["score"] > 0:
        direction = f"互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 {', '.join(missing_signals[:4]) if missing_signals else '无'}；覆盖证据信号并集后，才可重新评为领先。"
    elif status == "none":
        direction = "先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。"
    elif scope == "project-bound":
        direction = "只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。"
    elif missing_signals:
        direction = f"追齐领先信号：优先补 {', '.join(missing_signals[:4])}；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。"
    else:
        direction = "补证据质量：扩大正文可读性、补迁移说明、验证样例或检查脚本，让能力从可见提升到可复用。"

    leader_labels = [leader["project"].label for leader in comparison_cells]
    return {
        "skill": str(skill["name"]),
        "display_name": str(skill["display_name"]),
        "scope": scope,
        "scope_label": SCOPE_LABELS.get(scope, scope),
        "member_names": [str(item) for item in skill.get("member_display_names", [skill["display_name"]])],
        "source_projects": [str(item) for item in skill.get("source_projects", [])],
        "origin_projects": [str(item) for item in skill.get("origin_projects", skill.get("source_projects", []))],
        "project": project.label,
        "status": status,
        "status_label": STATUS_LABELS[status],
        "score": cell["score"],
        "max_score": row["max_score"],
        "score_gap": score_gap,
        "leaders": leader_labels,
        "leader_gap": leader_gap,
        "leader_rule_note": str(cell.get("leader_rule_note", "")),
        "required_leader_fingerprint": leader_signals,
        "signals": current_signals,
        "fingerprint": current_fingerprint,
        "missing_leader_signals": missing_signals,
        "evidence_note": cell["note"],
        "evidence_paths": [project_ref(path, project) for path in cell.get("hits", [])],
        "recommended_direction": direction,
    }


def diagnostics_for_context(context: Dict[str, Any]) -> List[Dict[str, Any]]:
    diagnostics: List[Dict[str, Any]] = []
    for row in context["matrix"]:
        for cell in row["cells"]:
            diagnostics.append(cell_diagnostic(row, cell))
    return diagnostics


def render_json(context: Dict[str, Any]) -> str:
    diagnostics = diagnostics_for_context(context)
    payload = {
        "generated_at": context["generated"],
        "source_revision": context["source_revision"],
        "source_scope": "local skill/governance/sensor/view/template discovery; no runtime validation",
        "outputs": {
            "html": relative_output(OUTPUT),
            "diagnostics_md": relative_output(DIAGNOSTICS_OUTPUT),
            "data_json": relative_output(DATA_OUTPUT),
        },
        "projects": [
            {
                "key": project.key,
                "label": project.label,
                "role": project.role,
                "path": str(project.path),
                "registry_level": project.registry_level,
                "exists": project.path.exists(),
            }
            for project in PROJECTS
        ],
        "skills": [
            {
                "name": str(skill["name"]),
                "display_name": str(skill["display_name"]),
                "scope": str(skill.get("capability_scope", "general")),
                "scope_note": str(skill.get("scope_note", "")),
                "member_names": [str(item) for item in skill.get("member_display_names", [skill["display_name"]])],
                "source_projects": [str(item) for item in skill.get("source_projects", [])],
                "origin_projects": [str(item) for item in skill.get("origin_projects", skill.get("source_projects", []))],
                "source_paths": [str(item) for item in skill.get("source_paths", [])],
                "has_transfer": str(skill.get("has_transfer", "no")),
                "has_source": str(skill.get("has_source", "no")),
            }
            for skill in context["skills"]
        ],
        "diagnostics": diagnostics,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def render_markdown(context: Dict[str, Any]) -> str:
    diagnostics = diagnostics_for_context(context)
    by_project: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for item in diagnostics:
        by_project[item["project"]].append(item)

    lines = [
        "---",
        "type: skill-maturity-diagnostics",
        "lens_id: lens-skill-maturity-diagnostics-current",
        "focus_object: per-project action diagnostics for cross-project skill maturity gaps",
        "lens_type: knowledge",
        "source_pages: skills/README.md; projects/governance/registry.md; scripts/update_skill_maturity_matrix.py",
        "source_scope: same scan context as skill-maturity-matrix.html and skill-maturity-matrix.data.json",
        "source_of_truth: false",
        f"generated_at: {context['generated']}",
        f"source_revision: {context['source_revision']}",
        "evidence_boundary: local skill/governance/sensor/view/template discovery and content-volume signals only; no runtime validation",
        "context_frame: action-oriented companion to the HTML matrix; groups diagnostics by project so each project can see missing signals and recommended modification directions",
        "output_mode: generated_markdown_diagnostics",
        "export_profile: none; HTML matrix owns PDF/PNG exports",
        "print_profile: not optimized for print; use HTML matrix for print-oriented output",
        "equivalence_profile: generated from the same build_context as HTML and JSON outputs",
        "canonical_policy: overwritten by scripts/update_skill_maturity_matrix.py on every matrix refresh",
        "snapshot_policy: freeze separately only when a dated audit snapshot is needed",
        "staleness_policy: stale when any scanned skill/governance/sensor/view/template path, ranking rule, action diagnostic rule, project registry, or data schema changes",
        "refresh_trigger: rerun scripts/update_skill_maturity_matrix.py",
        "tags: [views, governance, skill-maturity, diagnostics]",
        "---",
        "",
        "# 跨工程技能成熟度行动诊断",
        "",
        "本页由 `scripts/update_skill_maturity_matrix.py` 生成，和 [[views/current/governance/skill-maturity-matrix.html]]、`views/current/governance/skill-maturity-matrix.data.json` 使用同一轮扫描上下文。它不是手写真相源；每次刷新矩阵时应同步重写。",
        "",
        "## 使用边界",
        "",
        "- `领先 / 成熟 / 接入 / 局部 / 未见` 只表示本地文件证据信号强弱，不代表运行时验收。",
        "- `领先` 要求该工程覆盖同一技能下全体工程已经出现的独特证据信号；如果多个工程各有特色但没有任何一个覆盖并集，只能标为成熟或接入，并在诊断里提示互补对齐方向。",
        "- `建议修改方向` 只指出下一步补证据或补能力的方向；项目 / 领域绑定技能只能抽象方法，不复制业务表、路径、运行 ID、状态或一次性 handoff。",
        "- HTML 负责鸟瞰，JSON 负责结构化数据，本页负责每个工程可读的行动诊断。",
        "",
        "## 输出互链",
        "",
        f"- HTML 总览：[[{relative_output(OUTPUT)}]]",
        f"- JSON 数据：`{relative_output(DATA_OUTPUT)}`",
        "",
    ]

    status_sort = {"none": 0, "partial": 1, "adopted": 2, "mature": 3, "leader": 4, "blocked": 5}
    for project in PROJECTS:
        items = by_project.get(project.label, [])
        if not items:
            continue
        counts = {status: sum(1 for item in items if item["status"] == status) for status in STATUS_LABELS}
        lines.extend(
            [
                f"## {project.label}",
                "",
                f"- **工程路径**：`{project.path}`",
                f"- **成熟概览**：领先 {counts['leader']}；成熟 {counts['mature']}；接入 {counts['adopted']}；局部 {counts['partial']}；未见 {counts['none']}；阻塞 {counts['blocked']}。",
                "",
                "| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |",
                "| --- | --- | --- | ---: | --- | --- | --- | --- |",
            ]
        )
        sorted_items = sorted(
            items,
            key=lambda item: (
                status_sort.get(item["status"], 9),
                -item["score_gap"],
                item["display_name"],
            ),
        )
        for item in sorted_items:
            leaders = "、".join(item["leaders"]) if item["leaders"] else "暂无"
            signals = "、".join(item["signals"]) if item["signals"] else "无"
            missing = "、".join(item["missing_leader_signals"]) if item["missing_leader_signals"] else "无"
            lines.append(
                "| "
                f"{item['display_name']} (`{item['skill']}`) | "
                f"{item['scope_label']} | "
                f"{item['status_label']} {item['score']}/{item['max_score']} | "
                f"{item['score_gap']} | "
                f"{leaders} | "
                f"{signals} | "
                f"{missing} | "
                f"{item['recommended_direction']} |"
            )
        lines.append("")
        lines.append("### 证据路径")
        lines.append("")
        for item in sorted_items:
            if not item["evidence_paths"]:
                continue
            lines.append(f"- **{item['display_name']}**：`" + "`、`".join(item["evidence_paths"][:5]) + "`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    context = build_context()
    for path, content in [
        (OUTPUT, render_html(context)),
        (DIAGNOSTICS_OUTPUT, render_markdown(context)),
        (DATA_OUTPUT, render_json(context)),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"updated {path}")


if __name__ == "__main__":
    main()

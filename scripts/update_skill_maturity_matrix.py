#!/usr/bin/env python3
"""Generate the cross-project skill maturity HTML lens."""

from __future__ import annotations

import html
import os
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "views" / "current" / "governance" / "skill-maturity-matrix.html"


@dataclass(frozen=True)
class Project:
    key: str
    label: str
    role: str
    path: Path
    registry_level: str


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
    "knowledge-linking": ["knowledge-linking"],
    "technology-research-router": ["technology-research"],
    "technical-topic-research": ["technical-topic"],
    "open-source-project-research": ["open-source-project"],
    "industry-ai-research": ["industry-ai"],
    "cross-project-skill-adoption-prompt": ["skill-adoption", "skill-transfer"],
}


STATUS_OVERRIDES: Dict[Tuple[str, str], Tuple[str, str]] = {
    ("cross-project-governance-audit", "ack"): ("source", "源审计技能，读取注册表与平台标准生成漂移报告。"),
    ("cross-project-governance-audit", "doccust"): ("partial", "有治理台账、episode 与 sensor，可作为审计对象成熟样本。"),
    ("cross-project-governance-audit", "docfilm"): ("partial", "有治理台账和 sensor，适合继续审计补齐。"),
    ("cross-project-governance-audit", "fetch"): ("partial", "有子工程 harness 规则和检查脚本，但审计能力不在本地。"),
    ("cross-project-governance-audit", "train"): ("partial", "有问题聚焦技能和部分治理痕迹，需审计确认深度。"),
    ("cross-project-governance-audit", "prefect"): ("partial", "有规则和技能目录，episode / sensor 证据较薄。"),
    ("cross-project-governance-audit", "wiki"): ("mature", "模板源具备治理台账、复盘 sensor 和模板，可反哺审计维度。"),
    ("cross-project-skill-adoption-prompt", "ack"): ("source", "当前唯一源技能，承担上游归一和迁移任务书生成。"),
    ("historical-dialogue-retrospective", "ack"): ("source", "源技能 + TRANSFER，已接入复盘概念和 Harness episode。"),
    ("historical-dialogue-retrospective", "doccust"): ("mature", "本地有历史对话复盘、项目复盘和多份真实复盘档案。"),
    ("historical-dialogue-retrospective", "wiki"): ("mature", "模板源有复盘技能、复盘 sensor 和概念/模板链。"),
    ("historical-dialogue-retrospective", "customer"): ("adopted", "已有 .codex 技能，偏子工程文档协作场景。"),
    ("historical-dialogue-retrospective", "life"): ("adjacent", "system-harness-review 是生活系统化的相邻成熟能力。"),
    ("issue-analysis", "ack"): ("source", "主控侧 issue / incident 分析源技能。"),
    ("issue-analysis", "doccust"): ("mature", "主控项目内有 issue skill、事项体系、报告链和实战验收反馈。"),
    ("issue-analysis", "docfilm"): ("mature", "已吸收主控侧 issue skill，并补充快速诊断/升级边界。"),
    ("issue-analysis", "wiki"): ("adopted", "模板源已安装 issue-analysis，可作为结构对照。"),
    ("issue-analysis", "docerp"): ("adopted", "存在同名主控 issue skill，证据尚未展开。"),
    ("issue-analysis", "fetch"): ("adjacent", "有 issue-incident-analysis，偏子工程故障/文档变更场景。"),
    ("knowledge-linking", "ack"): ("source", "当前源技能，并有专项 sensor。"),
    ("problem-focused-visual-presentation", "ack"): ("source", "源技能 + TRANSFER + views/registry + sensor。"),
    ("problem-focused-visual-presentation", "doccust"): ("mature", "有同名 skill、TRANSFER、views 合同和业务图文 lens 落地。"),
    ("problem-focused-visual-presentation", "docfilm"): ("mature", "同名 skill 已本地化到主控项目 views 体系。"),
    ("problem-focused-visual-presentation", "life"): ("mature", "problem-focused-lens 是已反哺上游的重要成熟样本。"),
    ("problem-focused-visual-presentation", "train"): ("adopted", "有训练平台本地化问题聚焦 skill。"),
    ("problem-focused-visual-presentation", "h100"): ("adopted", "有 H100 本地化问题聚焦 skill。"),
    ("problem-focused-visual-presentation", "customer"): ("adopted", "有 .codex 同名问题聚焦 skill。"),
    ("problem-focused-visual-presentation", "fetch"): ("adopted", "有 .codex 同名问题聚焦 skill。"),
    ("technology-research-router", "ack"): ("source", "技术调研总控源技能。"),
    ("technical-topic-research", "ack"): ("source", "技术专题调研源技能。"),
    ("open-source-project-research", "ack"): ("source", "开源工程尽调源技能。"),
    ("industry-ai-research", "ack"): ("source", "IT / AI 行业调研源技能。"),
}


STATUS_LABELS = {
    "source": "源",
    "mature": "成熟",
    "adopted": "已接入",
    "partial": "局部",
    "adjacent": "相邻",
    "none": "未见",
    "blocked": "阻塞",
}

STATUS_SCORES = {
    "source": 5,
    "mature": 4,
    "adopted": 3,
    "partial": 2,
    "adjacent": 1,
    "none": 0,
    "blocked": -1,
}


def run(cmd: List[str], cwd: Path = ROOT) -> str:
    try:
        return subprocess.check_output(cmd, cwd=cwd, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def read_skill_manifest() -> List[Dict[str, str]]:
    rows = []
    for skill_path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = skill_path.read_text(encoding="utf-8")
        name = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
        desc = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
        rows.append(
            {
                "name": name.group(1).strip() if name else skill_path.parent.name,
                "path": str(skill_path.relative_to(ROOT)),
                "description": desc.group(1).strip() if desc else "",
                "has_transfer": "yes" if (skill_path.parent / "TRANSFER.md").exists() else "no",
            }
        )
    return rows


def iter_candidate_files(project: Project) -> Iterable[Path]:
    if not project.path.exists():
        return []
    patterns = [
        "skills/**/SKILL.md",
        ".codex/skills/**/SKILL.md",
        ".claude/skills/**/SKILL.md",
        ".agents/skills/**/SKILL.md",
        "governance/*.md",
        "rules/*.md",
        ".codex/context/*.md",
        "logs/system/*.md",
        "templates/*harness*.md",
        "scripts/check_*.py",
        "tools/check_*.py",
        "automation/scripts/check_*.py",
    ]
    files: List[Path] = []
    for pattern in patterns:
        files.extend(project.path.glob(pattern))
    return sorted(set(p for p in files if p.is_file()))


def evidence_for(project: Project, skill_name: str) -> List[Path]:
    terms = [skill_name] + ALIASES.get(skill_name, [])
    normalized_terms = [t.lower().replace("_", "-") for t in terms]
    hits = []
    for path in iter_candidate_files(project):
        rel = str(path.relative_to(project.path)).lower().replace("_", "-")
        if any(term in rel for term in normalized_terms):
            hits.append(path)
            continue
        if skill_name in {"cross-project-governance-audit", "historical-dialogue-retrospective"}:
            if any(token in rel for token in ["harness", "retrospective", "governance"]):
                hits.append(path)
        elif skill_name == "issue-analysis" and any(token in rel for token in ["issue", "incident"]):
            hits.append(path)
    return hits[:5]


def infer_status(project: Project, skill: Dict[str, str], hits: List[Path]) -> Tuple[str, str]:
    key = (skill["name"], project.key)
    if key in STATUS_OVERRIDES:
        return STATUS_OVERRIDES[key]
    if not project.path.exists():
        return "blocked", "本机路径当前不可读。"
    if not hits:
        return "none", "未在常见 skill / governance / sensor 路径发现等价能力。"
    rels = [str(p.relative_to(project.path)) for p in hits]
    if any(f"{skill['name']}/SKILL.md" in rel for rel in rels):
        return "adopted", "存在同名本地 skill，需进一步读正文判断成熟度。"
    return "partial", "发现相邻文件或治理痕迹，但未确认等价 skill。"


def render_cell(status: str, note: str, hits: List[Path], project: Project) -> str:
    label = STATUS_LABELS[status]
    cls = f"status {status}"
    evidence = ""
    if hits:
        rel = html.escape(str(hits[0].relative_to(project.path)))
        evidence = f"<span class=\"evidence\">{rel}</span>"
    return (
        f"<div class=\"cell-stack\"><span class=\"{cls}\">{label}</span>"
        f"<span class=\"note\">{html.escape(note)}</span>{evidence}</div>"
    )


def render_html() -> str:
    skills = read_skill_manifest()
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    source_revision = run(["git", "rev-parse", "--short", "HEAD"]) or "working-tree"

    matrix = []
    for skill in skills:
        cells = []
        mature_projects = []
        coverage_score = 0
        for project in PROJECTS:
            hits = evidence_for(project, skill["name"])
            status, note = infer_status(project, skill, hits)
            coverage_score += max(STATUS_SCORES[status], 0)
            if status in {"mature", "source"}:
                mature_projects.append(project.label)
            cells.append({"project": project, "status": status, "note": note, "hits": hits})
        matrix.append({"skill": skill, "cells": cells, "mature_projects": mature_projects, "score": coverage_score})

    summary_rows = []
    for row in matrix:
        absorbers = [p for p in row["mature_projects"] if p != "AcknowledgeBase"]
        if not absorbers:
            absorbers = ["暂无下游成熟样本"]
        summary_rows.append(
            f"<tr><td><code>{html.escape(row['skill']['name'])}</code></td>"
            f"<td>{html.escape(row['skill']['has_transfer'])}</td>"
            f"<td>{html.escape('、'.join(absorbers))}</td>"
            f"<td>{row['score']}</td></tr>"
        )

    project_headers = "\n".join(
        f"<th><span>{html.escape(p.label)}</span><small>{html.escape(p.role)}</small></th>" for p in PROJECTS
    )
    table_rows = []
    for row in matrix:
        skill = row["skill"]
        cells = "\n".join(
            f"<td>{render_cell(c['status'], c['note'], c['hits'], c['project'])}</td>"
            for c in row["cells"]
        )
        absorbers = [p for p in row["mature_projects"] if p != "AcknowledgeBase"]
        recommendation = "、".join(absorbers) if absorbers else "先补上游 TRANSFER / sensor，再观察下游。"
        table_rows.append(
            "<tr>"
            f"<th class=\"skill-col\"><code>{html.escape(skill['name'])}</code>"
            f"<span>{html.escape(skill['description'])}</span>"
            f"<em>source: {html.escape(skill['path'])}</em></th>"
            f"<td class=\"recommend\">{html.escape(recommendation)}</td>"
            f"{cells}</tr>"
        )

    project_cards = "\n".join(
        f"<article><strong>{html.escape(p.label)}</strong><span>{html.escape(p.registry_level)}</span>"
        f"<p>{html.escape(str(p.path))}</p></article>"
        for p in PROJECTS
    )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>跨工程技能成熟度矩阵</title>
  <meta name="lens_id" content="lens-skill-maturity-matrix-current">
  <meta name="focus_object" content="AcknowledgeBase skills across subprojects">
  <meta name="lens_type" content="knowledge">
  <meta name="generated_at" content="{html.escape(generated)}">
  <meta name="source_revision" content="{html.escape(source_revision)}">
  <meta name="source_pages" content="skills/README.md; projects/governance/registry.md; views/lens-registry.md">
  <meta name="source_scope" content="local project skill directories and governance/sensor evidence">
  <meta name="evidence_boundary" content="confirmed local file presence; likely maturity from known source chains; no runtime validation">
  <meta name="context_frame" content="skill adoption and upstream absorption lens; presentation only, not target project status source">
  <meta name="output_mode" content="html_report / print_view">
  <meta name="visual_structure" content="matrix / recommendation table / project cards">
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
      --blue: #2764a4;
      --green: #2d7d4c;
      --amber: #a96713;
      --red: #ad3939;
      --violet: #6650a4;
      --teal: #0f766e;
      --gray: #536171;
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
    .cards {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
    .card, article {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 16px; box-shadow: 0 6px 18px rgba(28, 36, 48, 0.05); }}
    .card strong {{ display: block; font-size: 28px; line-height: 1; margin-bottom: 8px; }}
    .legend {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .status {{ display: inline-flex; align-items: center; justify-content: center; min-width: 46px; min-height: 24px; padding: 2px 8px; border-radius: 999px; color: white; font-size: 12px; font-weight: 800; }}
    .source {{ background: var(--violet); }}
    .mature {{ background: var(--green); }}
    .adopted {{ background: var(--blue); }}
    .partial {{ background: var(--amber); }}
    .adjacent {{ background: var(--teal); }}
    .none {{ background: var(--gray); }}
    .blocked {{ background: var(--red); }}
    .table-shell {{ overflow: auto; border: 1px solid var(--line); border-radius: 8px; background: var(--panel); max-height: 78vh; }}
    table {{ border-collapse: separate; border-spacing: 0; min-width: 2240px; width: 100%; }}
    th, td {{ vertical-align: top; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 10px; background: var(--panel); }}
    thead th {{ position: sticky; top: 0; z-index: 3; background: #edf3f8; text-align: left; font-size: 13px; }}
    thead th small {{ display: block; color: var(--muted); font-weight: 500; margin-top: 3px; }}
    .skill-col {{ position: sticky; left: 0; z-index: 2; width: 310px; min-width: 310px; background: #f8fafc; }}
    thead .skill-col {{ z-index: 4; }}
    .recommend {{ position: sticky; left: 310px; z-index: 2; width: 210px; min-width: 210px; background: #fbfcfe; font-weight: 650; color: #2f3b4a; }}
    thead .recommend {{ z-index: 4; background: #edf3f8; }}
    .skill-col code {{ display: block; font-size: 13px; color: #172033; white-space: normal; }}
    .skill-col span, .skill-col em {{ display: block; margin-top: 6px; color: var(--muted); font-style: normal; font-size: 12px; }}
    .cell-stack {{ display: grid; gap: 6px; min-width: 150px; max-width: 210px; }}
    .note {{ color: #384657; font-size: 12px; }}
    .evidence {{ color: var(--muted); font-size: 11px; word-break: break-word; }}
    .summary-table {{ min-width: 760px; }}
    .summary-table td, .summary-table th {{ position: static; }}
    .project-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
    article strong {{ display: block; font-size: 16px; }}
    article span {{ display: block; margin-top: 4px; color: var(--blue); font-weight: 700; font-size: 12px; }}
    article p {{ margin: 8px 0 0; color: var(--muted); font-size: 12px; word-break: break-word; }}
    .boundary {{ border-left: 5px solid var(--amber); }}
    .source-list {{ color: var(--muted); font-size: 13px; }}
    @media (max-width: 900px) {{
      .cards, .project-grid {{ grid-template-columns: 1fr; }}
      .wrap {{ width: min(100vw - 20px, 1440px); }}
      h1 {{ font-size: 34px; }}
    }}
    @media print {{
      @page {{ size: A4 landscape; margin: 10mm; }}
      body {{ background: white; }}
      .wrap {{ width: 100%; }}
      .hero {{ min-height: 0; padding: 0 0 12px; }}
      .table-shell {{ overflow: visible; max-height: none; }}
      table {{ min-width: 0; font-size: 9px; }}
      th, td {{ padding: 5px; }}
      .skill-col, .recommend, thead th {{ position: static; }}
      .cards, .project-grid {{ grid-template-columns: repeat(4, 1fr); }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap hero">
      <div class="eyebrow">Skill maturity lens · 每三天刷新</div>
      <h1>跨工程技能成熟度矩阵</h1>
      <p class="subtitle">按 AcknowledgeBase 当前技能逐行盘点各子工程接入状态，并标出哪些工程里的同类能力更成熟、值得抽象反哺。状态来自本机文件扫描和已知治理注册表；本页只作呈现，不替代各工程自己的 source of truth。</p>
      <div class="meta-row">
        <span class="pill">生成：{html.escape(generated)}</span>
        <span class="pill">源版本：{html.escape(source_revision)}</span>
        <span class="pill">技能数：{len(skills)}</span>
        <span class="pill">工程数：{len(PROJECTS)}</span>
      </div>
    </div>
  </header>
  <main class="wrap">
    <section class="cards">
      <div class="card"><strong>{len(skills)}</strong><span>当前知识库技能</span></div>
      <div class="card"><strong>{sum(1 for s in skills if s['has_transfer'] == 'yes')}</strong><span>已有 TRANSFER.md</span></div>
      <div class="card"><strong>{sum(1 for row in matrix if any(c['status'] == 'mature' for c in row['cells']))}</strong><span>存在下游成熟样本</span></div>
      <div class="card"><strong>3d</strong><span>建议刷新周期</span></div>
    </section>

    <section>
      <h2>状态图例</h2>
      <div class="legend">
        {''.join(f'<span class="status {k}">{v}</span>' for k, v in STATUS_LABELS.items())}
      </div>
    </section>

    <section>
      <h2>一眼吸收建议</h2>
      <div class="table-shell">
        <table class="summary-table">
          <thead><tr><th>技能</th><th>TRANSFER</th><th>更成熟 / 值得吸收的工程</th><th>覆盖分</th></tr></thead>
          <tbody>{''.join(summary_rows)}</tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>技能 x 子工程矩阵</h2>
      <div class="table-shell">
        <table>
          <thead>
            <tr><th class="skill-col">技能</th><th class="recommend">值得吸收</th>{project_headers}</tr>
          </thead>
          <tbody>
            {''.join(table_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>工程范围</h2>
      <div class="project-grid">{project_cards}</div>
    </section>

    <section class="card boundary">
      <h2>证据边界</h2>
      <p>confirmed：本机文件存在、技能入口可读、注册表已记录。likely：根据同名 skill、TRANSFER、sensor、治理台账和近期 log 判断成熟度。possible：只发现相邻文件或局部规则，未读完整正文。blocked：路径不可读或本轮未覆盖。</p>
      <p>本页不直接修改子工程，不裁定子工程状态，也不表示可从下游原样复制。任何“值得吸收”都必须先按上游归一规则抽象系统层信息，剥离项目事实、业务链路、运行 ID、本地路径和一次性 handoff。</p>
      <p class="source-list">主要来源：skills/README.md、skills/*/SKILL.md、projects/governance/registry.md、各工程 skill / governance / sensor 路径。生成脚本：scripts/update_skill_maturity_matrix.py。</p>
    </section>
  </main>
</body>
</html>
"""


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render_html(), encoding="utf-8")
    print(f"updated {OUTPUT}")


if __name__ == "__main__":
    main()

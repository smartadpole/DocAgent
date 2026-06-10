#!/usr/bin/env python3
"""Generate the cross-project skill maturity HTML lens."""

from __future__ import annotations

import html
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "views" / "current" / "governance" / "skill-maturity-matrix.html"


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
    "historical-dialogue-retrospective": "历史对话复盘",
    "industry-ai-research": "行业 / AI 调研",
    "issue-analysis": "Issue / 事故分析",
    "knowledge-linking": "知识关联",
    "open-source-project-research": "开源工程调研",
    "problem-focused-visual-presentation": "问题聚焦式图文呈现",
    "technical-topic-research": "技术专题调研",
    "technology-research-router": "技术调研路由",
}


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
                "display_name": SKILL_DISPLAY_NAMES.get(
                    name.group(1).strip() if name else skill_path.parent.name,
                    name.group(1).strip() if name else skill_path.parent.name,
                ),
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
        "views/README.md",
        "views/lens-registry.md",
        "views/current/**/*.html",
        "templates/*harness*.md",
        "templates/*lens*.md",
        "templates/*research*.md",
        "templates/*issue*.md",
        "scripts/check_*.py",
        "tools/check_*.py",
        "automation/scripts/check_*.py",
    ]
    files: List[Path] = []
    for pattern in patterns:
        files.extend(project.path.glob(pattern))
    return sorted(set(p for p in files if p.is_file()))


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def skill_terms(skill_name: str) -> List[str]:
    return [normalize(t) for t in [skill_name] + ALIASES.get(skill_name, [])]


def is_relevant_text(path: Path, terms: List[str]) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")[:200_000]
    except Exception:
        return False
    normalized = normalize(text)
    return any(term and term in normalized for term in terms)


def skill_entry_terms(path: Path, project: Project) -> List[str]:
    rel = path.relative_to(project.path)
    if path.name != "SKILL.md" or len(rel.parts) < 2:
        return []
    return [normalize(rel.parts[-2]), normalize(str(rel))]


def evidence_for(project: Project, skill_name: str) -> List[Path]:
    terms = skill_terms(skill_name)
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
        elif is_relevant_text(path, terms):
            hits.append(path)
    return sorted(set(hits))


def score_evidence(project: Project, skill: Dict[str, str], hits: List[Path]) -> Evidence:
    if not project.path.exists():
        return Evidence(score=-1, note="本机路径当前不可读。", hits=[], signals=[])
    if not hits:
        return Evidence(score=0, note="未在常见 skill / governance / sensor 路径发现等价能力。", hits=[], signals=[])

    terms = skill_terms(skill["name"])
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


def render_html() -> str:
    skills = read_skill_manifest()
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    source_revision = run(["git", "rev-parse", "--short", "HEAD"]) or "working-tree"

    matrix = []
    for skill in skills:
        scored_cells = []
        for project in PROJECTS:
            hits = evidence_for(project, skill["name"])
            evidence = score_evidence(project, skill, hits)
            scored_cells.append({"project": project, "evidence": evidence})

        max_score = max((cell["evidence"].score for cell in scored_cells), default=0)
        cells = []
        leading_projects = []
        mature_projects = []
        coverage_score = 0
        for cell in scored_cells:
            evidence = cell["evidence"]
            status = status_for(evidence.score, max_score)
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
            }
        )

    compact_cards = []
    overview_rows = []
    for row in matrix:
        skill = row["skill"]
        leaders = row["leading_projects"]
        mature_projects = [p for p in row["mature_projects"] if p not in leaders]
        adopted = [c["project"].label for c in row["cells"] if c["status"] == "adopted"]
        partial = [c["project"].label for c in row["cells"] if c["status"] == "partial"]
        missing_count = sum(1 for c in row["cells"] if c["status"] == "none")
        if leaders == ["AcknowledgeBase"]:
            next_step = "源头当前领先；下一步是把源技能增量按目标工程结构迁移出去。"
        elif leaders:
            next_step = "复核领先工程的可复用增量，抽象后反哺源 skill / TRANSFER / sensor。"
        else:
            next_step = "先补可检测的 skill / TRANSFER / sensor / views 证据。"
        compact_cards.append(
            "<article class=\"skill-card\">"
            f"<div class=\"skill-card-head\"><div><code>{html.escape(skill['name'])}</code>"
            f"<p>{html.escape(skill['description'])}</p></div>"
            f"<span class=\"score\">{row['max_score']}</span></div>"
            "<div class=\"compact-grid\">"
            f"<div><strong>领先</strong><span>{html.escape('、'.join(leaders) if leaders else '暂无')}</span></div>"
            f"<div><strong>成熟</strong><span>{html.escape('、'.join(mature_projects) if mature_projects else '暂无')}</span></div>"
            f"<div><strong>已接入</strong><span>{html.escape('、'.join(adopted[:5]) if adopted else '暂无')}</span></div>"
            f"<div><strong>局部 / 缺口</strong><span>{html.escape('、'.join(partial[:4]) if partial else '暂无局部')}；{missing_count} 个未见</span></div>"
            "</div>"
            f"<p class=\"next-step\">{html.escape(next_step)}</p>"
            f"<p class=\"source-line\">source skill: {html.escape(skill['path'])} · TRANSFER: {html.escape(skill['has_transfer'])} · max score: {row['max_score']}</p>"
            "</article>"
        )
        overview_cells = "\n".join(
            f"<td class=\"heat-cell heat-{c['status']}\" title=\"{html.escape(c['project'].label + ': ' + c['note'])}\"><span>{STATUS_LABELS[c['status']]}<small>{c['score']}</small></span></td>"
            for c in row["cells"]
        )
        recommendation = "领先：" + "、".join(leaders) if leaders else "补可检测证据"
        overview_rows.append(
            "<tr>"
            f"<th title=\"{html.escape(skill['name'])}\"><code>{html.escape(skill['display_name'])}</code><span>{html.escape(recommendation)}</span></th>"
            f"{overview_cells}</tr>"
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
  <meta name="source_scope" content="local project skill, transfer, governance, sensor, template, view, and selected log evidence">
  <meta name="evidence_boundary" content="confirmed local file presence and content-volume signals; relative maturity is recomputed for every project on every refresh; no runtime validation">
  <meta name="context_frame" content="cross-project skill maturity ranking lens; source project participates in the same ranking as downstream projects">
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
    .cards {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
    .card, article {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 16px; box-shadow: 0 6px 18px rgba(28, 36, 48, 0.05); }}
    .card strong {{ display: block; font-size: 28px; line-height: 1; margin-bottom: 8px; }}
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
    .heat-cell {{ min-width: 76px; height: 44px; color: white; text-shadow: 0 1px 1px rgba(0, 0, 0, 0.24); }}
    .heat-cell span {{ display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 44px; font-size: 13px; font-weight: 900; letter-spacing: 0; }}
    .heat-cell small {{ margin-top: 1px; font-size: 10px; font-weight: 800; opacity: 0.88; }}
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
      .cards, .project-grid, .compact-grid {{ grid-template-columns: 1fr; }}
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
      <div class="eyebrow">Skill maturity lens · 每三天刷新</div>
      <h1>跨工程技能成熟度矩阵</h1>
      <p class="subtitle">按 AcknowledgeBase 当前技能逐行盘点所有注册工程和观察工程的相对成熟度。源工程也参与同一套证据评分；每次刷新都会重新扫描 skill、TRANSFER、sensor、views、template、governance 和内容体量信号，不沿用静态成熟标签。</p>
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
      <div class="card"><strong>{sum(1 for row in matrix if row['leading_projects'] == ['AcknowledgeBase'])}</strong><span>源工程当前领先</span></div>
      <div class="card"><strong>3d</strong><span>建议刷新周期</span></div>
    </section>

    <section>
      <h2>状态图例</h2>
      <div class="legend">
        {''.join(f'<span class="status {k}">{v}</span>' for k, v in STATUS_LABELS.items())}
      </div>
    </section>

    <section>
      <h2>技能 x 子工程矩阵</h2>
      <div class="overview-shell">
        <table class="overview-matrix">
          <thead><tr><th>技能 / 当前领先</th>{''.join(f'<th><span>{html.escape(p.label)}</span></th>' for p in PROJECTS)}</tr></thead>
          <tbody>{''.join(overview_rows)}</tbody>
        </table>
      </div>
      <p class="overview-note">格子显示本轮动态得分后的相对等级；数字是该工程在该技能下的证据信号分，不代表目标工程运行验收。</p>
    </section>

    <section>
      <h2>技能详情</h2>
      <div class="skill-card-list">
        {''.join(compact_cards)}
      </div>
    </section>

    <section>
      <h2>工程范围</h2>
      <div class="project-grid">{project_cards}</div>
    </section>

    <section class="card boundary">
      <h2>证据边界</h2>
      <p>confirmed：本机文件存在、技能入口可读、注册表已记录。relative ranking：每次刷新重新扫描所有工程，按同名 / 别名 skill、TRANSFER、sensor、views、template、governance 和正文体量信号计算相对成熟度。blocked：路径不可读。</p>
      <p>本页不直接修改子工程，不裁定子工程状态，也不表示可从下游原样复制。任何“领先”或“成熟”都只是本轮信号强弱；吸收动作仍必须先按上游归一规则抽象系统层信息，剥离项目事实、业务链路、运行 ID、本地路径和一次性 handoff。</p>
      <p class="source-list">主要来源：skills/README.md、skills/*/SKILL.md、projects/governance/registry.md、各工程 skill / TRANSFER / governance / sensor / views / template 路径。生成脚本：scripts/update_skill_maturity_matrix.py。</p>
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

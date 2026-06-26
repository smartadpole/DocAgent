---
type: template
id: TEMPLATE-RESEARCH-INTAKE-001
status: active
updated: 2026-06-26
tags: [template, research, intake, frontier-technology-intake]
---

# Research Intake Template

用于把外部技术材料、论文、repo、产品更新、社区讨论或用户提供的资料归一成可研究、可路由、可验证的 intake item。它是 [[skills/research-capability/SKILL]] 的前置 intake 模板，不替代正式研究报告或项目决策。

## Intake Contract

- **item_id**：
- **source_type**：official-doc / paper / repo / release / blog / community / social / file / screenshot / user-note
- **source_ref**：
- **captured_at**：
- **title**：
- **topic_hint**：
- **access_boundary**：public / login / paid / private / user-provided / unknown
- **rights_notes**：
- **raw_landing**：
- **capture_method**：api / rss / browser-export / static-fetch / playwright / file / ocr / manual
- **extraction_quality**：complete / partial / low-confidence / blocked

## Intelligence Contract

- **frontier_tech_intake**：yes / no；新论文、repo、release、产品发布、官方博客、社区帖子或用户转发材料默认先作为 intake，不直接写成结论。
- **sensing_mode**：manual / watchlist / RSS / API / bot / browser clipper / watch folder
- **acquisition_mode**：
- **parser_agent**：
- **evaluator_oracle**：
- **human_review_rule**：
- **knowledge_landing**：
- **refresh_monitor**：
- **anti_overreach_rules**：

## Triage

| 字段 | 值 |
| --- | --- |
| object_type | concept / paper / repo / product / industry / community / poc / policy / unknown |
| decision_goal | learn / observe / select / poc / adopt / productize / govern / hold |
| depth_level | quick scan / decision brief / deep research / PoC plan / source audit intake |
| Path ROOT / repo root |  |
| optional_lens | Three Horizons / War Game / Wild Cards / Van Westendorp / OECD-DAC / not-applicable |
| 深度等级 | quick scan / decision brief / deep research / PoC plan / source audit intake |
| evidence_level | L1 / L2 / L3 / L4 / L5 / L6 |
| priority | A-immediate / B-this-week / C-watch / D-skip |
| route | technology-research / open-source / industry-ai / issue-analysis / knowledge-linking / hold |
| state | queued / parsed / routed / landed / skipped / blocked |
| landing_plan | raw / article / concept / skill / template / project / no-op |
| 行动 owner |  |
| 检查方式 |  |
| 完成口径 |  |

## Frontier Tech Intake

- **Frontier Tech Intake source**：paper / GitHub / Hugging Face / official blog / product release / community thread / benchmark / policy update
- **evidence level**：L1 / L2 / L3 / L4 / L5 / L6
- **refresh trigger / update mechanism**：

## Decision Asset Gate

- **So-What**：这条来源对选型、采购、PoC、治理、继续观察或放弃意味着什么。
- **counter-evidence / 反证**：否定信号、失败案例、替代解释、不可复现证据、社区争议或过期风险。
- **deal-breaker**：足以否决、延后、转人工确认或停止投入的条件。
- **decision_output**：直接使用 / 封装使用 / Fork / 只参考 / 放弃 / 继续观察。
- **staleness / update trigger**：release、CVE、license、pricing、API、benchmark、法规、公司状态、PoC 或社区信号触发复查。

## Claims With Sources

| claim | evidence_level | source_artifact | status |
| --- | --- | --- | --- |
|  |  |  | confirmed / observed / reported / inferred / blocked |

## A3 Compensation

- **actual_automation_level**：A0 / A1 / A2 / True A3 / Compensated A3
- **A3_gap**：
- **human_micro_action**：
- **compensation_bundle**：
- **regained_intelligence**：
- **stop_boundary**：

## Writeback

- **raw**：
- **article**：
- **concept**：
- **skill / template**：
- **project**：
- **log**：
- **refresh_trigger**：
- **human_confirmation**：
- **loop_readiness**：

## 禁止项

- 不把社区热度、转发、点赞、Star 或二级文章直接写成事实。
- 不把没有原文保真的聊天摘要当作可复查证据。
- 不把单条帖子总结上推成完整专题研究。
- 不绕过平台权限、版权、登录、付费或隐私边界。
- 不让 intake item 自动替代采购、生产接入、项目状态关闭、规则升级或人工拍板。

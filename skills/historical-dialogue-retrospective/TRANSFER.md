---
type: skill-transfer-manifest
skill: historical-dialogue-retrospective
status: active
updated: 2026-06-12
tags: [skill, transfer, retrospective]
---

# Historical Dialogue Retrospective Transfer Manifest

## 能力目标

把历史对话、当前对话、Harness episode、log、git diff / commit、检查输出和受影响页面中的 agent 工作过程，复盘成可改进、可沉淀、可验证的工作流经验。

## 源资料路径

- `skills/historical-dialogue-retrospective/SKILL.md`
- `skills/README.md`
- `concepts/agent-work-retrospective.md`
- `concepts/project-retrospective.md`
- `projects/retrospectives/README.md`
- `templates/project-retrospective-template.md`
- `governance/harness-evolution.md`
- `governance/harness-feedback-ledger.md`
- `scripts/check_retrospective_system.py`
- `scripts/check_skill_maturity.py`

## 可以吸收

- 触发场景：历史对话复盘、agent 工作偏差、效率质量、沉淀路由和 workflow 改进。
- 响应模式：快速诊断、知识沉淀、规则升级 / Harness 自演进、验收关闭分开处理。
- 证据源分层：当前上下文、log、ledger、原始 session / rollout、git diff / commit、受影响页面、检查输出、memory、最终回复 / handoff。
- 复盘对象框定：时间范围、工作对象、复盘目标、不做范围。
- 工作链还原：用户目标、模式判断、事实源读取、文件变更、工具调用、验证、最终回复和后续纠偏。
- 偏差分类：目标、路由、读取、执行、验证、沟通、沉淀和收尾。
- 改进路由：log、复盘档案、concept、skill、template、ledger、sensor、WORKFLOW、AGENTS、POLICY 或项目 memory。

## 只能抽象吸收

- 本库的复盘档案层、Harness ledger、sensor 和治理页命名方式。
- 本库的软件研发事项体系和具体文档结构。
- 本库的 log 写法、wikilink 和提交闭环。

## 禁止复制

- 不复制本库历史 log 条目、具体 episode、项目状态、提交历史或一次性复盘结论。
- 不把单次 agent 偏差直接升级成目标工程硬规则。
- 不把复盘行动项留在复盘正文形成平行看板。
- 不把 Agent 工作复盘替代项目结果复盘、Issue 事实档案、事故档案、测试报告或验收关闭。

## 目标工程结构自检

- 如果目标工程已有 retrospective / postmortem / incident / lessons-learned / governance 入口，优先复用并补职责边界。
- 如果目标工程没有复盘档案层，优先建立轻量入口和模板；不要一次铺满不使用的目录。
- 如果目标工程没有 Harness ledger，重复失守可以先进入现有 issue / governance backlog；不要强行复制本库表格。
- 如果目标工程没有 `skills/` 体系，先把流程写入 AGENTS 或治理文档；等高频使用后再拆成 skill。

## 验证要求

- 用一个近期对话或 commit 区间验证是否能分清当前上下文、log、git diff、检查输出和最终回复。
- 用一个偏差样本验证是否能给出 `confirmed / likely / possible / blocked`，并说明未验证边界。
- 用一个改进项验证是否能路由到既有 owner 页面，而不是停在复盘正文。
- 跑目标工程已有检查；如果接入复盘 skill 或模板，补对应入口检查或人工检查清单。
- 最终回复必须说明落位、使用的证据、检查结果、未验证边界和没有复制的项目事实。

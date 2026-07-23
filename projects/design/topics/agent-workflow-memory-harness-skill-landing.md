---
type: design-topic
id: DES-TOPIC-AGENT-SYSTEM-LANDING-001
project: PROJ-WIKI-001
status: accepted-design
stage: system-landing
updated: 2026-07-23
tags: [design, agent, workflow, memory, harness, skill, topic]
---

# Agent / Workflow / Memory / Harness / Skill 落地矩阵

上游：[[projects/design/topics/implementation-engineering-template-system]]、[[agent-system-maturity]]、[[acknowledgebase-topic-system-adoption.v1]]

相关：[[response-mode-routing]]、[[agent-orchestration]]、[[projects/memory/README]]、[[skills/README]]、[[harness-evolution]]、[[harness-feedback-ledger]]

## 定位

本页把已在 AcknowledgeBase topic 中覆盖的通用方案，落实成 wiki 本地系统矩阵。它回答：一个方案进入 wiki 后，究竟落在 agent、workflow、memory、harness、skill、template、sensor、topic owner 中哪一层，而不是停留在“已参考 AcknowledgeBase”。

本页是摘要矩阵；逐 topic 的 source_topic、capability extraction、wiki system layers、wiki owner landing、agent-system action 和 validation 以 [[acknowledgebase-topic-system-adoption.v1]] 为准。只写本页的 topic family 摘要，不能等同于所有 source topic 已经落实。

## 系统矩阵

| 层 | 必备能力 | wiki owner | 关闭证据 |
| --- | --- | --- | --- |
| agent | 每轮先读入口、判模式、守写入边界、最终回复证明 | [[AGENTS]]、[[.codex/AGENTS]]、[[response-mode-routing]] | 入口链接 + project-docs / harness-governance sensor |
| workflow | 快诊断、设计、沉淀、验收、规则升级、子工程回传、批处理、收尾 | [[WORKFLOW]]、[[response-mode-routing]] | mode routing terms + check_harness_governance |
| memory | BRAIN / project memory / trace / log / ledger / report 分层 | [[BRAIN]]、[[projects/memory/README]]、[[projects/trace]]、[[log]] | owner-first 入口 + 不把 memory 当 live readback |
| harness | Goal、Loop、Run Capsule、Subproject Git Preflight、Evaluator、Persistence Decision | [[agent-orchestration]]、[[skills/goal-contract/SKILL]]、[[skills/loop-engineering/SKILL]] | loop / run templates + harness-governance / loop-engineering |
| skill | 通用技能、项目绑定技能、TRANSFER、template、sensor、evidence boundary | [[skills/README]] | skill-maturity + transferable-skill-baseline |
| evaluation | 本地专项 sensor、完整 gate、外部 readback blocked boundary | `scripts/check_all.py`、[[agent-system-maturity]] | 本地 green + 不上推到外部矩阵 |
| topic | 设计专题只承接本地 owner 和吸收矩阵，不复制源工程事实 | [[projects/design/topics/README]]、本页 | implementation-template-system sensor |
| migration | target self-check、source-depth、project conformance、Goodhart guard | [[skills/transferable-skill-governance/SKILL]]、[[templates/skill-transfer-manifest-template]] | true-gap / recognition-gap / signal-only-gap 裁决 |

## Topic 吸收裁决

| Source topic family | 决策 | 落地动作 |
| --- | --- | --- |
| agent harness baseline | complete | 保留七层 agent-system owner，并把实现类工程 profile 接入 sensor。 |
| memory / workflow freshness | upgrade | 在 profile 中要求 memory owner、trace、log、runtime readback 分开。 |
| goal orchestration governance | complete | 由 [[agent-orchestration]]、Run Capsule 和 Loop Contract 承接，不另建平行流程。 |
| process knowledge persistence | adapt | 作为 Persistence Decision 字段进入 Goal / Run / Loop 收尾，不默认新建 runs 目录。 |
| cross-repository governance acceptance | complete | 由 Subproject Git Preflight、handoff、controller evaluator 和不上推边界承接。 |
| research operating system | complete | 由 research-capability 聚合技能、technology-research 分支、research intake 和 evidence matrix 承接。 |
| topic placement and topic file governance | adapt | 当前先以少量 design-topic owner + sensor 接线承接，不提前做大规模目录迁移。 |
| dialogue persistence / work-state capture | partial | 先落实 Persistence Decision、log / memory / ledger 分层；真实行为样本和自动 evaluator 仍保留 `insufficient-evidence`。 |

## 逐 Topic Manifest

完整覆盖清单见 [[acknowledgebase-topic-system-adoption.v1]]。该 manifest 将 AcknowledgeBase `projects/design/topics/` 下每个 source topic 映射到 wiki 的 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 和 migration owner，并由 `acknowledge-topic-adoption` sensor 检查。

## 不上推边界

- `sensor passed` 只能证明结构接线，不证明每个 agent 行为已经最智能。
- `topic adopted` 只表示抽象方案已经有本地 owner，不表示源工程全部事实已迁移。
- `implementation profile complete` 只证明目标工程接入合同齐全，不替代 runtime smoke、E2E 或人工确认。
- `memory owner exists` 不能替代当前事实 readback。

## 验证

- `python3 scripts/check_all.py --only implementation-template-system`
- `python3 scripts/check_all.py --only acknowledge-topic-adoption`
- `python3 scripts/check_all.py --only agent-system-maturity,skill-maturity,harness-governance`

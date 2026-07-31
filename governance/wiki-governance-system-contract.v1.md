---
type: governance
id: GOV-WIKI-GOVERNANCE-SYSTEM-CONTRACT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-23
tags: [governance, agent, workflow, memory, harness, skill, evaluation, sensor]
---

# Wiki Governance System Contract

主入口：[[governance/README]]

相关：[[agent-system-maturity]]、[[acknowledgebase-topic-system-adoption.v1]]、[[agent-orchestration]]、[[harness-evolution]]、[[projects/memory/README]]、[[skills/README]]、[[templates/governance-system-upgrade-contract-template]]

## 定位

本页是 wiki 治理体系全面整改的运行合同。它回答“整改完了吗”的判断标准：不是新增一篇说明、复制一组 topic、或让某个 sensor 绿，而是让能力进入 agent、workflow、memory、harness、skill、evaluation、governance、template、topic、migration 的本地 owner，并改变后续 agent 的读取、判断、执行、回写、验证和收尾行为。

## 完成定义

一次治理体系整改只有同时满足以下条件，才能写 `complete`：

1. `ability source` 已明确：上游 topic、下游经验、用户纠偏、矩阵信号或本库设计稿分别是什么。
2. `system layer` 已明确：每个能力落到 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 或 migration 的哪一层。
3. `owner landing` 已完成：能力进入本仓对应 owner 页面、技能、模板、memory、ledger 或 sensor，而不是只进入一张汇总表。
4. `agent behavior` 已改变：后续 agent 知道何时触发、读什么、写哪里、怎么验证、哪些证据不能上推。
5. `sensor / evaluator` 已接入：可机器检查的结构必须进 `scripts/check_all.py --only <key>`；不可机器检查的行为必须写 evaluator 或人工确认边界。
6. `closeout proof` 已收口：最终回复、log 和提交说明必须写清结构通过、行为未验证、runtime / external readback / manual review 的边界。

只满足其中一项时，状态只能是 `partial / review / blocked`。

## 层级合同

| layer | 必须落下的能力 | owner / landing | 不算完成的情况 |
| --- | --- | --- | --- |
| agent | 启动读取、响应模式、写入边界、最终回复证明 | [[.codex/AGENTS]]、[[AGENTS]]、[[response-mode-routing]] | 只在 topic manifest 写“agent”但入口不触发。 |
| workflow | 从 intake 到 owner discovery、能力抽象、落点、验证、提交的执行顺序 | [[WORKFLOW]]、[[response-mode-routing]] | 只有文档列表，没有执行步骤。 |
| memory | 稳定事实、项目记忆、trace、log、ledger、负空间证据分层 | [[projects/memory/README]]、[[projects/memory/shared]]、[[BRAIN]]、[[log]] | 把 memory 当 live readback，或只留在最终回复。 |
| harness | Goal、Run Capsule、Worker / Evaluator、Loop、Persistence Decision、Subproject Git Preflight | [[agent-orchestration]]、[[harness-evolution]]、[[harness-feedback-ledger]] | Worker 自评、sensor 绿灯或 health 被上推为闭环。 |
| skill | 可复用触发、事实源、流程、输出、回写守卫、TRANSFER 边界 | [[skills/README]]、各 `skills/*/SKILL.md` | 为了覆盖率新增空 skill，或复制项目事实。 |
| evaluation | 专项 sensor、negative evidence、Goodhart guard、external readback、manual reviewer | `scripts/check_all.py`、[[agent-system-maturity]] | 本地结构检查通过就宣称行为智能达标。 |
| governance | P0 / P1 / P2 / P3、规则晋升、降级、episode、指令遵循 | [[agent-governance-strategy]]、[[instruction-adherence]]、[[harness-evolution]] | 单次纠偏直接写硬规则，或规则只停在自然语言。 |
| template | 可复制字段、验收合同、回传包、治理升级合同 | [[templates/README]]、[[templates/governance-system-upgrade-contract-template]] | 没有字段约束，后续只能靠人记。 |
| topic | source topic 到本地 owner 的 ability adoption | [[acknowledgebase-topic-system-adoption.v1]]、[[projects/design/topics/README]] | 只复制 topic 正文，或只写 topic family 摘要。 |
| migration | recognize / complete / upgrade / adapt / defer / reject、source-depth、project conformance | [[agent-system-cross-project-alignment.v1]]、[[skills/transferable-skill-governance/SKILL]] | 把源工程目录、分数、运行 ID、业务事实写成本仓事实。 |

## 实战控制面吸收要求

当下游工程把生产 readback、长任务编排、agent-finalizer、external-write-boundary、acceptance-governance、performance-bandwidth-analysis 或 runtime-config-switch 打磨到 agent 治理层时，wiki 不能只把它们记成 source signal。可迁移部分必须至少进入一个实际 owner：

- 控制面默认行为进入 [[agent-orchestration#Production-Grade Control Plane Hardening]]。
- 性能 / 带宽 / timing / capacity 方法进入 [[skills/performance-bandwidth-analysis/SKILL]]。
- runtime 配置切换进入 [[skills/runtime-config-switch/SKILL]]。
- 结构接线进入 `scripts/check_all.py --only agent-control-plane-hardening`。
- 下游强业务绑定能力，例如带业务表、账号、DSN、批次前缀或项目 schema 的 DB readback，不新增通用 skill，只抽象“receipt、ingress、DB / service-side readback 不能互替”的证据分层。

## 注册表全工程吸收要求

当用户要求“举一反三”“所有工程都吸收一下”或等价目标时，本仓不能用单一强工程、旧矩阵摘要、某个能力覆盖集或本机 `find` 扫描结果替代内部 source registry。默认完成口径是 registry-driven，但 wiki 对外模板面必须 source-deidentified：

1. 先读取内部 source registry 或等价登记面，确认注册表全集；能力覆盖集、优先级列表和额外本地路径只能作为补充证据。
2. 对注册表每一行完成内部审计，但进入 wiki 正文时写成 source archetype、project profile、capability pack、`decision` 和 `wiki landing / guard`；轻量仓也要说明最小治理 profile 或无可吸收增量。
3. 对已上升到 agent 治理层级的能力，不能只写 `candidate`；必须进入 owner、skill、template、sensor、harness 或 evaluation contract。
4. 对项目事实、业务链路、服务实例、数据库、运行 ID、账号、端口、数据集、模型、机器和一次性 handoff，必须写明不复制边界。
5. 本地存在 AcknowledgeBase 且本轮改变 agent / workflow / memory / harness / skill / evaluator / sensor / template 默认行为时，对应 topic 必须 `updated` 才能报 complete。
6. 具体 source project 名称只允许留在对应私有 registry 或私有审计证据；不得进入本公开仓库的正文、历史 log、报告、trace、decision、ledger、view source pack、脚本常量、示例、工程类型、能力名称或默认 profile 名。

## 公开仓库持久化边界

本仓以“公开可见”为默认状态。公开不要求达到开源工程配套水平，但要求每个 tracked 文件都满足 public-safe persistence：

1. 公司 / 内部工程的名称、路径、registry 明细、业务事实、服务拓扑、机器、账号、端口、运行 ID、内部 URL、一次性 handoff 和未公开个人信息不得写入本仓。
2. 跨工程读取可以发生，但落盘内容必须先去标识，只保留 source archetype、project profile、capability pack、抽象规则、验证方法和不上推边界。
3. `log.md`、报告、trace、decision、ledger 和 view source pack 都不是例外；“真实用户意图”必须改写为公开安全的结果导向摘要，不能保存含内部身份的原文。
4. `raw/` 可以保留经用户确认可公开的外部网页抓取、JS / CSS 和图片；公司 / 私有材料、凭据、会话能力和未授权个人信息仍不得借 `raw/` 绕过边界。
5. 机器 sensor 负责拦截可识别的绝对路径、内部地址和本地 deny terms；语义上是否仍能识别具体内部工程，必须在写入和提交前人工复核。
6. 没有可写的私有 owner 时，内部证据的 Persistence Decision 只能是 `blocked` 或 `no-op`；不得为了满足本仓的沉淀、log 或收尾要求而降级写入公开仓库。

专项检查：`python3 scripts/check_all.py --only public-repository-content`。

## 执行包

治理体系全面整改按这个顺序执行：

1. `intake`：复述用户目标和最新纠偏，判定是不是全面治理整改，不用旧目标偷换完成口径。
2. `source coverage`：列出上游 topic、现有 owner、缺口和不能复制的内容。
3. `ability extraction`：把文档内容转成触发条件、事实源分层、执行合同、回写守卫、验证和不上推边界。
4. `owner landing`：逐层写入 agent、workflow、memory、harness、skill、evaluation、governance、template、topic、migration。
5. `sensor landing`：新增或升级专项 sensor，检查 entrypoint、owner、template、ledger、memory 和不复制边界。
6. `episode landing`：如果整改来自用户纠偏或重复失守，写入 [[harness-feedback-ledger]]，再决定是否晋升规则或模板。
7. `closeout`：跑专项和完整门禁，提交同主题 diff；最终回复说明是否只是结构整改，还是已有行为 / runtime / external evaluator 证据。

## 不完成条件

以下任一情况出现时，不得回答“整改完了”：

- 只新增 manifest、摘要矩阵、索引或入口链接。
- 只跑 sensor，但没有写入实际 owner、技能、模板、memory 或 harness。
- 只复制 AcknowledgeBase 文档，没有抽象成 wiki 本地能力。
- 只更新技能页，没有回到 workflow、harness、evaluation 或 closeout proof。
- 缺少 log / ledger / memory 中应有的持久化路由。
- 缺少 `structure-only`、`insufficient-evidence`、runtime readback、external evaluator 或人工确认边界。

## 验证

- `python3 scripts/check_all.py --only governance-system-rectification`
- `python3 scripts/check_all.py --only acknowledge-topic-adoption,agent-system-maturity,implementation-template-system,harness-governance,skill-maturity,harness-feedback-ledger`
- `python3 scripts/check_all.py`

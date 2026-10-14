---
type: design-topic
id: DES-TOPIC-AGENT-SYSTEM-LANDING-001
project: PROJ-WIKI-001
status: accepted-design
stage: system-landing
updated: 2026-10-14
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
| research operating system | strong-template-kernel | 由 research-capability 聚合技能、technology-research 分支、R2+ source plan、coverage / Evidence Delta 模板、验证阶梯、修订循环和结构化正负 fixture evaluator 承接；上游设计与领域知识不复制。 |
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

## 模板继承的当前执行基线

本轮目标是让后续工程从模板创建时直接获得统一流程，同时保留知识深度、融合问候、事项父级归属、复盘 / 研究能力、公开安全和证据分层。采用上游既有设计，当前范围为入口、技能发现、Goal / Loop 触发、阶段合同、检查器及收尾。未授权业务模型迁移、生产操作或仓库外配置修改。

| 要求 / 保留特色 | 原位置与差异 | 当前承接 | 验证 |
| --- | --- | --- | --- |
| 单一规则正文、冷启动与领域深度 | 根入口过厚，平台 adapter 重复正文 | 根 [[AGENTS]] 保留 guard 与原融合问候；四个条件页保留原知识、治理、执行、呈现细则；adapter 只导入根入口 | agent-guidance 与 harness-governance；专业检查跟随链接，根 guard 独立检测 |
| 原生技能发现 | 只有 skills 正文，无项目发现投影 | `.agents/skills/` 使用仓库内相对链接 | 原路径和隔离目录均验证链接；运行发现单独记录 |
| 持续推进不过度编排 | Goal / Loop / Run Capsule 用时长和复杂程度触发 | [[skills/goal-contract/SKILL]]、[[skills/loop-engineering/SKILL]] 和 [[agent-orchestration]] 各自唯一条件；路由 / workflow / 模板同步 | 边界回归；不能上推到所有模型行为 |
| 最小登记与高风险证据 | TASK / Issue 模板一次要求完整字段 | staged-v1，保留 wiki 的 parent_ep 与本地编号；按执行影响和阶段补齐 | 原始症状、重复字段、失败证据、跨仓、生产、服务边界回归；模板实例化验证 |
| 提交与公开安全 | 既有规则保留，增加最终状态读回 | 执行条件页、public-repository-content 与 scoped commit | 文件清单、完整门禁、commit / staged / dirty 读回 |

此基线直接替换活跃入口与创建模板，不保留旧触发路径。现有历史报告仍是历史证据；模板仓当前无 TASK / Issue 实例，任何新实例都必须声明阶段合同，缺 profile 不允许绕过检查。源技能按模块原生适配，不整库复制；模板维护机器、私有工程事实和运行身份不成为衍生项目默认值。

模板接入方式为复制或 clone 仓库后按 [[templates/implementation-project-profile-template|接入配置]] 校准身份、能力包与边界，没有另一个模板生成器。复制时必须包含 `.agents/`、`.codex/`、根 AGENTS 和相对链接指向的 `skills/`；丢失隐藏目录或链接应由检查失败暴露。采纳证据、未测范围与回退见 [[projects/development/reports/2026-10-13-template-agent-remediation|整改记录]]。


## 高能力模型完整适配

目标基线来自能力、真实任务、用户要求与风险；历史目录和冗长提示不限制目标设计。GPT-6 Astra 是本轮行为验证目标，模型能力和可用名称以实际运行环境确认；模板不强制模型切换，更不授权业务模型迁移。官方依据为 [Skills 与提示词审查](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) 和 [模型使用指南](https://developers.openai.com/api/docs/guides/latest-model)。

本轮接续入口整改，覆盖全部 18 个技能、关联 TRANSFER、Goal / Loop / Run Capsule 长模板与原有消费者。只保留一套活动流程：迁移在授权内直接实施；普通问因先最小诊断；持续执行复用事项；普通 HTML 按内容和阅读需求验证；深度研究、复盘、跨仓协作和正式导出在命中条件时加载专业部分。专业知识不会因不常驻而删除。

- **能力保留**：研究 R0–R4 / L1–L6、R2+ 来源覆盖与反证、深度复盘原始证据和用户纠偏、性能分母与分层耗时、配置默认路径与非默认值验证、发布隔离与 live / denial readback、原事项父级和公开模板边界。
- **按需加载**：入口明确触发和最小完成合同；`conditional_sources` 只声明有链接且受条件约束的专业参考。离线 sensor 按显式依赖验证完整能力，运行时不把所有参考注入上下文。断链、越界、重复和循环依赖必须失败。
- **验收分层**：静态结构检查、隔离模板加载、真实模型任务、项目运行 / 服务验收各自记录；不得从字数、marker 或模型自述推导整体成功。当前模型测例只支持已测场景，不证明所有任务或未来模型。
- **维护方式**：使用 `scripts/run_model_adaptation.py` 显式运行隔离真实模型探针，固定模型、推理强度、输入快照、原始事件和外部 oracle；默认完整检查不调用付费模型、不访问生产。测试产物落在仓库外数据目录，公共仓库只保留去标识方法与结论。

逐技能处理、实测结果及回退见 [[projects/development/reports/2026-10-14-full-model-adaptation]]。旧报告只保留当时范围的证据，不作为本轮完成凭证。

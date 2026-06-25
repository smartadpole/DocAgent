---
type: index
id: INDEX-ROOT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-05-25
tags: [index, root]
---

# 知识库入口

这是一套给 Obsidian + Codex 用的文档系统，内部链接默认依赖 Obsidian 的 `[[wikilink]]` 解析。

如果你不知道先看什么，按这个顺序：

1. 先看 [[README]]，知道这个 vault 是干什么的、怎么启动、怎么选动作。
2. 再看 [[governance/README]]，先知道治理层怎么分。
3. 再看 [[BRAIN]]，知道哪些已确认背景会自动参与后续工作。
4. 再看 [[POLICY]]，知道规则、优先级和 memory 路由怎么定。
5. 要处理项目运行层，就看 [[projects/README]] 和 [[projects/memory/README]]。
6. 要处理文件和目录细节，就看 [[WORKFLOW]]。
7. 要知道 agent 的维护边界，就看 [[AGENTS]]。
8. 要找入口分类和主题化后的运行记录，就留在这页。

这页只做总导航，不承载细节。

## 入口

- [[README]]：vault 总说明和启动入口
- [[governance/README]]：治理层入口
- [[BRAIN]]：共享背景
- [[POLICY]]：规则、优先级和 memory 路由
- [[response-mode-routing]]：响应模式路由，决定 agent 每轮先快速诊断、沉淀、验收、实现还是升级规则
- [[proactive-dialogue-system]]：主动对话与引导式设计，决定目标未成形时如何自动判定场景、少量提问、带假设推进并产物化
- [[agent-governance-strategy]]：Agent 治理分级，决定规则、模板、sensor、log、Goal 或复盘应按 P0 / P1 / P2 / P3 落位
- [[state-constraint-reasoning]]：状态约束推理，决定权限、远程、dirty 状态、预算和证据层级是否允许执行动作
- [[agent-orchestration]]：Agent 编排入口，定义 Goal、Run Capsule、Orchestrator、Worker、Evaluator、Subproject Git Preflight 和沉淀路由
- [[instruction-adherence]]：指令遵循治理，决定已有规则如何进入触发矩阵、模板字段、sensor、门禁和最终证明
- [[execution-contract-semantics]]：执行合同语义，防止参考规则、非目标和证据说明漂移成隐形待办
- [[harness-evolution]]：Harness H5 自演进入口，决定 episode 如何晋升为 sensor、模板、技能或规则
- [[harness-feedback-ledger]]：Harness episode、sensor backlog、规则晋升和降级队列
- [[log-writing-rules]]：`[[log]]` 的记录规则入口
- [[skills/README]]：项目内可复用 agent 技能入口和技能成熟度模型
- [[skills/technology-research/SKILL]]：技术、开源工程、行业 / AI 赛道和 PoC 调研总控技能
- [[skills/research-capability/SKILL]]：调研 / 研究能力聚合入口，统一调研合同、证据等级、行动等级、风险门和沉淀落位
- [[skills/goal-contract/SKILL]]：长时任务完成契约技能，用于防目标漂移、证据漂移和无限探索
- [[skills/transferable-skill-governance/SKILL]]：可迁移技能治理技能，用于矩阵驱动升级时判定 true-gap / recognition-gap / signal-only-gap
- [[skills/knowledge-linking/SKILL]]：知识关联、落位、入口和回链技能
- [[skills/cross-project-skill-adoption-prompt/SKILL]]：跨工程技能迁移任务书生成技能
- [[skills/cross-project-governance-audit/SKILL]]：跨工程治理审计技能
- [[skills/problem-focused-visual-presentation/SKILL]]：问题聚焦式图文呈现技能
- [[skills/documentation-maintenance/SKILL]]：代码、结构或规则变化后的文档维护技能
- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析、定位、分工和联测验证技能
- [[skills/retrospective-capability/SKILL]]：复盘能力总技能，统一项目交付、软件研发链、历史对话、Agent 工作流、Harness episode 和治理自演进复盘合同
- [[skills/delivery-retrospective/SKILL]]：项目交付与软件研发链复盘子技能
- [[skills/historical-dialogue-retrospective/SKILL]]：历史对话与 Agent 工作流复盘子技能
- [[views/README]]：图文呈现层入口，承接 current / snapshot lens 和 registry
- [[projects/README]]：活跃软件研发项目的运行入口
- [[projects/memory/README]]：项目级稳定记忆入口
- [[projects/trace]]：需求演进链入口
- [[projects/service-registry]]：服务实例台账入口
- [[projects/meetings/README]]：项目正式会议入口
- [[projects/retrospectives/README]]：复盘档案入口，承接阶段、专题、交付链、Issue / 事故后和 Agent 协作复盘
- [[trace-writing-rules]]：`[[projects/trace]]` 的记录规则入口
- [[template-feedback-rules]]：下游项目系统层信息反哺入口

## 设计思路

- [[articles/2026-04-09-obsidian-doc-system-design]]：Obsidian 文档系统整体设计研究
- [[concepts/document-os]]：文档操作系统概念定义
- [[articles/2026-04-09-layered-memory-research]]：分层 memory 研究
- [[concepts/layered-memory]]：分层 memory 概念定义
- [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]：agent 响应效率治理反思，记录快速诊断和治理闭环分层的来源分析
- [[response-mode-routing]]：已生效的响应效率治理入口，承接快速诊断、知识沉淀、Issue 分析、验收关闭和规则升级的模式路由
- [[proactive-dialogue-system]]：主动对话和引导式设计系统，承接场景包、置信度、无感交流等级、性能预算和每轮产物化落地判定

## 产品写作

- [[concepts/prd-writing]]：PRD 写作方法
- [[articles/2026-04-13-prd-writing-guide]]：PRD 写作指南摘要卡片

## 研发方法

- [[WORKFLOW#1.9.0 新应用探索模式]]：全新桌面端、web 或 app 从多方向探索到当前项目推进的轻量路径
- [[response-mode-routing]]：agent 工作先快后重的统一路由，避免简单诊断默认进入完整治理闭环。
- [[agent-governance-strategy]]：Agent Governance Strategy，用 P0 / P1 / P2 / P3 防止规则和检查过重。
- [[state-constraint-reasoning]]：State Constraint Reasoning，把权限、远程状态、预算和证据边界传播到可执行动作。
- [[agent-orchestration]]：Agent Orchestration，用 Run Capsule 管主控 / Worker / Evaluator 和子工程 Git preflight。
- [[skills/technology-research/SKILL]]：技术调研总控，先固定调研合同、证据等级、成熟度、风险门和沉淀落位。
- [[skills/research-capability/SKILL]]：research-capability 聚合入口，避免把外部研究子项原样平铺进本库。
- [[skills/cross-project-skill-adoption-prompt/SKILL]]：把已沉淀技能生成目标工程可执行迁移任务书。
- [[skills/transferable-skill-governance/SKILL]]：判断外部通用技能吸收时应 recognize、complete、upgrade、merge、adapt、defer 还是 reject。
- [[skills/goal-contract/SKILL]]：复杂长时任务的完成契约，连接目标、证据层级、停止条件和记录落点。
- [[skills/problem-focused-visual-presentation/SKILL]]：把复杂主题、状态、风险或证据链转成问题聚焦图文 lens。
- [[skills/documentation-maintenance/SKILL]]：代码、结构、规则或公开行为变化后检查并同步文档。
- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析技能，用于模糊问题、故障、联调失败、验收争议和跨工程阻塞的定位、分工与联测收口。
- [[concepts/codex-goals]]：Codex 长时任务的线程级完成契约，适合终点明确但路径依赖中间证据的持续工作。
- [[articles/2026-05-25-codex-goals-research]]：Codex Goals 专题调研，整理 Goal 的完成契约、生命周期、强弱写法和研究型任务用法。
- [[concepts/harness-engineering]]：AI Agent 的工程化运行环境方法，关注上下文、工具、规则、工作流、验证和演化闭环。
- [[articles/2026-05-25-harness-engineering-research]]：Harness Engineering 深度调研，汇总本地材料、OpenAI、Martin Fowler、LangChain、Vercel 和近期论文案例。
- [[harness-evolution]]：把用户纠偏、检查失败、模式切换和重复失守转成可复盘 episode。
- [[concepts/project-retrospective]]：项目复盘方法入口，说明复盘和 log、Issue、事故、决策、memory、trace 的分工。
- [[concepts/software-development-project-retrospective]]：软件研发项目复盘维度，覆盖需求、设计、事项、实现、测试、发布、运行和协作治理。
- [[concepts/agent-work-retrospective]]：Agent 工作复盘维度，覆盖目标理解、阶段判断、上下文读取、工具使用、验证、沟通、边界和收尾质量。
- [[skills/retrospective-capability/SKILL]]：复盘总技能，先固定复盘对象、深度等级、证据计划、子项路由和行动兑现回检。
- [[concepts/software-testing-acceptance-release]]：软件测试、验收和上线的通用概念，强调环境是证据面而不是荣誉阶梯。
- [[concepts/progressive-design-freeze]]：阶段门滚动冻结
- [[projects/development/plan/README]]：研发执行总控
- [[projects/development/plan/work-item-system-model]]：`Gate -> FP -> EP -> TASK` 事项系统模型
- [[projects/development/plan/test-acceptance-planning-model]]：测试计划与验收合同模型
- [[projects/development/acceptance/README]]：验收计划入口
- [[projects/development/acceptance/plans/README]]：AP 验收计划索引
- [[projects/development/plan/task-design-model]]：TASK 状态化交付合同模型
- [[projects/development/execution/README]]：研发执行层入口
- [[projects/development/execution/execution-packages/README]]：EP 执行包入口
- [[projects/development/execution/tasks/README]]：TASK 任务入口
- [[projects/development/issues/README]]：Issue 案件入口
- [[projects/development/reports/README]]：测试、复验和准出报告入口

## 模板治理

- [[templates/README]]：可复制模板入口
- [[templates/development-work-item-matrix-template]]：Gate / FP / EP / TASK 事项矩阵模板
- [[templates/development-execution-package-template]]：EP 执行包模板
- [[templates/development-task-template]]：TASK 任务模板
- [[templates/development-issue-template]]：Issue 案件模板
- [[templates/development-acceptance-plan-template]]：AP 验收计划模板
- [[templates/project-retrospective-template]]：项目、阶段、交付链、Issue / 事故后和 Agent 工作复盘的通用核心模板，包含证据地图、上轮行动兑现回检、行动分流、治理自演进和未验证边界
- [[templates/goal-contract-template]]：长时任务完成契约模板，用于定义期望最终状态、完成判定、验证面 / 证据边界、约束、预算和阻塞停止条件。
- [[templates/problem-focused-lens-template]]：问题聚焦式图文 lens 模板，用于 current / snapshot / print view 的 source pack、证据边界和导出字段
- [[templates/problem-focused-lens-source-pack-contract]] / [[templates/problem-focused-lens-review-contract]]：问题聚焦 lens 的 source pack 和审核合同
- [[templates/public-html-publication-template]]：HTML 公开发布 profile 模板，用于声明 source root、public_url、HTML-only、multi-host / multi-project 和 blocked 口径
- [[templates/technology-research-contract-template]] / [[templates/technology-research-report-template]]：调研合同和正式研究报告骨架
- [[templates/technology-research-evidence-matrix-template]] / [[templates/technology-research-adoption-contract-template]]：研究证据矩阵和采用合同
- [[templates/skill-transfer-contract-template]] / [[templates/skill-transfer-evidence-contract]] / [[templates/skill-transfer-review-contract]]：跨工程技能迁移任务书、证据和审核合同
- [[templates/guided-discovery-session-template]]：引导式设计会话模板，用于承接对话所得、agent 思考结果、场景包、性能预算和产物化闭环。
- [[templates/harness-adoption-template]]：新系统或子工程接入 Agent Harness 时的单一信息源、写权限、验证层级和回传模板
- [[templates/harness-episode-package-template]]：单次 Harness episode 的 checkpoint、执行轨迹、证据边界和反馈模板
- [[templates/harness-evolution-review-template]]：周期性复盘 episode、sensor backlog、晋升和降级决策的模板
- [[template-feedback-rules]]：其他项目进化出的系统层信息如何反哺模板库

## 项目接手与代码基线

- [[projects/codebase/README]]：现实代码、旧工程或外部模板的审计入口
- [[projects/codebase/source-code-audit-workflow]]：源码工程深度解读工作流

## 软件架构包

- [[projects/design/README]]：软件架构总入口和推荐阅读顺序
- [[projects/design/topics/README]]：重要设计专题入口，承接未拍板专题和专项储备
- [[projects/design/diagrams/README]]：设计图资产入口，承接 Excalidraw 源文件、Diagrams.Net 正式图和 SVG / PNG 预览图
- [[projects/design/tech-selection]]：技术选型
- [[projects/design/architecture]]：业务架构、页面动作和状态机
- [[projects/design/backend-frontend-structure]]：前后端工程结构、接口约定和代码落点
- [[projects/design/permission-boundary]]：权限真相源、角色可见性和业务授权边界
- [[projects/design/write-boundary]]：写操作分级和服务端收口边界
- [[projects/design/database]]：数据模型、约束、索引和迁移策略
- [[projects/design/deployment]]：环境、部署、发布和回滚
- [[projects/design/runtime-quality]]：监控、告警、幂等、重试和补偿

## 层级

- 入口层：[[README]]、[[INDEX]]
- 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[response-mode-routing]]、[[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[POLICY]]、[[BRAIN]]
- 技能层：[[skills/README]] 和 `skills/`
- 呈现层：[[views/README]] 和 `views/`
- 运行层：`projects/`，其中复盘档案入口是 [[projects/retrospectives/README]]
- 沉淀层：`articles/`、`concepts/`、`indexes/`
- 历史层：[[log]]、`archive/`
- 证据层：`raw/`、`inbox/`、`assets/`

## 物理结构

- 根目录保留高频入口：[[README]]、[[INDEX]]、[[AGENTS]]、[[log]]
- `governance/` 收治理页和规则页
- `skills/` 收项目内可复用 agent 技能
- `views/` 收问题聚焦式图文 lens、current / snapshot 和 registry；导出缓存不作为事实源
- `projects/` 收运行层
- `articles/`、`concepts/`、`indexes/` 收知识沉淀
- `archive/` 收退役历史，`raw/`、`inbox/`、`assets/` 收证据

## 运行记录

- [[log]]：按时间降序记录每次对话的主题、用户意图、关键动作和结构调整
- [[log-writing-rules]]：`[[log]]` 的记录单位、主题合并规则和跨日期边界

## 更新原则

- 工具名和概念名尽量用 `[[双向链接]]`
- 新内容先写成摘要卡片，再汇总到概念页和索引页
- 长期不变的规则和偏好分别写进 [[BRAIN]]、[[POLICY]] 和 `workspace-memory`

## Loop Engineering 接入

- [[skills/loop-engineering/SKILL]]：持续 agent 循环控制技能，用于判断何时从一次性 Goal / Run Capsule 升级为可验证、可停、可持久化的 loop。
- [[templates/loop-contract-template]]：Loop Contract 控制面，记录 discovery source、run queue、evaluator、persistent state、budget / stop 和 next-run decision。
- [[templates/run-capsule-template]]：单轮运行胶囊，承接 Parent Loop Contract、Input discovery item、Worker limits、State transition 和 Next-run recommendation。
- 专项检查：`python3 scripts/check_all.py --only loop-engineering`。

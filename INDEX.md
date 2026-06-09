---
type: index
id: INDEX-ROOT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-05
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
- [[agent-governance-strategy]]：Agent 治理策略，区分 P0 硬约束、P1 语义门、P2 流程和 P3 backlog
- [[response-mode-routing]]：响应模式路由，决定 agent 每轮先快速诊断、沉淀、验收、实现还是升级规则
- [[proactive-dialogue-system]]：主动对话与引导式设计，决定目标未成形时如何自动判定场景、少量提问、带假设推进并产物化
- [[state-constraint-reasoning]]：状态与约束推演，决定新信息进入系统后如何识别受影响状态、做约束传播并先判可执行性
- [[instruction-adherence]]：指令遵循治理，决定已有规则如何进入触发矩阵、模板字段、sensor、门禁和最终证明
- [[execution-contract-semantics]]：执行合同语义，防止参考规则、非目标和证据说明漂移成隐形待办
- [[harness-evolution]]：Harness H5 自演进入口，决定 episode 如何晋升为 sensor、模板、技能或规则
- [[harness-feedback-ledger]]：Harness episode、sensor backlog、规则晋升和降级队列
- [[log-writing-rules]]：`[[log]]` 的记录规则入口
- [[knowledge-linking-rules]]：新增知识页、概念页和摘要卡片的网状关联规则入口
- [[skills/README]]：项目内可复用 agent 技能入口
- [[skills/problem-focused-visual-presentation/SKILL]]：问题聚焦式图文呈现技能，把文档、主题、状态、风险、决策、计划、验收或知识材料重组为带背景框、证据边界、同源一致性和 ignored PDF / PNG 导出配置的图文 lens
- [[skills/cross-project-skill-adoption-prompt/SKILL]]：跨工程技能升级提示词生成技能
- [[skills/knowledge-linking/SKILL]]：知识关联技能，把调研、沉淀、总结方案、补链和 `knowledge-linking` sensor 验证做成可复用流程
- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析、定位、分工和联测验证技能
- [[skills/historical-dialogue-retrospective/SKILL]]：历史对话与 Agent 工作流复盘技能
- [[projects/README]]：活跃软件研发项目的运行入口
- [[projects/memory/README]]：项目级稳定记忆入口
- [[projects/trace]]：需求演进链入口
- [[projects/service-registry]]：服务实例台账入口
- [[projects/meetings/README]]：项目正式会议入口
- [[projects/retrospectives/README]]：项目复盘档案入口
- [[trace-writing-rules]]：`[[projects/trace]]` 的记录规则入口
- [[template-feedback-rules]]：下游项目系统层信息反哺入口

## 设计思路

- [[articles/2026-04-09-obsidian-doc-system-design]]：Obsidian 文档系统整体设计研究
- [[concepts/document-os]]：文档操作系统概念定义
- [[concepts/ai-era-information-presentation]]：AI 时代信息记录、处理与呈现方式，区分 Markdown 真相源、向量检索索引、超链接关系网、语义 / 动态 HTML 和 PPT / PDF / WARC / MHTML 归档格式
- [[concepts/problem-focused-information-presentation]]：问题聚焦式信息呈现，按当前关注问题为所有信息类型选择图文混排 lens，用表格、脑图、框图、关系图、时间线、状态卡和同源 PDF / PNG 下载降低阅读与流转成本，同时避免重复渲染物入库。
- [[concepts/image-text-layout-system]]：图片与图文排版体系，说明图文 lens 内部如何按图片职能、空间骨架、视觉组织、图文绑定、媒介适配和生成治理来排版。
- [[articles/2026-06-08-image-text-layout-system-research]]：图片与图文排版体系调研，汇总设计史、设计系统、Web 标准、可访问性和 AI layout generation 的方法线索。
- [[articles/2026-06-05-ai-era-information-presentation-research]]：AI 时代信息记录、处理与呈现方式调研，梳理文件记录、chunk / vector 处理、Markdown 记录 + 处理、HTML 实时呈现和 HTML 记录边界
- [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]：跨 Life、DocCustomeranalysis、prefect、fetch-adapter 和 DocFilmCommunity 校准问题聚焦式图文 lens 的 current / snapshot、源刷新、背景框、用户入口、同源导出和重复渲染物边界
- [[articles/2026-04-09-layered-memory-research]]：分层 memory 研究
- [[concepts/layered-memory]]：分层 memory 概念定义
- [[articles/2026-05-28-openclaw-memory-system-research]]：OpenClaw 记忆系统调研，覆盖 workspace memory、active memory、dreaming、QMD 和 `memory-wiki`
- [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]：agent 响应效率治理反思，记录快速诊断和治理闭环分层的来源分析
- [[articles/2026-05-28-state-constraint-planning-research]]：系统状态模型、约束传播与计划可执行性调研，收口自动规划、时间约束网络、约束规划、MBSE 和系统思维的组合方法
- [[articles/2026-05-28-state-constraint-template-pack]]：状态与约束推演模板样式包，覆盖超简版、生活版和工程版三类专题成果
- [[response-mode-routing]]：已生效的响应效率治理入口，承接快速诊断、知识沉淀、Issue 分析、验收关闭和规则升级的模式路由
- [[proactive-dialogue-system]]：主动对话和引导式设计系统，承接场景包、置信度、无感交流等级、性能预算和每轮产物化落地判定
- [[state-constraint-reasoning]]：计划型问题的治理入口，承接状态变量、约束传播、未知变量和可执行性判断

## 产品写作

- [[concepts/prd-writing]]：PRD 写作方法
- [[articles/2026-04-13-prd-writing-guide]]：PRD 写作指南摘要卡片

## 企业与产品观察

- [[concepts/beijing-xinzhi-ruisheng]]：北京芯智睿声科技有限公司，AI + 柔性传感 + 可穿戴智能人工喉方向的早期辅助科技企业实体页。
- [[articles/2026-06-09-xinzhi-ruisheng-company-research]]：芯智睿声企业调研，梳理基本画像、产品路线、公开进展、机会判断和待核验边界。

## 研发方法

- [[WORKFLOW#1.9.0 新应用探索模式]]：全新桌面端、web 或 app 从多方向探索到当前项目推进的轻量路径
- [[response-mode-routing]]：agent 工作先快后重的统一路由，避免简单诊断默认进入完整治理闭环。
- [[concepts/state-constraint-planning]]：把计划问题表示成状态变量、约束关系、外部不确定和可执行性判断的方法概念。
- [[state-constraint-reasoning]]：把“先判可执行性，再写安排”落成治理页，适用于搬家、旅行、采购、部署、上线等计划型问题。
- [[concepts/project-retrospective]]：项目复盘专题，沉淀目标、过程、结果、偏差、原因和改进行动的通用框架。
- [[projects/retrospectives/README]]：具体复盘档案入口，承接当前项目的阶段、专题、事故后、Issue 后和 Agent 协作复盘。
- [[templates/project-retrospective-template]]：复盘档案模板，覆盖证据地图、交付链、Agent 工作、行动分流和治理自演进判断。
- [[concepts/software-development-project-retrospective]]：软件研发项目复盘子专题，把需求、设计、拆解、实现、测试验收、发布运行和协作治理串成一条交付链回看。
- [[concepts/agent-work-retrospective]]：Agent 工作复盘子专题，回看 agent 的目标理解、读取预算、工具使用、验证质量、沟通节奏和沉淀路由。
- [[concepts/agent-governance]]：Agent 治理专题，统筹规则、响应路由、技能、模板、sensor、复盘和 H5 自演进之间的知识库关系。
- [[concepts/agent-skills]]：Agent Skills 概念，把可重复工作封装成 agent 可发现、可加载、可执行和可审计的能力单元。
- [[articles/2026-06-09-scientific-agent-skills-research]]：Scientific Agent Skills 调研，分析 K-Dense 科研技能库如何把科研流程、数据库、工具链和方法规范打包成约 140+ 个 Agent Skill，并校准安全边界。
- [[articles/2026-06-04-knowledge-linking-mechanism-research]]：新增知识关联机制调研，说明为什么语义关联不能只依赖自动图谱展示，并把本库方案收口为规则、技能、模板和 sensor 四层。
- [[concepts/agent-instruction-sharing]]：Claude Code 和 Codex 共享 agent 项目规则的方法，推荐根 `AGENTS.md` 作为唯一规则正文，`CLAUDE.md` 和可选 `.codex/AGENTS.md` 只做薄导入入口。
- [[agent-governance-strategy]]：Agent 治理策略整改入口，收口入口瘦身、log eligibility、产物化资格、检查预算和规则升级预算。
- [[articles/2026-05-29-finalizer-write-scope-case]]：Finalizer 写入范围失守案例，分析用户收窄写入范围后，finalizer 只证明 clean 而不证明 scope 的 Harness 缺口。
- [[articles/2026-05-30-agent-governance-reflection-doccustomer]]：Agent 治理整体反思，以 DocCustomer 为例，归纳规则膨胀、角色边界、分流过重、状态冗余等八类结构性问题和改进方向。
- [[articles/2026-05-30-agent-governance-cross-project-synthesis]]：跨 8 个工程的 Agent 治理横向对比，抽象出独立重发明、规则只增不减、边界靠声明、协议不统一等共性问题，提出共享治理内核方案。
- [[articles/2026-05-30-agent-system-deep-analysis]]：基于 Karpathy Software 3.0、OpenClaw memory、AHE 可观测性支柱和多 agent 架构理论，对当前 8 工程 agent 体系做深度诊断，归纳六大根本性设计缺陷和三阶演进路径。
- [[articles/2026-05-30-acknowledgebase-governance-hub-design]]：AcknowledgeBase 作为跨工程治理中控的具体设计：四类治理动作、调度频率、中控职责边界、wiki template-changelog 最小改动方案。
- [[skills/cross-project-skill-adoption-prompt/SKILL]]：把任意已沉淀 skill / 能力转换成目标工程可执行升级提示词，并附资料路径、吸收边界、落地步骤和验证要求。
- [[skills/knowledge-linking/SKILL]]：新增或大改长期知识页时，按调研、分层、关系画像、入口回链和 sensor 验证完成知识网络落地。
- [[skills/historical-dialogue-retrospective/SKILL]]：从历史对话、当前上下文、log、Harness episode、git 证据和检查输出中复盘 agent 偏差、效率质量与 workflow 改进。
- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析技能，用于模糊问题、故障、联调失败、验收争议和跨工程阻塞的定位、分工与联测收口。
- [[concepts/codex-goals]]：Codex 长时任务的线程级完成契约，适合终点明确但路径依赖中间证据的持续工作。
- [[articles/2026-05-25-codex-goals-research]]：Codex Goals 专题调研，整理 Goal 的完成契约、生命周期、强弱写法和研究型任务用法。
- [[concepts/harness-engineering]]：AI Agent 的工程化运行环境方法，关注上下文、工具、规则、工作流、验证和演化闭环。
- [[articles/2026-05-25-harness-engineering-research]]：Harness Engineering 深度调研，汇总本地材料、OpenAI、Martin Fowler、LangChain、Vercel 和近期论文案例。
- [[harness-evolution]]：把用户纠偏、检查失败、模式切换和重复失守转成可复盘 episode。
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
- [[templates/goal-contract-template]]：长时任务完成契约模板，用于定义期望最终状态、完成判定、验证面 / 证据边界、约束、预算和阻塞停止条件。
- [[templates/guided-discovery-session-template]]：引导式设计会话模板，用于承接对话所得、agent 思考结果、场景包、性能预算和产物化闭环。
- [[templates/harness-adoption-template]]：新系统或子工程接入 Agent Harness 时的单一信息源、写权限、验证层级和回传模板
- [[templates/harness-episode-package-template]]：单次 Harness episode 的 checkpoint、执行轨迹、证据边界和反馈模板
- [[templates/harness-evolution-review-template]]：周期性复盘 episode、sensor backlog、晋升和降级决策的模板
- [[templates/project-retrospective-template]]：项目复盘档案模板
- [[templates/skill-transfer-manifest-template]]：技能跨工程迁移资料清单模板
- [[template-feedback-rules]]：其他项目进化出的系统层信息如何反哺模板库，并区分知识库模板与系统治理模板

## 项目接手与代码基线

- [[projects/codebase/README]]：现实代码、旧工程或外部模板的审计入口
- [[projects/codebase/source-code-audit-workflow]]：源码工程深度解读工作流

## 软件架构包

- [[projects/design/README]]：软件架构总入口和推荐阅读顺序
- [[projects/design/topics/README]]：重要设计专题入口，承接未拍板专题和专项储备
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
- 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[state-constraint-reasoning]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[POLICY]]、[[BRAIN]]
- 技能层：[[skills/README]] 和 `skills/`
- 运行层：`projects/`
- 沉淀层：`articles/`、`concepts/`、`indexes/`
- 历史层：[[log]]、`archive/`
- 证据层：`raw/`、`inbox/`、`assets/`

## 物理结构

- 根目录保留高频入口：[[README]]、[[INDEX]]、[[AGENTS]]、[[log]]；`CLAUDE.md` 只作为 Claude Code 适配入口导入 [[AGENTS]]；`.codex/AGENTS.md` 如存在只能作为 thin Codex adapter 指回根 [[AGENTS]]，不维护规则副本
- `governance/` 收治理页和规则页
- `skills/` 收项目内可复用 agent 技能
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

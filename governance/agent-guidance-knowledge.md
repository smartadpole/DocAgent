# 知识维护与上下文

本页是 [[AGENTS]] 按需加载的唯一条件正文；只读取与当前任务相关的章节。

## 分层总览

- 入口层：[[README]]、[[INDEX]]
- 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[POLICY]]、[[BRAIN]]
- 技能层：[[skills/README]] 和 `skills/`
- 呈现层：[[views/README]] 和 `views/`
- 运行层：[[projects/README]] 和 `projects/`
- 沉淀层：`articles/`、`concepts/`、`indexes/`
- 历史层：[[log]]、`archive/`
- 证据层：`raw/`、`inbox/`、`assets/`

治理层当前已经物理收口到 `governance/`，只有 [[AGENTS]] 保留在根目录。原因不是例外随意，而是它本身就是 agent 的根级特殊入口。

## 角色分工

- `governance/`：治理层目录。放流程、规则、共享背景和写法指南；具体由 [[governance/README]] 收口。
- `skills/`：项目内 agent 技能层。放面向当前项目的可复用分析流程、判断框架和执行套路；技能可以带项目语境，但不替代项目状态、需求、设计、EP / TASK 状态、轻量 TODO 或测试报告的单一信息源。
- `views/`：问题聚焦式图文呈现层。放 current / snapshot lens、registry 和可追溯呈现入口；只承接 source pack 的视觉重组、证据边界、导出配置和刷新条件，不替代项目页、知识页、报告、决策、验收或 log 的事实源职责。
- `raw/`：原始资料层。优先保持原样，少改动。
- `inbox/`：临时收口区。来源还没完全处理完时先放这里。
- `assets/`：支持性附件层。图片、截图、导图、导出物和 canvas 放这里。
- `projects/`：活跃研发项目层。需求、设计、会议、任务、决策、记忆、发布和复盘放这里，具体目录和文件组织以 `projects/STRUCTURE.md` 为准。
- `projects/service-registry.md`：服务实例台账层。承接已确认的服务运行事实、健康检查、配置 profile、数据目录、日志、代码版本和更新方式；不承接真实密钥或一次性排障流水。同一代码工程 / 部署上下文下的 API、UI、scheduler、worker 或 sidecar 默认作为一个服务组的组件记录。
- `projects/trace.md`：需求演进链层。记录原始意图、约束变化、修补性需求、关键取舍和最终实现口径之间的串联。
- `projects/codebase/`：代码基线审计层。承接现实实现、既有工程、外部模板或旧系统的页面图、schema 图、基础设施、冲突和复用边界；它不反向定义主工程口径。
- `projects/codebase/source-code-audit-workflow.md`：源码工程深度解读工作流。遇到源码解读、既有系统审计或生产接入判断时，必须先按该页定义目标等级、证据矩阵和终态自审，不允许把首轮核心链路理解说成完整审计。
- `projects/design/`：正式设计层。`README.md` 做总入口；`tech-selection.md`、`architecture.md`、`backend-frontend-structure.md`、`permission-boundary.md`、`write-boundary.md`、`database.md`、`deployment.md`、`runtime-quality.md` 共同组成完整软件架构包；`topics/` 承接重要设计专题和专项储备。
- `projects/design/diagrams/`：设计图资产层。承接正式架构图、服务拓扑图、业务到实现总览图和设计推演图；Excalidraw 是当前主力源文件格式，Diagrams.Net 只用于架构稳定后的正式交付版，Markdown 正文默认嵌入 SVG / PNG 作为可读预览，并在同段落回链 Excalidraw 源文件用于编辑。
- `projects/meetings/`：会议层。正式会议材料、纪要、行动项和会后分流放这里，`worklog.md` 记录时间线。
- `projects/retrospectives/`：复盘 archive root。根目录只保留 `README.md`、`indexes/` 和年份目录；阶段、专题、交付链、事故后、Issue 后和 Agent 协作复盘正文进入 `projects/retrospectives/<year>/`。复盘行动项必须分流到已有 Issue / 事故、事项、会议、决策、项目记忆、trace、模板、skill、sensor 或治理页，不在这里形成平行看板。
- `projects/design/topics/`：设计专题层。承接未拍板但需要持续推进的设计问题，以及当前不进入完整架构包、但要长期保留的专项设计储备；会议页只引用，不重复维护主正文。
- `projects/development/plan/`：研发总控层。承接当前阶段、阶段门摘要、执行入口、事项关系模型和支撑文件分组。
- `projects/development/execution/`：执行控制层。承接 EP 执行包、TASK、待办、编码交接、工程反馈闭环和开发过程记录。
- `projects/development/gates/`：阶段门层。承接准入、准出、冻结对象、验收证据和风险边界。
- `projects/development/acceptance/`：验收计划层。承接复杂验收的 AP 计划、长用例索引、fixture / oracle、人工确认和发布 runbook，不承接测试报告正文。
- `projects/development/reports/`：验证证据层。承接测试方案执行后的证据、测试结论、相关回归和准出报告。
- `projects/development/risks/`：研发风险层。承接阻塞、待确认项、owner 归口和会议 / 决策分流。
- `projects/development/feature-points/`：功能点实体层。一页一个功能点，`status` 和 `phase` 写在各自页面属性里，`README.md` 只做索引。
- `projects/development/issues/`：Issue 案件层。承接已发生问题、bug、偏差和验收失败的原始现象、分层事实、修复、复验和关闭裁决；报告只记录每次验证过程，不替代 Issue 案件档案。
- 角色分层固定为：`projects/README.md` 偏首席技术官 / 项目负责人视角，`projects/development/README.md` 和 `projects/development/plan/README.md` 偏研发经理视角，`projects/development/execution/README.md` 偏执行协调视角，`projects/meetings/README.md` 偏会议协作视角，`projects/retrospectives/README.md` 偏长期学习和改进闭环视角，`projects/development/feature-points/README.md` 和实体页偏工程师视角。
- `articles/`：摘要卡片层。每篇材料一张主卡。
- `concepts/`：概念和实体层。工具、项目、术语都放这里。
- `indexes/`：导航层。只负责入口、分类和检索。
- `archive/`：退役和历史层。保留旧页面、合并结果和历史版本。
- `log.md`：按时间降序维护、按对话组织的主题化活动记录，记录提炼后的主题、用户意图、关键动作和结构变化；日期只是分组容器，不是合并单位，同一天内部也按最新记录在前排序。

## 单一信息源

- 同一类信息只保留一个主入口，不允许在多个页面复制粘贴同一段正文。
- 状态类信息以 `projects/README.md` 为主，其他页面引用或链接它，不重复维护第二份状态说明。
- 服务实例类信息以 `projects/service-registry.md` 为主，部署页只保留部署原则、环境治理和配置边界，不重复维护每台机器的当前运行事实。
- 概念类信息以 `concepts/` 主页面为主，项目页只写与当前项目直接相关的上下文。
- 导航类信息放 `indexes/`，不要在多个说明页里重复堆导航列表。
- 需要在别处提及时，优先链接、摘一句、或写简短引用说明，不复制整段内容。
- 会议相关信息也遵守单一信息源：如果某场会已经拆出独立会前材料页，那么议程、目标、阅读顺序、讨论方式、会前材料和预期输出只保留在该页；`projects/meetings/worklog.md` 只保留这场会的时间线摘要、结论、待办和分流，不再维护第二份完整会前正文。
- 如果一场会目前只存在于 `projects/meetings/worklog.md`，可以先在同一条记录里承接必要的会前信息；但只要后续拆出了独立会议页，就必须同轮把 `worklog` 里的重复段落收回成链接和简述，不能让两份正文并存。
- 单条会议记录内部也要去重：`议题` 只写这次要回答什么，`结论` 只写最终确认了什么，`行动项` 只写会后仍需要跟踪的事项；同一件事不要在三个字段里换句话重复写。
- 会议记录里的固定字段按需保留：如果 `会前材料`、`分流` 或 `关联链接` 只是在重复同一批默认链接或默认分流，就删到最小，不为了模板完整性保留冗余段落。

## 记忆路由

- 会影响所有后续工作的硬约束，进入 [[AGENTS]]。
- 多轮确认后会持续影响判断的共享背景，进入 [[BRAIN]]。
- 会影响路由、优先级和自动沉淀边界的规则，进入 [[POLICY]]。
- 会影响“先轻后重”、首次反馈、读取预算和模式切换的响应效率规则，进入 [[response-mode-routing]]，再由 [[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]] 保持短引用。
- 只反映当前项目长期有效事实的内容，进入 `projects/memory/README.md`。
- 只反映当前项目里需求、功能、约束、修补和最终范围如何收敛的内容，进入 `projects/trace.md`；原始来源材料的索引、出处、文件改名和格式转换过程不进入 trace。
- 全新应用探索期的多个候选方向，先留在 `inbox/`、`raw/`、`articles/`、`concepts/`；只有某个方向明确成为当前项目，才进入 [[projects/requirements]]、[[projects/trace]] 和设计 / 研发链路。
- 稳定的个人偏好、命名习惯、表达偏好，进入 `workspace-memory`。
- 项目阶段出现的思维碰撞、方案冲突和最终取舍，进入 `projects/decisions.md`。
- 只反映时间降序、按对话组织的主题化过程记录，进入 `log.md`，但 `log.md` 不是主动背景。
- 下游项目已经验证过的结构、流程、规则、记忆路由、模板、通用写法和自动化契约，需要先按 [[template-feedback-rules]] 抽象成系统层信息，再回写模板库对应入口。
- 如果反哺候选和既有规则冲突，或会让规则层明显变重，先改旧规则或升级冲突，不新增平行规则。

## 上下文模型

- 这里的“上下文”，不是当前文件附近几段话，而是为了正确更新目标内容，必须一起判断的最小相关信息集合。
- 每次更新都要先判断目标内容属于哪一层：证据层、项目运行层、技能层、知识沉淀层、导航层、历史层。
- 证据层是 `raw/`、`inbox/`、`assets/`，回答“信息从哪里来”。
- 项目运行层是 `projects/README.md` 加上需求、设计、会议、复盘、决策、记忆、开发、服务实例台账、发布、事故这些页面，回答“当前项目正在做什么、为什么这样做、做到哪里了、哪些经验会影响下一轮，以及真实服务现在在哪里运行”。
- 其中 `projects/trace.md` 专门回答“这轮需求是怎样收敛到当前实现口径的”，它属于项目运行层，不属于历史层或规则层，也不承接原始来源材料整理。
- 技能层是 `skills/`，回答“agent 遇到高频任务时按什么可复用流程分析和执行”；它可以引用项目主页面，但不能复制项目事实正文或替代正式回写。
- 知识沉淀层是 `articles/`、`concepts/`、`indexes/`，回答“哪些结论已经稳定、哪些概念可以复用、入口如何组织”。
- 历史层是 `archive/` 和 `log.md`，回答“那次对话在解决什么主题、怎么演进、哪些内容已退役、这次结构调整从何时开始生效”。
- 同一段内容至少同时拥有四个属性：响应模式、所属阶段、主入口、受影响页面。
- 只要新增模块、目录、页面类型，或某个文件开始承担新职责，就必须同步更新这套上下文模型，不允许结构已经变化而规则仍停留在旧版本。

## 关联关系

- `projects/README.md` 是项目运行层主入口，连接项目层其他主页面。
- `projects/service-registry.md` 上连项目主页和部署页，横向连接相关代码基线、开发执行、测试报告和事故记录；它只记录已确认的运行实例事实，不替代部署设计、服务合同或密钥治理。
- `projects/development/plan/work-item-system-model.md` 上连研发总控、需求、设计和决策，下连 Gate、FP、EP、TASK、risk、issue、test、报告和服务台账；它是事项关系和关闭守卫的单一信息源。
- `projects/development/plan/test-acceptance-planning-model.md` 上连事项模型和 TASK 模型，下连 `projects/development/acceptance/`、报告、issue、TASK、EP、FP 和 Gate；它是测试计划与验收合同的单一信息源。
- `projects/development/acceptance/README.md` 横向连接 AP 计划索引、报告和事项页；它承接测试前计划，不承接测试后证据正文。
- `projects/development/issues/README.md` 横向连接 EP、TASK、测试报告、风险、服务台账和事故目录；它保存已发生问题的案件档案，不能被单次测试报告替代。
- 需求页上连项目主页，下连设计页和决策页，外连相关 `raw/` 来源。
- `projects/trace.md` 上连项目主页、需求页和设计页，横向连接决策与开发，负责把原始意图、约束变化、修补性需求和最终范围串成一条可回看主链；原始来源材料的出处和整理过程不放进去。
- `projects/codebase/README.md` 上连项目主页、需求页、设计页和决策页，横向连接页面图、schema 图、基础设施、冲突和复用边界；它只记录现实实现事实和复用判断，不反向覆盖主需求或主设计。
- `projects/meetings/README.md` 上连项目主页、需求页、设计页、设计专题页、决策页和开发页，横向连接正式会议记录、行动项和会后分流。
- `projects/retrospectives/README.md` 上连项目主页、trace、决策、开发、Issue、事故、log 和复盘概念页；它承接 archive root 规则、索引入口、跨复盘共性主题和沉淀路由，不承接正文平铺，不替代事实主档案、决策页或行动项 owner 页面。
- 设计页上连项目主页和需求页，横向连接决策页，必要时连到相关 `concepts/`；如果设计层拆出技术选型、架构、工程结构、权限边界、写操作边界、数据库、部署、运行质量等子页，它们仍然属于同一个设计层。
- 决策页要能回溯到需求、设计和当时约束，必要时连到开发页、发布页、记忆页或事故目录。
- 记忆页连接项目主页、决策、设计和运行记录，是稳定背景，不是过程日志。
- 开发页连接项目主页、决策和实际推进记录，是过程上下文，不是长期知识主入口。
- 发布页连接项目主页、设计、决策和验证结果；事故目录连接发布、运行现象、根因和修复动作。
- `articles/` 连接原始来源和稳定结论；`concepts/` 连接多个文章页和项目页；`indexes/` 只负责把这些主页面串起来。
- [[skills/README]] 上连入口层和治理层，横向连接会被技能使用的项目主页面；具体技能页只承接分析流程和输出格式，不承接项目事实的单一信息源。
- `archive/` 只承接退役内容，不承担当前主入口职责。

## 演进关系

- 默认演进链路是：`raw/inbox -> projects -> articles/concepts/indexes -> archive/log.md`。
- 新信息先作为来源进入 `raw/` 或 `inbox/`。
- 全新应用探索的早期链路是：`inbox/` / `raw/` -> `articles/` / `concepts/` -> [[projects/requirements]] -> [[projects/trace]] -> [[projects/design/topics/README]] -> [[projects/decisions]] -> [[projects/design/README]] -> [[projects/development/README]]；进入 `projects/` 前，先确认它已经不是多个候选方向之一，而是当前要推进的应用。
- 当信息开始参与当前项目判断和推进时，进入 `projects/`。
- 当正式会议材料、会议纪要和行动项开始参与当前项目判断和推进时，优先进入 `projects/meetings/`。
- 当阶段、专题、事故、Issue、交付链或 Agent 协作暴露长期学习价值时，具体复盘档案进入 `projects/retrospectives/<year>/` 并同步索引；抽象后的方法再回写 `concepts/`、`templates/`、`skills/` 或治理层。
- 当项目里的某些结论已经脱离当前阶段、可以跨阶段或跨问题复用时，提升到 `articles/` 或 `concepts/`。
- 当某类 agent 分析动作在当前项目中反复出现，且需要项目语境、证据链、分工和验证格式保持稳定时，可以沉淀到 `skills/`。
- 当一个主题需要长期导航、分类和检索时，再由 `indexes/` 收口。
- 当页面不再承担当前入口职责但仍有历史价值时，转入 `archive/`，同时在 `log.md` 留痕。

## 读取顺序

- 写任何内容时都要先建立全局背景，不允许只盯着当前文件局部改写。
- 先判断这段内容在整个文档库里的位置：它服务哪个主题、哪个阶段、哪个主入口、哪类读者。
- 任何一段内容都不是孤立的，修改前必须先判断它的上游、下游和主入口。
- 用 `INDEX.md` 和相关入口定位目标 owner，再读直接依赖；已经加载且未变化的页面复用，不默认全量重读。
- [[BRAIN]] 提供共享背景；已加载且未变化时直接复用，发现新需求或证据冲突时再回看相关章节。
- 默认先按 [[response-mode-routing]] 判定本轮读取深度；快速诊断只读最小事实源，状态关闭、规则升级、结构变更和跨工程沉淀必须升级到对应完整读取集。
- 如果目标涉及规则、优先级或自动沉淀边界，再读 [[POLICY]]。
- 如果目标涉及项目级稳定记忆，再读 `projects/memory/README.md`。
- 如果目标在 `projects/`，先读 `projects/README.md` 和 `projects/STRUCTURE.md`，再读相关的需求、设计、会议、复盘、决策、记忆、开发页面。
- 如果目标是服务实例台账或服务运行事实，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/service-registry.md`、`projects/design/deployment.md`，再按服务补读相关代码基线、开发执行、测试报告或事故页。
- 如果目标在 `projects/codebase/`，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/codebase/README.md`、`projects/requirements.md`、`projects/design/README.md` 和 `projects/decisions.md`，再读对应代码基线子页。
- 如果目标在 `projects/meetings/`，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/meetings/README.md`、`projects/meetings/worklog.md`，再读相关的需求、决策、开发和记忆页面；如果会议涉及未决设计专题，再补读 `projects/design/topics/README.md` 和对应专题页。
- 如果目标在 `projects/retrospectives/`，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/retrospectives/README.md`、[[skills/retrospective-capability/SKILL]]、[[concepts/project-retrospective]]，再按对象补读 trace、决策、开发、Issue、事故、会议、log、[[skills/delivery-retrospective/SKILL]]、[[skills/historical-dialogue-retrospective/SKILL]] 或相关概念页。
- 如果目标在 `projects/development/`，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/development/README.md`、`projects/development/plan/README.md` 和 `projects/development/plan/work-item-system-model.md`，再按任务补读 `execution/`、`gates/`、`implementation/`、`issues/`、`acceptance/`、`reports/`、`risks/` 或功能点实体页。
- 如果目标在 `skills/`，先读 [[README]]、[[INDEX]]、[[skills/README]]、[[BRAIN]]、[[POLICY]] 和 [[WORKFLOW]]；如果技能包含项目业务语境，再读对应项目主页面、相关设计页、EP / TASK、轻量 TODO、测试报告或服务台账，确认技能没有复制正式项目事实正文。
- 如果目标在知识库层，先找对应的主摘要页、概念页和索引页，确认哪一页才是单一信息源。
- 如果这次改动会影响阶段判断、导航结构、概念定义、项目状态或记忆路由，就必须额外回看相关入口页和主页面。
- 改动后要回看相关入口页和链接页，确认结构、跳转和职责没有被破坏。

### 批处理模式的读取顺序

- 先做一次批次级校准：判断这批内容属于证据层、项目运行层还是知识沉淀层，并确认主入口和单一信息源。
- 再读这批材料共享的一组入口页，不要把同一批入口页按材料份数重复读取。
- 之后按单份材料只补读它自己的直接来源、对应主页面和必要的邻接页。
- 只有出现异常信号时才升级读取：规则变化、结构变化、项目状态变化、冲突升级、设计拍板、记忆路由变化。

## 目标文件的最小读取集

- 改 `projects/README.md` 时，至少读：`README.md`、`INDEX.md`、`projects/STRUCTURE.md`、相关项目层主页面；如果这次更新涉及记忆或规则，再加读 [[BRAIN]]、[[POLICY]] 和 `projects/memory/README.md`。
- 改 `projects/service-registry.md` 时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、`projects/design/deployment.md`、相关代码基线页、相关测试报告或运维记录；如果新增服务会影响阶段、风险、owner 或准出，再同步检查 `projects/status.md`、`projects/development/execution/todo.md`、风险页和会议页。
- 改需求页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、相关 `raw/` 来源、已有设计页、已有决策页。
- 改 `projects/trace.md` 时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、需求页、已有设计页、已有决策页、当前相关开发页；如果 trace 涉及记忆或规则边界，再加读 [[BRAIN]]、[[POLICY]] 和 `projects/memory/README.md`。
- 改代码基线页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、`projects/codebase/README.md`、需求页、设计页和已有决策页；如果现实实现和主线冲突，先写 [[projects/codebase/conflicts]]，再升级到 [[projects/decisions]]。
- 改设计页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、`projects/design/README.md`、`projects/design/topics/README.md`、需求页、已有决策页、相关设计子页 / 专题页、相关 `concepts/`；如果设计会影响记忆或规则，还要读 [[BRAIN]]、[[POLICY]] 和 `projects/memory/README.md`。
- 改决策页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、需求页、设计页、相关开发页或事故目录；如果决策涉及记忆路由，再读 [[BRAIN]]、[[POLICY]] 和 `projects/memory/README.md`。
- 改开发页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、当前相关决策页，必要时读发布页或事故目录。
- 改开发执行页、EP、TASK、待办、Issue、AP、测试报告、Gate 或风险页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、`projects/development/README.md`、`projects/development/plan/README.md`、`projects/development/plan/work-item-system-model.md`、`projects/development/plan/test-acceptance-planning-model.md`、当前相关 EP / TASK / FP / Gate / Issue / AP / 报告页和必要设计页。
- 改会议页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、`projects/meetings/README.md`、`projects/meetings/worklog.md`、相关需求页、决策页和开发页；如果会议讨论的是未决设计专题，还要补读 `projects/design/topics/README.md` 和对应专题页；如果会议规则或分流方式变更，再读 [[WORKFLOW]]、[[POLICY]] 和 [[BRAIN]]。
- 改复盘页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、`projects/retrospectives/README.md`、[[skills/retrospective-capability/SKILL]]、[[concepts/project-retrospective]]；软件研发复盘补读 [[skills/delivery-retrospective/SKILL]] 和 [[concepts/software-development-project-retrospective]]，Agent 工作复盘补读 [[concepts/agent-work-retrospective]] 和 [[skills/historical-dialogue-retrospective/SKILL]]，事故 / Issue 后复盘补读事实主档案。
- 改发布页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、设计页、决策页、相关验证记录。
- 改事故目录或事故文件时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、发布页、相关开发页、相关决策和原始证据。
- 改 `skills/` 时，至少读：[[README]]、[[INDEX]]、[[skills/README]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]；如果技能包含项目业务语境，再读对应项目主页面、相关设计页、EP / TASK、轻量 TODO、测试报告或服务台账，确认技能没有复制正式项目事实正文。
- 改 `articles/` 时，至少读：对应 `raw/` 来源、相关 `concepts/`、必要时读相关项目页。
- 改 `concepts/` 时，至少读：相关 `articles/`、相关项目页、相关 `indexes/`。
- 改 `indexes/` 时，至少读：它要导航到的主页面，不允许只看索引本身闭门重排。
- 改 [[response-mode-routing]] 时，至少读：[[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]、[[skills/README]] 和相关技能 / 模板；如果改动影响项目状态、验收或模板接入，再补读相关项目主页面、[[projects/trace]] 和 [[projects/decisions]]。

### 批处理模式的最小读取集

- 批量改 `articles/` 时，先读一次：`README.md`、`INDEX.md`、相关 `articles/` 主入口或相邻摘要卡、相关 `concepts/` 主页面；然后每篇材料只补读自己的来源和直接回链目标。只有当摘要明确参与当前项目判断时，才补读相关项目页。
- 批量改设计材料或设计草稿时，先读一次：`projects/README.md`、`projects/STRUCTURE.md`、对应设计主入口、当前相关需求页或决策页；然后每份材料只补读自己的直接来源和必要的相关 `concepts/`。只有当某份材料会改变记忆、规则、项目状态或关键取舍时，才追加 [[BRAIN]]、[[POLICY]]、`projects/memory/README.md` 和更多项目页。
- 批量改 `concepts/` 时，先读一次相关概念主页面和索引页，再按条目补读必要的 `articles/` 或项目页，不为每个概念重复读同一组导航入口。

## 文件与目录操作

- 新建目录前先确认是不是已有目录的子集。
- 新建目录后先补 `README.md`；模板和索引按需补，不要为了完整性先铺满。
- 模板正文只允许维护在对应的 `templates/` 页面；其他页面只做入口说明、使用约束和跳转，不重复粘贴第二份模板正文。
- 对 `projects/` 这类运行层，已经形成多文件职责的模块可以保留子目录；如果子目录当前只有一个 `README.md`，默认优先收平成单文件。`incidents/`、`meetings/`、`retrospectives/` 这类天然按条目累积的模块默认保留目录。
- 新建文件先确认它属于 `raw/`、`inbox/`、`articles/`、`concepts/` 还是 `indexes/`。
- 如果是当前项目内可复用的 agent 分析流程或执行技能，优先放 `skills/`，并补 [[skills/README]] 入口；不要塞进 `templates/` 或项目状态页。
- 如果是支持性附件，优先放 `assets/`；如果是退役页面，优先放 `archive/`。
- 如果是活跃研发项目的文档，优先放 `projects/`。
- 对单一小项目，优先一页到底，拆分目录和子文件必须有明确理由。
- 修改文件前先读现有内容，只改必要部分。
- 重命名文件或目录时，优先保持内部链接同步更新。
- 处理已有目录时，先扩展再拆分，尽量不要平行复制一套新结构。
- 原始来源不要回写成整理稿，整理稿也不要再塞回 `raw/`。
- 合并、归档、删除都要同步更新 `INDEX.md` 和 `log.md`。
- 研发项目结束后，把稳定结论回收到知识库层，把项目特有上下文保留在 `projects/` 或 `archive/`。
- 结构性变更要写进 `log.md`。

## 链接规则

- Markdown 方言、链接、显示名、表格转义、frontmatter、资产、生成内容和验证层级统一读取 [[governance/markdown-document-governance-profile.v1]]；不要在 AGENTS 维护第二份语法清单。
- wiki profile 使用 Obsidian wikilink 表达内部页面语义跳转，外部来源使用普通 Markdown link；其他工程不得直接继承本 profile。
- 新增或修改 Markdown 时先判 canonical source / generated 边界，运行 `python3 scripts/check_all.py --only markdown-document-governance` 和受影响的语义检查；用户可见渲染问题还要做 primary renderer readback。
- 新发现且可稳定复现的 Markdown 坏格式同轮补失败 / 通过 fixture，或说明为什么暂不适合硬化。

## 写作规则

- 优先短页、强链接、可检索。
- 把事实、解释、推测分开写。
- 不确定时明确标注不确定。
- 名词尽量稳定，避免同义词泛滥。
- 只要一条记录采用“标签：内容”这种主题展开式写法，默认把冒号前的标签加粗，写成 `**标签**：内容`；适用于 [[log]]、[[projects/trace]]、[[projects/decisions]]、会议记录和其他同类记录页。
- 正文默认中文；英文只保留文件名、产品名、代码标识、API 名和必要的专有术语。
- 如果页面本身是术语表、代码示例、外部资源清单或产品原名说明，可以保留原始英文表达。
- 同一页面里必须保持一种主语言，除必要专有名词外，不得随意中英混排。
- 新增正式决策时，默认使用 `**背景**`、`**要决策什么**`、`**可选项**`、`**最终决策**`、`**影响**`、`**各自优劣**`、`**风险点**` 这组骨架；其中 `**最终决策**` 和 `**影响**` 必须放在 `**各自优劣**`、`**风险点**` 之前，不要只写结论不写比较过程，也不要补成另一份需求或设计全文。

## 新文档处理

1. 新材料先进入 `inbox/` 或 `raw/`。
2. 生成或更新摘要卡。
3. 回链到相关概念页。
4. 更新索引页。
5. 在 `log.md` 顶部新增一条主题化记录。

## 定期检查

- 找断链。
- 找孤儿页。
- 找过时结论。
- 找没有实体页的重要概念。
- 找适合拆分成新页面的高频主题。

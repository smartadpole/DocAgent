# 维护约束

这份文件是给 Codex 和其他 agent 的维护约束。目标不是写说明书，而是把这套文档库持续维护成一个可演化的知识库。

## 分层总览

- 入口层：[[README]]、[[INDEX]]
- 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[agent-governance-strategy]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[state-constraint-reasoning]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[POLICY]]、[[BRAIN]]
- 技能层：[[skills/README]] 和 `skills/`
- 运行层：[[projects/README]] 和 `projects/`
- 沉淀层：`articles/`、`concepts/`、`indexes/`
- 历史层：[[log]]、`archive/`
- 证据层：`raw/`、`inbox/`、`assets/`

治理层当前已经物理收口到 `governance/`，只有 [[AGENTS]] 保留在根目录作为共享 agent 规则正文。Codex 直接读取根 `AGENTS.md`；`CLAUDE.md` 可以作为 Claude Code 适配壳导入 [[AGENTS]]；`.codex/AGENTS.md` 如果存在，只能作为导入 `../AGENTS.md` 的 thin Codex adapter，不承接第二份规则正文。

## 工具入口统一

- 项目级 agent 规则正文只维护根目录 `AGENTS.md` 一份。
- Claude Code 通过根目录 `CLAUDE.md` 的 `@AGENTS.md` 导入共享规则，只追加 Claude 专用补充。
- Codex 优先直接读取根 `AGENTS.md`；如果工程保留 `.codex/AGENTS.md`，该文件只能通过 `@../AGENTS.md` 指向根规则，并追加极少量 Codex Only 外壳说明。
- 如果其他工程同时存在根 `AGENTS.md` 和 `.codex/AGENTS.md` 且内容重复，默认把 `.codex/AGENTS.md` 的有效规则并回根 `AGENTS.md`；随后按项目需要删除 `.codex/AGENTS.md`，或把它改成 thin Codex adapter。
- 工作阶段优先跑专项 sensor：`python3 scripts/check_all.py --only harness-governance`、`python3 scripts/check_all.py --only testing-system-maturity` 或 `python3 scripts/check_all.py --only execution-contract-semantics`；收尾或提交前跑完整 `python3 scripts/check_all.py`。

## 角色分工

- `governance/`：治理层目录。放流程、规则、共享背景和写法指南；具体由 [[governance/README]] 收口。
- `skills/`：项目内 agent 技能层。放面向当前项目的可复用分析流程、判断框架和执行套路；技能可以带项目语境，但不替代项目状态、需求、设计、EP / TASK 状态、轻量 TODO 或测试报告的单一信息源。
- `raw/`：原始资料层。优先保持原样，少改动。
- `inbox/`：临时收口区。来源还没完全处理完时先放这里。
- `assets/`：支持性附件层。图片、截图、导图、导出物和 canvas 放这里。
- `projects/`：活跃研发项目层。需求、设计、会议、任务、决策、记忆、发布和复盘放这里，具体目录和文件组织以 `projects/STRUCTURE.md` 为准。
- `projects/service-registry.md`：服务实例台账层。承接已确认的服务运行事实、健康检查、配置 profile、数据目录、日志、代码版本和更新方式；不承接真实密钥或一次性排障流水。同一代码工程 / 部署上下文下的 API、UI、scheduler、worker 或 sidecar 默认作为一个服务组的组件记录。
- `projects/trace.md`：需求演进链层。记录原始意图、约束变化、修补性需求、关键取舍和最终实现口径之间的串联。
- `projects/codebase/`：代码基线审计层。承接现实实现、既有工程、外部模板或旧系统的页面图、schema 图、基础设施、冲突和复用边界；它不反向定义主工程口径。
- `projects/codebase/source-code-audit-workflow.md`：源码工程深度解读工作流。遇到源码解读、既有系统审计或生产接入判断时，必须先按该页定义目标等级、证据矩阵和终态自审，不允许把首轮核心链路理解说成完整审计。
- `projects/design/`：正式设计层。`README.md` 做总入口；`tech-selection.md`、`architecture.md`、`backend-frontend-structure.md`、`permission-boundary.md`、`write-boundary.md`、`database.md`、`deployment.md`、`runtime-quality.md` 共同组成完整软件架构包；`topics/` 承接重要设计专题和专项储备。
- `projects/meetings/`：会议层。正式会议材料、纪要、行动项和会后分流放这里，`worklog.md` 记录时间线。
- `projects/retrospectives/`：复盘档案层。承接阶段、专题、事故后、Issue 后和 Agent 协作复盘文件；复盘行动项必须分流到已有 Issue / 事故、事项、会议 / 决策、项目记忆、trace、模板、skill 或治理页，不在这里形成平行看板。
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

## 治理层边界

- [[POLICY]]：规则裁定层。回答“什么允许自动晋升、什么必须人工确认、冲突时先按谁”
- [[agent-governance-strategy]]：Agent 治理策略层。回答“哪些防线是 P0 硬约束，哪些应降成语义门、流程或 backlog”
- [[AGENTS]]：执行约束层。回答“agent 修改时必须怎么做”
- [[WORKFLOW]]：流程编排层。回答“通常按什么顺序推进”
- [[response-mode-routing]]：响应效率路由层。回答“本轮先快诊断、沉淀、验收、实现还是升级规则”
- [[proactive-dialogue-system]]：主动对话与引导式设计层。回答“目标不完整时，agent 怎么自动判定场景、少量提问、带假设推进并产物化”
- [[state-constraint-reasoning]]：状态与约束推演层。回答“新信息进入系统后，哪些状态、依赖、阻塞和可执行性会被改变”
- [[instruction-adherence]]：指令遵循层。回答“已有规则怎样升级成触发器、模板字段、sensor、门禁和最终证明”
- [[execution-contract-semantics]]：执行合同语义层。回答“当前执行合同是否被参考规则、非目标或上层证据污染”
- [[harness-evolution]]：Harness 自演进层。回答“用户纠偏、检查失败、模式切换和重复失守如何形成 episode，并何时晋升为 sensor、模板、技能或规则”
- [[harness-feedback-ledger]]：Harness episode 台账。回答“哪些 episode 已观察、已晋升、待补 sensor 或待降级”
- [[BRAIN]]：共享背景层。回答“哪些已确认前提要自动带入后续工作”

判断时优先用这条：

- 如果问题是“怎么判”，先看 [[POLICY]]
- 如果问题是“治理规则是不是过硬、是否该降级或先做资格判断”，先看 [[agent-governance-strategy]]
- 如果问题是“怎么执行”，先看 [[AGENTS]]
- 如果问题是“怎么推进”，先看 [[WORKFLOW]]
- 如果问题是“要不要先轻量诊断、何时进入重治理”，先看 [[response-mode-routing]]
- 如果问题是“用户只有粗糙目标、需要把想法想完整或要更智能地推进”，先看 [[proactive-dialogue-system]]
- 如果问题是“计划在当前系统状态下是否可执行、哪些条件会连锁传播”，先看 [[state-constraint-reasoning]]
- 如果问题是“规则已有但没有执行”，先看 [[instruction-adherence]]
- 如果问题是“当前事项到底要不要做、做到哪算关闭”，先看 [[execution-contract-semantics]]
- 如果问题是“Harness 怎样从真实 episode 里自我修正”，先看 [[harness-evolution]] 和 [[harness-feedback-ledger]]
- 如果问题是“默认背景是什么”，先看 [[BRAIN]]

## 维护规则

- 先读 `INDEX.md` 和相关页面，再决定是否新建页面。
- 先读 [[BRAIN]]，把已经确认过的共享背景带入当前工作，不要让用户重复说明同一件事。
- 如果这次内容会改变规则、优先级或自动沉淀边界，先读 [[POLICY]]。
- 如果这次内容是项目级稳定事实，先读 `projects/memory/README.md`。
- 每一次有新的知识、材料、代码事实、会议结论或验收结果进入，都要从上层主题和全局方案重新思考它解决了哪些旧疑问、引出了哪些新问题、是否冲击已有需求 / 设计 / 决策 / 记忆 / 状态，并同步到对应主页面、风险、会议或决策页。
- 对外 API、调度入口、服务间回调、webhook、跨工程数据合同和数据库写入接口变更时，不能只沉淀在 handoff 或最终回复里；必须同步写入正式中文文档，handoff 只承接执行证据和临时问题。
- 做验收或复验时，必须先说明本轮验收对象、测试方案、核心用例 / 检查点、相关功能回归范围、分层验证结论和人工确认边界；缺少 `local validation`、`service-side validation` 或 `end-to-end validation` 中关键层级时，不能把局部通过写成完整闭环。
- 做验收或复验时，如果涉及请求参数、配置参数、profile、feature flag、限流值、采样数量、筛选条件或 retry context，不得只用默认值 happy path 或接口回显判定通过；至少验证一个非默认值 / 边界值，并证明它真实改变了执行结果。
- 研发事项默认主链是 `Gate -> FP -> EP -> TASK`；risk、issue、test、验收、报告和服务台账是关系节点。新增或关闭 Gate / FP / EP / TASK 时，必须补齐 `risk:`、`test:`、`验收:`、`issue-trigger:` 覆盖，不得把 issue-trigger 当成已发生 Issue。
- TASK 是父 EP 下的状态化交付合同；没有父 EP 的任务只能作为待关系校准候选，不能直接派发为正式编码任务。
- risk 是事前风险或待确认项；已发生 bug、偏差、验收失败或用户可见问题必须进入 [[projects/development/issues/README]]，并保留原始现象，不让日志、API 错误或推测根因改写问题陈述。
- 测试报告是验证证据，不是案件单一信息源。已发生问题的主档案在 Issue；报告必须回链 Issue / EP / TASK / FP / Gate，并写明本次证据能关闭哪一层、不能上推到哪一层。
- 代码工程或外部工程里的 agent 处理本库 TASK / EP / FP / Gate 时，默认把本库作为只读上下文源；TODO 只作轻量兼容视图。除非任务明确授权“受控回写”，否则不得直接改本库文档、改 TASK / EP 状态、关闭 Gate 或提交文档仓库。
- 本库侧 agent 默认不直接修改代码工程或子工程文件、handoff 或代码；除非用户明确授权修改该子工程，否则只在本库测试报告、TASK、父 EP、风险和最终回复中写清需要子工程吸收的证据与建议。
- 源码工程解读必须先使用 [[projects/codebase/source-code-audit-workflow]]，明确本次目标等级、实际达到等级、证据覆盖矩阵和未读 / 阻塞清单；没有完成 L3 自审时，不得暗示已经完成完整源码审计或已经可以做生产接入结论。
- 优先更新已有页，不要无脑新建重复页。
- 新页面先写最小可用版本，再补链接。
- 所有重要概念都要双向链接，避免孤岛页。
- 有长期价值的结论要回写到文档库，而不是只留在对话里。
- 过程性决定和修复动作要写进 `log.md`，并补上这次对话真正想解决的问题主题；关键动作不要压缩到失真。
- 写 `log.md` 时，同一天、同文件、同领域都不是自动合并理由；只有仍然属于同一条连续用户意图和同一段推进链，才允许并到同一条记录里。
- 写 `log.md` 的三级标题时，直接写一句话标题，不加前缀。
- 如果把几轮内容合并后，只能用“完善 `log`”“继续调整规则”这类过宽标题概括，说明已经合并过度，应拆回多条记录。
- `workspace-memory` 只记稳定偏好和重复习惯，不作为唯一规则源。
- [[BRAIN]] 是共享背景，承接跨多轮确认、会持续影响后续工作的共同背景。
- [[POLICY]] 是规则和优先级层，承接自动沉淀边界、冲突处理和路由约束。
- `projects/memory/README.md` 是项目级记忆入口，承接只对当前项目长期有效的事实。
- `projects/trace.md` 是项目演进链入口，承接需求从原始意图到当前实现的结构化收敛过程。
- 探索全新应用时，先判断是否仍是多方向探索；如果还没有明确选定当前项目，默认使用 `inbox/`、`raw/`、`articles/`、`concepts/` 轻量收集和比较，不为每个候选应用铺完整 `projects/` 结构。
- 当用户提出新系统、新工具、新应用、粗糙产品想法，或只给出“更智能 / 更前沿 / 更高效”这类质量目标时，先按 [[proactive-dialogue-system]] 自动判定场景包和置信度；高置信可带假设推进，中低置信只问会改变结构、权限、成本或验收的关键问题。
- 研发项目的阶段和状态由人读项目主页手动推进，不做隐藏自动流控。
- 活跃研发项目先读项目主页，再改需求、设计、决策、记忆、发布或运行记录。
- 极简小项目默认只保留一个项目主页，除非内容明显变多，否则不要先建空的需求、设计、发布之类页面。
- 下游项目反哺模板时，先按 [[template-feedback-rules]] 判断是否属于可复用系统层信息；回写结构、流程、规则、记忆路由、模板、通用写法和自动化契约，不复制项目事实、业务名、具体技术拍板或一次性状态。
- 模板反哺里的“规则默认反哺”指默认进入候选并必须判断，不表示原样写入；写入前必须完成抽象、事实剥离、冲突、单一信息源和规则体积检查。
- 听到“模板 / template / 模板化”时，先按 [[template-feedback-rules]] 判断它是知识库模板还是系统治理模板；知识库模板属于专题成果，优先落到 owning topic 或项目专题页，只有系统治理可复制骨架才进入 `templates/`。
- 下游项目出现可复用 agent 技能时，只吸收任务触发条件、事实源分层、定位方法、输出格式、回写守卫和禁止项；不要把下游项目的业务链路、服务名、数据表、运行 ID、仓库路径或本地 handoff 规则原样写入模板技能。
- 当用户要把本库已沉淀技能 / 能力升级到其他工程时，优先使用 [[skills/cross-project-skill-adoption-prompt/SKILL]] 生成提示词；高价值技能应补 `TRANSFER.md` 作为资料清单，而不是长期维护一份固定完整提示词。
- 跨项目采纳设计时，禁止整库同步、整目录复制或把对方项目设计页原样搬进当前库；必须先列候选项并标注系统层信息 / 项目材料，只有通过事实剥离后的系统规则、结构、流程、技能、模板和自动化契约才能写入。
- 如果具体工程或下游项目提供“不适合吸收”的清单，只把它当作下游处理项目材料和反哺边界的参考；当前库作为上游模板库，只从具体工程中抽象吸收系统层信息，不在本库维护模板到项目的吸收状态或项目侧同步记录。

## 会话级规则

- 每轮动手前先按 [[response-mode-routing]] 判断响应模式：快速诊断、引导式设计、图文呈现、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传或批处理。
- 当用户要看一份文档、一个主题、状态、风险、计划、决策、验收或知识材料，并强调直观、图文混排、一图胜千言、HTML 呈现或阅读不方便时，默认按 [[skills/problem-focused-visual-presentation/SKILL]] 进入图文呈现模式；不要把长文字摘要当作最终体验。
- 引导式设计不是轻模式例外；只要本轮形成用户意图、场景、范围、约束、风险、验收、候选决策、拆解关系或 agent 判断，就必须按 [[proactive-dialogue-system]] 做产物化落地判定。还不适合进正式项目链路时，使用 [[templates/guided-discovery-session-template]] 承接轻量 discovery。
- 只要本轮在处理搬家、旅行、办证、采购、部署、上线、签合同等计划型问题，且动作依赖权限、资源、时间窗或外部确认，就必须先按 [[state-constraint-reasoning]] 更新状态变量、做约束传播并判可执行性，再决定是否把动作写进计划。
- 如果用户指出“规则已有但没有执行”、或本轮发现提交、证据、验收边界、最终回复扫描等失守，必须按 [[instruction-adherence]] 判断该补触发器、模板字段、sensor、门禁还是最终证明，不得只追加一句更严厉的自然语言规则。
- 写入 TASK、issue、AP、EP、FP、Gate、报告目标包、handoff、状态页或会议行动项时，必须按 [[execution-contract-semantics]] 检查执行合同语义：当前裁决单值，非目标不展开成后续任务，参考规则不下沉到下层事项，证据层级不回流成普通修复闭环。
- 发现 `[[log]]`、产物化、完整检查、二阶反思、Goal Contract、模板反哺或入口同步开始变成无条件仪式时，先按 [[agent-governance-strategy]] 做资格判断；P0 防线保留，P1/P2/P3 不硬化成每轮必做。
- 快速诊断只默认读取入口规则和最相关的少量事实源；它可以给 `confirmed / likely / possible / blocked` checkpoint，但不能替代验收、关闭、准出、提交或规则升级。
- 如果根因已经形成而后续是在沉淀、验收、规则升级或收尾，必须显式告诉用户当前阶段，不要把治理闭环伪装成仍在分析。
- 当用户要求长时间持续推进、反复尝试、直到完成或跨多轮跟进时，先判断是否需要 Goal Contract；主控侧定义完成契约，子工程侧按契约回传证据，不用 Goal 自述替代验收关闭。
- 如果本轮出现用户纠偏、检查失败、模式切换、重复失守或明显可脚本化缺口，先判断是否写入 [[harness-feedback-ledger]]；单次 episode 不直接新增硬规则，按 [[harness-evolution]] 判断是否晋升为模板、sensor、技能或规则。
- 如果用户只要求“为什么 / 在哪 / 先分析”，默认不自动扩大成正式 issue、TASK、Gate 或状态回写；除非发现明确长期项目价值、用户授权沉淀，或当前规则要求必须沉淀。
- 复杂问题不要一次改完，先拆成几个中间节点，再逐步推进。
- 每个中间节点都要形成一个可理解、可回看、可提交的结果。
- 批量处理同类材料时，先判断这次是不是“批处理模式”，不要把单篇深度判断的读取负担机械复制到每一份材料上。
- 如果用户明确下达“收尾 / 执行收尾 / finalize”这类执行命令，本轮进入收尾模式；如果用户是在讨论收尾规则、排查收尾问题或询问怎么收尾，不进入收尾模式。
- 收尾模式禁止继续扩需求、追加新功能或顺手做下一轮结构调整；只允许完成与本轮已发生改动直接相关的同步、核对、补记和提交。
- 工作阶段按本轮范围优先跑专项 sensor，例如 `python3 scripts/check_all.py --only harness-governance`、`python3 scripts/check_all.py --only work-item-matrix`、`python3 scripts/check_all.py --only testing-system-maturity` 或 `python3 scripts/check_all.py --only execution-contract-semantics`；收尾或提交前跑完整 `python3 scripts/check_all.py`。
- 性能优化不能靠跳过关键语义边界实现。每轮先守性能预算：读取预算、问题预算、检查预算和产物大小预算。能用 1 到 3 个事实源判断时不扩读，能用专项 sensor 证明时不先跑全量，早期探索先写轻量 discovery，不为未定方向铺完整项目结构。
- 只要这次对话产生了实际内容变更或结构变更，保底在对话结束前做一次 commit，除非用户明确禁止或存在无法提交的例外。
- 只要这次对话产生了实际内容变更或结构变更，就必须按 [[agent-governance-strategy]] 和 [[log-writing-rules]] 做 log eligibility 判断：影响规则、结构、状态、决策、验收、跨工程边界或长期知识时写入 `[[log]]`；纯格式、错别字、无语义链接修复或临时本地状态可免写但要在收尾中说明。
- 如果这次改动会影响 `projects/trace.md` 的当前需求主题，就和相关页面同轮同步更新 trace，不要等其他文档都写完后再回来补。
- 维护 `log.md` 时，默认先判断“这是在续写上一条记录，还是已经进入新的对话意图”；不要因为它们发生在同一天，或都在改同一个页面，就压成单日总记录。
- 纯本地状态、临时草稿、界面缓存这类不影响文档内容和结构的变化，不要求 commit。
- 如果问题明显复杂，中间节点完成后就提交，不要把多个大变化混成一个 commit。
- commit 只包含同一主题的改动，不把无关内容打包进去。
- commit message 必须使用英文；正文、说明和文档内容仍然可以使用中文。
- 每次对话收尾前必须做一次二阶反思资格判断：本轮问题是否只是单点修补，还是暴露了同类漏检、流程缺口、模板缺口、协作契约缺口或记忆路由缺口；只有属于可复用教训、重复失守或 P0 风险时，才同轮回写到对应主入口。
- 二阶反思不是追加新需求；它只回答“这次为什么会错 / 为什么会漏 / 下次怎样提前发现同类问题”，并按 [[POLICY]] 判断写入 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、`templates/` 或 [[log]]。

### 收尾模式

- 收尾模式的目标是把当前轮已经完成的工作收口成一个可回看、可校验、可提交的结果，不负责继续推进下一轮开发。
- 进入收尾模式后，默认按这个顺序执行：确认本轮范围、检查受影响页面、补齐必要文档同步、做 log eligibility 判断、做一致性检查、做二阶反思资格判断、提交当前主题。
- 一致性检查至少覆盖：主入口是否已同步、内部链接是否可点击、受影响页面职责是否仍然清楚、`log.md` 是否按资格判断记录了本轮真实用户意图和关键动作，或明确属于免写。
- 二阶反思至少覆盖：同类问题是否会再次出现、是否需要补模板 / 入口 / 读取顺序 / 协作边界 / 自动沉淀边界、是否已有规则但没有执行、是否需要把旧规则改得更可执行。
- 如果这轮改动涉及规则、结构或入口页，收尾时只补与这轮 diff 直接相关的同步页，不扩大成整库巡检。
- 如果工作区里存在本轮未触及的预存脏改动，默认不把它们并入本次收尾或 commit，除非用户明确要求一起纳入。

### 批处理模式

- 当一次对话要连续处理大量同类型材料，而且目标主要是摘要、归类、补链接、回链或轻量整理时，可以进入批处理模式。
- 批处理模式只在这次工作不改规则、不改结构、不改项目阶段、不改项目级状态、不拍板冲突时使用。
- 进入批处理模式后，允许先完成一次全局校准，再在同批材料上复用这次校准结果；不要对每一份材料都重新全量读取同一批入口页。
- 只要某一份材料开始涉及规则、结构、项目状态、关键设计取舍或记忆路由，就退出批处理模式，回到默认读取路径。

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
- 会影响“哪些治理动作应硬化、哪些只做资格判断、哪些应降级或删除”的策略，进入 [[agent-governance-strategy]]，再由 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]] 和相关规则页保持短引用。
- 会影响“先轻后重”、首次反馈、读取预算和模式切换的响应效率规则，进入 [[response-mode-routing]]，再由 [[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]] 保持短引用。
- 会影响计划型问题里“先判状态与约束、再写动作”的默认方法，进入 [[state-constraint-reasoning]]，再由 [[AGENTS]]、[[WORKFLOW]]、[[response-mode-routing]] 和 [[proactive-dialogue-system]] 保持短引用。
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
- `projects/retrospectives/README.md` 上连项目主页、trace、决策、开发、事故、Issue、log 和复盘概念页；它承接具体复盘档案、跨复盘共性主题和沉淀路由，不替代事实主档案、决策页或行动项 owner 页面。
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
- 当项目里的某些结论已经脱离当前阶段、可以跨阶段或跨问题复用时，提升到 `articles/` 或 `concepts/`。
- 当某类 agent 分析动作在当前项目中反复出现，且需要项目语境、证据链、分工和验证格式保持稳定时，可以沉淀到 `skills/`。
- 当一个主题需要长期导航、分类和检索时，再由 `indexes/` 收口。
- 当页面不再承担当前入口职责但仍有历史价值时，转入 `archive/`，同时在 `log.md` 留痕。

## 结构变更同步规则

- 新增模块、目录、模板、入口页或高频文件类型时，必须在同一次变更里同步检查并更新 [[AGENTS]]、[[WORKFLOW]]，必要时更新 `README.md`。
- 新增项目层目录、执行流程、事项类型或高频页面时，必须同轮检查是否需要系统治理模板；缺的是可复制页面骨架才补 `templates/`，缺的是专题方法或报告结构则回到 owning topic，不允许把知识库模板误塞进 `templates/`。
- 如果新增内容涉及当前文档库和外部实现工程、代码仓库或子模块协作，必须同轮写清主控系统和实现工程的职责边界、交付物、回传格式、写权限模式和冲突升级路径；不能只写文档库内部流程。
- 如果新增内容改变了主入口、上下游关系、阶段映射、单一信息源或记忆路由，就必须同步更新对应章节，不允许以后再补。
- 如果新增内容只是一次性页面，不改变系统结构，可以不改上下文模型，但要确认它挂靠在哪个既有主入口之下。
- 任何结构性扩展都要在 `log.md` 留痕，说明它进入了哪一层、服务什么职责、和哪些页面产生关联。
- 写 `log.md` 时不要机械抄录问题清单；先下游处理这次对话的一个或多个主题，再提炼用户意图和关键动作。

## 读取顺序

- 写任何内容时都要先建立全局背景，不允许只盯着当前文件局部改写。
- 先判断这段内容在整个文档库里的位置：它服务哪个主题、哪个阶段、哪个主入口、哪类读者。
- 任何一段内容都不是孤立的，修改前必须先判断它的上游、下游和主入口。
- 默认先读 `README.md`、`INDEX.md`、相关目录的 `README.md`，再读目标文件本身。
- 默认把 [[BRAIN]] 当作共享背景读取入口之一，不要跳过。
- 默认先按 [[response-mode-routing]] 判定本轮读取深度；快速诊断只读最小事实源，状态关闭、规则升级、结构变更和跨工程沉淀必须升级到对应完整读取集。
- 如果目标涉及规则、优先级或自动沉淀边界，再读 [[POLICY]]。
- 如果目标涉及项目级稳定记忆，再读 `projects/memory/README.md`。
- 如果目标在 `projects/`，先读 `projects/README.md` 和 `projects/STRUCTURE.md`，再读相关的需求、设计、会议、决策、记忆、开发页面。
- 如果目标是服务实例台账或服务运行事实，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/service-registry.md`、`projects/design/deployment.md`，再按服务补读相关代码基线、开发执行、测试报告或事故页。
- 如果目标在 `projects/codebase/`，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/codebase/README.md`、`projects/requirements.md`、`projects/design/README.md` 和 `projects/decisions.md`，再读对应代码基线子页。
- 如果目标在 `projects/meetings/`，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/meetings/README.md`、`projects/meetings/worklog.md`，再读相关的需求、决策、开发和记忆页面；如果会议涉及未决设计专题，再补读 `projects/design/topics/README.md` 和对应专题页。
- 如果目标在 `projects/retrospectives/`，先读 `projects/README.md`、`projects/STRUCTURE.md`、`projects/retrospectives/README.md`、[[concepts/project-retrospective]]，再按对象补读 trace、决策、开发、Issue、事故、会议、log、Agent 复盘或软件研发复盘相关页面。
- 启动复盘体系时，先判断是轻量 checkpoint、标准复盘还是深度复盘；具体档案进入 `projects/retrospectives/`，行动项必须分流到已有 Issue / 事故、事项、会议、决策、memory、trace、模板、skill、sensor 或规则入口，不在复盘目录形成平行看板。
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

## 冲突升级

- 如果新需求和 [[BRAIN]]、[[POLICY]]、[[AGENTS]]、`projects/STRUCTURE.md` 或既有项目决策发生碰撞，不要直接覆盖旧结论。
- 在项目阶段，先升级到 `projects/decisions.md`，形成明确决策后，再同步更新相关页面。
- 没有形成决策前，不把冲突内容直接写入共享脑或规则层。

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
- 改复盘页时，至少读：`projects/README.md`、`projects/STRUCTURE.md`、`projects/retrospectives/README.md`、[[concepts/project-retrospective]]；软件研发复盘补读 [[concepts/software-development-project-retrospective]]，Agent 工作复盘补读 [[concepts/agent-work-retrospective]] 和对应 skill，事故 / Issue 后复盘补读事实主档案。
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

- 同一文档库内的页面跳转，默认优先使用 `[[wikilink]]`，不要再写成本机绝对路径。
- 仓库内文档之间的引用，默认统一使用 `[[wikilink]]`，不要再保留 `[xxx](./foo.md)`、`[xxx](../bar.md)`、`[xxx](foo.md)` 这类指向本库内页面的 Markdown 链接。
- 只要语义上是在引用本库页面、模板页、入口页或跳转目标，就必须使用 `[[wikilink]]`；不要写成反引号文件名、裸文件名或纯文本路径。
- 只有在说明命令、环境变量、工作区位置时，才提“当前工作区”这类概念；不要把本机用户名和绝对目录写进长期文档。
- 外部网站、官方文档、仓库地址这类外部资源，继续使用普通 Markdown 链接。
- 如果一个页面只是作为导航入口出现，优先用 `[[wikilink]]`；如果需要附带解释，可以在链接后补一句说明，不复制整段内容。
- 页内引用如果指向本库的标题、区块或子页面，也优先使用 Obsidian 可解析的 `[[page#heading]]`、`[[page#^block-id]]`、`[[page|alias]]`，不要混回 `.md#heading` 形式。
- 当语义上是在引用本库内页面本身、入口职责或跳转目标时，优先直接写成 `[[wikilink]]`，不要写成 [[BRAIN]]、[[POLICY]]、`log.md` 这类裸文件名。
- 不允许保留空链接、占位链接、缺失目标的半成品引用；发现 `[]()`、`[text](#)`、只剩文本没有目标的引用时，必须在交付前修正或删除。
- 只要本次处理新增或修改了 Markdown 引用，就必须顺手修正同一文件内发现的错误引用，不把坏格式留给下一轮。
- 交付前必须回看引用格式是否满足这组约束；引用格式不合规，视为结果未完成。
- 如果本次改动涉及模板页、模板入口或内部链接，交付前必须额外检查两件事：有没有复制出第二份模板正文；有没有把本库页面写成不可点击的文件名字符串。

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

## 规则治理

- 新规则只在跨多次对话稳定成立、且能明显减少混乱时才新增。
- 能修改现有规则解决的问题，不新增平行规则。
- `README.md` 保持短入口，[[WORKFLOW]] 保持唯一流程，[[AGENTS]] 保持硬约束，避免同一规则散落三处。
- 如果规则开始变重，优先压缩、合并、改写旧规则，不继续堆叠新章节。

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

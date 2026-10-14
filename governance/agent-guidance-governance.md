# 规则演进与跨工程边界

本页是 [[AGENTS]] 按需加载的唯一条件正文；只读取与当前任务相关的章节。

## 治理层边界

- [[POLICY]]：规则裁定层。回答“什么允许自动晋升、什么必须人工确认、冲突时先按谁”
- [[AGENTS]]：执行约束层。回答“agent 修改时必须怎么做”
- [[WORKFLOW]]：流程编排层。回答“通常按什么顺序推进”
- [[response-mode-routing]]：响应效率路由层。回答“本轮先快诊断、沉淀、验收、实现还是升级规则”
- [[proactive-dialogue-system]]：主动对话与引导式设计层。回答“目标不完整时，agent 怎么自动判定场景、少量提问、带假设推进并产物化”
- [[agent-governance-strategy]]：Agent 治理分级层。回答“哪些规则是 P0 硬约束，哪些只是 P1/P2/P3 语义门、流程默认或 backlog”
- [[state-constraint-reasoning]]：状态约束推理层。回答“当前权限、远程、预算、证据和人工确认状态允许做什么”
- [[agent-orchestration]]：Agent 编排层。回答“Goal、Run Capsule、Orchestrator、Worker、Evaluator、子工程 Git preflight 和沉淀路由怎么分工”
- [[agent-system-maturity]]：Agent System Maturity 层。回答“agent system 七层对象、智能化证据、外部 evaluator 识别和 Goodhart 边界怎么分开判断”
- [[instruction-adherence]]：指令遵循层。回答“已有规则怎样升级成触发器、模板字段、sensor、门禁和最终证明”
- [[execution-contract-semantics]]：执行合同语义层。回答“当前执行合同是否被参考规则、非目标或上层证据污染”
- [[harness-evolution]]：Harness 自演进层。回答“用户纠偏、检查失败、模式切换和重复失守如何形成 episode，并何时晋升为 sensor、模板、技能或规则”
- [[harness-feedback-ledger]]：Harness episode 台账。回答“哪些 episode 已观察、已晋升、待补 sensor 或待降级”
- [[BRAIN]]：共享背景层。回答“哪些已确认前提要自动带入后续工作”

判断时优先用这条：

- 如果问题是“怎么判”，先看 [[POLICY]]
- 如果问题是“怎么执行”，先看 [[AGENTS]]
- 如果问题是“怎么推进”，先看 [[WORKFLOW]]
- 如果问题是“要不要先轻量诊断、何时进入重治理”，先看 [[response-mode-routing]]
- 如果问题是“用户只有粗糙目标、需要把想法想完整或要更智能地推进”，先看 [[proactive-dialogue-system]]
- 如果问题是“治理动作是否过重、规则该升级还是降级”，先看 [[agent-governance-strategy]]
- 如果问题是“当前状态是否允许执行、提交、推送、发布或关闭”，先看 [[state-constraint-reasoning]]
- 如果问题是“多 agent、子工程、Worker / Evaluator 如何分工”，先看 [[agent-orchestration]]
- 如果问题是“规则已有但没有执行”，先看 [[instruction-adherence]]
- 如果问题是“当前事项到底要不要做、做到哪算关闭”，先看 [[execution-contract-semantics]]
- 如果问题是“Harness 怎样从真实 episode 里自我修正”，先看 [[harness-evolution]] 和 [[harness-feedback-ledger]]
- 如果问题是“默认背景是什么”，先看 [[BRAIN]]

## 维护规则

- 用 `INDEX.md` 与当前 owner 定位；已加载且未变化时复用，再决定是否新建页面。
- 复用 [[BRAIN]] 中已加载且未变化的共享背景；缺口决定补读，不让用户重复说明同一件事。
- 如果这次内容会改变规则、优先级或自动沉淀边界，先读 [[POLICY]]。
- 如果这次内容是项目级稳定事实，先读 `projects/memory/README.md`。
- 每一次有新的知识、材料、代码事实、会议结论或验收结果进入，都要从上层主题和全局方案重新思考它解决了哪些旧疑问、引出了哪些新问题、是否冲击已有需求 / 设计 / 决策 / 记忆 / 状态，并同步到对应主页面、风险、会议或决策页。
- 对外 API、调度入口、服务间回调、webhook、跨工程数据合同和数据库写入接口变更时，不能只沉淀在 handoff 或最终回复里；必须同步写入正式中文文档，handoff 只承接执行证据和临时问题。
- 做验收或复验时，必须先说明本轮验收对象、测试方案、核心用例 / 检查点、相关功能回归范围、分层验证结论和人工确认边界；缺少 `local validation`、`service-side validation` 或 `end-to-end validation` 中关键层级时，不能把局部通过写成完整闭环。
- 做验收或复验时，如果涉及请求参数、配置参数、profile、feature flag、限流值、采样数量、筛选条件或 retry context，不得只用默认值 happy path 或接口回显判定通过；至少验证一个非默认值 / 边界值，并证明它真实改变了执行结果。
- 研发事项默认主链是 `Gate -> FP -> EP -> TASK`；risk、issue、test、验收、报告和服务台账是关系节点。新增或关闭 Gate / FP / EP / TASK 时，按阶段补齐或引用父项的 `risk:`、`test:`、`验收:`、`issue-trigger:` 覆盖，不得把 issue-trigger 当成已发生 Issue。
- 当前 wiki 的研发事项自动拆解使用 [[skills/work-item-auto-decomposition/SKILL]]；它是项目 / 领域绑定能力，必须绑定本仓事项模型、模板、sensor 和不上推边界，不硬升为所有工程通用 skill。
- TASK 是父 EP 下的状态化交付合同；没有父 EP 的任务只能作为待关系校准候选，不能直接派发为正式编码任务。
- risk 是事前风险或待确认项；已发生 bug、偏差、验收失败或用户可见问题必须进入 [[projects/development/issues/README]]，并保留原始现象，不让日志、API 错误或推测根因改写问题陈述。
- 测试报告是验证证据，不是案件单一信息源。已发生问题的主档案在 Issue；报告必须回链 Issue / EP / TASK / FP / Gate，并写明本次证据能关闭哪一层、不能上推到哪一层。
- 复盘是长期学习工程，不替代 [[log]]、Issue、事故、报告、handoff、ledger、决策、memory 或 trace。测试报告通过、Issue 关闭或事故修复都不能自动等价为复盘完成；只有当目标、事实、偏差、原因、保留做法、改进行动和沉淀路由形成可复用学习资产时，才进入 [[projects/retrospectives/README]]。
- 复盘体系统一入口是 [[skills/retrospective-capability/SKILL]]；项目交付 / 软件研发链复盘使用 [[skills/delivery-retrospective/SKILL]]，历史对话 / Agent 工作流复盘使用 [[skills/historical-dialogue-retrospective/SKILL]]。不要把这些子项平铺成互相竞争的入口。
- 用户显式要求“复盘 / 写复盘 / 沉淀复盘 / 总结教训”时，默认标准复盘并落档到 `projects/retrospectives/<year>/`；显式要求“深度 / 完整 / 全面复盘”时，进入深度复盘，必须纳入首轮目标、用户纠偏序列、原始 session / rollout 证据计划、git / 检查输出、产物即档案和上层抽象。自动触发的 `no-op / 轻量 checkpoint` 不能降级显式复盘请求。标准 / 深度复盘必须同步 [[projects/retrospectives/indexes/by-year]]，稳定主题或类型再同步主题 / 类型索引。
- 代码工程或外部工程里的 agent 处理本库 TASK / EP / FP / Gate 时，默认把本库作为只读上下文源；TODO 只作轻量兼容视图。除非任务明确授权“受控回写”，否则不得直接改本库文档、改 TASK / EP 状态、关闭 Gate 或提交文档仓库。
- 本库侧 agent 默认不直接修改代码工程或子工程文件、handoff 或代码；除非用户明确授权修改该子工程，否则只在本库测试报告、TASK、父 EP、风险和最终回复中写清需要子工程吸收的证据与建议。
- 源码工程解读必须先使用 [[projects/codebase/source-code-audit-workflow]]，明确本次目标等级、实际达到等级、证据覆盖矩阵和未读 / 阻塞清单；没有完成 L3 自审时，不得暗示已经完成完整源码审计或已经可以做生产接入结论。
- 优先更新已有页，不要无脑新建重复页。
- 新页面先写最小可用版本，再补链接。
- 所有重要概念都要双向链接，避免孤岛页。
- 有长期价值的结论要回写到文档库，而不是只留在对话里。
- 本仓是公开可见仓库。任何 tracked 写入在落盘前都必须通过 [[wiki-governance-system-contract.v1#公开仓库持久化边界]]：公司 / 内部工程的名称、路径、registry 明细、业务事实、服务拓扑、机器、账号、端口、运行 ID、内部 URL、一次性 handoff 和未公开个人信息，不得写入本仓任何 tracked 文件，包括 `log.md`、报告、trace、decision、ledger、view source pack、脚本常量和示例。跨工程吸收只能持久化为去标识的 source archetype、capability pack、抽象规则和不上推边界；原始证据留在对应私有 owner。`raw/` 可以保留经用户确认可公开的外部网页抓取，但不是公司 / 私有材料的例外通道。
- 过程性决定和修复动作要写进 `log.md`，并补上这次对话真正想解决的问题主题；关键动作不要压缩到失真。
- `log.md` 的“真实用户意图”只保留公开安全的结果导向摘要；如果原始意图含公司工程、私有路径或内部运行事实，必须去标识后再写，不得以“历史记录”“受控 provenance”或“完整回看”为理由保留原文。
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
- 当规则、模板、sensor、log、复盘或 Goal 看起来可能被过度使用时，先按 [[agent-governance-strategy]] 做 P0 / P1 / P2 / P3 分级；不要把一次偏差直接升级成硬规则。
- 当行动依赖权限、远程状态、dirty / diverged 工作区、浏览器 profile、外部服务、预算或人工确认时，先按 [[state-constraint-reasoning]] 判断 `executable / conditional / blocked / ask-human`，再写计划或执行。
- 研发项目的阶段和状态由人读项目主页手动推进，不做隐藏自动流控。
- 活跃研发项目先读项目主页，再改需求、设计、决策、记忆、发布或运行记录。
- 极简小项目默认只保留一个项目主页，除非内容明显变多，否则不要先建空的需求、设计、发布之类页面。
- 下游项目反哺模板时，先按 [[template-feedback-rules]] 判断是否属于可复用系统层信息；回写结构、流程、规则、记忆路由、模板、通用写法和自动化契约，不复制项目事实、业务名、具体技术拍板或一次性状态。
- 模板反哺里的“规则默认反哺”指默认进入候选并必须判断，不表示原样写入；写入前必须完成抽象、事实剥离、冲突、单一信息源和规则体积检查。
- 下游项目出现可复用 agent 技能时，只吸收任务触发条件、事实源分层、定位方法、输出格式、回写守卫和禁止项；不要把下游项目的业务链路、服务名、数据表、运行 ID、仓库路径或本地 handoff 规则原样写入模板技能。
- 跨工程通用技能吸收、矩阵缺口处理或外部附件建议吸收时，先使用 [[skills/transferable-skill-governance/SKILL]] 判定 `true-gap / recognition-gap / signal-only-gap` 和 `recognize / complete / upgrade / merge / adapt / defer / reject`，再决定是否写入 skill、TRANSFER、template、governance、sensor 或 views。
- 跨工程读取或吸收任务在写入前必须运行 `python3 scripts/check_all.py --only public-repository-content`；检查通过只证明机器可识别的路径、内部地址、其他工程公开 host 和本地 deny terms 未泄漏，源工程身份是否已充分去标识仍需人工语义复核。
- 当目标是 Agent System Capability Package、agent-system maturity 或 intelligence maturity 时，先使用 [[agent-system-maturity]] 填写 Matrix Recognition Capsule；skill maturity 高分不能上推成 runtime、memory、evaluation、governance、migration 或 intelligence 高分。
- 当前 wiki 的目标角色是实现类工程合集与模板；主控、子工程、runtime service、数据 / 模型工程或文档治理工程接入时，先使用 [[projects/design/topics/implementation-engineering-template-system]] 和 [[templates/implementation-project-profile-template]]，写清 project_role、owner surfaces、agent system layers、control plane、implementation boundaries、evidence contract、Template Adoption 和 Closeout Proof。对应检查是 `python3 scripts/check_all.py --only implementation-template-system`。
- 跨项目采纳设计时，禁止整库同步、整目录复制或把对方项目设计页原样搬进当前库；必须先列候选项并标注系统层信息 / 项目材料，只有通过事实剥离后的系统规则、结构、流程、技能、模板和自动化契约才能写入。
- 如果具体工程或下游项目提供“不适合吸收”的清单，只把它当作下游处理项目材料和反哺边界的参考；当前库作为上游模板库，只从具体工程中抽象吸收系统层信息，不在本库维护模板到项目的吸收状态或项目侧同步记录。
- 升级 agent 规则、治理层、memory、workflow、skill、harness、evaluator、sensor、template 或 agent 入口默认行为时，先判本地是否存在 AcknowledgeBase，再判 `acknowledge_topic_update_required` 和 `upstream_write_authorization`：如果本机存在 AcknowledgeBase，则对应 topic 必须 `updated` 才算闭环；`rejected / deferred` 只能说明本次上游吸收被明确裁决，不能替代闭环。只有用户或 Run Capsule / dispatch 明确授权上游写入，且 allowed write roots 包含 AcknowledgeBase owner 时，才可受控直编 AcknowledgeBase；本仓普通运行即使本机能访问 AcknowledgeBase，也只能保留本仓库项目事实、handoff、验证证据和 conformance，并产出 system-layer extraction / handback。handback 必须写清 owner discovery、system-layer delta、本地 conformance、验证证据、禁止项、不上推边界，以及 `design-owner: existing / deferred / not-applicable`；handback 只是 pending / blocked 证据，不是完成态；不得把本仓事实写进 AcknowledgeBase 或用户级 `~/.codex/AGENTS.md`。
- 有实际沉淀信号时给出 Persistence Decision：`artifact-needed / no-op / blocked`。仅实际可复用的方法、结构变化或未来任务知识记录 owner、landing path、发现入口与证据；未触发时不要求 `no-op`，真正阻塞时保留恢复条件。

## 结构变更同步规则

- 新增模块、目录、模板、入口页或高频文件类型时，必须在同一次变更里同步检查并更新 [[AGENTS]]、[[WORKFLOW]]，必要时更新 `README.md`。
- 新增项目层目录、执行流程、事项类型或高频页面时，必须同轮检查 `templates/` 是否已有对应可复制骨架；缺模板就补模板，已有模板就确认入口链接和唯一正文，不允许只补目录和规则正文。
- 如果新增内容涉及当前文档库和外部实现工程、代码仓库或子模块协作，必须同轮写清主控系统和实现工程的职责边界、交付物、回传格式、写权限模式和冲突升级路径；不能只写文档库内部流程。
- 如果新增内容改变了主入口、上下游关系、阶段映射、单一信息源或记忆路由，就必须同步更新对应章节，不允许以后再补。
- 如果新增内容只是一次性页面，不改变系统结构，可以不改上下文模型，但要确认它挂靠在哪个既有主入口之下。
- 任何结构性扩展都要在 `log.md` 留痕，说明它进入了哪一层、服务什么职责、和哪些页面产生关联。
- 写 `log.md` 时不要机械抄录问题清单；先下游处理这次对话的一个或多个主题，再提炼用户意图和关键动作。

## 冲突升级

- 如果新需求和 [[BRAIN]]、[[POLICY]]、[[AGENTS]]、`projects/STRUCTURE.md` 或既有项目决策发生碰撞，不要直接覆盖旧结论。
- 在项目阶段，先升级到 `projects/decisions.md`，形成明确决策后，再同步更新相关页面。
- 没有形成决策前，不把冲突内容直接写入共享脑或规则层。

## 规则治理

- 新规则只在跨多次对话稳定成立、且能明显减少混乱时才新增。
- 能修改现有规则解决的问题，不新增平行规则。
- `README.md` 保持短入口，[[WORKFLOW]] 保持唯一流程，[[AGENTS]] 保持硬约束，避免同一规则散落三处。
- 如果规则开始变重，优先压缩、合并、改写旧规则，不继续堆叠新章节。

## 条件检查入口

- 全面治理整改读取 [[wiki-governance-system-contract.v1]]，用 `governance-system-rectification` 检查；source topic 采纳读取 [[acknowledgebase-topic-system-adoption.v1]]，用 `acknowledge-topic-adoption` 检查。
- 模板接入读取 [[projects/design/topics/implementation-engineering-template-system|工程模板设计]] 与 [[templates/implementation-project-profile-template|工程接入配置]]，使用 `implementation-template-system`。
- Agent System Capability Package 读取 [[agent-system-maturity]]，使用 `agent-system-maturity`；当前 wiki 的事项拆解使用 [[skills/work-item-auto-decomposition/SKILL]]。
- 本仓公开可见，去标识边界见 [[wiki-governance-system-contract.v1]]；`public-repository-content` 仅证明结构检查，不能代替语义复核。

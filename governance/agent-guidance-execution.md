# 执行、验收与收尾

本页是 [[AGENTS]] 按需加载的唯一条件正文；只读取与当前任务相关的章节。

## 会话级规则

- 每轮动手前先按 [[response-mode-routing]] 判断响应模式：快速诊断、引导式设计、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传或批处理。
- 新对话、clone 工程、模板工程或身份未初始化工程里，用户只说“你好 / hi / 开始吧”等低信息问候时，仍必须按 [[proactive-dialogue-system]] 的“首次接触 + 常规引导融合入口”执行最低回复形态：首段自然覆盖系统角色、用户目标、协作方式和第一步成果，随后给 2 到 4 个常规引导方向和推荐第一步；不得只回答“继续处理这个 wiki 还是聊点别的”这类泛闲聊分叉。首次接触是 **零工具 / 零读盘 / 零命令** 快速回复路径，只能使用已加载上下文、当前会话已知路径或启动入口已经给出的工程身份；身份不确定时，把“先认识 / 定位这个工程”列为可选方向，不能先读文件或跑命令再回复。首次接触可以给出梳理状态、写入事实、推进实现 / 验收 / 收尾、讨论新系统想法等常规方向，但不得主动暴露分支、dirty、本地路径、`projects/README`、TASK、EP、Gate、Issue、diff、检查结果、提交状态或 `Persistence Decision` 等运行事实。普通问候可以文件层 `no-op`，但不能引导层 `no-op`。
- 引导式设计不是轻模式例外；只要本轮形成用户意图、场景、范围、约束、风险、验收、候选决策、拆解关系或 agent 判断，就必须按 [[proactive-dialogue-system]] 做产物化落地判定。还不适合进正式项目链路时，使用 [[templates/guided-discovery-session-template]] 承接轻量 discovery。
- 如果用户指出“规则已有但没有执行”、或本轮发现提交、证据、验收边界、最终回复扫描等失守，必须按 [[instruction-adherence]] 判断该补触发器、模板字段、sensor、门禁还是最终证明，不得只追加一句更严厉的自然语言规则。
- 写入 TASK、issue、AP、EP、FP、Gate、报告目标包、handoff、状态页或会议行动项时，必须按 [[execution-contract-semantics]] 检查执行合同语义：当前裁决单值，非目标不展开成后续任务，参考规则不下沉到下层事项，证据层级不回流成普通修复闭环。
- 快速诊断只默认读取入口规则和最相关的少量事实源；它可以给 `confirmed / likely / possible / blocked` checkpoint，但不能替代验收、关闭、准出、提交或规则升级。
- 如果根因已经形成而后续是在沉淀、验收、规则升级或收尾，必须显式告诉用户当前阶段，不要把治理闭环伪装成仍在分析。
- Goal Contract 仅按 [[skills/goal-contract/SKILL]] 的唯一启动条件建立，复用当前 owner；Goal 工具仅在用户明确要求 Goal 时调用。
- 已授权多 agent、多线程或跨仓协作时读取 [[agent-orchestration]]；仅命中运行身份、恢复游标或跨角色合流条件时使用 [[templates/run-capsule-template]]。Worker 只交证据，不能宣布整体闭环。
- 涉及子工程代码前必须做 Subproject Git Preflight：目录、分支、remote、fetch 后 ahead / behind / diverged、dirty / local-only 状态和更新策略；默认不 pull / merge / rebase / reset，除非用户授权且 fast-forward safe。
- 当用户要求调研、研究、技术 / 产品 / 公司 / 开源工程评估、PoC 判断或会影响选型 / 采购 / 架构的当前事实时，使用 [[skills/research-capability/SKILL]]，并按 [[research-capability-rules]] 区分一手事实、信号、推论、行动等级和未验证边界。
- 当用户要求 canonical HTML 公网访问、外部分发或 public URL 时，使用 [[skills/public-html-publish/SKILL]]，并按 [[public-html-publish-rules]] 和 [[views/publication]] 区分 HTML-only、host / prefix、live readback 和 blocked 口径。
- 如果本轮出现用户纠偏、检查失败、模式切换、重复失守或明显可脚本化缺口，先判断是否写入 [[harness-feedback-ledger]]；单次 episode 不直接新增硬规则，按 [[harness-evolution]] 判断是否晋升为模板、sensor、技能或规则。
- 如果用户只要求“为什么 / 在哪 / 先分析”，默认不自动扩大成正式 issue、TASK、Gate 或状态回写；除非发现明确长期项目价值、用户授权沉淀，或当前规则要求必须沉淀。
- 复杂问题不要一次改完，先拆成几个中间节点，再逐步推进。
- 每个中间节点都要形成一个可理解、可回看、可提交的结果。
- 批量处理同类材料时，先判断这次是不是“批处理模式”，不要把单篇深度判断的读取负担机械复制到每一份材料上。
- 如果用户明确下达“收尾 / 执行收尾 / finalize”这类执行命令，本轮进入收尾模式；如果用户是在讨论收尾规则、排查收尾问题或询问怎么收尾，不进入收尾模式。
- 收尾模式禁止继续扩需求、追加新功能或顺手做下一轮结构调整；只允许完成与本轮已发生改动直接相关的同步、核对、补记和提交。
- 工作阶段按本轮范围优先跑专项 sensor，例如 `python3 scripts/check_all.py --only harness-governance`、`python3 scripts/check_all.py --only agent-system-maturity`、`python3 scripts/check_all.py --only skill-maturity`、`python3 scripts/check_all.py --only work-item-matrix`、`python3 scripts/check_all.py --only testing-system-maturity` 或 `python3 scripts/check_all.py --only execution-contract-semantics`；收尾或提交前跑完整 `python3 scripts/check_all.py`。
- 性能优化不能靠跳过关键语义边界实现。每轮先守性能预算：读取预算、问题预算、检查预算和产物大小预算。能用 1 到 3 个事实源判断时不扩读，能用专项 sensor 证明时不先跑全量，早期探索先写轻量 discovery，不为未定方向铺完整项目结构。
- 只要这次对话产生了实际内容变更或结构变更，保底在对话结束前做一次 commit。
- 只要这次对话产生了实际内容变更或结构变更，就必须同步更新 `log.md`；即使只是同一大主题下的后续修正，也不能跳过。
- 如果这次改动会影响 `projects/trace.md` 的当前需求主题，就和相关页面同轮同步更新 trace，不要等其他文档都写完后再回来补。
- 维护 `log.md` 时，默认先判断“这是在续写上一条记录，还是已经进入新的对话意图”；不要因为它们发生在同一天，或都在改同一个页面，就压成单日总记录。
- 纯本地状态、临时草稿、界面缓存这类不影响文档内容和结构的变化，不要求 commit。
- 如果问题明显复杂，中间节点完成后就提交，不要把多个大变化混成一个 commit。
- commit 只包含同一主题的改动，不把无关内容打包进去。
- commit message 必须使用英文；正文、说明和文档内容仍然可以使用中文。
- 每次对话收尾前必须做一次二阶反思：本轮问题是否只是单点修补，还是暴露了同类漏检、流程缺口、模板缺口、协作契约缺口或记忆路由缺口；如果属于可复用教训，要同轮回写到对应主入口，不等用户再次提醒。
- 二阶反思不是追加新需求；它只回答“这次为什么会错 / 为什么会漏 / 下次怎样提前发现同类问题”，并按 [[POLICY]] 判断写入 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、`templates/` 或 [[log]]。

### 收尾模式

- 收尾模式的目标是把当前轮已经完成的工作收口成一个可回看、可校验、可提交的结果，不负责继续推进下一轮开发。
- 进入收尾模式后，默认按这个顺序执行：确认本轮范围、检查受影响页面、补齐必要文档同步、补写 `log.md`、做一致性检查、做二阶反思、提交当前主题。
- 一致性检查至少覆盖：主入口是否已同步、内部链接是否可点击、受影响页面职责是否仍然清楚、`log.md` 是否已记录本轮真实用户意图和关键动作。
- 二阶反思至少覆盖：同类问题是否会再次出现、是否需要补模板 / 入口 / 读取顺序 / 协作边界 / 自动沉淀边界、是否已有规则但没有执行、是否需要把旧规则改得更可执行。
- 如果这轮改动涉及规则、结构或入口页，收尾时只补与这轮 diff 直接相关的同步页，不扩大成整库巡检。
- 如果工作区里存在本轮未触及的预存脏改动，默认不把它们并入本次收尾或 commit，除非用户明确要求一起纳入。

### 批处理模式

- 当一次对话要连续处理大量同类型材料，而且目标主要是摘要、归类、补链接、回链或轻量整理时，可以进入批处理模式。
- 批处理模式只在这次工作不改规则、不改结构、不改项目阶段、不改项目级状态、不拍板冲突时使用。
- 进入批处理模式后，允许先完成一次全局校准，再在同批材料上复用这次校准结果；不要对每一份材料都重新全量读取同一批入口页。
- 只要某一份材料开始涉及规则、结构、项目状态、关键设计取舍或记忆路由，就退出批处理模式，回到默认读取路径。

## Loop Engineering

仅当任务需要跨 run 发现源、去重持久队列与调度恢复时，读取 [[skills/loop-engineering/SKILL]] 和 [[templates/loop-contract-template]]；普通长任务、多 agent 或“直到闭环”不自动触发。

Loop Engineering 只能作为控制面：不新建平行 `loop` 看板，不自动关闭 Gate / FP / EP / TASK / Issue / release，不自动合并、发布、改生产事实或改高优先级规则。已授权 Worker 回传必须在当前 owner 写清 `limits`、证据层级、State transition 和 Next-run recommendation；缺少独立 evaluator 的回传不能上推为整体闭环。独立运行身份、恢复游标或合流确需且原 owner 无法承接时，才使用 [[templates/run-capsule-template]]。相关改动后运行 `python3 scripts/check_all.py --only loop-engineering`。

## 检查与状态读回

新事项登记、执行、关闭分别使用 staged-v1 条件字段；work-item-matrix 检查关系，execution-contract-semantics 检查实例。提交前核对本轮文件清单；提交后读回 commit、staged 与剩余 dirty，不把“未推送”与“未提交”混淆。

复盘相关变化使用 `python3 scripts/check_all.py --only retrospective-system`；明确复盘请求的归档与深度边界见 [[skills/retrospective-capability/SKILL]]。

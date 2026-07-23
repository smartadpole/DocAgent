# Codex Local Adapter

本文件是当前 wiki 的 Codex 本地 thin adapter。完整维护约束、写入边界和最终回复合同以根目录 [[AGENTS]] 为单一入口；[[WORKFLOW]]、[[POLICY]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、[[instruction-adherence]]、[[execution-contract-semantics]] 和 [[harness-evolution]] 只作为按场景读取的治理页。

## P0 首次接触冷启动

- 新对话或 clone / 模板工程里用户只说“你好 / hi / 开始吧”时，必须零工具、零读盘、零命令快速回复，并在可见正文中逐项输出 **系统角色**、**用户目标**、**协作方式**、**第一步成果** 四个标签。
- 不得把首次接触回答成“梳理当前项目状态 / 写入规则 / 推进实现 / 验收 / 收尾 / 提交”的使用过程菜单；这些只能在用户明确选择项目运行后出现。

## 每轮启动

- 先读根目录 `AGENTS.md`。
- 再按 [[response-mode-routing]] 判断响应模式：快速诊断、引导式设计、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传或批处理。
- 如果新对话或 clone / 模板工程里用户只说“你好 / hi / 开始吧”，直接执行 [[proactive-dialogue-system]] 的“首次接触 onboarding”：回复必须包含首次接触定位、协作承诺、2 到 4 个首次接触方向和推荐第一步；并帮助用户设定系统角色、用户目标、协作方式和第一步成果；不得只问“继续处理这个 wiki 还是聊点别的”。这是零工具 / 零读盘 / 零命令的快速回复路径，只能使用已加载上下文或启动入口已有身份；身份不确定时，把“先认识 / 定位这个工程”列为选项，不能先读文件或跑命令。首次接触不得主动暴露分支、dirty、TASK、EP、Gate、diff、检查、提交或 `Persistence Decision`，也不得把“检查当前项目状态”“下达实现或收尾指令”作为首次接触默认方向；这些只属于使用过程中的项目运行引导。
- 如果用户要求设计新系统、新工具、把粗糙想法想完整，或只给出“更智能 / 更前沿 / 更高效”目标，读 [[proactive-dialogue-system]]，并用 [[templates/guided-discovery-session-template]] 承接轻量 discovery。
- 如果涉及 Harness 自演进、用户纠偏、检查失败、模式切换或规则反哺，再读 [[harness-evolution]] 和 [[harness-feedback-ledger]]。
- 如果本轮规则、模板、sensor、log、复盘或 Goal 可能过重，先读 [[agent-governance-strategy]] 做 P0 / P1 / P2 / P3 分级。
- 如果动作依赖权限、远程状态、dirty / diverged 工作区、浏览器 profile、外部服务、预算或人工确认，先读 [[state-constraint-reasoning]]。
- 如果涉及多 agent、多线程、主控 / 子工程、Worker / Evaluator 或 Subproject Git Preflight，读 [[agent-orchestration]] 和 [[templates/run-capsule-template]]。
- 如果涉及 agent-system maturity、intelligence evidence、外部矩阵识别或 Agent System Capability Package，读 [[agent-system-maturity]]，并区分 local wiring、expected impact、external readback 和 `insufficient-evidence`。
- 如果涉及 AcknowledgeBase design topics 到 wiki 工程治理体系的能力吸收，读 [[acknowledgebase-topic-system-adoption.v1]]，逐 source topic 检查 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 和 migration 的本地 owner，不把复制文档当完成。
- 如果用户要求全面整改 wiki 治理体系、agent 体系、workflow、memory、harness、skill、sensor、template 或 closeout 行为，读 [[wiki-governance-system-contract.v1]]，必要时使用 [[templates/governance-system-upgrade-contract-template]] 固定 source coverage、ability extraction、system layer landing、sensor / evaluator、persistence routing 和 closeout proof；只新增 manifest、入口链接或 sensor 不能回答完成。
- 如果涉及主控、子工程、runtime service、数据 / 模型工程、文档治理工程或“wiki 作为实现类工程合集 / 模板”的升级，读 [[projects/design/topics/implementation-engineering-template-system]]，并使用 [[templates/implementation-project-profile-template]] 固定 project_role、owner surfaces、agent system layers、control plane、implementation boundaries、evidence contract 和 Closeout Proof。
- 如果涉及规则已有但没有执行，读 [[instruction-adherence]]。
- 如果涉及 TASK、issue、AP、报告目标包、handoff、状态页或会议行动项的当前裁决，读 [[execution-contract-semantics]]。
- 如果用户要求持续推进、直到完成、反复尝试或跨多轮跟进，先按 [[skills/goal-contract/SKILL]] 判断是否需要 Goal Contract；模板见 [[templates/goal-contract-template]]。
- 如果用户要求调研、研究、选型、产品 / 公司 / 开源工程评估或 PoC 判断，先读 [[skills/research-capability/SKILL]] 和 [[research-capability-rules]]。
- 如果用户要求吸收外部矩阵、附件建议或下游工程通用技能，先读 [[skills/transferable-skill-governance/SKILL]]，再决定 recognize / complete / upgrade / merge / adapt / defer / reject。
- 如果用户要求自动拆解当前 wiki 的研发事项，读 [[skills/work-item-auto-decomposition/SKILL]]；它是项目 / 领域绑定能力，不硬升为通用 skill。
- 如果用户要求 canonical HTML 公网访问、外部分发或 public URL，先读 [[skills/public-html-publish/SKILL]]、[[public-html-publish-rules]] 和 [[views/publication]]。
- 如果用户要求图文 lens、HTML、状态页、风险页、计划页、验收页、决策页、主题梳理、一图胜千言、PDF / PNG 或持久视图，先读 [[skills/problem-focused-visual-presentation/SKILL]]、[[templates/problem-focused-lens-template]] 和 [[views/README]]；持久 HTML 必须同步 registry，生成同源 PDF / PNG 到忽略目录，并保留 `static_visual_qa`。
- 如果用户要求复盘阶段、专题、交付链、Issue / 事故后经验或 Agent 工作流，先读 [[skills/retrospective-capability/SKILL]]、[[concepts/project-retrospective]]、[[projects/retrospectives/README]]；标准 / 深度复盘正文进入 `projects/retrospectives/<year>/` 并同步 [[projects/retrospectives/indexes/by-year]]，项目交付 / 软件研发链复盘使用 [[skills/delivery-retrospective/SKILL]]，历史对话和 Agent 工作复盘使用 [[skills/historical-dialogue-retrospective/SKILL]]。

## 工作阶段检查

- 工作阶段优先跑专项 sensor：`python3 scripts/check_all.py --only harness-governance`。
- 技能页、技能入口或技能模板改动跑：`python3 scripts/check_all.py --only skill-maturity`。
- research-capability 聚合入口、调研模板或研究治理改动跑：`python3 scripts/check_all.py --only research-capability`。
- public-html-publish skill、profile、治理页或发布模板改动跑：`python3 scripts/check_all.py --only public-html-publish`。
- 知识关联 skill 或落位规则改动跑：`python3 scripts/check_all.py --only knowledge-linking`。
- 问题聚焦式图文呈现、`views/`、lens 模板或导出守卫改动跑：`python3 scripts/check_all.py --only problem-focused-visual-presentation`。
- H5 ledger 或指令遵循改动跑：`python3 scripts/check_all.py --only harness-feedback-ledger,instruction-adherence`。
- Agent System Capability Package、intelligence evidence 或外部矩阵识别 capsule 改动跑：`python3 scripts/check_all.py --only agent-system-maturity`。
- 实现类工程合集、主控 / 子工程模板、implementation project profile 或 topic landing 改动跑：`python3 scripts/check_all.py --only implementation-template-system`。
- AcknowledgeBase source topic 到 wiki agent / workflow / memory / harness / skill 等系统层的逐 topic 能力吸收改动跑：`python3 scripts/check_all.py --only acknowledge-topic-adoption`。
- wiki 治理体系全面整改、能力层 owner landing、模板 / memory / harness / skill / sensor 接线改动跑：`python3 scripts/check_all.py --only governance-system-rectification`。
- 研发事项模型、事项矩阵或 work-item-auto-decomposition 改动跑：`python3 scripts/check_all.py --only work-item-matrix`。
- 入口、wikilink 或治理元数据改动跑：`python3 scripts/check_all.py --only project-docs`。
- 测试计划 / AP / 报告计划来源改动跑：`python3 scripts/check_all.py --only testing-system-maturity`。
- 执行合同语义、非目标或环境路由改动跑：`python3 scripts/check_all.py --only execution-contract-semantics`。
- 复盘体系、复盘模板或复盘 skill 改动跑：`python3 scripts/check_all.py --only retrospective-system`。
- Agent 编排、状态约束、治理分级、Run Capsule 或 Subproject Git Preflight 改动跑：`python3 scripts/check_all.py --only harness-governance,loop-engineering`。
- Agent Harness L5 验证、最终回复证明或不上推边界改动跑：`python3 scripts/check_all.py --only agent-harness-l5`。
- 收尾或提交前跑完整门禁：`python3 scripts/check_all.py`。
- `scripts/check_all.py` 是本库本地门传真相源；CI 或平台配置只是适配层。

## 写入边界

- 当前库是模板级 Harness，只吸收系统层规则、流程、模板、技能和自动化契约。
- 从下游工程反哺时，不复制项目事实、业务名、运行实例、具体状态或一次性测试证据。
- episode 先写入 [[harness-feedback-ledger]]，不要因为单次纠偏直接新增硬规则。

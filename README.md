---
type: entry
id: ENTRY-ROOT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-05-25
tags: [entry, root]
---

# 文档系统说明

这个文档库的目标很简单：把散乱资料变成能查、能连、能持续更新的知识网络，同时给未来的半自动 / 自动化项目推进留好路由。

如果只记一件事，就记住这套八层模型：

- 入口层：[[README]]、[[INDEX]]
- 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[response-mode-routing]]、[[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、[[POLICY]]、[[BRAIN]]
- 技能层：[[skills/README]] 和 `skills/`
- 呈现层：[[views/README]] 和 `views/`
- 运行层：[[projects/README]] 和 `projects/`
- 沉淀层：`articles/`、`concepts/`、`indexes/`
- 历史层：[[log]]、`archive/`
- 证据层：`raw/`、`inbox/`、`assets/`

当前物理结构再补一句：

- 根目录保留高频入口：[[README]]、[[INDEX]]、[[AGENTS]]、[[log]]
- `governance/` 收治理页：[[governance/README]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[response-mode-routing]]、[[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、[[agent-system-maturity]]、[[agent-system-cross-project-alignment.v1]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[harness-evolution]]、[[harness-feedback-ledger]]、[[log-writing-rules]]、[[trace-writing-rules]]、[[template-feedback-rules]]
- `skills/` 收项目内可复用的 agent 技能，例如 [[skills/issue-analysis/SKILL]]
- `views/` 收问题聚焦式图文 lens 的 current / snapshot / registry；导出缓存不作为事实源提交
- `projects/` 收运行中的项目内容
- `projects/retrospectives/` 是复盘 archive root，只放 README、indexes 和年份目录；正文进入 `projects/retrospectives/<year>/`
- 其他目录分别承接沉淀、历史和证据

## 怎么用这个总入口

如果你第一次打开这个文档库，就按这个顺序走：

1. 先看这页，知道它是做什么的、怎么分层、怎么启动。
2. 再看 [[governance/README]]，先建立治理层的整体边界。
3. 再看 [[BRAIN]]，了解已经确认过、后续会自动参与工作的共享背景。
4. 再看 [[POLICY]]，知道哪些规则、优先级和记忆路由是硬约束。
5. 如果你要处理项目推进，就去看 [[projects/README]] 和 [[projects/STRUCTURE]]。
6. 如果你要先看项目当前阶段、阻塞和下一步，也可以直接看 [[projects/status]]。
7. 如果你要新增或修改文档，去看 [[WORKFLOW]]。
8. 如果你要知道 agent 能做什么、不能做什么，去看 [[AGENTS]]。
9. 如果你只是想找入口，直接看 [[INDEX]]。

常见操作对应关系：

- 想知道“这个系统怎么用” -> 读这页
- 想知道“治理层是怎么分的” -> 读 [[governance/README]]
- 想知道“之前确认过哪些前提，以后不用重复说” -> 读 [[BRAIN]]
- 想知道“规则、优先级和自动沉淀边界” -> 读 [[POLICY]]
- 想知道“本轮该先轻量诊断还是进入沉淀 / 验收 / 规则升级” -> 读 [[response-mode-routing]]
- 想知道“规则、模板、Goal、log 或 sensor 是否用得过重” -> 读 [[agent-governance-strategy]]
- 想知道“当前权限、远程、dirty 状态或证据层级是否允许继续执行” -> 读 [[state-constraint-reasoning]]
- 想知道“多 agent、Run Capsule、子工程 Git preflight 和 Worker / Evaluator 怎么分工” -> 读 [[agent-orchestration]]
- 想判断“wiki 治理体系全面整改是否真的完成，还是只做了文档 / manifest / sensor 子项” -> 读 [[wiki-governance-system-contract.v1]]
- 想判断“目标工程 agent system 是否具备七层能力、外部矩阵能否识别、智能化证据是否足够” -> 读 [[agent-system-maturity]]
- 想判断“wiki 作为独立模板工程应该按主控、子工程、知识库、运维 agent 还是 hybrid 被采纳” -> 读 [[projects/design/topics/implementation-engineering-template-system]] 和 [[templates/implementation-project-profile-template]]，先裁决 Project Profile Overlay、Capability Packs、required / optional / forbidden packs 和 project_bound_facts
- 想把所有工程里的 agent、harness、memory、workflow、evaluation 和 migration 能力抽象吸收到本仓 -> 读 [[agent-system-cross-project-alignment.v1]]
- 想确认 AcknowledgeBase 所有 design topics 是否逐 topic 落到 wiki 的 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 和 migration 体系 -> 读 [[acknowledgebase-topic-system-adoption.v1]]
- 想知道“Harness 如何从真实 episode 中自我修正、何时升级 sensor / 模板 / 规则” -> 读 [[harness-evolution]] 和 [[harness-feedback-ledger]]
- 想知道“规则已有但为什么执行会漏、如何升级成触发器 / 模板 / sensor / 最终证明” -> 读 [[instruction-adherence]]
- 想知道“当前执行页有没有把参考规则、非目标或证据说明漂成隐形待办” -> 读 [[execution-contract-semantics]]
- 想知道“项目级稳定记忆放哪” -> 读 [[projects/memory/README]]
- 想知道“一轮需求是怎么从原始意图收敛成当前实现口径的” -> 读 [[projects/trace]]
- 想知道“`[[projects/trace]]` 应该怎么写、怎么续写旧主题” -> 读 [[trace-writing-rules]]
- 想知道“其他项目进化出的系统层信息怎么反哺模板” -> 读 [[template-feedback-rules]]
- 想把长时任务写成可审计完成契约 -> 读 [[concepts/codex-goals]] 和 [[templates/goal-contract-template]]
- 想找“可复制模板” -> 读 [[templates/README]]
- 想使用或维护“项目内 agent 技能”或判断技能成熟度 -> 读 [[skills/README]]
- 想做调研、研究、选型、产品 / 公司 / 开源工程评估或 PoC 判断 -> 读 [[skills/research-capability/SKILL]]、[[skills/technology-research/SKILL]] 和 [[research-capability-rules]]
- 想把外部技术材料、论文、repo、产品更新或社区讨论先归一成研究输入 -> 读 [[templates/research-intake-template]]，再按 [[skills/research-capability/SKILL]] 分流。
- 想给长时任务建立完成契约、防止目标或证据漂移 -> 读 [[skills/goal-contract/SKILL]] 和 [[templates/goal-contract-template]]
- 想根据外部矩阵或下游经验吸收通用技能 -> 读 [[skills/transferable-skill-governance/SKILL]]
- 想看 AcknowledgeBase 2026-06-26 `agent-evidence-v12` 矩阵快照如何 repo-native 吸收到本仓 -> 读 [[skills/transferable-skill-governance/matrix-adoption-2026-06-26-agent-evidence-v12]]，验证用 `python3 scripts/check_all.py --only transferable-skill-baseline`
- 想为某个通用技能做迁移源能力清单 -> 读 [[templates/skill-transfer-manifest-template]]；真正交给目标工程 agent 的任务书再用 [[templates/skill-transfer-contract-template]]。
- 想生成或维护主题图文 / HTML / PDF / PNG -> 读 [[skills/topic-visual-presentation/SKILL]]、[[templates/topic-presentation-template]] 和 [[views/README]]，先做 eligibility，再固定 subject/source、三轴、五门边界和同源导出要求
- 想把 canonical HTML views 公开发布或生成 public URL -> 读 [[skills/public-html-publish/SKILL]]、[[public-html-publish-rules]] 和 [[views/publication]]
- 想看“现实代码 / 旧工程怎么审计” -> 读 [[projects/codebase/README]]
- 想看“源码工程深度解读怎么分级推进” -> 读 [[projects/codebase/source-code-audit-workflow]]
- 想看“真实服务实例现在在哪里运行、怎么健康检查” -> 读 [[projects/service-registry]]
- 想看“完整软件架构包” -> 按 [[projects/design/README]] 里的顺序读技术选型、架构、工程结构、权限边界、写操作边界、数据库、部署、运行质量和设计图资产
- 想看“大型架构图 / 服务拓扑图怎么画、放哪、怎么维护” -> 读 [[projects/design/diagrams/README]]
- 想看“还没拍板但已经需要持续推进的设计专题” -> 读 [[projects/design/topics/README]]
- 想看“Gate、FP、EP、TASK、Issue、risk、test、验收和台账怎么组织” -> 读 [[projects/development/plan/work-item-system-model]]
- 想自动拆解本仓研发事项、补齐 Gate / FP / EP / TASK / risk / issue / test / 验收关系 -> 读 [[skills/work-item-auto-decomposition/SKILL]]
- 想看“测试计划、AP 验收计划、环境路由和测试报告怎么分工” -> 读 [[projects/development/plan/test-acceptance-planning-model]] 和 [[projects/development/acceptance/README]]
- 想看“复盘体系、复盘档案和经验沉淀怎么运行” -> 读 [[skills/retrospective-capability/SKILL]]、[[concepts/project-retrospective]]、[[projects/retrospectives/README]]、[[projects/retrospectives/indexes/by-year]] 和 [[templates/project-retrospective-template]]
- 想复盘“项目交付或软件研发链” -> 读 [[skills/delivery-retrospective/SKILL]] 和 [[concepts/software-development-project-retrospective]]
- 想复盘“历史对话或 Agent 工作流” -> 读 [[concepts/agent-work-retrospective]] 和 [[skills/historical-dialogue-retrospective/SKILL]]
- 想知道“新建目录 / 新建文件 / 修改文件怎么做” -> 读 [[WORKFLOW]]
- 想知道“`[[log]]` 应该怎么写、怎么合并主题” -> 读 [[log-writing-rules]]
- 想知道“会议很多时怎么收口会议材料” -> 读 [[projects/meetings/README]]
- 想知道“Codex 处理时有哪些约束” -> 读 [[AGENTS]]
- 想知道“入口页、索引页、层级在哪” -> 读 [[INDEX]]

## 先看这些关键问题

如果你只从总入口判断要不要动文档，先看这 5 件事：

- 这是新目录，还是已有目录的扩展？
- 这是新文件，还是对已有文件的修改？
- 这份材料该进 `raw/`、`inbox/`、`articles/`、`concepts/` 还是 `indexes/`？
- 这次改动会不会影响链接、目录名或索引？
- 这次处理是不是有长期价值，需要把按对话整理后的主题、用户意图和关键动作写进 [[log]]，或把稳定偏好写进 `workspace-memory`？

## 这组工具怎么配合

- `Obsidian` 是这套库的原生阅读 / 编辑工具，用来浏览、编辑和串联笔记；不用 `Obsidian` 时，`[[wikilink]]` 导航和双向链接不会完整生效。
- `Codex CLI` 用来读取、改写、批量生成 Markdown。
- `workspace-filesystem` 让 Codex 直接操作当前工作区下的文件。
- `workspace-memory` 记录长期规则、偏好、命名习惯和稳定结论。
- [[response-mode-routing]] 负责把每轮 agent 工作先分成快速诊断、知识沉淀、Issue 分析、验收关闭、规则升级、子工程实现或批处理，减少无谓重启动。
- [[agent-governance-strategy]] 负责把规则和检查分成 P0 / P1 / P2 / P3，避免把普通任务推成重治理。
- [[state-constraint-reasoning]] 负责在提交、推送、发布、关闭状态或调用外部工具前判断当前状态是否可执行。
- [[agent-orchestration]] 负责把 Goal、Run Capsule、Orchestrator、Worker、Evaluator、Subproject Git Preflight 和沉淀路由接起来。
- [[wiki-governance-system-contract.v1]] 负责治理体系全面整改的 source coverage、ability extraction、system layer landing、sensor / evaluator、persistence routing 和 closeout proof。
- [[agent-system-maturity]] 负责 Agent System Capability Package、Matrix Recognition Capsule、intelligence evidence lens 和 external evaluator blocked/readback 边界。
- [[agent-system-cross-project-alignment.v1]] 负责跨工程智能化能力的 source coverage、七层吸收矩阵、adoption decision 和 `structure-only` / `insufficient-evidence` 边界。
- [[acknowledgebase-topic-system-adoption.v1]] 负责 AcknowledgeBase source topic 的 ability adoption manifest，逐 topic 证明能力落到 wiki 工程治理体系而不是复制文档。
- [[instruction-adherence]] 负责把关键规则从自然语言推进到触发矩阵、模板字段、sensor、门禁和最终回复证明。
- [[execution-contract-semantics]] 负责防止参考规则、条件路由、非目标和上层证据污染当前执行合同。
- [[harness-evolution]] 和 [[harness-feedback-ledger]] 负责把用户纠偏、检查失败、模式切换和重复失守记录成 episode，再决定是否晋升为 sensor、模板、技能或规则。
- [[BRAIN]] 承接跨多轮确认、后续需要自动进入思考背景的共享内容。
- [[POLICY]] 承接共享规则、优先级和记忆路由。
- [[projects/memory/README]] 承接项目级稳定记忆。

## 治理层怎么分

治理层现在已经逻辑和物理两次收口：

- 逻辑上，治理层负责约束、流程、裁定、背景和写法指南
- 物理上，治理页统一收进 `governance/`，只保留 [[AGENTS]] 在根目录做 agent 特殊入口

最容易混的是这四页：

- [[POLICY]]：系统裁定规则。回答“什么允许、什么不允许、冲突时先按谁”
- [[AGENTS]]：执行约束。回答“agent 修改时必须怎么做”
- [[WORKFLOW]]：流程编排。回答“通常按什么顺序推进”
- [[response-mode-routing]]：响应模式路由。回答“先快后重、读取深度和模式切换怎么判”
- [[BRAIN]]：共享背景。回答“哪些前提以后默认带入”

一句话记忆：

- [[POLICY]] 决定怎么判
- [[AGENTS]] 决定怎么执行
- [[WORKFLOW]] 决定怎么走
- [[response-mode-routing]] 决定先轻还是先重
- [[BRAIN]] 决定默认带什么背景

## 软件研发模式怎么叠加

可以把原有底座理解成只有知识库模式。

知识库模式负责长期沉淀，研发模式负责项目推进，技能层负责把高频 agent 分析套路沉淀成可复用执行流程。

- 知识库模式：收集资料，整理成 `articles/`、`concepts/`、`indexes/`
- 研发模式：在 `projects/` 里维护项目主页、设计、决策、发布和复盘
- 技能层：在 `skills/` 里维护项目内 agent 技能，服务问题分析、定位、分工、验证和回写等高频动作
- 呈现层：在 `views/` 里维护问题聚焦式图文 lens，只呈现 source pack 和证据边界，不替代事实源
- 路由层：[[BRAIN]] 放共享背景，[[POLICY]] 放规则，[[projects/memory/README]] 放项目级稳定记忆
- 演进链：[[projects/trace]] 放当前项目里需求、约束、决策变化和最终落地范围之间的串联
- 两者衔接：项目里的稳定结论，最后回写到知识库层
- 流程控制：不做自动流控，由人读项目主页后手动推进
- 模板反哺：下游项目里被真实使用验证过的结构、流程、规则、记忆路由、写法、模板和自动化契约，抽掉项目事实后按 [[template-feedback-rules]] 回写模板库

如果是在探索一个全新的桌面端、web 或 app 产品，先进入“新应用探索模式”，不要一上来铺满完整研发结构：

- 多个候选方向、竞品、访谈、截图和灵感，先放 `inbox/`、`raw/`、`articles/`、`concepts/`。
- 只有当某个方向开始变成当前要推进的应用，才正式进入 `projects/`。
- 刚进入项目层时，先轻量维护 [[projects/README]]、[[projects/requirements]] 和 [[projects/trace]]。
- 等问题、人群、范围和验收开始稳定，再补 [[projects/design/topics/README]]、[[projects/decisions]]、完整架构包和研发拆解。
- 推荐路径是：`inbox/` / `raw/` -> `articles/` / `concepts/` -> [[projects/requirements]] -> [[projects/trace]] -> [[projects/design/topics/README]] -> [[projects/decisions]] -> [[projects/design/README]] -> [[projects/development/README]]。

## 角色和 memory 的关系

这套文档库里的角色分层，和 memory 分层不是一回事。

- 角色分层回答“谁负责什么”：项目负责人、研发经理、工程师
- memory 分层回答“该把哪些上下文放哪”：共享背景、规则、项目级稳定记忆
- 角色是职责视角，memory 是上下文视角
- 当前设计不打算给每个角色单独一套 memory，而是让同一套分层 memory 按作用域服务不同角色
- 如果未来要做角色专属 memory，需要额外补 ownership 和 routing 设计，那会是框架层变更，不是项目层内容
- 这类框架级说明以后优先维护在 [[README]]、[[governance/README]]、[[BRAIN]] 和 [[POLICY]]，不要下放到 `projects/` 及其子页

如果你正在做研发，先看 [[projects/README]]；如果已经进入拆解、执行或准出阶段，再看 [[projects/development/plan/README]]。
如果你想先看项目层的目录、文件、依赖和读取顺序，直接看 [[projects/STRUCTURE]]。
如果你想按一条固定顺序看完整架构，直接看 [[projects/design/README]] 里的 `完整架构包` 和 `查看顺序`；如果要维护大型架构图、服务拓扑图或业务到实现总览图，再看 [[projects/design/diagrams/README]]。

如果你想看这套文档库的整体设计思路，去看 [[articles/2026-04-09-obsidian-doc-system-design]] 和 [[concepts/document-os]]。
如果你想看分层记忆的设计，去看 [[articles/2026-04-09-layered-memory-research]] 和 [[concepts/layered-memory]]。

研发阶段的详细说明、阶段映射和推进方式，统一看 [[WORKFLOW]] 里的 `1.9 软件研发模式`；新应用从模糊想法到立项的轻量路径，看 [[WORKFLOW]] 里的 `1.9.0 新应用探索模式`。
如果你要让智能体直接推进一个具体功能，也统一看 [[WORKFLOW]] 里的 `1.9.9` 到 `1.9.12`。

## 最短工作流

1. 新材料先丢进 `inbox/` 或直接放进 `raw/`。
2. 让 Codex 把材料整理成一篇 `articles/` 摘要卡片。
3. 把反复出现的工具和概念抽到 `concepts/`。
4. 把入口、分类和时间线写到 `indexes/`。
5. 把按对话整理后的主题、用户意图、关键动作和关键决策写进 [[log]]。
6. 把共享背景写进 [[BRAIN]]，把规则写进 [[POLICY]]，把项目级稳定记忆写进 [[projects/memory/README]]。
7. 如果这轮已经进入项目推进或实现，就把需求演进链写进 [[projects/trace]]。
8. 如果这轮已经进入研发拆解、执行或准出，就按 [[projects/development/plan/work-item-system-model]] 把 `Gate -> FP -> EP -> TASK` 主链，以及 risk、issue、test、验收、报告和服务台账关系理清；如果需要 agent 自动候选拆解，使用 [[skills/work-item-auto-decomposition/SKILL]]，它是本仓项目 / 领域绑定能力，不硬升为所有工程通用 skill。
9. 如果这轮暴露了阶段、事故、Issue、交付链或 Agent 协作里的长期学习价值，先按 [[skills/retrospective-capability/SKILL]] 固定复盘合同，再把复盘正文写进 `projects/retrospectives/<year>/` 并同步 [[projects/retrospectives/indexes/by-year]]；项目交付 / 软件研发链看 [[skills/delivery-retrospective/SKILL]]，历史对话 / Agent 工作流看 [[skills/historical-dialogue-retrospective/SKILL]]，模板看 [[templates/project-retrospective-template]]。
10. 如果某类 agent 分析动作会反复出现，把可复用流程沉淀到 [[skills/README]] 和对应技能页；技能成熟度按 `skill / README entry / template / governance / sensor / TRANSFER / evidence boundary` 证据信号判断。若目标是 Agent System Capability Package，不能只看 skill maturity，要回到 [[agent-system-maturity]] 分层判断。
11. 如果这轮需要持久图文呈现，把 canonical lens 写进 [[views/README]] 管辖的 current / snapshot 结构，并同步 [[views/lens-registry]]；PDF / PNG / SVG 导出件只进忽略目录。
11. 个人稳定偏好继续放进 `workspace-memory`，避免下次重复决定。
12. 如果某个下游项目进化出了可复用的系统层信息，按 [[template-feedback-rules]] 反哺回模板。
13. 如果这次反哺暴露的是 Harness 自身缺口，先写 [[harness-feedback-ledger]]，再按 [[harness-evolution]] 判断是否升级模板、sensor 或规则。

## 为什么入口页不写太多

- [[README]] 负责让你快速判断方向，不负责承载所有细则。
- 更完整的治理边界放在 [[governance/README]]。
- 详细的文件和目录流程放在 [[WORKFLOW]]。
- 维护约束和行为边界放在 [[AGENTS]]。
- 这样总入口不会变成长手册，但关键分流点仍然能一眼看到。

## 打开方式

- 优先用 `Obsidian` 打开当前文档库；如果只用普通 Markdown 阅读器，可以看正文，但不会完整解析 `[[wikilink]]`。
- 在文档库里直接打开 `INDEX.md`

## 更新原则

- 一篇材料只维护一张主摘要卡片。
- 一个概念只维护一个主页面。
- 索引页永远指向最新入口，不堆内容。
- 同一类信息只保留一个主入口，其他页面优先链接，不复制粘贴正文。
- 正文默认中文，英文只保留文件名、产品名、代码标识和必要术语，不为了表面统一强行翻译专有名词。
- 更新任何内容时，先看它在整个系统里的位置，再动当前文件。
- 上下文不是“当前文档前后几段”，而是和目标内容直接相关的主入口、上下游文件、阶段位置和知识层级。
- 同一文档库内的页面跳转，默认优先使用 `[[wikilink]]`，不要写死本机绝对路径。
- [[log]] 不做对话转录；新记录按时间降序插在前面，并按“日期下的对话”组织；详细写法与合并规则统一见 [[log-writing-rules]]。
- 原始来源只进 `raw/`，临时待处理内容只进 `inbox/`，整理稿不要回塞 `raw/`。
- 支持性图片、截图、图表和 canvas 等辅助文件优先放 `assets/`。
- 不再作为默认入口但仍需保留的页面放 `archive/`。
- 如果暂时不知道怎么归类，先放 `inbox/`。
- 只要新增模块或新类型文件，就要同步更新上下文规则，不允许文档结构和规则描述脱节。
- 只有实际内容或结构变更才需要 commit；本地状态和缓存不纳入正式提交。

更细的会话级约束、读取顺序和提交规则，以 [[AGENTS]] 和 [[WORKFLOW]] 为准。

## Loop Engineering 接入

- [[skills/loop-engineering/SKILL]]：持续 agent 循环控制技能，用于判断何时从一次性 Goal / Run Capsule 升级为可验证、可停、可持久化的 loop。
- [[templates/loop-contract-template]]：Loop Contract 控制面，记录 discovery source、run queue、evaluator、persistent state、budget / stop 和 next-run decision。
- [[templates/run-capsule-template]]：单轮运行胶囊，承接 Parent Loop Contract、Input discovery item、Worker limits、State transition 和 Next-run recommendation。
- 专项检查：`python3 scripts/check_all.py --only loop-engineering`。

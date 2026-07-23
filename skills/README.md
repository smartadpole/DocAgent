# 技能层

这里放当前文档项目内可复用的 agent 技能。

## 边界

- `skills/` 承接面向 agent 的分析流程、判断框架和执行套路。
- `templates/` 承接可复制的文档骨架和页面模板。
- `governance/` 承接规则、流程、背景和裁定边界。
- [[response-mode-routing]] 先判断本轮是否需要调用完整技能流程；快速诊断不应默认触发完整沉淀链。
- [[harness-evolution]] 用来判断技能执行中的重复偏差是否应先记录为 episode，再升级为技能规则、模板字段或 sensor。

技能可以带当前项目的业务语境，但不直接承担项目状态、需求、设计、TODO 或测试报告的单一信息源职责。涉及项目事实时，技能只提示应该回到哪些主页面取证和回写。

## 技能成熟度模型

判断一个技能是否成熟，不能只看有没有 `SKILL.md` 文件。优先看它是否同时具备这些证据信号：

- `skill`：技能页存在，frontmatter 写清 `name`、`description`，正文有定位、触发 / 适用场景、工作流、输出格式、回写守卫或禁止项。
- `README entry`：技能在本页有入口，读者不用猜路径。
- `template`：如果技能会反复产出同类文档、报告、任务或回传包，已有对应模板；如果不需要模板，要在技能边界里说明。
- `governance`：技能会改变响应模式、写入边界、验收口径或规则升级时，已回到 [[response-mode-routing]]、[[WORKFLOW]]、[[POLICY]] 或 [[AGENTS]] 等主入口，而不是只写在技能里。
- `sensor`：能脚本化检查的结构、字段、入口或禁止项，已接入 `scripts/check_all.py` 的专项 sensor；技能层当前用 `python3 scripts/check_all.py --only skill-maturity` 检查。
- `TRANSFER`：准备跨工程迁移的技能，必须先形成迁移边界或等价说明，写清吸收什么、不复制什么、目标工程如何自检。
- `views`：如果技能会生成持久图文 lens、HTML report、print view 或 snapshot，必须有 [[views/README]]、registry、模板和导出缓存边界；没有持久呈现需求时要写明不需要。
- `evidence boundary`：任何成熟度比较、能力排行或迁移建议都只代表本轮信号强弱，不代表运行验收、项目状态或可从下游原样复制。

`body` / `large-body` 只能作为“材料是否足以承载复杂流程”的弱信号，不能作为写作目标。为追成熟度矩阵而扩写模板、堆清单或制造正文体量，视为过度吸收；正确做法是补真实缺口，例如治理裁定、sensor、模板字段、source pack、验证边界或迁移禁止项。外部附件、矩阵和诊断建议必须先经过本库身份筛选，不得照单全收。

状态词建议只作治理提示：`领先` 表示证据信号最完整且可反哺；`成熟` 表示本地可稳定使用；`接入` 表示有入口但仍缺模板、sensor 或迁移边界；`局部` 表示只有零散信号；`未见` 表示未发现等价能力；`阻塞` 表示路径不可读或证据不足。状态不能替代验收、关闭或项目裁决。

所有长期技能默认对标当前最佳设计：技能正文、README 入口、成熟度 frontmatter、证据信号章节、必要模板 / 等价说明、治理接线、sensor 和同目录 `TRANSFER.md`。会产出持久图文 lens 的技能还必须有 `views` 接线。如果某个技能暂不适合迁移，必须在成熟度章节说明原因，并把 `transfer_ready` 保持为 `false`。

跨工程技能成熟度矩阵只作为“发现缺口和评价维度”的来源，不作为本库事实源。吸收通用技能时只拿触发条件、事实源分层、流程、输出格式、验证、回写守卫、迁移边界和成熟度证据信号；不复制外部工程排行、分数、源头标记、项目状态、本地路径、业务表、服务名、运行 ID、source revision 或一次性 handoff。项目 / 领域绑定能力只能抽象方法，不能直接变成本库通用技能。

当目标是 Agent System Capability Package 或 intelligence maturity，不用 skill maturity 替代整体判断；先读 [[agent-system-maturity]]，再区分 skill、runtime、harness、memory、evaluation、governance、migration 和八维 `insufficient-evidence` 边界。

## Governance System Capability Pack

当目标不是单个 skill，而是“全面整改 wiki 治理体系”或同时触及 agent、workflow、memory、harness、skill、evaluation、governance、template、topic、migration 多层时，先读 [[wiki-governance-system-contract.v1]]，再决定哪些现有技能参与。

技能层在这个 Capability Pack 中只承担可复用执行流程，不独占整体完成裁决：

| 能力 | 主要技能 / owner | 完成边界 |
| --- | --- | --- |
| 长时目标和完成契约 | [[skills/goal-contract/SKILL]] | Goal Contract 不能替代验收和治理系统完成定义。 |
| 多轮 / Worker / Evaluator | [[skills/loop-engineering/SKILL]]、[[agent-orchestration]] | Loop 只负责发现、分派、验证、持久化和 next-run decision。 |
| 能力迁移与 topic 吸收 | [[skills/transferable-skill-governance/SKILL]]、[[acknowledgebase-topic-system-adoption.v1]] | 只吸收系统能力，不复制项目事实、分数或目录。 |
| 调研和源计划 | [[skills/research-capability/SKILL]]、[[skills/technology-research/SKILL]] | 调研证据不能直接上推为治理能力已落地。 |
| 复盘和纠偏学习 | [[skills/retrospective-capability/SKILL]]、[[harness-evolution]] | episode 先进入 ledger，再决定晋升为模板、sensor、skill 或 rule。 |
| 文档维护和入口一致性 | [[skills/documentation-maintenance/SKILL]] | 入口同步不能替代 owner landing 和 sensor / evaluator。 |

治理体系整改的可复制字段使用 [[templates/governance-system-upgrade-contract-template]]；专项检查为 `python3 scripts/check_all.py --only governance-system-rectification`。

## 本工程 baseline conformance

本节是本仓通用 agent 技能体系的 project conformance 声明。它只描述本仓自己的执行事实和验证入口，不代表 AcknowledgeBase、下游工程或矩阵快照已经完成迁移。

矩阵级源能力吸收清单见 [[skills/transferable-skill-governance/matrix-adoption-2026-06-26-agent-evidence-v12]]。它记录 AcknowledgeBase `generated_at=2026-06-26 11:39`、`source_revision=308bc64`、`scoring_schema_version=agent-evidence-v12` 快照下的逐能力 `true-gap / recognition-gap / signal-only-gap` 和 `recognize / complete / upgrade / merge / adapt / defer / reject` 裁决；本页只保留当前生效入口和 conformance 摘要。

| 字段 | 本工程声明 |
| --- | --- |
| `local_source_of_truth` | [[skills/README]] 是通用技能入口；各技能 `SKILL.md` 是执行流程源；同目录 `TRANSFER.md` 是迁移边界源；[[governance/README]]、[[POLICY]]、[[WORKFLOW]] 和 [[AGENTS]] 是规则入口；`views/` 只承接持久呈现；`projects/` 继续承接项目事实。 |
| `allowed_write_scope` | 本仓 agent 可在本轮授权范围内更新 `skills/`、`templates/`、`governance/`、`scripts/`、`views/`、`projects/` 和 [[log]]；不得把外部工程项目事实、运行 ID、服务实例、handoff 或历史 log 写成本仓通用事实。 |
| `required_profile` | 先按 [[response-mode-routing]] 判断响应模式；跨工程吸收先走 [[skills/transferable-skill-governance/SKILL]]；长时执行使用 [[skills/goal-contract/SKILL]]；持续循环使用 [[skills/loop-engineering/SKILL]]；实现类工程接入先填 [[templates/implementation-project-profile-template]]；持久图文和公开发布分别使用 [[skills/problem-focused-visual-presentation/SKILL]] 与 [[skills/public-html-publish/SKILL]]。 |
| `validation_command` | 局部改动优先跑对应专项 sensor；技能体系改动至少跑 `python3 scripts/check_all.py --only skill-maturity,transferable-skill-baseline,research-capability,loop-engineering,public-html-publish,problem-focused-visual-presentation,documentation-maintenance,cross-project-governance-audit,implementation-template-system`；收尾前跑完整 `python3 scripts/check_all.py` 和 `git diff --check`。 |
| `blocked_when_missing` | 缺少目标工程结构自检、`TRANSFER.md` 迁移边界、owner 页面、专项 sensor、人工确认边界、live readback 或真实证据时，只能写 `partial / blocked / review`，不能写成验收完成、发布完成或迁移完成。 |
| `exceptions` | 简单问答、一次性小修、只读解释、没有持久沉淀价值的临时判断不强行套完整技能包；项目 / 领域绑定能力只抽象方法，不新建通用 skill；sensor 只证明 wiring，不证明真实运行质量、审美质量或业务验收。 |

## 本轮通用能力吸收裁决

以下裁决基于本仓现有结构和 AcknowledgeBase 2026-06-26 11:39 `agent-evidence-v12` 快照。它用于指导本仓落位，不把矩阵分数写成事实源。

完整裁决和 source-depth 见 [[skills/transferable-skill-governance/matrix-adoption-2026-06-26-agent-evidence-v12]]；本节保留短表，避免入口页膨胀成迁移报告。

| 能力 | 分类 | 缺口类型 | 处理方式 | 本仓落位 |
| --- | --- | --- | --- | --- |
| Goal Contract | baseline 候选 | recognition-gap + 局部 true-gap | complete | 保留 [[skills/goal-contract/SKILL]]，补手工确认、非默认值、code-level / business-flow、method-candidate 和 conformance 边界到 `TRANSFER`。 |
| Loop Engineering | baseline 候选 | recognition-gap | upgrade | 保留 [[skills/loop-engineering/SKILL]]，补 direct-execution、ff-only update 和 Orchestrator-only / Worker preflight 边界。 |
| 复盘能力 | baseline 候选 | signal-only-gap | recognize | 现有总技能、子项、archive、索引和 sensor 已是 owner；不新建平行复盘体系，只保持 `views` 不替代复盘档案。 |
| Public HTML Publish | baseline 候选 | recognition-gap | complete | 保留 [[skills/public-html-publish/SKILL]]、[[views/publication]] 和 sensor；补 share-only live profile 与 Cloudflare Pages / Pages Direct Upload 只是可选模式的边界。 |
| 文档维护 | transferable skill | recognition-gap | upgrade | 保留 [[skills/documentation-maintenance/SKILL]]，显式补 duplicate-rule、generated guard、quality-gate 和 verification-loop。 |
| Issue 分析 | transferable skill | signal-only-gap | recognize | 保留 [[skills/issue-analysis/SKILL]] 和 [[templates/development-issue-template]]；不复制下游业务 issue 事实。 |
| 图文呈现 | transferable skill | signal-only-gap + 局部 true-gap | recognize / complete | 现有 `views/`、registry、reference、HTML 样本和 sensor 继续作为 owner；补 visual floor 词汇时只为明确完成合同，不追求堆视觉术语。 |
| 知识关联 | transferable skill | recognition-gap | recognize | 保留 [[skills/knowledge-linking/SKILL]]；`skill-transfer` 和 `Transfer Manifest` 只作为迁移场景的关系画像要求。 |
| 调研 / 研究能力 | transferable skill | true-gap | upgrade | 保留聚合入口，不平铺外部子项；把 frontier technology intake 吸收为研究 intake 子项和模板字段。 |
| 跨工程治理审计 | transferable skill | recognition-gap | upgrade | 保留自查 / 审计技能，补 source-depth、handoff-ready、non-reference 和 no runtime validation 边界。 |
| 跨工程技能迁移任务书 | transferable skill | recognition-gap | upgrade | 保留 meta skill，新增 [[templates/skill-transfer-manifest-template]]，任务书必须达到 `taskbook-ready` 并区分源能力、目标结构自检和验证。 |
| Transferable Skill Governance | transferable skill | recognition-gap | complete | 本页和 [[skills/transferable-skill-governance/SKILL]] 作为裁决面；补 repo-native、Path ROOT 和输出裁决表口径。 |
| Frontier Technology Intake | transferable skill 子项 | true-gap | adapt | 不新增并列 skill；作为 [[skills/research-capability/SKILL]] 的前沿信息流 intake 子项和 [[templates/research-intake-template]] 吸收。 |
| project-context-entry、work-item-auto-decomposition、customer-group-db-readback、backlog-management、lifeos-management | project-bound | 不适用 | reject / adapt | 只抽象事实源分层、批处理、验收或上下文加载方法；不迁移业务表、运行 ID、队列、生活项目事实或开源 backlog 状态。 |
| Agent System Capability Package | system capability | true-gap + recognition-gap | complete | 落到 [[agent-system-maturity]]、`governance/agent-system-maturity-snapshot.v1.json` 和 `scripts/check_agent_system_maturity.py`；不把 skill maturity 上推为 intelligence 总分。 |
| Implementation Project Template System | system capability | true-gap | complete | 落到 [[projects/design/topics/implementation-engineering-template-system]]、[[projects/design/topics/agent-workflow-memory-harness-skill-landing]]、[[templates/implementation-project-profile-template]] 和 `implementation-template-system` sensor；wiki 明确作为所有实现类工程合集与模板。 |
| work-item-auto-decomposition | project-bound | true-gap | adapt | 落到 [[skills/work-item-auto-decomposition/SKILL]]，绑定本仓 `Gate -> FP -> EP -> TASK` 模型；`transfer_ready: false`，不硬升通用 skill。 |

## 当前技能

- [[skills/research-capability/SKILL]]：调研 / 研究能力聚合技能。用于把技术、开源工程、产品、公司、行业、AI、PoC 和源码工程研究统一到调研合同、证据等级、行动等级、风险门和沉淀落位。
- [[skills/technology-research/SKILL]]：research-capability 的当前执行分支。用于技术、开源工程、行业 / AI 赛道或 PoC 调研，先固定调研合同、证据等级、成熟度、风险门、分支路线和沉淀落位，再产出可支撑判断的研究结果。
- [[skills/knowledge-linking/SKILL]]：知识关联技能。用于新增、调研或大改长期知识页时判断分层落位、入口、上位 / 邻接关系、反向回链和验证方式，避免知识成为孤岛。
- [[skills/goal-contract/SKILL]]：长时任务完成契约技能。用于终点清楚但路径需要探索、可能跨多轮推进、跨工程回传或证据边界敏感时，先固定目标、范围、证据层级、验证面、预算、停止条件和记录落点。
- [[skills/transferable-skill-governance/SKILL]]：可迁移技能治理技能。用于根据矩阵、源技能或下游经验吸收通用能力时，先判断 true-gap / recognition-gap / signal-only-gap，再决定 recognize / complete / upgrade / merge / adapt / defer / reject。
- [[skills/cross-project-skill-adoption-prompt/SKILL]]：跨工程技能迁移任务书生成技能。用于把已沉淀技能或能力抽象成可交给目标工程 agent 执行的提示词、资料清单、吸收边界、落位步骤和验证要求。
- [[skills/cross-project-governance-audit/SKILL]]：跨工程治理审计技能。用于按需读取多个工程的关键治理文件，对照平台级标准评估成熟度、漂移、共性缺口和可执行 handoff 边界。
- [[skills/work-item-auto-decomposition/SKILL]]：项目 / 领域绑定的研发事项自动拆解技能。用于本仓需求、Gate、FP、EP、TASK、risk、issue、test、验收关系不完整时，生成候选拆解、关系节点和关闭证据；不作为通用迁移 skill。
- [[skills/problem-focused-visual-presentation/SKILL]]：问题聚焦式图文呈现技能。用于把复杂文档、主题、状态、风险、计划、验收、知识或证据链重组为可读、可追溯、带证据边界的图文 lens；持久 HTML 还必须同步 registry、保留 `static_visual_qa`，并同源导出 PDF / PNG 到忽略目录。
- [[skills/public-html-publish/SKILL]]：HTML 公开发布技能。用于把 canonical HTML views 按 [[views/publication]] 生成 public_url 或明确 blocked 原因，并守住 HTML-only、host / prefix 和 live readback 边界。
- [[skills/documentation-maintenance/SKILL]]：文档维护技能。用于代码、结构、规则或公开行为变化后，保守检查文档是否过期、缺失或不准确，并产出修正报告或受控文档改动。
- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析技能。用于把模糊问题拆成权威事实源、最小根因链、责任边界、跨工程分工、联测方案和主控文档回写。
- [[skills/retrospective-capability/SKILL]]：复盘能力总技能。用于把项目交付、软件研发链、历史对话、Agent 工作流、Harness episode 和治理自演进复盘收敛到统一合同、子项路由、行动兑现回检、年份归档、索引和沉淀边界。
- [[skills/delivery-retrospective/SKILL]]：项目交付与软件研发链复盘子技能。用于阶段、里程碑、发布、事故后专题、Issue 后专题或交付链复盘，覆盖需求、设计、拆解、实现、测试验收、发布运行和协作治理。
- [[skills/historical-dialogue-retrospective/SKILL]]：历史对话与 Agent 工作流复盘子技能。用于复盘当前上下文、log、Harness ledger、原始 session / rollout、git diff / commit、检查输出、memory 和最终回复里的 agent 协作质量、偏差和改进路由。

- [[skills/loop-engineering/SKILL]]：Loop Engineering / 持续 agent 循环控制技能。用于把 Goal、Run Capsule、子 agent、harness、memory 和软件研发体系组织成可持续的发现、分派、验证、持久化和下一轮决策闭环；不替代项目状态、验收或发布。

## 维护原则

- 新技能先写最小可用版本，不铺无关资源目录。
- 技能正文只写可复用流程，不复制项目主页、设计页或 TODO 的长正文。
- 如果技能引入新的项目事实判断口径，同轮检查是否需要回写 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]] 或项目主页面。
- 从外部矩阵、lens 或下游工程再次吸收技能时，先判断它是通用可迁移能力、治理能力还是项目 / 领域绑定能力；只有前两类可落为本库技能，项目 / 领域绑定能力只抽象方法并记录不复制原因。
- 例外：当用户明确要求把项目 / 领域绑定能力做成当前目标工程自己的能力时，可以落为 `transfer_ready: false` 的本地 skill，并必须绑定本仓 owner、template、sensor 和不上推边界。
- 外部诊断里的 `missing signals` 是候选修复方向，不是执行命令；补完后要回看本库是否更清晰、更可维护，而不是只看矩阵分数是否更高。

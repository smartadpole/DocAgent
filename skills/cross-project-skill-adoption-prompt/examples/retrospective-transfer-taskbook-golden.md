---
type: skill-transfer-golden-example
skill: cross-project-skill-adoption-prompt
case: retrospective-transfer-taskbook
status: active
updated: 2026-06-04
tags: [skill, transfer, golden-baseline, retrospective]
---

# Retrospective Transfer Taskbook Golden Example

这个样例用于校准“生成一段提示词，把复盘体系迁移到其他工程”的输出质量。

它不是长期固定提示词资产，也不替代 `skills/historical-dialogue-retrospective/TRANSFER.md`。它只作为回归样例：生成稿必须达到同等任务书粒度，不能退化成迁移说明、模块标题清单或泛化框架。

## Golden Prompt

```markdown
请升级本工程的完整复盘体系。目标不是只新增一个复盘目录，也不是只写一篇复盘模板，而是建立一套可持续运行的复盘系统。

## 背景和目标

复盘是长期学习工程，用来把项目、阶段、事故、Issue、交付链偏差、Agent 协作偏差和治理缺口，沉淀成未来研发实践、方案设计、工程治理、测试验收、运行质量和 Agent 工作方式都会复用的经验资产。

## 复盘体系参考资料

请先读取 AcknowledgeBase 已沉淀资料，只吸收系统层信息：

- `/Users/hai/Documents/Docs/AcknowledgeBase/skills/historical-dialogue-retrospective/TRANSFER.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/skills/historical-dialogue-retrospective/SKILL.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/projects/retrospectives/README.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/templates/project-retrospective-template.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/project-retrospective.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/software-development-project-retrospective.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/agent-work-retrospective.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/AGENTS.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/WORKFLOW.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-evolution.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-feedback-ledger.md`

如需版本锚点，先在源工程确认当前参考提交，不要把未核实的 commit 写成事实。

## 吸收边界

不要整库复制。不要复制 AcknowledgeBase 的项目事实、log 历史、当前状态、案例原文、运行 ID、服务路径、提交历史或用户偏好。

只吸收系统层信息：复盘长期价值、对象分类、文件落位、模板字段、skill 触发条件、证据读取、输出结构、质量自检、行动分流、治理自演进、入口同步和检查方式。

## 目标工程结构自检与落位

先读取目标工程的 README、AGENTS、docs、projects、issues、incidents、tasks、decisions、memory、trace、skills、templates、scripts 等已有结构，再判断落位。

- 有 `projects/`：优先使用 `projects/retrospectives/`。
- 无 `projects/`：优先使用 `docs/retrospectives/`。
- 已有 retrospective / postmortem / incidents / lessons-learned / governance：优先复用，不新建平行体系。
- 如果 `templates/` 是业务模板、前端模板、服务端模板或运行资产，不要放复盘模板；改用 `docs/templates/`、`.codex/agents/templates/` 或目标工程已有文档模板目录。
- 如果没有 skills 体系，把可执行流程写入 AGENTS、docs/agent-workflows 或等价规则入口。

## 需要建立的复盘体系模块

1. 复盘方法入口

目标：让人和 agent 知道什么场景应该复盘，以及复盘和其他记录的分工。

必须写入：
- 什么是复盘。
- 什么时候启动复盘。
- 复盘和 log 的区别。
- 复盘和 Issue / 事故的区别。
- 复盘和测试报告的区别。
- 复盘和决策 / memory / trace 的关系。
- 复盘如何服务未来研发实践、方案设计、工程治理、测试验收、运行质量和 Agent 工作方式。

可落位为 `concepts/project-retrospective.md`、`docs/retrospective.md`，或目标工程已有方法论入口中的一节。

禁止只写一句“新增复盘说明页”。

2. 复盘档案入口

目标：让具体复盘文件有稳定入口、粒度和索引。

新增或完善 `projects/retrospectives/README.md`、`docs/retrospectives/README.md` 或目标工程等价入口。

入口至少说明：
- 这页负责什么。
- 这页不负责什么。
- 复盘文件放哪里。
- 复盘命名规则。
- 复盘粒度：轻量 checkpoint / 标准复盘 / 深度复盘。
- 当前复盘索引。
- 共性主题。
- 维护说明。
- 沉淀路由。

禁止只建一个 `retrospectives/` 空目录。

3. 复盘模板

目标：保证每次复盘不丢目标、事实、偏差、行动和未验证边界。

新增或完善 `project-retrospective-template.md`，至少包含：
- 复盘对象。
- 原始目标。
- 实际结果。
- 关键事实。
- 偏差与原因。
- 保留做法。
- 改进行动。
- 沉淀路由。
- 未验证边界。

软件研发对象要保留交付链回看；Agent 深度参与时要保留 Agent 工作回看。

禁止把模板压成时间线、问题列表或总结段落。

4. 软件研发项目复盘维度

如果目标工程是软件研发项目，必须覆盖交付链：

- 需求是否清楚。
- 设计是否支撑实现和验收。
- 事项关系是否清楚。
- 实现是否按合同落地。
- 测试、验收、发布证据是否足够。
- 运行质量、服务台账、事故和回滚是否闭环。
- 协作治理是否让信息进入正确单一信息源。

如果目标工程没有 Gate / FP / EP / TASK / AP / report 体系，映射到自己的 issue / task / milestone / acceptance / report 等等价事项。

禁止项：
- 不要把测试报告当复盘。
- 不要把 Issue 关闭当复盘完成。
- 不要把一次事故直接泛化成全项目结论。

5. Agent 工作复盘维度

如果目标工程由 agent 深度参与，必须加入 Agent 工作复盘。

至少覆盖：目标理解、阶段判断、上下文读取、工具使用、执行策略、验证质量、沟通节奏、权限和边界控制、沉淀路由、收尾和提交质量。

必须说明：Agent 工作复盘评价的是 agent 如何完成工作，不替代项目结果复盘。

禁止只评价“agent 做得好不好”。

6. 历史对话 / Agent 工作流复盘 skill

如果目标工程有 skills 体系，请新增或适配复盘 skill；否则写入 AGENTS 或等价 agent workflow。

该 skill 必须定义：触发场景、响应模式、证据源分层、复盘对象框定方法、工作链还原方法、Agent 偏差分类、效率和质量判断、Workflow 改进路由、输出格式、禁止项。

证据源至少区分：当前对话上下文、log、harness ledger 或类似反馈台账、原始 session / rollout、git diff / commit、受影响主页面、检查 / 测试输出、memory、最终回复 / handoff。

禁止项：
- 不要只凭 log 做历史对话复盘。
- 不要只凭当前上下文判断完整历史。
- 不要把一次偏差直接升级成硬规则。

7. 行动分流机制

复盘行动项不能停留在复盘正文里，也不能新建平行看板。

请明确行动项分流：bug、偏差、验收失败进入 Issue；事故事实和修复闭环进入 incidents；研发交付动作进入目标工程等价事项系统；跨 owner 协调进入 meetings；关键取舍进入 decisions；项目长期事实进入 memory；需求演进进入 trace；可复用方法进入 concepts 或 docs 方法页；可复制骨架进入 templates；高频 agent 流程进入 skills；重复失守或机制缺口进入 harness ledger / feedback ledger；可脚本化检查进入 sensor / check script；执行规则变化进入 AGENTS / WORKFLOW / POLICY 或等价入口。

8. 治理自演进关系

复盘体系必须连接治理自演进：

- 单次表现：记录复盘或 log，继续观察。
- 重复失守：进入 feedback ledger / harness ledger。
- 可模板化：更新模板。
- 可技能化：更新 skill。
- 可脚本化：新增 sensor 或检查。
- 影响执行顺序：更新 WORKFLOW。
- 影响必须 / 禁止行为：更新 AGENTS。
- 影响优先级或自动沉淀边界：更新 POLICY 或等价规则页。

禁止项：
- 不要把所有复盘结论都升级成硬规则。
- 不要为了完整复盘无限扩读。
- 不要让复盘体系变成新的治理噪音。

## 需要更新的入口

按目标工程实际结构选择更新 README.md、INDEX.md、AGENTS.md、WORKFLOW.md、docs/README.md、projects/STRUCTURE.md、projects/README.md、skills/README.md、templates/README.md 或 scripts/check 等价检查入口。

入口只放短说明和链接，不复制复盘正文。

## 验证和提交要求

完成后运行目标工程已有检查。若没有统一检查，至少做入口可发现性、内部链接、职责边界、模板字段、单一信息源边界自检。

如果检查无法运行，说明原因和未验证边界。

若本轮产生文件或结构变更，请按目标工程规则提交一个主题明确的 commit，commit message 使用英文。

## 最终回复要求

最终回复说明：读取了哪些目标工程入口、推荐落位、复盘体系落点、方法入口、档案入口、模板、skill 或等价流程、行动项分流、入口同步、检查结果、commit hash、未验证边界和后续建议。
```

## Regression Requirements

生成稿必须至少满足：

- 有直接命令、背景目标、参考资料、吸收边界、目标结构自检、模块展开、入口同步、验证提交、最终回复要求。
- `需要建立的复盘体系模块` 中每个模块都有目标或用途、字段或判断项、落位或替代落位、禁止项或反模式。
- 明确出现：不要把测试报告当复盘、不要把 Issue 关闭当复盘完成、不要只凭 log 做历史对话复盘。
- 不出现具体目标工程小节，不要求当前生成端预读目标工程。

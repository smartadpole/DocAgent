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

它不是长期固定提示词资产，也不替代 `skills/historical-dialogue-retrospective/TRANSFER.md`。它只作为回归样例：生成稿必须达到同等任务书粒度，不能退化成迁移说明、压缩后的通用迁移提示词、模块标题清单或泛化框架。

## Golden Prompt

```markdown
请升级本工程的完整复盘体系。目标不是只新增一个复盘目录，也不是只写一篇复盘模板，而是建立一套可持续运行的复盘系统。

复盘体系的目标：

复盘是长期学习工程，用来把项目、阶段、事故、Issue、交付链偏差、Agent 协作偏差和治理缺口，沉淀成未来研发实践、方案设计、工程治理、测试验收、运行质量和 Agent 工作方式都会复用的经验资产。

请先读取并参考 AcknowledgeBase 已沉淀资料。不要把未确认的版本号或 commit hash 写成事实；如需版本锚点，先在源工程确认当前参考提交。

## 一、复盘体系参考资料

1. 复盘档案层设计

`/Users/hai/Documents/Docs/AcknowledgeBase/projects/retrospectives/README.md`

2. 复盘档案模板

`/Users/hai/Documents/Docs/AcknowledgeBase/templates/project-retrospective-template.md`

3. 通用项目复盘方法论

`/Users/hai/Documents/Docs/AcknowledgeBase/concepts/project-retrospective.md`

4. 软件研发项目复盘方法论

`/Users/hai/Documents/Docs/AcknowledgeBase/concepts/software-development-project-retrospective.md`

5. Agent 工作复盘方法论

`/Users/hai/Documents/Docs/AcknowledgeBase/concepts/agent-work-retrospective.md`

6. 历史对话 / Agent 工作流复盘 skill

`/Users/hai/Documents/Docs/AcknowledgeBase/skills/historical-dialogue-retrospective/SKILL.md`

7. 复盘迁移资料清单

`/Users/hai/Documents/Docs/AcknowledgeBase/skills/historical-dialogue-retrospective/TRANSFER.md`

8. 复盘相关维护规则、读取路径和上下文模型

`/Users/hai/Documents/Docs/AcknowledgeBase/AGENTS.md`

`/Users/hai/Documents/Docs/AcknowledgeBase/governance/WORKFLOW.md`

`/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-evolution.md`

`/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-feedback-ledger.md`

## 二、吸收边界

不要整库复制。

不要复制 AcknowledgeBase 的项目事实、log 历史、当前状态、案例原文、一次性治理记录、运行 ID、服务路径、提交历史或用户偏好。

只吸收系统层信息：

- 复盘的长期价值
- 复盘对象分类
- 复盘文件落位
- 复盘方法论
- 复盘模板字段
- 复盘 skill 的触发条件、证据读取、输出结构和质量自检
- Issue / 事故 / log / 决策 / memory / trace / TASK / 会议之间的分工
- Agent 工作复盘和 Harness 自演进的关系
- 复盘行动项分流规则
- 复盘结论如何反哺模板、规则、skill、sensor 和项目记忆

## 三、请在目标工程中完成的设计

请先读取目标工程的 README、AGENTS、docs、projects、issues、incidents、tasks、decisions、memory、trace、skills、templates、scripts 等已有结构，然后判断本工程复盘体系应该落在哪里。

如果目标工程有 `projects/` 结构，优先使用：

`projects/retrospectives/`

如果目标工程没有 `projects/` 结构，优先使用：

`docs/retrospectives/`

如果目标工程已有自己的复盘、事故、postmortem、lessons-learned 或研发治理目录，先判断是否复用已有目录，不要重复造平行体系。

如果目标工程的 `templates/` 是前端模板、服务端渲染模板、业务生成物模板或运行资产，不要把复盘模板放进去；改用 `docs/templates/`、`.codex/agents/templates/` 或目标工程明确的文档模板目录。

如果目标工程没有 `skills/` 体系，把可执行复盘流程写入 AGENTS、docs/agent-workflows 或等价规则入口。

## 四、需要建立的复盘体系模块

### 1. 复盘方法入口

目标：让人和 agent 知道什么场景应该复盘，以及复盘和其他记录的分工。

目标工程应有一个复盘方法或说明入口。

必须写入：

- 什么是复盘
- 什么时候启动复盘
- 复盘和 log 的区别
- 复盘和 Issue / 事故的区别
- 复盘和测试报告的区别
- 复盘和决策 / memory / trace 的关系
- 复盘输出如何服务未来研发实践、方案设计、工程治理、测试验收、运行质量和 Agent 工作方式

可以是：

- `concepts/project-retrospective.md`
- `docs/retrospective.md`
- 或目标工程已有方法论入口中的一节

禁止只写一句“新增复盘说明页”。

### 2. 复盘档案入口

新增或完善复盘档案入口，例如：

`projects/retrospectives/README.md`

或：

`docs/retrospectives/README.md`

这个入口至少说明：

- 这页负责什么
- 这页不负责什么
- 复盘文件放哪里
- 复盘命名规则
- 复盘粒度：轻量 checkpoint / 标准复盘 / 深度复盘
- 当前复盘索引
- 共性主题
- 维护说明
- 沉淀路由

禁止只建一个空目录，或只写“这里放复盘”。

### 3. 复盘模板

新增或完善复盘模板，例如：

`templates/project-retrospective-template.md`

或：

`docs/templates/project-retrospective-template.md`

模板至少包含：

- 复盘对象
- 原始目标
- 实际结果
- 关键事实
- 偏差与原因
- 保留做法
- 改进行动
- 沉淀路由
- 未验证边界

如果是软件研发项目，模板还要保留交付链回看。

如果 Agent 深度参与，模板还要保留 Agent 工作回看。

禁止把模板压缩成时间线、问题列表或泛泛总结。

### 4. 软件研发项目复盘维度

如果目标工程是软件研发项目，复盘体系必须覆盖交付链：

- 需求是否清楚
- 设计是否支撑实现和验收
- Gate / FP / EP / TASK / risk / issue / AP / report 等事项关系是否清楚
- 实现是否按合同落地
- 测试、验收、发布证据是否足够
- 运行质量、服务台账、事故和回滚是否闭环
- 协作治理是否让信息进入正确单一信息源

如果目标工程没有 Gate / FP / EP / TASK / AP / report 体系，请映射到自己的 issue、task、milestone、acceptance、report 或等价事项系统。

不要把测试报告当复盘。

不要把 Issue 关闭当复盘完成。

不要把一次事故直接泛化成全项目结论。

### 5. Agent 工作复盘维度

如果目标工程由 agent 深度参与，必须加入 Agent 工作复盘。

复盘维度至少包括：

- 目标理解
- 阶段判断
- 上下文读取
- 工具使用
- 执行策略
- 验证质量
- 沟通节奏
- 权限和边界控制
- 沉淀路由
- 收尾和提交质量

Agent 工作复盘不是评价项目结果，而是评价 agent 是如何完成工作的。

禁止只写“评价 agent 做得好不好”。

### 6. 历史对话 / Agent 工作流复盘 skill

如果目标工程有 `skills/` 目录，请新增或适配一个复盘 skill，参考：

`/Users/hai/Documents/Docs/AcknowledgeBase/skills/historical-dialogue-retrospective/SKILL.md`

该 skill 应定义：

- 触发场景
- 响应模式
- 证据源分层
- 复盘对象框定方法
- 工作链还原方法
- Agent 偏差分类
- 效率和质量判断
- Workflow 改进路由
- 输出格式
- 禁止项

证据源至少区分：

- 当前对话上下文
- log
- harness ledger 或类似反馈台账
- 原始 session / rollout
- git diff / commit
- 受影响主页面
- 检查 / 测试输出
- memory
- 最终回复 / handoff

不要只凭 log 做历史对话复盘。

不要只凭当前上下文判断完整历史。

不要把一次偏差直接升级成硬规则。

### 7. 行动分流机制

复盘行动项不能停留在复盘正文里，也不能新建平行看板。

请明确行动项分流到哪里：

- bug、偏差、验收失败：Issue
- 事故事实和修复闭环：incidents
- 研发交付动作：Gate / FP / EP / TASK / risk / acceptance / report，或目标工程等价事项系统
- 跨 owner 协调：meetings
- 关键取舍：decisions
- 项目长期事实：memory
- 需求演进：trace
- 可复用方法：concepts 或 docs 方法页
- 可复制骨架：templates
- 高频 agent 流程：skills
- 重复失守或机制缺口：harness ledger / feedback ledger
- 可脚本化检查：sensor / check script
- 执行规则变化：AGENTS / WORKFLOW / POLICY 等规则入口

### 8. 治理自演进关系

复盘体系必须和治理自演进连接：

- 单次表现：记录复盘或 log，继续观察
- 重复失守：进入 feedback ledger / harness ledger
- 可模板化：更新模板
- 可技能化：更新 skill
- 可脚本化：新增 sensor 或检查
- 影响执行顺序：更新 WORKFLOW
- 影响必须 / 禁止行为：更新 AGENTS
- 影响优先级或自动沉淀边界：更新 POLICY 或等价规则页

不要把所有复盘结论都升级成硬规则。

不要为了完整复盘无限扩读。

不要让复盘体系变成新的治理噪音。

## 五、需要更新的入口

完成设计后，请更新目标工程自己的入口，让人和 agent 都知道复盘体系在哪里。

可能包括：

- README.md
- INDEX.md
- AGENTS.md
- WORKFLOW.md
- docs/README.md
- projects/STRUCTURE.md
- projects/README.md
- skills/README.md
- templates/README.md
- scripts/check 或等价检查入口

按目标工程实际结构选择，不要机械照搬。

入口只放短说明和链接，不复制复盘正文。

## 六、最终交付

请完成：

1. 读取目标工程现有结构。
2. 说明本工程复盘体系的推荐落位。
3. 新增或完善复盘方法入口。
4. 新增或完善复盘档案入口。
5. 新增或完善复盘模板。
6. 如果有 skills/ 体系，新增或适配历史对话 / Agent 工作流复盘 skill；如果没有，写入 AGENTS 或等价 agent workflow。
7. 同步 README / INDEX / AGENTS / WORKFLOW / docs / projects / skills / templates / scripts 等入口。
8. 跑目标工程已有检查。
9. 如果没有统一检查，至少做入口可发现性、内部链接、职责边界、模板字段、单一信息源边界自检。
10. 提交一个主题明确的 commit，commit message 使用英文。

最终回复中请说明：

- 读取了哪些目标工程入口
- 复盘体系落在哪里
- 方法论在哪里
- 档案入口在哪里
- 模板在哪里
- skill 或等价流程在哪里
- 行动项如何分流
- 同步了哪些入口
- 跑了哪些检查
- commit hash
- 未验证边界和后续建议
```

## Regression Requirements

生成稿必须至少满足：

- 有直接命令、目标定义、参考资料、吸收边界、目标工程结构自检、模块展开、入口同步、最终交付和最终回复要求。
- `需要建立的复盘体系模块` 中每个模块都有目标或用途、字段或判断项、落位或替代落位、禁止项或反模式。
- 明确出现：不要把测试报告当复盘、不要把 Issue 关闭当复盘完成、不要只凭 log 做历史对话复盘。
- 明确要求最后检查、提交、commit hash、未验证边界和后续建议。
- 不出现具体目标工程小节，不要求当前生成端预读目标工程。

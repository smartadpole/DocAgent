---
type: concept
id: CONCEPT-SOFTWARE-DEVELOPMENT-PROJECT-RETROSPECTIVE
status: active
source_of_truth: true
updated: 2026-06-03
tags: [concept, retrospective, software-engineering, project-management]
---

# 软件研发项目复盘

上级专题：[[concepts/project-retrospective]]

相关页面：[[concepts/software-testing-acceptance-release]]、[[concepts/agent-work-retrospective]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/plan/test-acceptance-planning-model]]、[[projects/incidents/README]]

软件研发项目复盘是项目复盘在软件交付场景下的子专题。它把需求、设计、研发拆解、实现、测试、验收、发布、运行和协作治理放在同一条交付链里回看。

具体软件研发复盘档案默认放在 `projects/retrospectives/<year>/`，并从 [[projects/retrospectives/README]] 和索引页可达；本页只维护可复用方法和读取框架，执行流程由 [[skills/retrospective-capability/SKILL]] 路由到 [[skills/delivery-retrospective/SKILL]]。

## 定义

软件研发项目复盘关注一个软件项目或阶段是否把“要解决的问题”稳定转成了“可运行、可验证、可维护的交付物”。

它不只看代码写完没有，还要看：

- 需求是否清楚，范围是否被守住。
- 设计是否足以支撑实现和验收。
- 事项拆解是否形成可执行合同。
- 实现是否和设计、接口、数据、权限、部署边界一致。
- 测试、验收和发布证据是否足以支撑当前结论。
- 事故、返工和沟通成本暴露了哪些系统缺口。
- 如果 agent 参与执行，它的工作方式、效率、质量和边界控制是否可靠。
- 哪些经验应该回到模板、规则、技能、sensor 或项目记忆。

## 复盘主线

| 主线 | 核心问题 | 常见证据 |
| --- | --- | --- |
| 需求 | 做的是不是正确问题 | 需求页、trace、用户反馈、范围变更 |
| 设计 | 方案是否支撑目标和边界 | 架构、接口、数据、权限、部署设计 |
| 拆解 | 事项是否能被执行和验收 | Gate / FP / EP / TASK、risk、issue、AP |
| 实现 | 代码是否按合同落地 | commit、diff、代码审查、handoff、运行记录 |
| 测试验收 | 证据是否覆盖关闭口径 | 测试计划、报告、fixture、回归、人工确认 |
| 发布运行 | 能力是否进入目标环境 | 发布记录、服务台账、监控、回滚、事故 |
| 协作治理 | 信息是否在正确位置流动 | 会议、决策、log、模板、规则和 sensor |
| Agent 工作 | agent 是否高质量、高效率、守边界地完成任务 | [[concepts/agent-work-retrospective]]、diff、验证、提交、最终回复 |

## 交付链检查

复盘时至少覆盖：

- **需求是否清楚**：问题定义、目标用户、范围、非目标、验收标准是否稳定。
- **设计是否支撑实现和验收**：架构、接口、数据、权限、部署和运行质量是否能支撑目标。
- **事项关系是否清楚**：Gate / FP / EP / TASK / risk、issue、AP、report 是否有明确上下游和关闭证据。
- **实现是否按合同落地**：实际代码、配置、服务和 handoff 是否符合任务合同。
- **测试、验收、发布证据是否足够**：证据是否覆盖 local / service-side / end-to-end、非默认值 / 边界值和人工确认边界。
- **运行质量是否闭环**：服务台账、监控、事故、回滚和恢复是否有记录和归口。
- **协作治理是否进入正确单一信息源**：需求变化进 trace，取舍进 decisions，问题进 Issue / incidents，证据进 reports，长期事实进 memory。

## 推荐输出结构

软件研发项目复盘可以按下面结构落地：

1. **复盘对象**：项目、阶段、发布、事故或某条工作链。
2. **原始目标**：用户价值、业务目标、工程目标和明确非目标。
3. **实际结果**：已交付、未交付、延期、降级、超出预期和遗留风险。
4. **交付链回放**：需求 -> 设计 -> 拆解 -> 实现 -> 测试验收 -> 发布运行。
5. **偏差和原因**：把需求偏差、设计偏差、实现偏差、验证偏差和协作偏差分开。
6. **协作治理回看**：检查信息流、owner、会议 / 决策、事项关系、证据边界和沉淀路由是否清楚。
7. **Agent 工作回看**：如果 agent 参与执行，补看目标理解、读取预算、工具使用、验证证据、沟通节奏和沉淀质量。
8. **保留项**：下轮仍应复用的结构、流程、模板、工具、检查或协作方式。
9. **改进行动**：写清 owner、落点、完成口径和检查方式。
10. **沉淀路由**：项目事实留项目层，可复用方法回知识库层，规则候选走治理层。

## 证据读取顺序

默认先读和复盘对象直接相关的单一信息源：

1. 项目目标和阶段：[[projects/README]]、[[projects/status]]
2. 需求和范围：[[projects/requirements]]、[[projects/trace]]
3. 设计和决策：[[projects/design/README]]、[[projects/decisions]]
4. 拆解和执行：[[projects/development/plan/README]]、[[projects/development/execution/README]]
5. 测试和验收：[[projects/development/acceptance/README]]、[[projects/development/reports/README]]
6. Issue 和事故：[[projects/development/issues/README]]、[[projects/incidents/README]]
7. 发布和运行：[[projects/releases]]、[[projects/service-registry]]
8. 历史过程：[[log]]、[[projects/development/execution/worklog]]

如果复盘对象只是单个事故或单个 Issue，不要机械扩大到整项目；先在事故或 Issue 主档案里完成事实保真，再判断是否提炼通用经验。

完整执行时使用 [[skills/delivery-retrospective/SKILL]] 和 [[templates/project-retrospective-template]]；本页不重复维护 skill 的执行步骤。

## 常见反模式

- 把测试报告当复盘，把“通过 / 失败”当成原因分析。
- 把 Issue 关闭当复盘完成。
- 把一次事故直接泛化成全项目结论，没有说明适用边界。
- 只按时间线复述开发过程，没有把偏差归到需求、设计、拆解、实现、验证或发布。
- 把下轮行动写成口号，没有 owner、触发条件和完成口径。

---
type: development
id: DEV-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-25
tags: [development]
---

# 开发

这页是研发经理视角的开发主入口。

如果只想判断“现在进度到哪、下一步做什么、这些文件分别看哪一个”，先看 [[projects/development/plan/README]]。本页保留开发层总入口和推进说明，不重复维护总控页正文。

上游：[[projects/design/README]]、[[projects/trace]]、[[projects/decisions]]、[[projects/memory/README]]、[[POLICY]]  \
下游：[[projects/releases]]、[[projects/incidents/README]]

子页：

- [[projects/development/plan/README]]：研发执行总控。
- [[projects/development/plan/work-item-system-model]]：`Gate -> FP -> EP -> TASK` 事项关系模型，以及 risk / issue / test / 验收关系节点。
- [[projects/development/plan/task-design-model]]：TASK 作为父级 EP 下状态化交付合同的设计规则。
- [[projects/development/plan/test-acceptance-planning-model]]：测试计划、AP 验收计划、环境路由和报告计划来源模型。
- [[projects/development/execution/README]]：EP、TASK、待办、编码交接、反馈纠偏和过程记录。
- [[projects/development/gates/README]]：阶段门和准出规则。
- [[projects/development/implementation/README]]：实现指导和候选功能点池。
- [[projects/development/issues/README]]：已发生问题、bug 和偏差的案件档案入口。
- [[projects/development/acceptance/README]]：复杂验收计划、AP、fixture / oracle、人工确认和发布 runbook 入口。
- [[projects/development/reports/README]]：测试计划执行后的证据、测试结论和准出报告。
- [[projects/development/risks/README]]：风险、卡点和待确认项。
- [[projects/development/feature-points/README]]：功能点实体目录。
- [[projects/meetings/README]]

## 这页负责什么

- 说明当前研发推进状态
- 说明阻塞和风险
- 说明下一步
- 汇总需要关注的验证项
- 维护活跃功能点的索引入口，不写单个功能点的完整执行正文

## 功能点推进

设计拆成模块以后，这页只负责整体研发推进和协调。
功能点的执行正文、状态字段和阶段字段都放到 [[projects/development/feature-points/README]] 及其下实体页。

研发经理负责拆解、协调、排期和跟进，不负责重复写单个功能点的执行正文。

### 从架构包往下拆

默认按这个顺序推进，不要跳步：

1. 先从 [[projects/requirements]]、[[projects/trace]] 和 [[projects/design/README]] 确认主工程口径。
2. 如果有既有代码或外部工程，再用 [[projects/codebase/README]]、[[projects/codebase/conflicts]] 和 [[projects/codebase/reuse-boundary]] 对照现实实现，明确可继承、需改造和应舍弃的部分。
3. 发生冲突时先升级到 [[projects/decisions]]，不要直接顺着代码改需求或改设计。
4. 再把已经拍板的主链路拆成功能点，落到 [[projects/development/feature-points/README]] 及其实体页。
5. 再按父 Gate / FP 拆 EP 执行包，并把具体可交付切片拆成 TASK。
6. 再为每个 EP / TASK 补接口、数据变更、验证项、risk / issue / test / 验收关系节点、AP / 报告落点和发布影响。
7. 整体推进状态、阻塞和优先级，才回收到这页。

更细的正式 SOP 统一看 [[WORKFLOW]] 里的 `1.9.6.1 完整架构包到研发拆解`。

### 维护方式

- 这页只保留整体推进状态、阻塞和下一步
- 具体功能点的 `status`、`phase` 和正文都只改对应实体页，不在这里重复维护
- 过程流水写到 [[projects/development/execution/worklog]]
- 正式会议纪要和行动项写到 [[projects/meetings/worklog]]
- 需求为什么这样收敛、哪些修补属于实现纠偏，优先回看 [[projects/trace]]
- 关键取舍写到 [[projects/decisions]]
- 可复用结论写到 [[projects/memory/README]] 或知识库层
- 如果这轮是从架构包进入实现拆解，先检查 FP、EP 和 TASK 是否补上接口、数据、验证、服务台账影响和发布影响，不要只留下标题卡

## 当前关注点

按需要补充：

- 当前阻塞
- 测试关注点
- 下一步

## 维护说明

- 开发推进时如果发现项目记忆、规则边界或决策发生变化，先回写到 [[projects/memory/README]]、[[POLICY]] 和 [[projects/decisions]]
- 功能点状态发生变化时，同步更新对应实体页、[[projects/status]] 和 [[projects/development/execution/worklog]]；如果已经发布，再看 [[projects/releases]]
- 开发页只记录推进过程，不重复写设计正文

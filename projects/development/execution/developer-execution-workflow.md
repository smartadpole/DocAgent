---
type: development_workflow
id: DEV-DEVELOPER-EXECUTION-WORKFLOW-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-25
tags: [development, workflow]
---

# 开发者执行工作流

主入口：[[projects/development/execution/README]]

上游：[[projects/development/plan/README]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/plan/task-design-model]]、[[projects/status]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]]、[[projects/development/execution/todo]]  \
下游：[[projects/development/feature-points/README]]、[[projects/development/issues/README]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/reports/README]]、[[projects/service-registry]]、[[projects/development/execution/worklog]]、[[projects/trace]]

## 这页解决什么

这页回答：

- 开发开始前先看哪几页
- 当前改动归属哪个 Gate / FP / EP / TASK
- 候选功能点什么时候需要变成实体页，临时 TODO 什么时候要提升为 TASK
- 代码工程最终要交付什么回传包
- 代码改完后应该同步哪些文档
- 哪些问题不能由开发者自行拍板

## 主控和实现工程协作边界

这里的主控系统指当前文档库；实现工程指真正改代码的仓库、服务或子模块。

| 协作环节 | 主控系统职责 | 实现工程职责 | 禁止事项 |
| --- | --- | --- | --- |
| 任务下发 | 给出 Gate / FP / EP / TASK、范围、不做项、验收、关闭证据和不上推边界 | 读取指定上下文，确认能否实现 | 实现工程自行扩大需求或改项目状态 |
| 开发执行 | 保持需求、设计、EP / TASK、Issue、报告、台账和风险的单一信息源 | 修改代码、schema、fixture、接口、worker 或配置 | 把主控文档整段复制进代码工程当第二份设计 |
| 测试反馈 | 判断测试结果关闭哪一层事项，并决定是否生成 Issue / 报告 / 台账回写 | 提供命令、结果、日志、失败项和未验证项 | 用“代码已改”替代 TASK / EP / Gate 关闭证据 |
| 回传吸收 | 根据回传包更新 TASK、父 EP、FP、Issue、worklog、测试报告、服务台账、风险、trace 或决策 | 按 [[templates/code-handoff-template]] 交付回传包 | 没有明确授权时直接改主控文档 |
| 冲突升级 | 把需求变化、设计不成立、业务 owner 判断不清的问题分流到 trace、决策、风险或会议 | 标出偏差和待确认项，不代替拍板 | 在实现工程里私自形成新口径 |

默认协作方式是“主控下发上下文，实现工程回传证据，主控吸收回写”。只有任务说明明确授权时，实现工程 agent 才能进入受控回写模式。

## 最短使用方式

1. 从 [[projects/development/plan/README]] 和 [[projects/status]] 确认当前阶段。
2. 先确认当前工作是否已有父 EP 和 TASK；没有父 EP 的事项只能作为待关系校准候选，不能直接派发为正式编码任务。
3. 临时下一步可从 [[projects/development/execution/todo]] 选择，但进入编码前要提升或绑定到 TASK，并写清主责模块、上游需求 / 目标、FP、关系类型和关闭证据。
4. 如果 TASK / TODO 已经是 `review`，先读最新测试报告、Issue 档案、worklog 和回传包，再判断是补修、补测、台账回写还是关闭。
5. 开发前补齐任务执行单里的父 EP、TASK Done Contract、依赖、接口、数据、测试方案、核心用例、相关功能回归范围、联调流程、验收流程、服务台账要求和阻塞项。
6. 完成一个可回看的节点后，在代码工程生成回传包，再由本库侧 Codex 消化并更新 TASK、父 EP、FP、Issue、测试报告、服务台账、worklog、风险、trace 或会议页。
7. 只有测试证据、失败分流、worklog、下游吸收、Issue / risk / service-registry 归口和父项上推边界都闭合，且本轮验收对象确实覆盖 TASK 的关闭语义时，TASK 才能关闭为 `done`。

## 单功能开发闭环

| 阶段 | 代码工程动作 | 本库动作 | 状态变化 | 准出条件 |
| --- | --- | --- | --- | --- |
| 选题 | 不改代码，确认要做的功能或修复 | 绑定 Gate / FP / EP / TASK，临时事项可先留 TODO | TASK 保持 `planned` | 有明确父 EP、TASK、范围、不做项和验收口径 |
| 开发准备 | 拉取代码、确认分支、读取合同和测试命令 | 补齐编码任务执行单；必要时更新 TASK 或父 EP | TASK 可改为 `in_progress` | 开发者知道改哪里、测什么、交什么、不能关闭什么 |
| 编码实现 | 修改代码、schema、fixture、接口、worker 或配置 | 暂不大面积改文档；设计缺口写入 TASK、risk 或会议 | FP / EP 保持执行中 | 代码能本地运行或形成可检查 diff |
| 自测验证 | 运行单测、合同测试、联调或人工检查 | 准备回传包所需证据 | 测试失败不关任务 | 命令、结果、失败项、日志和未验证边界明确 |
| 回传 / 回写 | 整理 diff、测试结果、commit hash、运行证据和偏差 | 更新 TASK、父 EP、worklog、测试报告、Issue / risk / service-registry；必要时更新设计或 trace | 通过自测后 TASK 可转 `review` | 能回答改了什么、测了什么、还差什么、不能上推什么 |
| 验收评审 | 根据反馈修复代码或补测试 | 验收失败进入 Issue / risk / report / TASK 反馈闭环 | 失败保持 `review` 或回到 `in_progress` | 验收人能看到证据、剩余风险和上推边界 |
| 关闭收口 | 代码合并或形成确认版本 | TASK 关闭为 `done`，同步父 EP、FP、报告和必要入口 | `done` | 关闭证据覆盖该 TASK 的关闭语义，父 EP / FP / Gate 另行裁决 |

## 编码任务执行单

默认复制 [[templates/developer-task-brief-template]]，不要在本页维护第二份模板正文。

## 代码工程回传包

代码工程处理 Gate / FP / EP / TASK 时，默认在代码工程内生成回传包。模板见 [[templates/code-handoff-template]]，不要在本页维护第二份模板正文。

回传包不是第二份设计正文，也不是把本库页面复制进代码工程；它只记录实现工程本次读了什么、改了什么、测了什么、还差什么，以及主控文档应该回写到哪里。

代码工程 handoff 是实现证据源，不是普通说明页，也不是本库项目事实源的替代品。每个影响代码语义、联调闭环或验收判断的 EP / TASK，默认至少随代码工程提交 `docs/handoffs/<work-id>/README.md`；原始日志、截图、大样本输出、机器路径、runtime 目录、下载缓存和敏感配置不提交，只写脱敏摘要、命令、相对路径规则和可复现方式。本库侧验收时仍要独立抽插代码、测试、fixture、artifact、日志、服务台账或接口读回，不能因为 handoff 已提交就直接把 TASK / EP 关闭为 `done`。

## 写权限模式

| 模式 | 适用场景 | 允许动作 | 禁止动作 |
| --- | --- | --- | --- |
| 只读上下文模式 | 需求理解、代码设计、实现探索 | 读取本库关键页，引用 Gate / FP / EP / TASK 方案 | 修改本库、改状态、关闭 TASK / EP |
| 受控回写模式 | 一个可回看的开发节点已经完成，且任务说明明确允许写本库 | 按回传包更新命中的 TASK、父 EP、Issue、worklog、测试报告、服务台账和必要设计页 | 顺手重写无关设计、扩大范围 |
| 无写权限回传模式 | 代码工程 agent 只能读本库，或当前不希望它写本库 | 在代码工程生成回传包，由本库侧 Codex 消化 | 让 agent 口头猜测文档状态 |

默认使用“只读上下文模式 + 无写权限回传模式”。直接改本库必须有明确授权。

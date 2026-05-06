---
type: development_workflow
id: DEV-DEVELOPER-EXECUTION-WORKFLOW-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-06
tags: [development, workflow]
---

# 开发者执行工作流

主入口：[[projects/development/execution/README]]

上游：[[projects/development/plan/README]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/execution/todo]]  \
下游：[[projects/development/feature-points/README]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/reports/README]]、[[projects/development/execution/worklog]]、[[projects/trace]]

## 这页解决什么

这页回答：

- 开发开始前先看哪几页
- 候选功能点什么时候需要变成实体页
- 代码工程最终要交付什么回传包
- 代码改完后应该同步哪些文档
- 哪些问题不能由开发者自行拍板

## 主控和实现工程协作边界

这里的主控系统指当前文档库；实现工程指真正改代码的仓库、服务或子模块。

| 协作环节 | 主控系统职责 | 实现工程职责 | 禁止事项 |
| --- | --- | --- | --- |
| 任务下发 | 给出 TODO / FP / Gate、范围、不做项、验收和关闭证据 | 读取指定上下文，确认能否实现 | 实现工程自行扩大需求或改项目状态 |
| 开发执行 | 保持需求、设计、TODO、报告和风险的单一信息源 | 修改代码、schema、fixture、接口、worker 或配置 | 把主控文档整段复制进代码工程当第二份设计 |
| 测试反馈 | 判断测试结果关闭哪一层事项 | 提供命令、结果、日志、失败项和未验证项 | 用“代码已改”替代 TODO / Gate 关闭证据 |
| 回传吸收 | 根据回传包更新 TODO、FP、worklog、测试报告、风险、trace 或决策 | 按 [[templates/code-handoff-template]] 交付回传包 | 没有明确授权时直接改主控文档 |
| 冲突升级 | 把需求变化、设计不成立、业务 owner 判断不清的问题分流到 trace、决策、风险或会议 | 标出偏差和待确认项，不代替拍板 | 在实现工程里私自形成新口径 |

默认协作方式是“主控下发上下文，实现工程回传证据，主控吸收回写”。只有任务说明明确授权时，实现工程 agent 才能进入受控回写模式。

## 单功能开发闭环

| 阶段 | 代码工程动作 | 本库动作 | 状态变化 | 准出条件 |
| --- | --- | --- | --- | --- |
| 选题 | 不改代码，确认要做的功能或修复 | 从 [[projects/development/execution/todo]] 选待办 | TODO 保持 `todo` | 有明确任务 ID、范围、不做项和验收口径 |
| 开发准备 | 拉取代码、确认分支、读取合同和测试命令 | 补齐编码任务执行单；必要时更新功能点页 | TODO 可改为 `doing` | 开发者知道改哪里、测什么、交什么 |
| 编码实现 | 修改代码、schema、fixture、接口、worker 或配置 | 暂不大面积改文档；设计缺口写入待办、风险或会议 | 功能点保持执行中 | 代码能本地运行或形成可检查 diff |
| 自测验证 | 运行单测、合同测试、联调或人工检查 | 准备回传包所需证据 | 测试失败不关任务 | 命令、结果、失败项和日志位置明确 |
| 回传 / 回写 | 整理 diff、测试结果、commit hash 和偏差 | 更新 TODO、功能点、worklog、测试报告；必要时更新设计或 trace | 通过自测后 TODO 可转 `review` | 能回答改了什么、测了什么、还差什么 |
| 验收评审 | 根据反馈修复代码或补测试 | 验收失败进入反馈闭环 | 失败保持 `review` 或回到 `doing` | 验收人能看到证据和剩余风险 |
| 关闭收口 | 代码合并或形成确认版本 | TODO 关闭为 `done`，同步相关入口 | `done` | 关闭证据覆盖该 TODO 的关闭语义 |

## 编码任务执行单

默认复制 [[templates/developer-task-brief-template]]，不要在本页维护第二份模板正文。

## 代码工程回传包

代码工程处理 TODO / FP 时，默认在代码工程内生成回传包。模板见 [[templates/code-handoff-template]]，不要在本页维护第二份模板正文。

回传包不是第二份设计正文，也不是把本库页面复制进代码工程；它只记录实现工程本次读了什么、改了什么、测了什么、还差什么，以及主控文档应该回写到哪里。

## 写权限模式

| 模式 | 适用场景 | 允许动作 | 禁止动作 |
| --- | --- | --- | --- |
| 只读上下文模式 | 需求理解、代码设计、实现探索 | 读取本库关键页，引用 TODO / FP / Gate 方案 | 修改本库、改状态、关闭 TODO |
| 受控回写模式 | 一个可回看的开发节点已经完成，且任务说明明确允许写本库 | 按回传包更新命中的 TODO、FP、worklog、测试报告和必要设计页 | 顺手重写无关设计、扩大范围 |
| 无写权限回传模式 | 代码工程 agent 只能读本库，或当前不希望它写本库 | 在代码工程生成回传包，由本库侧 Codex 消化 | 让 agent 口头猜测文档状态 |

默认使用“只读上下文模式 + 无写权限回传模式”。直接改本库必须有明确授权。

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

```md
## 编码任务执行单

- 任务 ID：
- 上游需求 / 目标：
- 功能点 / 候选项：
- 关系类型：
- 主责模块：
- 目标：
- 范围：
- 不做：
- 输入：
- 输出：
- 接口 / 数据合同：
- 测试方案：
- 核心用例 / 检查点：
- 相关功能回归范围：
- 需要回传的结果：
- 阻塞和待确认项：
```

## 代码工程回传包

代码工程处理 TODO / FP 时，默认在代码工程内生成回传包，推荐路径：

```text
docs/handoffs/<work-id>/README.md
```

轻量或历史兼容任务可以使用单文件形态：

```text
docs/handoffs/<work-id>-<short-topic>.md
```

回传包至少包含：

- **任务身份**：任务 ID、对应 TODO、对应 FP / 候选 ID、上游需求 / 目标、关系类型、当前阶段、主责模块。
- **交付物类型**：代码实现、handoff / artifact 包、接口细化稿、联调闭环证据或报告。
- **读取输入**：读过的本库页面、代码工程文件、外部依赖或命令依据。
- **实现范围**：改了哪些代码、接口、表、状态、配置、错误码或 fixture；同时写清不做项。
- **验证证据**：跑过的命令、测试结果、日志位置、失败项和未验证原因。
- **关闭判断**：当前证据能关闭哪一层对象：代码实现、handoff、TODO 还是 Gate。
- **反馈回写**：应回写到 TODO、FP、测试报告、Gate、trace、设计、风险、会议还是决策。
- **偏差和风险**：设计偏差、合同缺口、外部阻塞、需要 owner 拍板的问题。
- **下一步**：建议继续做什么，以及当前 TODO 建议进入哪种状态。

回传包不是第二份设计正文，也不是把本库页面复制进代码工程。

## 写权限模式

| 模式 | 适用场景 | 允许动作 | 禁止动作 |
| --- | --- | --- | --- |
| 只读上下文模式 | 需求理解、代码设计、实现探索 | 读取本库关键页，引用 TODO / FP / Gate 方案 | 修改本库、改状态、关闭 TODO |
| 受控回写模式 | 一个可回看的开发节点已经完成，且任务说明明确允许写本库 | 按回传包更新命中的 TODO、FP、worklog、测试报告和必要设计页 | 顺手重写无关设计、扩大范围 |
| 无写权限回传模式 | 代码工程 agent 只能读本库，或当前不希望它写本库 | 在代码工程生成回传包，由本库侧 Codex 消化 | 让 agent 口头猜测文档状态 |

默认使用“只读上下文模式 + 无写权限回传模式”。直接改本库必须有明确授权。

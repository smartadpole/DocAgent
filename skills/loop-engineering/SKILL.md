---
name: loop-engineering
description: Loop Engineering / 持续 agent 循环控制技能。用于把 Goal、Run Capsule、子 agent、harness、memory 和软件研发体系组织成可持续的发现、分派、验证、持久化和下一轮决策闭环；它是控制面能力，不是无人值守自动化许可，也不新建平行项目状态系统。
maturity: active
evidence_signals: [skill, README entry, template, governance, verification-loop, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only loop-engineering
---

# Loop Engineering

## 定位

Loop Engineering 是持续 agent 循环控制技能。它在 Goal Contract、[[templates/run-capsule-template|Run Capsule]] 和本工程 Harness / 项目研发体系之上，决定一个复杂问题是否应该从“一次长任务”升级为“持续循环”。

它只回答：这个工程是否具备安全、可停、可验证、可回看的循环条件，以及本轮循环怎样发现输入、分派 Worker、由独立 evaluator 合流、持久化状态并决定下一轮。它不是无人值守自动化许可，不替代项目状态页、Issue、TASK、测试报告、服务台账、memory、log 或 harness ledger，也不新建平行 `loop` 看板。

## 触发条件

满足以下任一条件时使用：

- 用户要求“用 Loop Engineering 武装工程”“持续发现并处理复杂问题”“多 agent 调度”“直到闭环”。
- 已经有 Goal Contract，但任务需要跨多轮发现、分派、验证和状态持久化。
- 复杂问题需要多个子 agent / worker 并行审计、实现或验证，并且主线程必须做 evaluator 合流。
- 需要周期性读取 CI、issue、commit、inbox、监控、服务台账、测试报告、知识链接检查或用户反馈。
- 需要判断某个自动化候选是否具备 Discovery source、Run queue、Evaluator oracle、Persistent state、Scheduler / trigger 和 Budget / stop。

不满足以下条件时，不进入 loop：

- 只有一次性解释、简单编辑或范围未裁定的探索。
- 缺少稳定发现源、持久状态或可复核 oracle。
- 循环会越过人工确认边界，自动关闭状态、合并发布、修改生产事实或改写规则单一信息源。
- 只是想“显得智能”，但没有清楚的停止条件、预算和证据层级。

## 读取顺序

1. [[AGENTS]] 和 [[governance/README]]：确认本工程 agent 边界、响应模式、写权限和单一信息源。
2. [[templates/loop-contract-template]]：建立 Loop Contract，不把运行状态只留在聊天里。
3. Goal Contract 与 [[templates/goal-contract-template]]：固定最终状态、证据边界和停止条件；没有本地 Goal Contract skill 时，使用本工程等价完成契约入口。
4. [[templates/run-capsule-template]]：定义单轮运行、Worker ownership、证据层级、State transition 和 Next-run recommendation。
5. Harness、issue、TASK、risk、AP、报告、服务台账、memory、log 或 feedback ledger 等本工程既有 owner 页面。
6. 变更技能、模板或入口后，运行 `python3 scripts/check_all.py --only loop-engineering`。

## 成熟度与证据信号

- `maturity`：`active`。本工程已具备技能正文、Loop Contract 模板、Run Capsule 模板、README / INDEX / governance 入口和专项 sensor。
- `evidence_signals`：`skill`、`README entry`、`template`、`governance`、`verification-loop`、`sensor`、`TRANSFER`。
- `template`：[[templates/loop-contract-template]] 负责循环控制面，[[templates/run-capsule-template]] 负责单轮执行和 Worker 回传。
- `governance`：启动条件、人工确认边界、禁止自动关闭状态和单一信息源回写在 [[AGENTS]] 与 [[governance/README]] 中可发现。
- `sensor`：`python3 scripts/check_all.py --only loop-engineering` 检查技能、模板、入口、Worker limits、Evaluator oracle、禁止项和 `check_all.py` 接线。
- `TRANSFER`：迁移边界见 [[skills/loop-engineering/TRANSFER]]。
- `evidence boundary`：本技能证明循环控制面具备结构化接线，不证明具体业务事项已经完成、发布、验收或关闭。

## 工作流

### 1. 判定 Loop Readiness

先回答七个问题：

- **Discovery source**：发现源是否稳定，能否重复读取，是否会产生噪音。
- **Run queue**：发现项如何去重、排序、标记 queued / running / passed / partial / blocked / failed / skipped。
- **Delivery boundary**：每个发现项进入只读建议、patch、TASK、Issue、risk、AP、报告、服务台账还是 engineering feedback。
- **Evaluator oracle**：谁判断结果，依据脚本、独立 agent、人工 reviewer、真实运行工具还是组合。
- **Persistent state**：状态落到哪个文件、看板、Issue、数据库、Run Capsule 或服务台账。
- **Scheduler / trigger**：人工触发、定时触发、事件触发还是外部平台触发；本地调度和云端无人值守要分开。
- **Budget / stop**：token、时间、轮次、并发、重试、退避、失败退出和人工复核点是什么。

任一关键项缺失时，结论只能是 `not-ready` 或 `discovery-only`，不能启动写入型 loop。

### 2. 建立 Loop Contract

使用 [[templates/loop-contract-template]] 记录：Objective、Discovery source、Trigger / schedule、Run queue、Agent topology、Worker ownership、Evaluator oracle、Persistence routing、Software-development landing、Budget / stop、Human approval、Rollback 和 Next-run decision。

Loop Contract 是控制面，不是新项目状态页。状态类事实仍回到本工程既有单一信息源。

### 3. 分派 Worker

主线程是 Orchestrator，负责目标、边界、证据和合流。每个 Worker 必须收到：

- scope：本 Worker 只负责什么。
- ownership：允许读 / 写哪些文件，或只读审计。
- inherited context：必须读取哪些规则、Goal、Loop Contract、Run Capsule 或 owning page。
- required evidence：需要回传哪些文件、命令、截图、检查、链接或结论。
- limits：必须写清未验证边界，不能宣布整体闭环。
- output state：passed / partial / blocked / failed。

缺少 `limits`、没有回到同一个 Loop Contract / Run Capsule，或把局部证据写成整体闭环的 Worker 回传，默认不能用于关闭整体循环。

### 4. Evaluator 合流

Evaluator 必须独立判断：

- 发现项是否真实有效，是否重复或误报。
- Worker 证据能关闭哪一层，不能上推到哪一层。
- 是否需要重试、退避、拆分、打回、人工确认或停止。
- 是否产生新候选，以及新候选应进入下一轮还是写成 blocked / backlog。
- 哪些结果进入 no-op、log、harness ledger、memory、skill、template、sensor、rule 或 software-development。

生成者自评、测试全绿、PR 已开、handoff 自述、health 或 accepted / running 状态都不能替代 evaluator。

### 5. 持久化和下一轮

每轮收口至少写清：

- consumed inputs：本轮消费了哪些发现项。
- state transition：queued / running / passed / partial / blocked / failed / skipped 如何变化。
- evidence landing：证据落到哪里。
- next-run decision：stop / rerun / retry-after / split / escalate / wait-human / schedule-next。
- prune decision：哪些候选是噪音，应降级、合并或删除。

如果发现软件研发问题，默认落到既有 Gate / FP / EP / TASK、risk、Issue、AP、测试报告、服务台账或 engineering feedback，不新建 loop 看板。

## 输出格式

```markdown
**Loop Engineering**
- Mode: discovery-only / assisted-patch / structured-auto-fix / not-ready
- Discovery source:
- Trigger / schedule:
- Run queue state:
- Orchestrator:
- Worker topology:
- Evaluator oracle:
- Persistent state:
- Budget / stop:
- Human approval:
- Software-development landing:
- Persistence routing:
- Next-run decision:
- Sensor / quality-gate:
```

## 验证

- Loop 技能、模板或入口接线变更后运行 `python3 scripts/check_all.py --only loop-engineering`。
- 同时改了 Harness、Goal、Run Capsule 或治理入口时，再运行本工程已有相关检查，例如 `harness-governance`、`skill-maturity` 或 `transferable-skills`。
- 收尾前按本工程规则决定是否运行完整 `python3 scripts/check_all.py`；不得运行会写业务产物的脚本作为验证替代。

## 禁止项

- 不把 Loop Engineering 当无人值守自动化许可。
- 不新建平行 `loop/` 状态系统、平行任务看板或第二套项目真相源。
- 不让 Worker 自述、模型自评、health、日志、accepted / running 或历史报告上推成完成。
- 不自动关闭 Gate / FP / EP / TASK / Issue / release，不自动合并、发布或改生产事实。
- 不让本地定时任务伪装成云端可靠调度；必须写清机器、会话、profile、权限和失效边界。
- 不因“更智能”而扩大读取、写入、子 agent 数量或调度频率，除非收益超过协调和验证成本。

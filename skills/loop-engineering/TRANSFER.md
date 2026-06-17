---
type: skill-transfer
skill: loop-engineering
updated: 2026-06-17
---

# Loop Engineering Transfer

## 能力目标

让目标工程具备受控循环能力：发现输入、形成队列、分派 Worker、独立评价、持久化状态并决定 `stop / rerun / retry-after / split / escalate / wait-human / schedule-next`。迁移目标不是新增一个 loop 目录、一个模板或一段说明，而是建立一套可持续运行的 agent 循环控制面。

## 可以吸收

- Loop 方法入口：何时从一次性 Goal / Run Capsule 升级为 loop，以及何时只能 `not-ready` 或 `discovery-only`。
- Loop Contract 字段：Objective、Discovery Source、Trigger / Schedule、Run Queue And State、Agent Topology、Worker Ownership、Evaluator Oracle、Persistence Routing、Budget And Safety、Next-run Decision。
- Run Capsule / Worker 回传接线：Parent Loop Contract、Input discovery item、Allowed writes、Required evidence、Limits、State transition、Next-run recommendation。
- Evaluator oracle：脚本、独立 agent、人工 reviewer 或真实运行工具；禁止生成者自评替代 evaluator。
- Persistence routing：no-op、log、harness ledger、memory、skill、template、sensor、rule、software-development 或目标工程等价项。
- Scheduler / trigger 与安全边界：人工、定时、事件、外部平台、本地调度失效边界、重试 / 退避、人工批准和 rollback。
- Sensor / 检查或结构化 review：入口存在、模板字段、Worker limits、Evaluator oracle、禁止项、单一信息源和检查命令。

## 只能抽象吸收

- 上游工程的项目状态、业务事实、服务实例、运行 ID、历史 handoff、矩阵排行和 source revision 只能作为方法参考，不能写进目标工程事实源。
- 目标工程已有 issue / task / risk / report / service registry / memory / log / feedback ledger 时，Loop 结果必须分流到这些 owner 页面；没有时先建立等价记录落点，不硬造平行看板。
- 目标工程没有 `skills/`、`templates/` 或 `scripts/check_all.py` 时，可把能力落到 agent workflow、governance 入口或结构化 review 清单，但仍要保留 Worker limits、Evaluator oracle 和 Next-run decision。
- 业务循环脚本只能作为 discovery source、Worker 工具或 evaluator oracle 候选，不能冒充 Loop Contract 或持久状态。

## 禁止复制

- 禁止复制 AcknowledgeBase 或其他源工程的项目事实、业务名、数据库表、服务名、运行 ID、本地 handoff、历史报告或一次性状态。
- 不把 Loop Engineering 迁移成无人值守自动化许可。
- 不新建平行 `loop/` 状态系统、平行任务看板或第二套真相源。
- 不自动关闭 Gate / FP / EP / TASK / Issue / release，不自动合并、发布、改生产事实或改高优先级规则。
- 不让 Worker 自述、模型自评、health、日志、accepted / running 或测试全绿替代 evaluator。

## 目标工程结构自检

1. 是否已有 `AGENTS.md`、README / INDEX、governance、skills、templates、scripts 和项目状态 / issue / task / report 入口。
2. 是否已有 Goal Contract、Run Capsule、handoff、task brief、runbook 或等价运行控制面。
3. 是否有稳定 Discovery source、可去重 Run queue、Persistent state 和 Evaluator oracle。
4. Loop 结果应回写到哪些单一信息源：issue、TASK、risk、AP、report、service-registry、memory、log、harness ledger 或 engineering feedback。
5. 哪些动作必须人工批准：写入生产、合并、发布、关闭状态、改规则、启用定时调度或外部事件触发。
6. 是否已有检查脚本；若无，至少写结构化 review 清单覆盖入口、模板字段、Worker limits、Evaluator oracle、禁止项和单一信息源。

## 验证要求

- `contract`：有 Loop Contract 或等价控制面，能记录 discovery source、queue、state、evaluator、budget 和 next-run decision。
- `quality-gate`：有脚本、真实运行工具、人工 reviewer 或独立 agent evaluator。
- `verification-loop`：每轮能把结果映射为 passed / partial / blocked / failed / skipped。
- `sensor`：有机器检查或结构化 review，防止概念页孤立、状态只留聊天、Worker 自评替代 evaluator。
- `entry`：README / INDEX / AGENTS / governance / skills / templates 入口能发现 skill、Loop Contract、Run Capsule 和检查命令。

## 目标工程落地顺序

1. 先补 Loop Contract 模板或等价字段。
2. 再把 Run Capsule / Worker 回传格式接入目标工程 agent 规则。
3. 再定义 Discovery source、Run queue、Persistent state 和 Evaluator oracle。
4. 再补 sensor，至少检查 loop 入口、模板字段、Worker limits、Evaluator oracle、禁止项和 `check_all.py` 接线。
5. 最后才考虑小范围、可回滚、人工批准的 assisted patch loop。

## 最终交付要求

目标工程 agent 必须说明：已更新位置、检查结果、未验证边界、未自动执行的动作和后续需要人工批准的事项。若用户禁止提交 commit，最终回复必须明确未提交。

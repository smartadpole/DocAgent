# Codex Local Adapter

本文件是当前 wiki 的 Codex 本地入口适配层。完整维护约束仍以根目录 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[response-mode-routing]] 和 [[harness-evolution]] 为准。

## 每轮启动

- 先读根目录 `AGENTS.md`。
- 再按 [[response-mode-routing]] 判断响应模式：快速诊断、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传或批处理。
- 如果涉及 Harness 自演进、用户纠偏、检查失败、模式切换或规则反哺，再读 [[harness-evolution]] 和 [[harness-feedback-ledger]]。

## 工作阶段检查

- 工作阶段优先跑专项 sensor：`python3 scripts/check_all.py --only harness-governance`。
- 收尾或提交前跑完整门禁：`python3 scripts/check_all.py`。
- `scripts/check_all.py` 是本库本地门传真相源；CI 或平台配置只是适配层。

## 写入边界

- 当前库是模板级 Harness，只吸收系统层规则、流程、模板、技能和自动化契约。
- 从下游工程反哺时，不复制项目事实、业务名、运行实例、具体状态或一次性测试证据。
- episode 先写入 [[harness-feedback-ledger]]，不要因为单次纠偏直接新增硬规则。

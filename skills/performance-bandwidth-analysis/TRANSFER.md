# Performance Bandwidth Analysis Transfer

## 能力目标

把下游工程打磨出的性能、带宽、trace 和容量分析方法迁移成通用证据合同：先分层、再测量、再归因、再优化，并明确哪些数字不能上推为生产容量。

## 可以吸收

- 触发条件：性能、延迟、吞吐、带宽、trace、并发、容量预算。
- 事实源分层：client wall、service timing、runtime artifact、server log、API readback、DB / receipt、UI / report。
- coverage matrix 字段：入口、样本、payload、并发、环境、revision、配置、artifact、未覆盖边界。
- 输出口径：`confirmed / partial / blocked` 与不可上推边界。

## 只能抽象吸收

- 具体工程的生产链路、服务拓扑、调度系统、表结构、artifact root、运行 ID 和业务分母只能作为目标工程事实，不进入通用 skill。
- 某个工程里有效的性能阈值、容量目标或配置默认值不能跨工程复用。

## 禁止复制

- 不复制服务名、机器地址、端口、数据库表、账号、DSN、运行 ID、批次 ID、业务状态或一次性 handoff。
- 不复制只对某个模型、数据集、客户场景或生产环境成立的容量数字。

## 目标工程结构自检

目标工程采纳前必须确认：

- `local_source_of_truth`：性能事实写入哪个 TASK / report / service registry / issue。
- `allowed_write_scope`：agent 是否允许修改 runtime、配置、脚本或只读诊断。
- `required_profile`：需要哪些入口、样本、并发档、artifact 和 readback。
- `validation_command`：本地检查、service-side readback、完整链路 run 或人工确认是什么。
- `blocked_when_missing`：缺 timing、缺 artifact、缺完整链路、缺业务分母或缺权限时如何降级。

## 验证要求

- 本仓结构验证：`python3 scripts/check_all.py --only skill-maturity,agent-control-plane-hardening`。
- 目标工程运行验证：必须使用目标工程自己的 runtime readback、报告和 owner 页面；不能用本仓 skill 存在证明性能结论。

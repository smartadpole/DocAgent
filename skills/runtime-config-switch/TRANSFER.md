# Runtime Config Switch Transfer

## 能力目标

把下游工程中的配置切换经验抽象成通用 runtime 变更合同：确认配置边界、最小编辑、live readback、default path proof、smoke、cleanup、service-registry 回写和 rollback。

## 可以吸收

- 配置切换触发条件和 out-of-scope 判定。
- live readback 证据链：文件、进程 / runtime endpoint、部署参数、日志、health、默认路径证明。
- 低风险 smoke、cleanup、rollback 和 owner 回写顺序。
- secret 不入 tracked 文档的守卫。

## 只能抽象吸收

- 具体服务的重启命令、配置文件路径、部署系统、feature flag 名称、base URL、端口和 callback 只能留在目标工程。
- 某个项目的 synthetic ID、验证样本、读回账号、清理 SQL 或服务台账格式不能原样迁移。

## 禁止复制

- 不复制真实环境变量、secret、DSN、token、机器地址、端口、账号、服务名、业务 URL 或一次性运行证据。
- 不把某工程的 config switch smoke 写成本仓的 runtime validation。

## 目标工程结构自检

目标工程采纳前必须确认：

- `local_source_of_truth`：service registry / TASK / report / log 的真实落点。
- `allowed_write_scope`：agent 是否有权限编辑配置、重启服务、触发 smoke 或清理数据。
- `required_profile`：哪些配置源、deployment params 和 runtime readback 必须检查。
- `validation_command`：health、runtime endpoint、smoke、readback 和 cleanup 如何证明。
- `blocked_when_missing`：无权限、活动任务风险、缺回滚源、缺 runtime readback 或缺 cleanup 时如何停下。

## 验证要求

- 本仓结构验证：`python3 scripts/check_all.py --only skill-maturity,agent-control-plane-hardening`。
- 目标工程 runtime 验证：必须由目标工程 live service / registry / report 证明；本仓技能只提供通用合同。

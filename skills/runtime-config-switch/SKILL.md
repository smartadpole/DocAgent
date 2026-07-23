---
name: runtime-config-switch
description: Runtime 配置切换技能。用于只改配置、不改代码的服务入口、base URL、端口、环境变量、feature flag、部署参数、回调地址、写入目标或上游依赖切换，并证明 live service 正在使用新配置。
maturity: active
evidence_signals: [skill, README entry, TRANSFER, governance, sensor, runtime-readback]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity,agent-control-plane-hardening
---

# Runtime Config Switch

## 定位

本技能处理配置型 runtime 变更。目标不是证明文件被改了，而是证明正在运行的服务使用了新配置，并且 owner 页面、验证报告、回滚边界和清理动作都能回看。

如果变更需要代码逻辑、schema、payload contract、模型行为、批处理策略或权限边界变化，必须停下改判为实现任务或设计任务。

## 成熟度与证据信号

| signal | 本技能状态 |
| --- | --- |
| skill | 本页定义配置切换的 preflight、执行、readback、cleanup 和 closeout。 |
| README entry | [[skills/README]] 提供入口。 |
| TRANSFER | [[skills/runtime-config-switch/TRANSFER]] 定义迁移边界。 |
| governance | [[state-constraint-reasoning]]、[[agent-orchestration]]、[[projects/service-registry]] 承接权限、控制面和运行事实。 |
| sensor | `agent-control-plane-hardening` 检查本技能和跨工程控制面 owner 的接线。 |
| evidence boundary | 文件 diff、health 或接口回显都不能单独证明默认 runtime 已切换。 |

## 触发场景

- 用户说只改配置、不改代码、换 base URL、换 port、改 env、改部署参数、改 feature flag、改 callback、改 write target、切上游服务。
- 需要证明服务重启 / 热加载后使用新配置。
- 需要把配置事实写回 service registry、TASK、报告、log 或 rollback 记录。
- 需要区分默认路径和请求级 override。

## 工作流

1. **确认配置边界**：列出 in-scope key/value 和 out-of-scope code/schema/contract 变更。
2. **命名 owner**：运行事实进入 service registry 或目标工程等价 owner；任务状态进入 TASK / Issue；验证证据进入报告。
3. **枚举配置来源**：检查 env、runtime JSON/YAML、部署参数、ignored local config、生成配置、请求默认值和 served config。
4. **preflight 变更窗口**：检查活动任务、服务健康、重启方式、回滚来源和权限边界。
5. **备份与最小编辑**：只改目标 key/value，不打印或持久化 secret，不覆盖整个 profile。
6. **重启 / reload**：使用目标工程记录的 runbook；不重置无关服务。
7. **live readback**：读取文件、进程 env / runtime endpoint、service health、部署参数、日志或等价 service-side target。
8. **证明默认路径**：优先证明默认 runtime target；请求级 override 只能作为辅助证据。
9. **最小副作用 smoke**：使用合成 ID 或低风险输入，捕获 receipt/status；如涉及持久化，分开记录 ingress/receipt 与 DB/service-side readback。
10. **cleanup 与回写**：清理 synthetic 数据，更新 service registry / TASK / report / log，写清 rollback 和未覆盖边界。

## 输出格式

```markdown
**配置切换结论**
- state：passed / partial / blocked
- changed key：
- old / new boundary：

**Live Readback**
- file/config：
- process/runtime endpoint：
- deployment params：
- health/log：
- default path proof：

**Smoke / Cleanup**
- side effect：
- receipt：
- readback：
- cleanup：

**回写**
- service registry：
- task / issue：
- report / log：
- rollback：
```

## 回写守卫

- 非 secret runtime fact 写入目标工程 service registry 或等价 owner。
- secret、真实 token、DSN、密码、个人路径和临时值只允许存在于本地安全配置或运行时，不进入 tracked 文档。
- 配置切换 smoke 只能关闭配置切换任务，不能上推关闭模型质量、性能容量、业务验收、发布 Gate 或父 EP。

## 禁止项

- 不把文件 diff 当 runtime proof。
- 不把 health 当新配置已消费证明。
- 不用请求级 override 替代默认配置切换。
- 不在活动任务风险不清时重启服务。
- 不打印、提交或沉淀真实 secret。
- 不用配置 smoke 关闭无关业务任务、性能任务或发布验收。

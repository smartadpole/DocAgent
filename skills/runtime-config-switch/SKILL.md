---
name: runtime-config-switch
description: 在授权范围内切换服务运行配置，并用 live service 和默认路径证据确认生效；适用于配置变更，不把文件修改或请求 override 当作运行切换。
maturity: active
evidence_signals: [skill, README entry, TRANSFER, governance, sensor, runtime-readback]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity,agent-control-plane-hardening
---

# Runtime Config Switch

证明正在运行的服务消费新配置，而不仅是文件 diff。需要代码、schema、payload contract、模型行为或权限变化时重新判范围；已有授权涵盖则按实现流程继续，缺少必要授权才请求补充。

## 变更前

确认目标 key/value 与允许写入、重启、smoke、cleanup 的范围。查明配置来源及优先级：env、runtime JSON/YAML、部署参数、ignored local config、生成配置、请求默认值与 served config，只读相关来源。

检查活动任务、服务健康、变更窗口、runbook、回滚来源和写入目标。活动任务风险不清时不重启。记录可恢复旧值但不打印、提交或持久化 secret；不覆盖整个 profile。

## 执行与证明

最小编辑后按目标 runbook reload/restart，避免影响无关服务。live readback 将配置文件/部署参数与实际进程、runtime endpoint、服务端目标或等价证据关联起来。health 只是辅助证据。

证明 default path proof：未提供请求级 override 的真实默认路径使用新目标。override 成功不能替代默认配置切换。必要时使用合成 ID 或低风险输入做最小 smoke；涉及持久化时分别记录 ingress/receipt 与 DB/service-side readback。

清理本轮 synthetic 数据，验证清理结果，保留回滚方式和未覆盖边界。若关键 runtime readback 缺失，文件修改可报告已完成，但运行切换保持 partial/blocked。

## 记录与权限

非敏感运行事实进入 service registry 或等价 owner，任务状态和验证证据回到原 TASK/Issue/report，不重复建状态源。secret、token、DSN、密码不进入 tracked 文档。

配置 smoke 只支持配置切换结论，不能关闭模型质量、性能容量、业务验收、发布 Gate 或父 EP。专项结构检查：`python3 scripts/check_all.py --only agent-control-plane-hardening`；真实完成由 live service 证据证明。迁移见 [[skills/runtime-config-switch/TRANSFER]]。

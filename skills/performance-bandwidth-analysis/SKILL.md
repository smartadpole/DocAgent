---
name: performance-bandwidth-analysis
description: 性能、计时 trace 与带宽分析技能。用于诊断延迟、吞吐、传输、并发、runtime trace、服务入口、调度系统和端到端链路之间的差异，避免把单点指标误上推为生产容量或业务闭环。
maturity: active
evidence_signals: [skill, README entry, TRANSFER, governance, sensor, verification-loop]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity,agent-control-plane-hardening
---

# Performance Bandwidth Analysis

## 定位

本技能用于把“慢”“吞吐不够”“带宽不够”“trace 能不能支撑归因”“单点 probe 能不能代表 production / 生产”这类问题拆成可验证的性能账本 `timing ledger`。

它不是优化方案生成器。正确顺序是：先冻结入口和业务分母，再建立计时账本，再跑足够贴近目标形态的完整链路，最后才判断瓶颈和优化优先级。缺少模块级 timing、coverage matrix、runtime / service-side readback 或业务分母时，只能给 `partial / blocked`，不能写强根因；所有局部数字都要写清不可上推边界。

## 成熟度与证据信号

| signal | 本技能状态 |
| --- | --- |
| skill | 本页定义触发、证据分层、工作流、输出和禁止项。 |
| README entry | [[skills/README]] 提供入口。 |
| TRANSFER | [[skills/performance-bandwidth-analysis/TRANSFER]] 定义跨工程迁移边界。 |
| governance | [[agent-orchestration]] 与 [[wiki-governance-system-contract.v1]] 承接控制面和不上推边界。 |
| sensor | `agent-control-plane-hardening` 检查本技能、runtime-config-switch、跨工程对齐图和控制面 owner 的接线。 |
| evidence boundary | 结构接线不证明具体工程性能提升；每个工程必须用自己的 runtime evidence 证明。 |

## 触发场景

- 用户关注性能、带宽、吞吐、延迟、耗时、计时、trace、传输、上传、下载、打包、并发、容量预算或链路残差。
- 需要比较 direct API、业务 wrapper、调度任务、UI 入口、SSH / raw transfer、HTTP upload-only、服务端处理和端到端链路。
- 需要区分本机、远程服务、GPU / 模型服务、业务服务、数据库、队列、调度系统和外部依赖各自贡献的耗时。
- 需要判断某次 smoke、单请求、局部 probe、API readback、health、日志片段或 batch summary 能不能支持生产容量结论。

## 工作流

1. **冻结入口和分母**：说明这是 direct API、业务 wrapper、调度任务、UI 操作还是生产链路；并发单位是 request、item、file、order、store、worker、backend slot 还是 batch。
2. **建立计时账本**：至少分出 payload / encode、网络传输、入口读取、排队 / semaphore / pool wait、核心处理、响应返回、业务解析、持久化和调度等待。
3. **统一证据分层**：区分 client wall、service-side timing、runtime trace artifact、server log、API readback、DB / receipt、UI / report。它们不能互相替代。
4. **跑完整链路或降级**：目标是生产容量时，必须有接近目标形态的完整链路 run；只有局部 probe 时，结论状态上限为 `partial`。
5. **维护 coverage matrix**：记录入口、样本、payload、大小档、并发档、环境、revision、配置、成功 / 失败、artifact 和未覆盖边界。
6. **做分层归因**：先解释每层耗时占比、共享等待和失败分类，再判断瓶颈；不能先写结论再补证据。
7. **输出优化动作**：每个动作绑定 owner、预计影响层、复测指标、质量边界、回滚方式和复跑矩阵。

## 输出格式

```markdown
**结论**
- 当前能证明什么：
- 当前不能证明什么：

**计时账本**
- entrypoint：
- business denominator：
- measured layers：
- missing layers：

**覆盖矩阵**
- samples / payloads：
- concurrency：
- runtime / service-side readback：
- artifacts：

**采信边界**
- 可作为生产容量证据：
- 只能作为局部诊断：
- blocked / partial：

**下一步**
- instrumentation：
- full-chain run：
- optimization candidate：
```

## 回写守卫

- 性能报告是验证证据，不替代 Issue / TASK / Gate / service registry 的单一信息源。
- 运行时事实、服务版本、配置、PID、端口、artifact 路径和当前状态回到目标工程自己的 owner。
- 只有可复用的分层方法、检查字段、禁止项或模板能力才反哺 wiki / AcknowledgeBase。

## 禁止项

- 不把 raw transfer 当作 HTTP / business wrapper 吞吐。
- 不把 upload-only 当作端到端业务链路。
- 不把单请求、单图、小样本 smoke 或 health 当作生产容量。
- 不把不同样本、不同 payload、不同配置、不同并发单位的数字写成同一阶段前后对比。
- 不把 API readback 当作 trace 文件落盘证明。
- 不把调度日志当作模块级 timing 证明。
- 不在缺少完整链路、模块计时、coverage matrix 或业务分母时写“瓶颈已确认”。

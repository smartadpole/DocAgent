---
name: performance-bandwidth-analysis
description: 分析延迟、吞吐、带宽与并发瓶颈，区分客户端、服务、持久化和端到端证据；局部测量可支持局部判断，生产容量需要代表性完整链路。
maturity: active
evidence_signals: [skill, README entry, TRANSFER, governance, sensor, verification-loop]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity,agent-control-plane-hardening
---

# Performance Bandwidth Analysis

先明确要证明的是局部性能、具体瓶颈还是生产容量，再选择足够支持该结论的测量范围。缺生产链路不妨碍确认有直接证据的局部瓶颈，但不能将局部结果上推生产容量。

## 入口与计时

固定 entrypoint 与 business denominator：direct API、业务 wrapper、调度任务、UI、raw transfer、upload-only 或端到端；并发单位是 request、item、file、worker、backend slot 还是 batch。

建立 timing ledger，测量实际相关层：payload/encode、传输、入口读取、队列/semaphore/pool wait、核心处理、响应、解析、持久化和调度等待。区分墙钟与累计时间、串行与重叠区间，报告未解释残差，不能相加重叠耗时制造归因。

client wall、service-side timing、runtime trace artifact、server log、API readback、DB/receipt、UI/report 各证明不同事实。API readback 不证明 trace 文件落盘；调度日志不证明模块 timing。

## 对比与归因

coverage matrix 记录与结论有关的入口、样本/payload 大小、并发、环境、revision、配置、成功失败、artifact 和未覆盖边界。比较前后必须保持分母及主要条件可比，说明冷热启动、缓存、排队、重试和失败样本对结果的影响。

依据分层耗时、等待、负载变化与反证判断瓶颈；验证最能区分候选原因的条件。只有相关层测量缺失时才降低该层结论，不将一个缺口降级所有直接观察。

生产容量结论必须覆盖接近目标形态的完整链路与代表性负载、失败率和 service-side readback。单请求、小样本 smoke、health、raw transfer 或 upload-only 只支持对应局部判断。

## 建议与边界

优化建议绑定影响层、复测指标和质量约束；实际改变配置或运行方式时补 owner 与回滚条件。报告明确当前能证明什么、尚缺什么及下一项验证，避免虚假的精确容量数字。

性能事实进入目标工程报告/事项/服务 owner；通用层只吸收分层方法。结构检查：`python3 scripts/check_all.py --only agent-control-plane-hardening`，不替代 runtime evidence。迁移见 [[skills/performance-bandwidth-analysis/TRANSFER]]。

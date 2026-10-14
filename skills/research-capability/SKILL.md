---
name: research-capability
description: 围绕需要证据的研究问题形成可追溯判断和决策建议；按风险与深度选择技术分支或专业方法，简单事实查询不启动完整研究合同。
maturity: leading
adoption_level: strong-template-kernel
evidence_signals: [skill, README entry, governance, template, TRANSFER, sensor, quality-gate, verification-loop, positive-fixture, negative-fixture, outcome-boundary]
transfer_ready: true
sensor: python3 scripts/check_all.py --only research-capability
conditional_sources: [skills/research-capability/references/deep-research.md, skills/research-capability/reference/research-method-route-map.md]
---

# Research Capability

研究应回答用户的问题及证据对决策的含义。先复用已有目标与 owner，明确对象、关键问题、适当深度和输出；不预设正式报告、intake 队列或固定字段全集。

## 深度与路由

| 深度 | 适用目的 | 证据边界 |
| --- | --- | --- |
| R0 线索 | 判断材料价值和下一项核验 | 初步线索不等于事实已确认 |
| R1 桌面初筛 | 比较方向、筛选候选 | 桌面证据不等于本地可用 |
| R2 验证计划 | 为 PoC/用户/市场验证设计样本、指标与退出条件 | 计划不等于验证已完成 |
| R3 结构分析 | 解释机制、生态、替代路线与风险 | 反证与覆盖缺口须可追溯 |
| R4 尽调/接入 | 支撑采购、合作或长期承诺 | 需三角核验和相应专业批准边界 |

技术、开源、行业/AI、产品或 PoC 使用 [[skills/technology-research/SKILL]]。市场、用户、竞争、尽调、科研、政策、战略前瞻或证据不全的判断，仅在相应问题出现时读取 [[skills/research-capability/reference/research-method-route-map]]。

R2+、正式研究报告，或需要重复采集/解析的外部信息流，按模式读取 [[skills/research-capability/references/deep-research]]。单个链接、截图或短答不自动建立完整 intake。

## 证据与判断

区分 L1 一手事实、L2 权威分析、L3 产业信号、L4 媒体/社区线索、L5 推论和 L6 建议。等级是来源性质，不保证内容正确；关键陈述仍核对原文、方法、范围和相互独立性。价格、版本、license、release、政策、CVE、benchmark、平台能力等变化事实查当前一手来源。

给出 So-What、必要的 counter-evidence / 反证、替代解释、deal-breaker / 阻断条件和不确定性。行动建议使用适合领域的表达；技术采用可用 Adopt / Trial / Assess / Hold / Blocked 以及直接使用/封装/Fork/参考/放弃/观察，不强迫市场、政策或科研套技术采购枚举。

收到新材料先判 materiality：重复或澄清可局部修订；结论或架构变化则重新核验受影响判断、反证和行动，更新实际消费结论的 owner。不能仅在报告尾追加摘录，也不要求无关结论全部重算。

## 交付与落位

输出可追溯证据、结论、适用边界和下一步；正式资产保留读者可见的原文/source ledger/数据快照入口。需要长期保存时按文章、概念、项目决策、报告等现有 owner 落位，并使用 [[skills/knowledge-linking/SKILL]]。

研究不是采购、合规、安全或验收批准。desk evidence、local validation、PoC、service/runtime readback 与 human approval 分层；没有与 claim scope 相符的证据，不声称生产可用或正式接入完成。确定性 sensor、作者自评不能冒充独立 outcome review。

治理 owner：[[governance/research-capability-rules]]。结构与合同检查：`python3 scripts/check_all.py --only research-capability`；迁移见 [[skills/research-capability/TRANSFER]]。

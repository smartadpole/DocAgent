---
name: technology-research
description: 研究技术机制、开源工程、行业/AI方向、产品或 PoC 的可用性与选择；公共研究证据规则复用 research-capability，按对象保留专业验证。
maturity: leading
adoption_level: strong-template-kernel
evidence_signals: [skill, README entry, governance, template, TRANSFER, source-plan, coverage-matrix, revision-loop, outcome-boundary]
transfer_ready: true
sensor: python3 scripts/check_all.py --only research-capability
---

# Technology Research

这是 [[skills/research-capability/SKILL]] 的技术执行分支。复用研究目标、深度、来源分层、当前性与结论更新规则，不建立第二套合同或输出模板。

## 对象差异

| 对象 | 需要回答 | 关键验证 |
| --- | --- | --- |
| 技术概念/路线 | 解决什么问题、机制与假设、替代方案、适用/不适用场景 | 对关键机制核验原始论文/标准/文档，区分理论与实际约束 |
| 开源工程/GitHub/Hugging Face | 项目画像、维护健康、license/供应链、架构、效果性能、集成与退出成本 | release/issue/依赖直接证据；需要采用判断时按 claim scope 做运行验证 |
| 行业/AI赛道/公司群体 | 技术路线、产品应用、竞争/开源生态、机会与风险 | 比较独立一手证据，区分产业信号与已发生事实 |
| 产品/公司 | 用户价值、能力边界、交付形态、定价/成本、依赖与替代 | 官方能力和实际体验分开，采购/合规结论由相应 owner 裁决 |
| PoC | 哪个假设待验证、样本、指标、成功和失败退出条件 | 代表性输入、基线与反例、非默认/边界条件、质量和成本 |
| 本地源码工程 | 具体实现、调用路径、合同与运行行为 | 使用 [[projects/codebase/source-code-audit-workflow]]，外部资料不替代源码审计 |

以上是决策维度，按问题取舍，不为所有对象展开全部章节。R2+ 需要的 Source Plan checkpoint、coverage matrix、Evidence Delta Re-open 与修订机制由研究总技能的条件参考承接。

## 判断与建议

成熟度可使用 TRL 或工程成熟度说明，行动可使用 Adopt / Trial / Assess / Hold / Blocked；只有有用时输出等级，避免装饰性打分。判断联系机制证据、本地约束、替代方案、反证、deal-breaker、维护和迁移成本。

技术使用策略可为直接使用、封装使用、Fork、只参考、放弃或继续观察。解释为什么、适用范围与下一项最有区分力的验证。Star、README 宣传、新闻热度或旧 benchmark 不证明可用；单次跑通不证明生产可用。

版本、API、license、价格、CVE、模型能力等事实要核对当前来源。没有运行、PoC 或本地约束验证时保留对应未验证边界。研究结论不替代项目决策、采购批准或运行验收。

正式资产按需要使用 [[templates/technology-research-report-template]]，保留溯源入口与刷新触发；长期知识补入口与回链。相关检查：`python3 scripts/check_all.py --only research-capability`。迁移见 [[skills/technology-research/TRANSFER]]。

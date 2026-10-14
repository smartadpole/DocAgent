---
name: historical-dialogue-retrospective
description: 复盘历史对话或 Agent 工作过程中的目标理解、执行、验证与协作偏差；短问因先快诊，明确深度复盘时还原首轮目标、纠偏序列和原始执行证据。
maturity: leading
evidence_signals: [skill, README entry, template, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only retrospective-system,skill-maturity
conditional_sources: [skills/historical-dialogue-retrospective/references/deep-review.md]
---

# Historical Dialogue Retrospective

本技能是 [[skills/retrospective-capability/SKILL]] 的 Agent 工作分析分支。评价 agent 如何理解目标、用证据推进、验证与交付；不替代项目验收或 Issue 案件。

## 选择范围

“有没有问题”“为什么慢”先给最可信结论、依据和缺口。明确复盘请求按总入口处理；用户要求深度/完整历史复盘，或重复失守需要系统性调查时，读取 [[skills/historical-dialogue-retrospective/references/deep-review]]。不因每次收尾、多 agent、普通纠偏而自动全量复盘，也不输出无触发的 no-op 声明。

## 证据地图

| 来源 | 可证明 | 限制 |
| --- | --- | --- |
| 当前上下文 | 最新目标与约束 | 不代表完整历史 |
| 原始 session / rollout | 对话、工具调用与执行过程 | 限定时间窗，按缺口取证 |
| git diff / commit | 实际修改及提交边界 | 不能单独证明用户意图或行为效果 |
| 检查 / 测试输出 | 做过哪些验证、结果如何 | 通过不等于业务闭环 |
| log / ledger | 主题历史和已识别结构问题 | 整理记录，不是原始执行轨迹 |
| 受影响 owner | 当前落库内容 | 历史判断需匹配当时 revision |
| memory | 定位偏好、路径和历史线索 | 回到原始证据验证 |
| 最终回复 / handoff | 当时声称与交付表达 | 不能代替 diff、测试或运行事实 |

从用户目标和实际结果出发，追踪决定性理解、读取、执行、验证和纠偏事件。结论标明 confirmed / likely / possible / blocked，保留反证，缺原始记录就降低证据强度。

## 改进与交付

区分必要成本、重复读取/无效流程成本和返工成本。根据证据选择改进 owner：一次表现保留学习；重复机制失守进入 ledger；可执行检查进入 sensor；模板/skill 只承接可复用方法。不要把一次偏差升级硬规则，也不要预先认定“增加更多规则”是答案。

长期复盘档案、索引、上轮行动兑现与行动分流沿用总技能；最终回复摘要结论和实际落点。相关验证：`python3 scripts/check_all.py --only retrospective-system`。迁移见 [[skills/historical-dialogue-retrospective/TRANSFER]]。

---
name: research-capability
description: 调研 / 研究能力聚合技能。用于把技术、开源工程、产品、公司、行业、AI、PoC 和源码工程研究统一到同一套调研合同、证据等级、行动等级、风险门、沉淀落位和当前性审计；本工程采用聚合入口 + technology-research 执行分支，不平铺外部 13 个子项。
maturity: mature
evidence_signals: [skill, README entry, governance, template, TRANSFER, sensor, quality-gate, verification-loop]
transfer_ready: true
sensor: python3 scripts/check_all.py --only research-capability
---

# Research Capability

## 定位

本技能是本仓库的调研 / 研究能力总入口。它把“调研”固定成一个聚合能力，而不是把外部工程的所有研究子项原样搬进本库。

当前执行分支由 [[skills/technology-research/SKILL]] 承接，覆盖技术专题、开源工程、行业 / AI、产品 / 公司、PoC 和本地源码工程转接。Frontier Tech Intake / Frontier Technology Intake / 前沿技术信息流处理作为本技能的前置 intake 子项，由 [[templates/research-intake-template]] 承接 source package、access boundary、A3 compensation、parser agent、evaluator oracle、route 和 writeback 字段，不单独平铺成新的通用 skill。市场、用户、竞争、尽调、科研、政策、战略前瞻等外部子项只作为方法储备；除非本仓库出现稳定高频需求，否则不单独建空 skill。

本技能的目标不是“收集资料”，而是形成决策型研究资产。每份正式研究必须回答 `So-What`：这些证据对当前选型、采购、PoC、治理、继续观察或放弃意味着什么；必须保留 counter-evidence / 反证；必须声明 deal-breaker / 阻断条件；必须给出可执行的 decision output：`直接使用 / 封装使用 / Fork / 只参考 / 放弃 / 继续观察`。如果缺少这些字段，研究只能算资料整理或 intake，不能写成决策支持完成。涉及 Hugging Face、OpenAI、Cloudflare、Netlify、GitHub 等平台时，优先读官方文档、repo、release 或源码。

## 触发场景

- 用户要求“调研”“研究一下”“全面评估”“判断是否值得做 / 引入 / PoC / 产品化 / 采购 / 合作”。
- 对象是技术概念、开源工程、源码工程、公司、产品、市场、用户、竞争对手、政策、论文、模型能力或长期趋势。
- 结论会支撑选型、项目立项、采购合作、技术接入、治理规则、知识沉淀或后续实验。
- 事实可能过期，或用户会基于结论花钱、花时间、改架构、发任务。

简单事实查询不需要完整启动本技能；但只要事实可能变化，必须查当前一手来源或标注未验证。

## 成熟度与证据信号

- `skill`：本页是聚合入口，[[skills/technology-research/SKILL]] 是执行分支。
- `maturity`：`mature`。本技能已有聚合入口、technology-research 执行分支、Research Intake / Frontier Tech Intake 模板、证据等级、行动等级、决策型研究资产字段、迁移边界和专项 sensor。
- `governance`：研究证据等级、行动等级和沉淀边界由 [[research-capability-rules]] 约束。
- `template`：调研合同、报告、证据矩阵和采用合同分别见 [[templates/technology-research-contract-template]]、[[templates/technology-research-report-template]]、[[templates/technology-research-evidence-matrix-template]]、[[templates/technology-research-adoption-contract-template]]。
- `TRANSFER`：跨工程迁移边界见 [[skills/research-capability/TRANSFER]]。
- `sensor`：`python3 scripts/check_all.py --only research-capability` 检查聚合入口、执行分支、模板、governance 和 README wiring。
- `evidence boundary`：本技能输出研究判断，不替代源码审计、PoC 验收、采购 / 合规 / 安全批准或项目状态关闭。

## 工作流

1. 固定调研合同：对象、决策目标、关键问题、深度、证据计划、输出形态和不做项。
2. 如果输入是外部信息流、论文、repo、社区讨论、产品更新、截图或用户转发材料，先用 [[templates/research-intake-template]] 建 Research Intake：记录 source_type、source_ref、access boundary、raw landing、capture method、extraction quality、parser agent、evaluator oracle、A3 compensation 和 landing plan。
3. 判对象分支：技术专题、开源工程、行业 / AI、产品 / 公司、PoC、本地源码工程或其他。
4. 建证据等级：L1 一手事实、L2 权威分析、L3 产业信号、L4 媒体 / 社区线索、L5 推论、L6 建议。
5. 做当前性审计：版本、release、license、pricing、CVE、API、政策、benchmark、公司状态和平台能力必须查当前来源。
6. 判深度等级：quick scan / decision brief / deep research / PoC plan / source audit intake；复杂、不完整目标先按 [[proactive-dialogue-system]] 明确场景包和关键假设。
7. 选择可选研究 lens：技术和产品机会可用 Three Horizons、War Game、Wild Cards；市场 / 价格判断可用 Van Westendorp；政策 / 项目评估可用 OECD-DAC。可选 lens 只服务问题判断，不强行套模板。
8. 固定执行根：脚本和模板引用路径时以 `Path ROOT` / repo root 为基准，不把 AcknowledgeBase 或下游工程路径复制成本库事实。
9. 行动兑现回检：正式研究资产要写检查方式、行动 owner、完成口径和下一次复查触发。
10. 建 counter-evidence / 反证面：列支持证据之外的否定信号、替代解释、失败案例、不可复现信息、社区争议和旧结论过期风险。
11. 建 deal-breaker / 风险门：写清足以否决、延后、降级为人工确认或停止投入的条件。
12. 给行动等级：Adopt / Trial / Assess / Hold / Blocked，并连接 `So-What`、风险门、下一步和不能上推边界。
13. 给 decision output：`直接使用 / 封装使用 / Fork / 只参考 / 放弃 / 继续观察`，并说明触发复查的更新机制。
14. 决定沉淀落位和持久化边界：raw、article、concept、template、project、decision、trace、report、skill 或只留本轮回复；长期研究资产必须说明文档作为单一源、行动分流和 owner 链接。
15. 长期沉淀时调用 [[skills/knowledge-linking/SKILL]] 补入口、上位、邻接和回链。

## 输出格式

```markdown
**调研合同**
- 对象：
- 决策目标：
- 关键问题：
- 深度等级：
- 可选研究 lens：Three Horizons / War Game / Wild Cards / Van Westendorp / OECD-DAC / 不适用
- Path ROOT / repo root：
- 检查方式：
- 行动 owner：
- 完成口径：
- 输出形态：
- 不做项：

**证据计划**
- L1 一手事实：
- L2 权威分析：
- L3 信号：
- 待核验 / blocked：

**Research Intake / Source Package**
- source_type：
- source_ref：
- access_boundary：
- capture_method：
- extraction_quality：
- parser_agent：
- evaluator_oracle：
- A3 compensation：
- raw_landing：

**分支路由**
- 主分支：
- 辅助方法：
- 路由理由：

**结论**
- confirmed：
- observed：
- reported：
- inferred：
- blocked：

**So-What / 决策含义**
- 这对当前决策意味着什么：
- 反证 / counter-evidence：
- deal-breaker：
- decision output：直接使用 / 封装使用 / Fork / 只参考 / 放弃 / 继续观察
- 更新机制 / refresh trigger：

**建议**
- 行动等级：
- 置信度：
- 风险门：
- 刷新触发：
- 沉淀位置：
```

## 禁止项

- 不把外部 13 个研究子项原样平铺成本库技能目录。
- 不把 frontier technology intake 平铺成新的通用 skill；它是本技能的前置 source package / route 子项。
- 不把热点、宣传、Star 数、媒体报道、旧价格、旧 release 或二级文章直接写成结论。
- 不把没有原文保真、access boundary、extraction quality 或 evaluator 的聊天摘要写成 L1 / confirmed。
- 不在缺少一手事实、当前性核验或本地验证时写强采用、强购买、强生产接入。
- 不让研究结论替代采购、合规、安全、源码审计、PoC 验收、准出或人工拍板。
- 不把外部项目事实、公司结论、报告排行、source revision 或一次性调研数据写进通用技能。

---
name: research-capability
description: 调研 / 研究能力聚合技能。用于把技术、开源工程、产品、公司、行业、AI、PoC 和源码工程研究统一到同一套调研合同、证据等级、行动等级、风险门、沉淀落位和当前性审计；本工程采用聚合入口 + technology-research 执行分支，不平铺外部 13 个子项。
maturity: leading
adoption_level: strong-template-kernel
evidence_signals: [skill, README entry, governance, template, TRANSFER, sensor, quality-gate, verification-loop, positive-fixture, negative-fixture, outcome-boundary]
transfer_ready: true
sensor: python3 scripts/check_all.py --only research-capability
---

# Research Capability

## 定位

本技能是本仓库的调研 / 研究能力总入口。它把“调研”固定成一个聚合能力，而不是把外部工程的所有研究子项原样搬进本库。

本仓采用 `strong-template-kernel`：完整承接可迁移的研究合同、Evidence Delta、R2+ source plan、coverage matrix、验证阶梯、修订循环和 evaluator 机制；AcknowledgeBase 继续拥有上游设计与领域知识。本仓不复制其项目事实、研究正文、历史案例或子技能目录，不建立第二份 Research OS 事实源。

当前执行分支由 [[skills/technology-research/SKILL]] 承接，覆盖技术专题、开源工程、行业 / AI、产品 / 公司、PoC 和本地源码工程转接。Frontier Tech Intake / Frontier Technology Intake / 前沿技术信息流处理作为本技能的前置 intake 子项，由 [[templates/research-intake-template]] 承接 source package、access boundary、A3 compensation、parser agent、evaluator oracle、route 和 writeback 字段，不单独平铺成新的通用 skill。市场、用户、竞争、尽调、科研、政策、战略前瞻等外部子项只作为方法储备，统一沉淀在 [[skills/research-capability/reference/research-method-route-map]]；除非本仓库出现稳定高频需求，否则不单独建空 skill。

本技能的目标不是“收集资料”，而是形成决策型研究资产。每份正式研究必须回答 `So-What`：这些证据对当前选型、采购、PoC、治理、继续观察或放弃意味着什么；必须保留 counter-evidence / 反证；必须声明 deal-breaker / 阻断条件；必须给出可执行的 decision output：`直接使用 / 封装使用 / Fork / 只参考 / 放弃 / 继续观察`。如果缺少这些字段，研究只能算资料整理或 intake，不能写成决策支持完成。涉及 Hugging Face、OpenAI、Cloudflare、Netlify、GitHub 等平台时，优先读官方文档、repo、release 或源码。

## 触发场景

- 用户要求“调研”“研究一下”“全面评估”“判断是否值得做 / 引入 / PoC / 产品化 / 采购 / 合作”。
- 对象是技术概念、开源工程、源码工程、公司、产品、市场、用户、竞争对手、政策、论文、模型能力或长期趋势。
- 结论会支撑选型、项目立项、采购合作、技术接入、治理规则、知识沉淀或后续实验。
- 事实可能过期，或用户会基于结论花钱、花时间、改架构、发任务。

简单事实查询不需要完整启动本技能；但只要事实可能变化，必须查当前一手来源或标注未验证。

## 成熟度与证据信号

- `skill`：本页是聚合入口，[[skills/technology-research/SKILL]] 是执行分支。
- `maturity`：`leading / strong-template-kernel`。本技能已有聚合入口、technology-research 执行分支、Research Intake / Frontier Tech Intake、Evidence Delta、R2+ source plan、coverage matrix、验证阶梯、迁移边界、正负 fixture 和专项 evaluator。
- `governance`：研究证据等级、行动等级和沉淀边界由 [[research-capability-rules]] 约束。
- `template`：调研合同、报告、证据矩阵和采用合同分别见 [[templates/technology-research-contract-template]]、[[templates/technology-research-report-template]]、[[templates/technology-research-evidence-matrix-template]]、[[templates/technology-research-adoption-contract-template]]。
- `TRANSFER`：跨工程迁移边界见 [[skills/research-capability/TRANSFER]]。
- `sensor`：`python3 scripts/check_all.py --only research-capability` 同时检查聚合入口、执行分支、模板、governance、strong profile、结构化研究合同以及正负 fixture；它仍不替代独立研究 outcome review。
- `method route map`：市场、用户、竞争、尽调、科研、政策、战略前瞻、结构化判断和生活 / 现场决策等细分方法见 [[skills/research-capability/reference/research-method-route-map]]；它是方法储备，不是并列技能入口。
- `evidence boundary`：本技能输出研究判断，不替代源码审计、PoC 验收、采购 / 合规 / 安全批准或项目状态关闭。

## 工作流

1. 固定调研合同：对象、决策目标、关键问题、深度、证据计划、输出形态和不做项。
2. 如果输入是外部信息流、论文、repo、社区讨论、产品更新、截图或用户转发材料，先用 [[templates/research-intake-template]] 建 Research Intake：记录 source_type、source_ref、access boundary、raw landing、capture method、extraction quality、parser agent、evaluator oracle、A3 compensation 和 landing plan。
3. 判对象分支：技术专题、开源工程、行业 / AI、产品 / 公司、PoC、本地源码工程或其他。
4. 判深度等级：R0 线索、R1 桌面初筛、R2 验证计划、R3 结构分析、R4 尽调 / 接入。R2+ 在广泛搜索前必须通过 `Source Plan checkpoint`：列出问题到来源类型映射、必需一手来源、coverage target、contradiction plan、access boundary、停止条件和 owner。
5. 建证据等级与 coverage matrix：L1 一手事实、L2 权威分析、L3 产业信号、L4 媒体 / 社区线索、L5 推论、L6 建议；每个关键问题必须是 covered / partial / blocked，并登记支持证据、反证、stale evidence 和缺口。
6. 做当前性审计：版本、release、license、pricing、CVE、API、政策、benchmark、公司状态和平台能力必须查当前来源。
7. 如果用户补充截图、链接、文档、日志、接口响应或运行结果，执行 `Evidence Delta Re-open`：判 materiality，保存直接观察，补外围一手核验与反证，重算整体结论，并逐项记录 owner propagation；不能只追加摘要。
8. 选择可选研究 lens：技术和产品机会可用 Three Horizons、War Game、Wild Cards；市场 / 价格判断可用 Van Westendorp / Gabor-Granger；竞争情报可用 KIT / KIQ、battlecard 和 War Game；尽调可用分职能 DD 矩阵、三角验证和 red flag 分级；结构化判断可用 ACH 和关键假设检验；政策 / 项目评估可用 OECD-DAC。可选 lens 只服务问题判断，不强行套模板。
9. 固定执行根：脚本和模板引用路径时以 `Path ROOT` / repo root 为基准，不把 AcknowledgeBase 或下游工程路径复制成本库事实。
10. 建 counter-evidence / 反证面与 deal-breaker / 风险门：列否定信号、替代解释、失败案例、不可复现信息、社区争议、旧结论过期风险，以及足以否决、延后或转人工的条件。
11. 建验证阶梯：分别记录 desk evidence、local validation、PoC、service/runtime readback 和 human approval。`Adopt` 必须有与 claim scope 对应的一手证据与本地验证；生产、合规、采购或业务批准仍由各自 owner 裁决。
12. 给行动等级和 decision output：Adopt / Trial / Assess / Hold / Blocked；`直接使用 / 封装使用 / Fork / 只参考 / 放弃 / 继续观察`，并连接 So-What、风险门、下一步和不能上推边界。
13. 形成 Research Case Packet：Original Problem Brief、Research Contract、Source Plan、Source Ledger、Coverage Matrix、Evidence Delta、结论、采用合同、Revision Brief 和未验证边界按深度分级组合，不要求新建平行目录。
14. 执行评价与修订循环：确定性 sensor 检查合同；独立 evaluator 或人工 reviewer 检查证据覆盖、反证、结论校准和读者效用；失败时写 Revision Brief、Delta Source Plan 和 next-run decision，不用原作者自评替代 outcome 证明。
15. 决定沉淀落位和持久化边界：raw、article、concept、template、project、decision、trace、report、skill 或只留本轮回复；长期研究资产必须说明文档作为单一源、行动分流和 owner 链接。
16. 正式研究资产必须给读者可见的溯源入口：外部原文完整索引、本地 raw / source ledger、数据快照或社区深读入口，不能只把 URL 藏在对话、浏览器历史或脚注里。
17. 长期沉淀时调用 [[skills/knowledge-linking/SKILL]] 补入口、上位、邻接和回链。

## 输出格式

```markdown
**调研合同**
- contract revision：research-contract.v1
- 对象：
- 决策目标：
- 关键问题：
- 深度等级：R0 / R1 / R2 / R3 / R4
- 可选研究 lens：Three Horizons / War Game / Wild Cards / Van Westendorp / Gabor-Granger / OECD-DAC / ACH / DD matrix / 不适用
- 方法路由：参考 [[skills/research-capability/reference/research-method-route-map]]，说明主子项和辅助子项
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

**R2+ Source Plan / Coverage**
- source plan checkpoint：pass / blocked / not-required
- 必需来源类型：
- coverage target：
- contradiction plan：
- 停止条件：
- coverage matrix：covered / partial / blocked

**Evidence Delta**
- 新材料与 materiality：duplicate / clarification / conclusion-changing / architecture-changing / not-applicable
- 外围一手核验：
- 新反证：
- 结论重算：
- propagation results：

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

**溯源入口**
- 外部原文完整索引：
- 本地 raw / source ledger：
- 数据快照 / 社区深读：
- 报告层关键原文链接：

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

**评价与修订**
- deterministic validator：
- evaluator provenance：
- outcome review：passed / failed / unproven
- Revision Brief / Delta Source Plan：
- next-run decision：
```

## 禁止项

- 不把外部 13 个研究子项原样平铺成本库技能目录。
- 不把 frontier technology intake 平铺成新的通用 skill；它是本技能的前置 source package / route 子项。
- 不把热点、宣传、Star 数、媒体报道、旧价格、旧 release 或二级文章直接写成结论。
- 不把没有原文保真、access boundary、extraction quality 或 evaluator 的聊天摘要写成 L1 / confirmed。
- 不让 R2+ 跳过 Source Plan checkpoint 或用来源数量替代 coverage matrix。
- 不把补充材料降级成追加摘录；必须执行 Evidence Delta Re-open 并重算受影响结论。
- 不把 deterministic sensor 或作者自评写成独立 outcome evaluator 已通过。
- 不在缺少一手事实、当前性核验或本地验证时写强采用、强购买、强生产接入。
- 不让研究结论替代采购、合规、安全、源码审计、PoC 验收、准出或人工拍板。
- 不把外部项目事实、公司结论、报告排行、source revision 或一次性调研数据写进通用技能。

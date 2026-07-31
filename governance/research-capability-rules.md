---
type: governance
id: GOV-RESEARCH-CAPABILITY-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-31
tags: [governance, research-capability, technology-research, technical-topic-research, open-source-project-research, industry-ai-research]
---

# Research Capability Rules

本页是 `research-capability` 的治理裁定页。[[skills/technology-research/SKILL]] 是合并版执行技能；[[templates/technology-research-contract-template]] 和 [[templates/technology-research-report-template]] 是可复制骨架。本页约束研究何时必须联网查证、何时只做内部材料整理、何时不能给生产采用结论。

## Strong Template Kernel 裁决

本仓 `research_level: strong-template-kernel`。强吸收的对象是可迁移的 Research Contract、Source Plan、Source Ledger、coverage matrix、Evidence Delta、验证阶梯、采用合同、修订循环和 evaluator，不是 AcknowledgeBase 的领域知识、项目事实、研究正文、历史案例或目录形态。AcknowledgeBase 继续拥有上游设计和领域知识；wiki 拥有可复制、可执行、可验证的模板内核合同，两者不得形成第二真相源。

结构和字段齐全只证明 contract-ready；正负 fixture 通过只证明确定性 evaluator 能识别已知边界；没有独立 reviewer、真实研究 case outcome 或读者任务 oracle 时，不得宣称研究质量整体通过。

## 研究不是资料堆叠

research-capability 的完成标准不是“找到了很多资料”，而是形成可复查的判断：

- 研究问题明确。
- 证据等级明确。
- 当前事实和推论分开。
- 结论连接到行动等级。
- 风险和刷新触发明确。
- 长期落位和回链明确。

没有判断的问题清单只是资料整理；没有证据等级的判断只是观点。

## 必须查证当前事实的场景

涉及以下事实时，必须优先查当前一手来源：

- 软件版本、release、API、license、pricing、roadmap、维护状态。
- 法规、标准、政策、安全公告、CVE、模型风险或合规要求。
- 公司、产品、融资、客户、市场份额、竞争格局。
- benchmark、模型能力、硬件支持、云服务限制、供应链状态。
- OpenAI、Cloudflare、Netlify、GitHub、Hugging Face 等平台近期能力。

如果不能查证，结论必须降级为 `likely / possible / blocked`，并写出刷新触发。

## 研究分支

| 分支 | 入口问题 | 主要证据 | 不能替代 |
| --- | --- | --- | --- |
| 技术专题 | 这项技术是什么、适合什么场景 | 标准、论文、官方文档、实现案例 | 本地 PoC |
| 开源工程 | 这个 repo 是否值得用 | repo、release、license、issue、代码结构、运行验证 | 供应商合规批准 |
| 行业 / AI | 赛道是否成立、机会在哪里 | 一手产品、行业报告、论文、公司信号 | 投资 / 商业拍板 |
| 产品 / 公司 | 产品能力和风险如何 | 官方文档、价格、客户案例、状态页 | 采购决策 |
| PoC | 本地约束下能否跑通 | 本地命令、样本、指标、失败日志 | 生产验收 |
| 源码工程 | 现实实现是什么 | 本地代码、测试、运行、架构图 | 外部资料调研 |

源码工程解读必须回到 [[projects/codebase/source-code-audit-workflow]]；不能用外部 research 替代源码审计。

## R2+ Source Plan 与 Coverage

- R0 / R1 可以轻量执行，但仍要标注当前性和不可上推边界。
- R2 / R3 / R4 在广泛收集前必须通过 Source Plan checkpoint，至少包含问题到来源类型映射、必需 L1、coverage target、contradiction plan、access boundary、停止条件和 owner。
- coverage matrix 必须按关键问题记录 `covered / partial / blocked`，并同时登记支持证据、counter-evidence、stale evidence 和下一步。
- 来源数量、搜索轮数和报告篇幅不能代替 coverage；关键问题仍 blocked 时，结论必须同步降级。

## Evidence Delta Re-open

已有研究收到新截图、链接、文档、日志、接口响应或运行结果时，必须重新开启受影响的研究合同：判 materiality，区分直接观察和推论，补外围一手核验与反证，重算结论、行动等级和风险门，并对 source ledger、owner、decision、trace 或报告逐项记录 updated / no-op / blocked。只追加摘要不构成吸收完成。

## 验证与评价循环

研究验证分层为 desk evidence、local validation、PoC、service/runtime readback 和 human approval。`Adopt` 必须同时有 L1 或等价直接证据、与 claim scope 相符的 local validation，以及已闭合的 blocker；生产、采购、合规、安全和业务批准仍由对应 owner 决定。

评价至少区分：确定性 contract validator、builder-independent evaluator / 人工 reviewer、真实 case outcome 和 reader utility。失败或新证据改变覆盖时，必须形成 Revision Brief、Delta Source Plan 和 next-run decision；同一作者的自评不能替代独立 outcome evidence。

## 证据等级

研究报告必须标注证据等级：

- `L1`：官方文档、论文、标准、法规、仓库、release、本地运行结果。
- `L2`：监管机构、标准组织、可靠研究机构、行业报告。
- `L3`：客户案例、招聘、融资、社区活跃、会议演讲、生态集成。
- `L4`：媒体、博客、论坛、社交平台，只作线索。
- `L5`：推论，必须写依据和不确定性。
- `L6`：建议，必须连接证据、风险和行动等级。

没有 L1 时，不给强采用建议。只有 L4 / L5 时，结论最多是探索线索。

## 行动等级

研究结论必须给行动等级：

- `Adopt`：证据充分、风险可控、已有本地或生产约束验证。
- `Trial`：值得 PoC 或小范围试用，但未满足正式采用。
- `Assess`：继续观察或补证据。
- `Hold`：当前不建议投入，原因明确。
- `Blocked`：缺关键事实、权限、样本或合规确认。

行动等级必须连接到下一步，而不是停在评价。

## 沉淀落位

研究产物按长期价值落位：

- 单篇资料摘要：`articles/`。
- 稳定概念、方法或实体：`concepts/`。
- 可复用研究流程：`skills/`。
- 可复制研究骨架：`templates/`。
- 项目选型或决策：`projects/design/`、`projects/decisions.md`、`projects/trace.md`。
- 仍未处理的来源材料：`raw/` 或 `inbox/`。

所有长期研究产物必须调用 [[skills/knowledge-linking/SKILL]] 做入口和回链。

## 禁止项

- 不把热点、README、Star 数、排行榜或单篇媒体稿直接写成结论。
- 不把“能跑 demo”写成“可生产接入”。
- 不把旧价格、旧版本、旧政策当当前事实。
- 不把研究建议替代采购、合规、安全或项目决策。
- 不把外部项目事实搬进本库通用技能。

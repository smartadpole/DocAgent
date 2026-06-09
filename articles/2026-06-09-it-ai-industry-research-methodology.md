---
type: article
id: ARTICLE-IT-AI-INDUSTRY-RESEARCH-METHODOLOGY-2026-06-09
scope: shared
status: active
source_of_truth: false
updated: 2026-06-09
tags: [research, industry, ai, it, strategy, market-intelligence]
---

# IT / AI 行业调研方法论

## 来源

- 用户在 2026-06-09 对“IT 行业 / AI 领域如何做调研，二者侧重点是否不同”的方法输入。
- 本轮核对的高权重参考源包括：[Stanford HAI 2026 AI Index](https://hai.stanford.edu/ai-index/2026-ai-index-report%20)、[McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai?os=wtmbrgj5xbah)、[Gartner Top Strategic Technology Trends for 2026](https://www.gartner.com/en/articles/top-technology-trends-2026)、[NIST AI 600-1 Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)、[OECD AI Principles](https://www.oecd.org/en/topics/ai-principles.html)、[EU AI Act implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline)。
- 本库既有 [[articles/2026-06-09-technical-topic-research-methodology]]、[[articles/2026-06-09-open-source-project-due-diligence-methodology]]、[[concepts/technical-research-knowledge-asset]] 和 [[skills/knowledge-linking/SKILL]]。

## 一句话总结

IT / AI 行业调研不是搜热点，而是形成 [[concepts/it-ai-industry-research-asset|行业与 AI 领域研究资产]]：用产业视角判断趋势，用技术视角判断可行性，用产品视角判断价值，用工程视角判断落地成本，用治理视角判断风险，最终服务学习、研发、选型、产品规划和创业判断。

## IT 和 AI 的侧重点不同

IT 行业调研和 AI 领域调研都要看产业、技术、产品、公司和落地，但权重不同。

| 维度 | IT 行业调研更重 | AI 领域调研更重 |
| --- | --- | --- |
| 产业问题 | 企业数字化、降本增效、系统替换、预算迁移 | 模型能力变化、自动化边界、数据/算力/评测驱动的新工作流 |
| 技术路线 | 云、SaaS、数据库、安全、网络、DevOps、企业软件架构 | 基础模型、多模态、Agent、RAG、推理框架、LLMOps、AI security |
| 产品判断 | 采购链路、部署模式、集成难度、TCO、SLA | 是否进入真实 workflow、是否可评估、是否比人或传统软件更划算 |
| 公司竞争 | 渠道、生态、企业客户、存量替换、服务能力 | 模型/数据/算力/分发/产品闭环/场景 Know-how 壁垒 |
| 开源生态 | 降低采购成本、替代商业软件、可控部署 | 决定试错成本、私有化能力、模型/推理/RAG/Agent/评测基础 |
| 治理风险 | 安全、合规、供应商锁定、运维可靠性 | 幻觉、Prompt Injection、工具越权、隐私、版权、红队、AI Act 等 |

所以 IT 调研更像“企业技术和软件市场判断”，AI 调研更像“产业情报 + 技术路线判断 + 产品机会分析 + 落地治理评估”的组合。

## 六层结构

IT / AI 行业调研建议按六层看：

1. 宏观趋势层。
2. 技术路线层。
3. 产品应用层。
4. 公司竞争层。
5. 开源生态层。
6. 落地治理层。

这六层合起来，才算完整的行业 / AI 领域调研。

## 第一层：宏观趋势层

目标是回答：这个方向是大趋势，还是短期炒作？

要看：

- 市场规模。
- 资本投入。
- 大厂布局。
- 政策监管。
- 人才需求。
- 产业采用率。
- 技术成熟度。
- 企业付费意愿。

AI 领域还要额外问：

- 算力是否继续扩张。
- 模型能力是否继续提升。
- 企业是否真的获得 ROI。
- AI 是否进入核心业务流程。
- 哪些行业最快落地。
- 监管是否变严。
- 开源模型是否改变成本结构。

宏观层最终产物是行业阶段判断：

- 萌芽期。
- 快速增长期。
- 试点转生产期。
- 平台化竞争期。
- 泡沫消退期。
- 成熟基础设施期。

## 第二层：技术路线层

目标是回答：这个方向背后的技术路线是什么，未来会往哪走？

AI 技术路线不能只按模型名字看，要按技术栈看：

```text
基础模型
├── LLM
├── 多模态模型
├── 视觉 / 语音 / 视频模型
├── 3D / 世界模型
└── 机器人 / Physical AI

应用架构
├── RAG
├── Agent / Multi-agent
├── Workflow
├── Tool Calling
├── Memory
├── Fine-tuning
└── MCP / 工具协议

基础设施
├── 推理 / 训练框架
├── 向量数据库
├── 数据治理
├── 评测系统
├── 可观测性
├── 安全防护
└── MLOps / LLMOps
```

技术路线层要回答：

- 核心技术瓶颈是什么。
- 主流路线有哪些。
- 旧路线是否正在被替代。
- 关键论文、模型、框架和协议有哪些。
- 哪些能力已经工程可用。
- 哪些仍是实验室效果。

## 第三层：产品应用层

目标是回答：这个技术被做成了什么产品，用户为什么付费？

要看：

- 产品形态。
- 用户是谁。
- 使用频率。
- 付费方式。
- 核心功能。
- 替代了什么旧流程。
- 提升了什么指标。
- 是否有真实复购。
- 是否嵌入业务流程。

例如 Agent 方向，不要只调研“Agent 是什么”，还要拆开发者 Agent、办公 Agent、客服 Agent、销售 Agent、知识 Agent、安全 Agent 等产品场景。

AI 产品是否成立，关键不是“模型回答得好不好”，而是：

- 是否减少真实工作量。
- 是否能进入用户每天的工作流。
- 是否能被组织管理和审计。
- 是否能被稳定评估。
- 是否比人工或传统软件更划算。

## 第四层：公司竞争层

目标是回答：谁在做，谁领先，谁有壁垒，谁只是包装？

AI 公司调研不要只看融资和新闻，要看五个维度：

1. 技术壁垒。
2. 数据壁垒。
3. 分发渠道。
4. 产品闭环。
5. 商业化能力。

可以把公司分为：

- 基础模型公司。
- 云和基础设施公司。
- 应用产品公司。
- 垂直行业 AI 公司。
- 开源生态公司。

竞争判断要问：它靠模型能力、产品体验、数据闭环、渠道生态、成本优势，还是行业 Know-how 领先？只调用大模型 API 做一层 UI、又没有数据/流程/分发/场景壁垒的产品，容易被平台吞掉。

## 第五层：开源生态层

目标是回答：这个方向有没有成熟开源基础，我们能不能借力？

AI 领域必须看开源，因为开源决定：

- 试错成本。
- 研发效率。
- 技术可控性。
- 部署灵活性。
- 私有化能力。
- 人才学习路径。
- 商业替代空间。

要看代表项目、维护主体、商业支持、license、私有化部署、生产适用性、插件生态、社区活跃度和二开空间。具体项目评估应转入 [[articles/2026-06-09-open-source-project-due-diligence-methodology]] 和 [[skills/open-source-project-research/SKILL]]。

## 第六层：落地治理层

目标是回答：这个 AI 方向能不能安全、合规、稳定地进入真实业务？

AI 和传统 IT 最大的不同在于输出不稳定、可能幻觉、会接触隐私和版权材料、可能调用工具越权，并且监管正在快速演化。因此 AI 调研必须加入治理维度：

- 数据安全。
- 隐私保护。
- 模型幻觉。
- 越权调用。
- Prompt Injection。
- 工具调用风险。
- 审计日志。
- 人工审核。
- 评测体系。
- 红队测试。
- 合规要求。
- 版权风险。

最终要写风险等级、治理要求、上线门槛、合规成本、安全边界和人工介入机制。

## 标准工作流

1. **定义调研对象**：行业、技术方向、产品赛道、公司群体、开源生态还是落地场景。
2. **建立问题清单**：为什么现在重要、谁在使用、谁在做、技术成熟度如何、商业模式是否成立、我们有什么机会。
3. **资料扫描**：权威行业报告、大厂技术博客、论文和 benchmark、GitHub / Hugging Face、产品官网和文档、招聘 JD、投融资信息、用户评论和案例、监管政策。
4. **建立技术与产业地图**：上游基础设施、中游平台和框架、下游应用、关键玩家和生态关系。
5. **做横向对比**：公司、技术路线、商业模式、开源项目、国内外差异。
6. **提炼机会和风险**：值得切入、已经拥挤、概念炒作、适合学习、适合产品化、适合创业或适合内部落地。
7. **形成结论**：推荐等级、切入方式、PoC 计划、资源需求和观察指标。

## 信号源权重

AI 领域噪声很大，资料要分权重。

### 第一优先级：权威报告和一手资料

- Stanford AI Index。
- McKinsey / BCG / Deloitte / Gartner 等咨询和行业报告。
- NIST / OECD / EU 官方资料。
- 大厂官方技术博客。
- 论文原文。
- GitHub / Hugging Face 仓库。
- 产品官方文档。

### 第二优先级：产业观察和案例

- 公司案例。
- 客户案例。
- 招聘 JD。
- 开发者社区。
- 技术大会。
- 融资新闻。
- 产品更新日志。

### 第三优先级：媒体和自媒体

- 行业媒体。
- 公众号、博客、播客。
- X / Reddit / Hacker News / 知乎。

第三类可以用来发现线索，但不能直接作为结论依据。

## AI 领域调研 12 问

每次调研 AI 方向都要问：

1. 这个方向解决的核心问题是什么？
2. 为什么过去没解决，现在可以解决？
3. 依赖的是模型能力、数据、工程，还是场景？
4. 当前最强玩家是谁？
5. 开源方案是否已经足够好？
6. 商业闭环是否清晰？
7. 用户是否真的高频使用？
8. 成本结构是否可持续？
9. 效果是否可以评估？
10. 风险和监管是否可控？
11. 会不会被大模型平台直接吃掉？
12. 我们切入的最小可行点是什么？

这 12 个问题比单纯资料总结更重要。

## 最终产物

IT / AI 行业调研不应只是一篇文章，而应沉淀为：

- 行业地图。
- 技术地图。
- 公司清单。
- 开源清单。
- 产品案例。
- 风险清单。
- 机会判断。
- PoC 路线。

对于本库，它应做成“AI 行业情报卡 + 技术路线图 + 机会判断卡”，由 [[templates/industry-ai-research-template]] 承接，执行流程由 [[skills/industry-ai-research/SKILL]] 承接。

## 知识关联自检

- 上位概念 / owning page：[[concepts/it-ai-industry-research-asset]]
- 邻接页面：[[articles/2026-06-09-technical-topic-research-methodology]]、[[articles/2026-06-09-open-source-project-due-diligence-methodology]]、[[concepts/ai-era-information-presentation]]
- 执行技能：[[skills/industry-ai-research/SKILL]]、[[skills/technical-topic-research/SKILL]]
- 可复制骨架：[[templates/industry-ai-research-template]]
- 入口回链：[[INDEX]]、[[articles/README]]、[[concepts/README]]、[[skills/README]]、[[templates/README]]


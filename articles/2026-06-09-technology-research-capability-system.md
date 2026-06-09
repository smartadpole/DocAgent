---
type: article
id: ARTICLE-TECHNOLOGY-RESEARCH-CAPABILITY-SYSTEM-2026-06-09
scope: shared
status: active
source_of_truth: false
updated: 2026-06-09
tags: [research, technology-research, evidence, maturity, decision-system]
---

# 技术调研能力体系补全

## 来源

- 用户在 2026-06-09 要求“针对上述专题，补全未覆盖部分，做好全面调研，保证针对技术调研具有完整健全的知识储备”。
- 本库既有 [[articles/2026-06-09-technical-topic-research-methodology]]、[[articles/2026-06-09-open-source-project-due-diligence-methodology]]、[[articles/2026-06-09-it-ai-industry-research-methodology]]。
- 外部补充框架：[ISO 56006 strategic intelligence management](https://www.iso.org/standard/72621.html)、[NASA TRL](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/technology-readiness-levels) / [ISO 16290 TRL](https://www.iso.org/standard/56064.html)、[Thoughtworks Technology Radar](https://www.thoughtworks.com/radar/)、[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)、[OpenSSF Scorecard](https://openssf.org/scorecard/) / [SLSA](https://slsa.dev/)、[SPDX](https://spdx.dev/about/overview/) / [NTIA SBOM minimum elements](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)、[CHAOSS metrics](https://github.com/chaoss/metrics)、[Stanford HELM](https://crfm.stanford.edu/helm)、[MLCommons AI risk and reliability](https://mlcommons.org/working-groups/ai-risk-reliability/ai-risk-reliability/)。

## 一句话总结

完整的技术调研不是单一“查资料”动作，而是一套 [[concepts/technology-research-system|技术调研体系]]：先判对象层级，再建立证据链、成熟度、经济性、可落地性、安全治理、评估设计和更新机制，最后把结论转成学习、选型、PoC、引入、产品化、创业或观察的行动。

## 已覆盖和新增补全

此前已经沉淀三条主线：

| 主线 | 已覆盖 |
| --- | --- |
| 技术专题调研 | 概念、价值、适用、落地、决策 |
| 开源工程调研 | 项目画像、健康度、跑通、代码结构、效果性能、集成成本 |
| IT / AI 行业调研 | 宏观趋势、技术路线、产品应用、公司竞争、开源生态、治理风险 |

仍需补齐的是总控层：

1. 调研对象路由。
2. 证据等级和来源可信度。
3. 成熟度与采用阶段。
4. 商业和经济性判断。
5. 安全、合规和供应链风险。
6. AI 评测与可靠性。
7. 决策门和退出条件。
8. 知识资产更新周期。

## 1. 调研对象路由

每次调研先判对象，而不是直接套模板。

| 对象 | 应走方法 | 典型问题 |
| --- | --- | --- |
| 行业 / AI 赛道 / 公司群体 / 产品机会 | [[skills/industry-ai-research/SKILL]] | 是否是趋势，谁在做，我们能否切入 |
| 技术概念 / 技术路线 / 方法 | [[skills/technical-topic-research/SKILL]] | 它是什么，为什么重要，怎么落地 |
| 具体开源仓库 / 论文代码 / 开源产品 | [[skills/open-source-project-research/SKILL]] | 能不能跑，能不能接，风险多大 |
| 具体本地源码工程 | [[projects/codebase/source-code-audit-workflow]] | 已读到什么深度，能否生产接入 |
| 具体公司 / 产品 / 商业机会 | 行业调研 + 产品/公司尽调扩展 | 谁领先，壁垒和商业闭环是什么 |
| 具体 PoC / 实验 | 技术专题或开源调研的验证阶段 | 哪个不确定性需要被证明或证伪 |

路由错了，后续越认真越容易错：行业问题不能只写技术定义，具体仓库不能只写赛道趋势，PoC 不能只写“建议试试”。

## 2. 证据等级

调研结论必须分清事实、信号、推论和建议。

| 证据等级 | 说明 | 用法 |
| --- | --- | --- |
| L1 一手事实 | 官方文档、论文原文、标准、法规、GitHub 仓库、release、产品文档、运行日志、自测数据 | 可支撑核心事实 |
| L2 权威分析 | Stanford AI Index、McKinsey、Gartner、NIST、OECD、行业白皮书、标准组织报告 | 可支撑趋势和框架 |
| L3 产业信号 | 招聘 JD、客户案例、融资、会议、社区讨论、产品更新 | 可作为方向信号 |
| L4 媒体/自媒体 | 新闻、公众号、博客、X、Reddit、Hacker News、知乎 | 只能做线索，不能单独支撑结论 |
| L5 推论 | 基于多源证据的判断 | 必须标注不确定性 |
| L6 建议 | 关注、PoC、引入、放弃、创业、产品化 | 必须连接证据和行动 |

技术调研写作时，应把“已验证事实 / 强信号 / 推论 / 待确认项”分开，避免把热度、宣传或模型回答当成事实。

## 3. 成熟度和采用阶段

单纯“热门 / 不热门”不足以指导决策。可以组合三套成熟度语言：

| 框架 | 用法 |
| --- | --- |
| TRL | 判断技术成熟度：从基础原理到真实环境验证和可运行系统。NASA 和 ISO 都有 TRL 体系。 |
| Technology Radar | 判断采用建议：Hold / Assess / Trial / Adopt。Thoughtworks 用它表达技术采用阶段。 |
| 本库 A/B/C/D | 判断行动：A 立即试点，B 短期验证，C 持续观察，D 暂不投入。 |

本库建议输出双标签：

`成熟度：TRL / 试点转生产 / 平台化竞争 / 工程可用`
`行动等级：Adopt / Trial / Assess / Hold 或 A/B/C/D`

这样可以避免“技术很前沿”被误读成“现在就该接入”。

## 4. 商业和经济性判断

技术可行不等于值得做。完整调研要补经济性：

- TAM / SAM / SOM 或目标市场规模。
- 用户是谁，付费方是谁，使用者是谁。
- 预算来自新增预算、替代预算，还是效率收益。
- TCO：采购、集成、算力、运维、人力、合规、迁移成本。
- ROI：节省时间、提高收入、降低风险、提升质量。
- switching cost：从现有方案迁移的成本。
- build / buy / partner / open-source 的取舍。

对个人学习和职业规划，也要把“学习价值、简历价值、作品价值、进入门槛、迁移性”作为经济性的一部分。

## 5. 安全、合规和供应链

技术调研必须前置安全和合规，不要等 PoC 之后再补。

### 开源和软件供应链

- OpenSSF Scorecard：自动化评估开源项目安全实践。
- SLSA：用于软件供应链完整性和 provenance。
- SBOM / SPDX / CycloneDX：用于组件、license、安全和 provenance 透明化。
- CHAOSS：用于开源社区健康指标。
- OSV / CVE / dependabot 等：用于依赖漏洞信号。

开源项目调研不能只看 Star，还要看 provenance、依赖、构建、release、SBOM、license 和社区健康。

### AI 风险治理

- NIST AI RMF：用 Govern / Map / Measure / Manage 管理 AI 风险。
- NIST AI 600-1：生成式 AI 的风险 profile。
- OECD AI Principles：可信 AI、人权、民主价值和政策建议。
- EU AI Act：按风险和通用目的 AI 规则分阶段适用。

AI 调研不能只写机会，还要写风险等级、上线门槛、人工审核、日志审计、红队测试、数据和版权边界。

## 6. AI 评测和可靠性

AI 方向必须单独补评测层，因为能力 demo 不能直接代表真实可靠。

至少看：

- 任务指标：准确率、召回、延迟、成本、成功率。
- 质量指标：一致性、鲁棒性、可解释性、可控性。
- 安全指标：越狱、毒性、隐私泄露、偏见、工具越权。
- 场景指标：是否能处理真实输入、长尾、异常和多轮上下文。
- 运行指标：延迟、吞吐、缓存命中、失败恢复、成本上限。

外部参考可以用 HELM 这类 holistic evaluation 思路，以及 MLCommons AI risk / reliability benchmark 这类安全和可靠性评测工作。但最终必须回到自己的场景评估集。

## 7. 决策门和退出条件

每次调研都要带决策门：

| 阶段 | 决策门 | 退出条件 |
| --- | --- | --- |
| 初筛 | 是否值得继续读 | 证据不足、方向无关、明显高风险 |
| 深调研 | 是否值得 PoC | 无场景、无可衡量收益、成熟度太低 |
| PoC | 是否进入试点 | 指标不达标、成本不可控、无法稳定复现 |
| 试点 | 是否产品化 / 引入 | ROI 不成立、治理不可控、维护成本过高 |
| 引入后 | 是否扩大 / 替换 / 下线 | adoption 不足、风险高于收益、被更好方案替代 |

“放弃”“仅参考”“持续观察”都是有效结论，不是失败。

## 8. 更新机制

技术调研资产会过期，必须写刷新条件。

常见刷新触发：

- 新模型、新论文、新 release、新 license、新法规。
- 关键公司融资、倒闭、收购、产品转向。
- 开源项目停止维护或出现重大 CVE。
- 本地 PoC 失败或成功。
- 成本曲线、算力、API 价格、硬件支持改变。
- 用户场景、组织预算、合规要求变化。

每篇调研页至少写查询日期、来源、未验证边界和复查触发条件。

## 总控输出

完整技术调研最后应能输出：

- 对象路由：这是行业、技术、开源工程、公司产品还是 PoC。
- 证据包：一手事实、权威分析、产业信号、推论和待确认项。
- 成熟度：TRL / Radar / A-B-C-D。
- 价值判断：痛点、用户、ROI、TCO、替代关系。
- 落地判断：数据、工程、人员、成本、治理。
- 风险判断：安全、合规、供应链、AI 可靠性。
- 行动建议：学习、观察、PoC、引入、产品化、创业、放弃。
- 更新机制：下次什么时候需要重新看。

## 知识关联自检

- 上位概念 / owning page：[[concepts/technology-research-system]]
- 邻接页面：[[articles/2026-06-09-technical-topic-research-methodology]]、[[articles/2026-06-09-open-source-project-due-diligence-methodology]]、[[articles/2026-06-09-it-ai-industry-research-methodology]]
- 执行技能：[[skills/technology-research-router/SKILL]]、[[skills/technical-topic-research/SKILL]]、[[skills/open-source-project-research/SKILL]]、[[skills/industry-ai-research/SKILL]]
- 可复制骨架：[[templates/technology-research-intake-template]]
- 入口回链：[[INDEX]]、[[articles/README]]、[[concepts/README]]、[[skills/README]]、[[templates/README]]

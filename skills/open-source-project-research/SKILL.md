---
name: open-source-project-research
description: 调研 GitHub、Hugging Face 或其他开源工程时，用于完成项目画像、健康度体检、运行验证、代码结构分析、效果/性能评估、集成成本和使用策略判断。
---

# 开源工程调研技能

## 定位

本技能用于把一个具体开源项目从“看起来有用”验证成可判断、可复现、可接入、可维护的工程资产。

它是 [[skills/technical-topic-research/SKILL]] 的专项分支：技术专题调研关注技术路线，开源工程调研关注具体仓库是否值得使用、封装、Fork、参考或放弃。

如果本技能由 [[skills/technology-research-router/SKILL]] 路由进入，必须继承 router 的决策目标、证据要求、成熟度假设、风险门和沉淀路径，并明确本轮是初筛、运行验证、源码结构分析、集成评估还是正式接入前尽调。

## 触发场景

- 用户给出 GitHub、Hugging Face、GitLab、论文代码、开源产品或框架链接，要求调研。
- 用户问某个开源项目“能不能用、好不好接、是否值得引入、怎么 PoC、怎么二开”。
- 用户要求比较多个开源项目并给出选型建议。
- 某个技术专题调研已经进入具体开源实现评估阶段。
- 如果对象还不确定是“开源工程本身”“开源生态”“技术路线”还是“已有源码工程审计”，先切到 [[skills/technology-research-router/SKILL]]，再决定是否使用本技能。

## 边界

- 不只看 README、Star 或宣传页；必须区分热度、质量、可用性和可维护性。
- 如果要判断当前活跃度、release、issue、license、benchmark、stars、forks 或社区状态，必须查证项目当前来源。
- 没有实际运行验证时，不能给“可接入 / 可生产”的强结论，只能给初筛判断。
- 不把外部项目事实写成通用规则；具体项目结论放 `articles/` 或目标项目资料中。
- 如果项目进入正式接入、fork 或生产化审计，转入 [[projects/codebase/source-code-audit-workflow]]。

## 读取顺序

1. [[concepts/technology-research-system]]：对象不清楚时先确认总控路由和证据等级。
2. [[articles/2026-06-09-open-source-project-due-diligence-methodology]]：确认开源工程调研目标和判断框架。
3. [[concepts/open-source-project-due-diligence]]：确认概念边界和使用策略。
4. [[templates/open-source-project-research-template]]：需要正式报告时使用。
5. 目标项目官方资料：README、docs、examples、release、license、issues、PR、CI、tests、benchmark。
6. 本库已有相邻技术专题、概念或项目材料。
7. 如果需要深入源码，按入口、配置、examples、core pipeline、tests、deployment 的顺序读。

## 工作流

### 0. 判调研深度

先声明本轮深度：

| 深度 | 目标 | 不能越界 |
| --- | --- | --- |
| R0 收藏 / 线索 | 确认项目存在和方向 | 不给使用建议 |
| R1 健康度初筛 | 判断是否值得继续投入 | 不说可接入 |
| R2 运行验证 | README / demo / 自有数据跑通 | 不说可生产 |
| R3 代码结构 | 读入口、数据流、核心模块、测试 | 不替代生产审计 |
| R4 集成尽调 | license、供应链、性能、接口、维护策略 | 仍需项目侧验收 |

没有运行验证和代码结构证据时，结论只能是初筛。

### 1. 快速筛选

先建立项目画像：

- 项目名称、地址、方向、核心功能、主要语言。
- License、维护主体、当前版本、最近更新时间。
- Star / Fork、release、issue、PR、CI、测试、文档、示例、benchmark。
- 初判类型：成熟项目、论文代码、个人玩具、公司开源产品、社区基础设施、已废弃项目。

快速筛选的目标是决定是否继续投入运行和代码分析。

### 2. 健康度体检

重点判断：

- 最近 3 个月是否有维护。
- issue 是否有人回复。
- 核心 bug 是否长期无人处理。
- release 是否稳定。
- API 是否稳定。
- 文档是否能带人跑通。
- license 和依赖 license 是否可接受。

Star 高不是通过条件；README 漂亮也不是通过条件。

同时扫描供应链和治理信号：

- license、依赖 license、模型权重 / 数据集授权。
- release provenance、构建方式、CI、签名、可重复构建线索。
- 是否可生成或已有 SBOM，是否有明显 CVE / OSV 风险。
- OpenSSF Scorecard / SLSA / SPDX / CHAOSS 可作为参考框架，不要求每次完整跑，但高风险项目必须说明缺口。

### 3. 运行验证

按三层验证：

1. 官方 README 安装和 quick start。
2. 官方 demo / example。
3. 自有数据 / 自身场景。

记录环境、命令、日志、报错、修复方式、耗时和资源占用。只跑官方 demo 不能说明真实可用。

### 4. 代码结构分析

按顺序读：

`README -> Quick Start -> examples -> config -> entrypoint -> core pipeline -> model / algorithm / engine -> data loader -> inference / training -> evaluation -> tests -> deployment`

必须找出：

- CLI / service / API / config 入口。
- 输入到输出的数据流。
- 核心模块和调用链。
- 配置系统是否清晰。
- 模块边界是否适合二开。
- 错误处理、日志、timeout、retry、输入校验是否可靠。
- 测试和 CI 覆盖核心路径的程度。

### 5. 效果和性能评估

算法 / 模型类项目至少评估：

- 官方指标是否可复现。
- 自有数据指标和失败案例。
- 推理耗时、显存、CPU、冷启动、吞吐、并发、模型大小、部署包大小。
- 异常输入、长尾场景和环境变化下的稳定性。

工具 / 框架类项目则重点评估易用性、API 稳定性、扩展成本、自动化能力和团队推广成本。

### 6. 集成成本判断

判断：

- 语言栈、依赖、Docker、服务化、库调用、API 封装、目标硬件、离线部署。
- 端侧部署、ONNX / TensorRT / RKNN、动态 shape、自定义 CUDA op、Python-only 逻辑和后处理迁移。
- 安全、license、模型权重、数据集和第三方依赖边界。

### 7. 给使用策略

最终只能落到以下策略之一：

- 直接使用。
- 封装使用。
- Fork 改造。
- 只参考实现。
- 放弃。

结论必须写理由、证据、风险和下一步行动。

策略必须带证据等级和置信度：直接使用和 Fork 改造至少需要 R2 + R3 证据；生产接入建议必须进入项目侧源码审计、验收或 PoC，不在本技能里直接闭环。

## 输出要求

正式报告优先使用 [[templates/open-source-project-research-template]]，至少包含：

1. 一句话结论。
2. 项目概况。
3. 解决的问题。
4. 核心能力。
5. 工程健康度。
6. 安装与运行验证。
7. 代码结构分析。
8. 效果评估。
9. 性能评估。
10. 集成成本。
11. 风险分析。
12. 对比方案。
13. 使用建议。
14. 下一步行动。

## 验证

新增或大改知识页后运行：

```bash
python3 scripts/check_all.py --only knowledge-linking
```

如果新增或大改技能、模板、入口或治理页，收尾前运行：

```bash
python3 scripts/check_all.py
```

## 自检清单

- 是否先判断项目类型和健康度。
- 是否查证当前维护、release、issue、license 和文档状态。
- 是否实际跑过 README / demo / 自有数据，或明确标注未跑。
- 是否画出入口、数据流和核心模块。
- 是否评估效果、性能、资源和失败案例。
- 是否判断集成成本和二开成本。
- 是否前置 license、模型权重、数据集和依赖风险。
- 是否说明调研深度是 R0-R4 哪一层，并避免越级结论。
- 是否扫描供应链、provenance、SBOM / SPDX、CVE / OSV 和社区健康缺口。
- 是否给出直接用 / 封装用 / Fork / 参考 / 放弃中的一个策略。
- 是否补齐 article / concept / entrypoint / backlink。

---
type: article
id: ARTICLE-PROBLEM-FOCUSED-INFORMATION-PRESENTATION-CROSS-PROJECT-CALIBRATION-2026-06-05
scope: shared
status: active
source_of_truth: false
updated: 2026-06-05
tags: [information-architecture, presentation, html-lens, cross-project]
---

# 问题聚焦式信息呈现的跨工程校准

## 来源

本页基于 2026-06-05 对多个本机工程的只读抽样：

- `/Users/hai/Documents/Life`
- `/Users/hai/Documents/Code/DocCustomeranalysis`
- `/Users/hai/Documents/Code/prefect`
- `/Users/hai/Documents/Code/Customer/fetch-adapter`
- `/Users/hai/Documents/Code/DocFilmCommunity`

这些工程不是目标对象，而是复杂度样本。它们共同用于校准 [[concepts/problem-focused-information-presentation]]：当用户反复关注同一个问题时，知识库最终应该怎样生成合适的图文混排 lens。

## 一句话总结

用户真正要的不是更漂亮的文档，也不是一次性 dashboard，而是“一图胜千言”的图文阅读层：同一个问题再次被问起时，系统能找到稳定的当前 lens，刷新真相源，更新当前判断，用表格、脑图、框图、关系图、时间线和状态卡呈现；当需要下载、打印、批注或线下流转时，提前声明 A4 / A3、横竖版、分页和 PDF 导出策略；并在关键节点保留不可变快照。

## 用户目的判断

这轮方案设计背后的目的至少有四层：

1. **降低重复重组成本**：用户不想每次重新在状态页、报告、issue、handoff、log、服务台账和计划页之间拼图。
2. **让每次阅读都服务当前判断**：看状态、行动、验收、风险、知识和资源时，展示结构应该不同，视觉形式也应该不同。
3. **保留证据边界**：直观不等于省略证据。图文 lens 必须明确哪些结论是当前态，哪些只是历史快照、局部验证或辅助证据。
4. **形成用户视角体系**：用户入口应是“我要看什么问题”，而不是 `projects/`、`articles/`、`raw/` 等维护目录。
5. **呈现对象背景**：用户可能看一份文档，也可能看一个跨多文档主题；无论哪种对象，都要呈现它的上位背景、来源背景、历史背景、关系背景和使用边界。
6. **支持可下载和可打印交付**：用户有时不是只在屏幕里看，还需要把图文 lens 导出成 PDF、A4 / A3 打印、线下批注或外部分发；因此导出版式必须在设计阶段进入方案，而不是事后截图。

因此，方案的中心不是“生成 HTML 文件”本身，而是：围绕稳定关注对象建立可刷新、可追溯、可归档、可视化表达充分、可按需要导出的 lens 体系。HTML 是默认承载容器；如果 HTML 排版不能充分表达，就应补充 SVG、Canvas、Mermaid、ECharts / D3、Excalidraw 导出图、PDF / slide、独立图片或 HTML + assets 组合包。若用户需要打印或下载，HTML lens 应优先具备 print view，并用 `export_profile` / `print_profile` 约束 PDF 输出。

## 跨工程样本

| 样本 | 信息复杂度 | 暴露的问题 | 需要的 lens |
| --- | --- | --- | --- |
| Life | 搬家、家务、资产、健康、日计划混在同一生活系统里；同一输入常常同时包含当前行动、可复用经验、稳定偏好和风险状态。 | 用户要的常常不是完整生活系统，而是“今天怎么动”“哪些条件卡住”“某类生活知识以后怎么复用”。 | 行动 lens、计划 / 约束 lens、风险 lens、资源 lens、知识 lens。 |
| DocCustomeranalysis | 状态、EP、TASK、issue、测试报告、验收、服务实例和子工程边界高度交织；旧报告可能仍有证据价值，但不能代表当前裁决。 | 如果只看最新报告，会误把 snapshot 当 current；如果只看状态页，又可能看不到证据链和不能上推边界。 | 当前状态 lens、issue lens、验收 lens、证据链 lens、服务 / 资源 lens。 |
| prefect | 运行状态来自代码里的 progress、stage_progress、artifact、log、status payload 和测试用例投影。 | 用户关心“进度到底可信不可信”时，需要看原始 payload、规范化逻辑、展示日志、artifact 和测试覆盖之间的映射。 | 运行状态投影 lens、代码行为 lens、测试证据 lens。 |
| fetch-adapter | 一个店日切片会经过请求合同、服务状态、stage_progress、artifact、runbook、handoff 和主控吸收边界。 | 用户不只是要知道服务怎么启动，而是要知道一次 run 的锚点、进度、产物、失败边界、重跑 / 取消语义和对上游调度的合同。 | 运行实例 lens、artifact lineage lens、handoff / 归属 lens、服务资源 lens。 |
| DocFilmCommunity | 产品状态、MVP 缺口、功能点、TODO、报告、阻塞和外部依赖很密；当前状态页包含大量历史吸收和下一步分工。 | 用户打开时应先看到“能不能推进 / 谁要交什么 / 为什么不能准出”，而不是先读完整状态长文。 | blocker-first 状态 lens、准出 lens、功能点关系 lens、执行分工 lens。 |

## 对方案的修正

这些样本把方案从“信息类型分类”推进到“lens 运行机制”：

1. **同一个稳定关注对象只能有一个当前入口**：多次问同一问题时，应先解析 `focus_object + lens_type`，查 `views/lens-registry.md`，刷新源，再更新 canonical lens。不能每次散落生成一个新文件。

2. **snapshot 只在证据需要冻结时产生**：验收、决策、发布、事故、阶段复盘和外部分发应保留 snapshot。普通追问、澄清和轻量刷新只更新 canonical lens。

3. **图文 lens 必须有 freshness 判断**：视图需要显示 `generated_at`、`source_revision`、`source_pages` 和 `staleness_policy`。如果源页面、报告、服务状态或数据快照变化，旧视图不能继续冒充当前态。

4. **用户入口要先于文件入口**：入口应按“看状态 / 要行动 / 要拍板 / 看风险 / 要验收 / 理解知识 / 找资源 / 复盘过程”组织，再映射到底层源页面。

5. **不同工程需要 adapter，但不能把工程规则写死到通用方案**：Life、DocCustomer、prefect、fetch-adapter、DocFilmCommunity 可以各自声明高频 lens pack；通用层只定义关注对象、证据边界、刷新流程、registry 和 provenance。

6. **单文档和跨文档主题都要带背景框**：单文档 lens 要呈现这份文档在整个知识网络里的位置；主题 lens 要呈现多份文档之间的层级、证据关系、冲突、演进和当前裁决。

7. **导出版式属于 lens 设计，不是收尾动作**：只要用户可能下载、打印、线下批注或外部分发，就要在 lens 里声明 `export_profile` 和 `print_profile`，包括 A4 / A3 / custom、横排 / 竖排、边距、分页、页眉页脚、重复表头、图表裁切、来源页脚和证据边界。PDF 是从 current lens 派生的导出物；只有用于验收、决策、发布、事故或复盘固化时，才进入 snapshot。

## 图文 lens 的运行流程

一次问答进入呈现层时，推荐按下面流程处理：

1. **识别关注对象**：判断用户现在问的是状态、计划、决策、风险、验收、故障、知识、资源、owner 还是时间线。
2. **解析 lens id**：如果是稳定关注对象，复用已有 canonical lens；如果尚不稳定，先生成临时视图。
3. **组装 source pack**：读取状态页、报告、issue、计划、服务台账、代码证据、资产路径等最小必要源。
4. **建立背景框**：明确上位背景、来源背景、历史背景、关系背景和使用边界。
5. **刷新当前判断**：把源里的最新事实投影成一眼判断层、证据解释层和原始追溯层。
6. **选择图文表达**：根据对象选择表格、脑图、框图、流程图、关系图、时间线、状态卡或组合版式。
7. **声明导出配置**：如果需要下载、打印或分发，选择 A4 / A3 / custom、横排 / 竖排、分页策略、print CSS 和 PDF 生成方式。
8. **更新 current**：覆盖 canonical lens，并记录更新时间、来源、证据边界、失效条件和导出配置。
9. **判断是否 snapshot**：只有关键裁决、验收、发布、事故、复盘或外部分发时，另存不可变快照；PDF 如果只是打印副本，不自动等于 snapshot。

## 方案边界

- Markdown / 数据 / 报告仍是真相源，不被 HTML 替代。
- HTML 是默认阅读容器，不应该散落在每个源页面旁边；当 HTML 不足以表达关系时，应由配套图像、图表或演示型文件补足。
- PDF / print view 是导出和分发层，不是真相源；导出前必须检查分页、图表裁切、来源页脚、证据边界和打印可读性。
- lens 不是固定模板，而是阅读协议；简单问题可以短文本回答，复杂问题才升级为图文混排 lens。
- 直观展示不能牺牲证据边界，尤其不能把历史报告、局部成功或代码层测试包装成完整当前结论。

## 关联页面

- [[concepts/problem-focused-information-presentation]]
- [[concepts/ai-era-information-presentation]]
- [[articles/2026-06-05-ai-era-information-presentation-research]]
- [[governance/response-mode-routing]]
- [[governance/state-constraint-reasoning]]
- [[projects/development/plan/work-item-system-model]]

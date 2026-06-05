# 摘要卡片层

这里放每篇材料的一张摘要卡片。

## 建议命名

- `YYYY-MM-DD-标题.md`

## 每页建议包含

- 来源
- 一句话总结
- 关键观点
- 相关工具
- 关联概念
- 待办或后续动作

## 维护原则

- 尽量只写一次摘要，不重复抄原文。
- 如果文章涉及很多工具，优先加链接，不要堆长段解释。
- 新增或大改摘要卡片时，按 [[knowledge-linking-rules]] 同步相关概念、入口回链和必要的案例 / 上位页承接，并运行 `python3 scripts/check_all.py --only knowledge-linking`。

## 信息架构 / 知识呈现

- [[articles/2026-06-05-ai-era-information-presentation-research]]：AI 时代信息记录、处理与呈现方式调研，梳理文件记录、chunk / vector 处理、Markdown 记录 + 处理、HTML 实时呈现和 HTML 记录边界。
- [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]：用 Life、DocCustomeranalysis、prefect、fetch-adapter 和 DocFilmCommunity 只读样本校准问题聚焦式图文 lens 的 current / snapshot、源刷新、背景框和用户入口体系。
- [[articles/2026-06-04-knowledge-linking-mechanism-research]]：新增知识关联机制调研，校准 Obsidian 图谱、Evergreen notes 和 Zettelkasten 方法论，说明本库采用“agent 语义判断 + sensor 结构检查”的知识网络机制。

## Agent / Harness 案例

- [[articles/2026-06-02-issue-original-evidence-asset-intake]]：Issue 原始图片证据未入库案例，分析模型可见图片与本地证据资产之间的断层，并提出高效的证据资产门方案。
- [[articles/2026-05-29-finalizer-write-scope-case]]：finalizer 写入范围失守案例，分析 clean proof 与 scope proof 混淆的问题。

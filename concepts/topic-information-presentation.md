---
type: concept
name: Topic Information Presentation
status: active
source_of_truth: true
updated: 2026-07-29
---

# 主题信息呈现

主题信息呈现从即时 subject/source 输入组织关系、证据、生命周期、读者任务和交付形态；主题不等于仓库中必须预先存在 Topic 文档。运行以 `admit / reject / clarify / abstain` 路由，`admit` 默认 HTML，并为 inline、ephemeral、current、snapshot 生成同源 PDF/PNG。

项目 owner 与独立知识分离：项目事实留在 `projects/`，通用文章与概念留在 `articles/` / `concepts/`；呈现只做派生。`problem-focus` 是 content_scope 子模式。

质量分为五层：contract-schema、semantic-content、visual-quality、delivery-findability、reader-utility。semantic-content 需要确定性 sensor、独立模型 judge、版本化 rubric/calibration/trace；任何一层都不能上推，reader utility 在没有真实任务数据时保持 unproven。运行入口为 [[skills/topic-visual-presentation/SKILL]]，模板为 [[templates/topic-presentation-template]]，公开发布由 [[skills/public-html-publish/SKILL]] 独立承接。

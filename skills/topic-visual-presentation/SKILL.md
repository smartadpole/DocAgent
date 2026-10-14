---
name: topic-visual-presentation
description: 将主题材料组织为可阅读的 HTML：快速呈现默认轻量，来源有层级时映射页面树；显式导出、正式 page bundle 或治理评审时启用对应合同。
maturity: adopted-v2
evidence_signals: [skill, concept, template, governance, sensor, renderer, fixtures, legacy-baseline, runtime-readback]
transfer_ready: true
sensor: python3 scripts/check_all.py --only topic-visual-presentation
conditional_sources: [skills/topic-visual-presentation/references/formal-delivery.md]
---

# Topic Visual Presentation

从用户阅读目标和现有材料生成派生呈现，不要求先建 Topic 文档。项目事实留在项目 owner，独立知识留在知识 owner；HTML 和导出件不成为第二真相源。

## 默认快速呈现

适合图文组织时默认 HTML；普通短答、text-only 或视觉无收益时直接回答。根据来源中的信息关系组织结构，不把长文机械切卡片。已知/未知、来源冲突和结论边界保真；不得为了页面整齐删去用户要求的专业深度。

来源已有稳定层级时映射页面树；复杂单文档按独立语义模块判断拆页收益。单页与 page-tree 的选择服从阅读路径和导航成本，不由固定字数决定。页面树保留一个 root 与单一 edges，派生导航避免互相矛盾。

普通 inline/ephemeral HTML 不强制 subject/source schema、calibration、逐 claim binding、PDF/PNG、独立五门或持久 registry。按实际风险检查内容、来源、布局、移动阅读和链接；使用工具可见的证据报告结果，不虚报独立评审。

## 正式交付

用户要求 PDF/PNG、正式 canonical bundle、可审计治理证据或修改受 v2 管理的 artifact 时，读取 [[skills/topic-visual-presentation/references/formal-delivery]]，按实际模式采用 `topic-presentation-contract.v2`、renderer 与对应验证。请求单一导出格式时不自动追加其他格式；选择完整 v2 bundle 才执行该合同要求的同源导出与 binding。

公开分发是独立权限与交付范围；只有要求发布时使用 [[skills/public-html-publish/SKILL]]。没有公开下载 endpoint 不暴露 `.exports` 或本机绝对路径。

## 交付边界

交付实际 HTML/页面入口、用户所需导出及已验证范围。结构、内容、视觉、发布和读者效用分别表达：builder 自评不是 independent judge；任一检查通过都不能关闭业务 owner。历史 artifact 未修改时不追补新合同，既有源码和来源内容不以 alias 或摘要替换。

相关 owner：[[concepts/topic-information-presentation]]、[[governance/topic-visual-presentation-rules]]、[[templates/topic-presentation-template]]。迁移见 [[skills/topic-visual-presentation/TRANSFER]]。

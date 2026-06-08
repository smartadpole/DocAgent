---
type: article
id: ARTICLE-IMAGE-TEXT-LAYOUT-SYSTEM-RESEARCH-2026-06-08
scope: shared
status: active
source_of_truth: false
updated: 2026-06-08
tags: [information-architecture, presentation, layout, image-text, visual-design]
---

# 图片与图文排版体系调研

## 来源

本页基于 2026-06-08 的专题调研，重点参考：

- [Britannica: The New Typography](https://www.britannica.com/topic/The-New-Typography-A-Handbook-for-Modern-Designers)：现代主义排版把文字、留白、尺度对比和空间关系当成设计元素。
- [Britannica: International Typographic Style](https://www.britannica.com/art/graphic-design/Graphic-design-1945-75)：瑞士风格把模块网格、摄影和无装饰信息组织推到系统化。
- [Interaction Design Foundation: Gestalt Principles](https://ixdf.org/literature/topics/gestalt-principles)：相似、接近、连续、闭合、图地等知觉原则解释人如何把视觉元素组织成整体。
- [Material Design: Understanding layout](https://m2.material.io/design/layout/understanding-layout.html) 与 [Responsive UI](https://m1.material.io/layout/responsive-ui.html)：用列、沟槽、边距、断点和一致空间组织跨屏布局。
- [IBM Carbon 2x Grid](https://carbondesignsystem.com/elements/2x-grid/usage/)：把网格、比例、对比、留白和内容分组落成产品设计系统。
- [W3C CSS Grid Layout](https://www.w3.org/TR/css-grid/) 与 [MDN CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)：Web 端二维布局系统，适合定义区域、位置、层叠和组件内部关系。
- [MDN Responsive images](https://developer.mozilla.org/docs/Web/HTML/Guides/Responsive_images) 与 [`picture`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)：响应式图片和 art direction，把同一视觉意图适配到不同屏幕和像素密度。
- [MDN `figure`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure) 与 [W3C WAI alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)：图片、说明文字、替代文本和可访问语义的边界。
- [MUI Image List](https://mui.com/material-ui/react-image-list/)：标准、瀑布流等图片集合模式，用重复结构提高视觉理解。
- [Canva Creative Operating System](https://www.canva.com/newsroom/news/creative-operating-system/)：商业工具正把 AI 设计能力从生成单张图推进到理解布局、层级和品牌规则。
- [Intelligent layout generation survey](https://www.sciencedirect.com/science/article/pii/S1566253523002567)、[LayoutDiT](https://arxiv.org/abs/2407.15233)、[AI-Driven Graphic Design survey](https://arxiv.org/abs/2503.18641)：AI layout generation 开始把元素位置、尺寸、裁切、变换、审美和语义关系作为可学习对象。

## 一句话总结

图片排版不是“把图摆好看”，图文排版也不是“图片旁边配文字”；更稳定的体系是：先判图片在当前问题中承担什么信息职能，再用网格、比例、视觉层级、图文绑定、响应式媒介和可访问语义，把图片、标题、正文、标注、证据和行动入口组织成一条可理解的阅读路径。

## 历史线索

| 阶段 | 核心变化 | 对本库的启发 |
| --- | --- | --- |
| 现代主义排版 | 文字、图像、留白、比例和尺度对比开始作为同一个视觉系统处理 | 图文不是装饰关系，而是共同承担信息结构 |
| 瑞士网格 / 国际主义 | 模块网格、摄影、无装饰、客观信息组织成为主流方法 | 图文 lens 需要先有空间骨架和对齐关系 |
| Web / 响应式设计 | CSS Grid、断点、`srcset`、`picture` 让布局和图片裁切按媒介变化 | 同一图文结论必须能跨桌面、移动和打印保持语义一致 |
| AI layout generation | 模型开始生成或修正元素位置、尺寸、层级、品牌和背景适配 | AI 可以辅助出稿，但仍要受源、层级、可访问性和可编辑性约束 |

## 核心模型

图片 / 图文排版可以拆成七层：

| 层级 | 要回答的问题 | 典型对象 |
| --- | --- | --- |
| 意图层 | 这张图为什么出现 | 证据、示意、对比、情绪、导航、品牌、封面 |
| 素材层 | 图片本身是否适合当前任务 | 主题、裁切、清晰度、比例、版权、来源、alt、caption |
| 空间骨架层 | 页面如何承载这些元素 | 网格、列、沟槽、边距、基线、断点、纸张尺寸 |
| 视觉组织层 | 读者先看哪里、怎样分组 | 层级、对比、接近、相似、连续、留白、节奏 |
| 图文绑定层 | 图片和文字是什么关系 | 标题、说明、标注、旁注、overlay、callout、引用、证据表 |
| 媒介适配层 | 换屏幕、打印、导出后还是否成立 | 响应式图片、art direction、A4 / A3、PDF / PNG、打印分页 |
| 治理生成层 | 这套排版如何复用和审计 | design tokens、模板、manifest、source pack、AI 生成约束、可编辑层 |

这个模型和 [[concepts/problem-focused-information-presentation]] 的关系是：问题聚焦式信息呈现决定“当前要看什么 lens”，图片 / 图文排版体系决定“这个 lens 里的视觉和文字如何组织”。

## 图片排版

| 图片职能 | 优先版式 | 关键风险 |
| --- | --- | --- |
| 主图 / 封面 | hero、全幅、焦点裁切、标题避让 | 裁切掉主体、文字压在复杂背景上、装饰盖过信息 |
| 证据图片 | figure + caption、证据表、前后对比、缩略图 + 放大入口 | 缺来源、缺时间、缺可访问说明、把局部证据上推 |
| 过程截图 | 时间线、步骤序列、编号标注、局部放大 | 截图太小、步骤和说明错位、未标明环境 |
| 图库 / 素材集 | 标准网格、等比例 tile、瀑布流、筛选 gallery | 瀑布流不适合严格比较；同等大小会抹平层级 |
| 对比图 | 2-up / 3-up、同步裁切、差异标注、热区 overlay | 视角不一致导致比较失真 |
| 图解 / 架构 | 框图、关系图、流程图、分层图 | 只画漂亮结构，不保留源和边界 |
| 情绪 / 品牌图 | 大留白、色调统一、低信息密度背景 | 用氛围图替代真实内容，导致判断失焦 |

图片排版的判断顺序应是：先判图片是否是信息本体，再判是否需要裁切、缩放、组合、标注、说明和替代文本；最后才选择视觉风格。

## 图文排版

| 图文关系 | 适用场景 | 版式要点 |
| --- | --- | --- |
| 图主文辅 | 产品、地点、证据、人物、封面 | 图像占主视觉，文字只解释判断和行动 |
| 文主图辅 | 研究、说明、知识文章 | 图片作为例证、图解或证据，不打断阅读流 |
| 图文并列 | 方案比较、案例拆解、before / after | 两侧信息粒度要对齐，避免图片和文字各讲各的 |
| 图内标注 | 截图说明、地图、界面分析、故障定位 | callout 要短，长解释放到旁注或证据表 |
| 图上覆盖文字 | 海报、封面、社交图、hero | 必须保证对比度、主体避让和响应式裁切 |
| 卡片聚合 | 资源库、状态、人物、案例、产品列表 | 固定比例、统一信息槽位、稳定对齐点 |
| 长图叙事 | 时间线、教程、报告摘要、社交 carousel | 每屏一个判断，避免长图变成无法追溯的压缩文档 |
| 图表 + 文字 | 数据报告、验收、诊断、趋势分析 | 标题说结论，图表承载证据，脚注讲口径和边界 |

好的图文排版不是“图多一点”，而是每个视觉单元都有清楚的信息责任：吸引注意、建立上下文、证明判断、解释关系、比较差异、引导行动或保存证据。

## 决策矩阵

| 当前任务 | 优先图文体系 | 不建议默认使用 |
| --- | --- | --- |
| 看一个文档的背景和作用 | 单文档 lens：封面信息 + 结构图 + 关键 figure + 关系回链 | 只给长文字摘要 |
| 看一个主题的材料体系 | 主题地图 + 证据分层 + 关键图组 + 时间线 | 一张大而全脑图 |
| 验收 / 复验 | 证据截图表 + local / service-side / end-to-end 分层 + 缺口矩阵 | 漂亮 dashboard 替代关闭裁决 |
| 问题定位 | 原始截图 + 时间线 + fault tree + 局部放大 | 先做结论海报 |
| 方案比较 | 统一比例对比图 + 决策矩阵 + 风险标注 | 瀑布流图库 |
| 知识教学 | 概念框图 + 逐层例图 + 反例图 | 全靠 PPT bullet |
| 项目状态 | blocker-first 状态卡 + owner / evidence 关系图 | 历史报告截图堆叠 |
| 对外分发 | 同源 HTML + print profile + PDF snapshot | 手工另排一份 PDF |

## AI 方向的判断

AI layout generation 的价值不在“替你摆图”，而在四类能力：

1. **布局候选生成**：根据图片、标题、文案、品牌和媒介生成多个可编辑候选。
2. **内容感知排版**：识别图像主体、留白、显著区域和文字避让区，避免裁切或遮挡关键内容。
3. **多格式重排**：同一设计从海报、文章、slide、社交图、移动页、A4 PDF 之间转换。
4. **质量检查**：发现对齐、拥挤、层级缺失、低对比、图片失真、caption / alt 缺口和品牌不一致。

但它仍有硬边界：不能把 AI 输出的扁平图当真相源；不能牺牲可编辑层、可访问文本、来源、证据边界和响应式适配；不能让模板审美覆盖当前问题的判断目的。

## 对本库的落地建议

本库以后遇到“图片排版 / 图文排版 / 一图胜千言 / HTML 图文 lens”时，可以先套这个判断顺序：

1. 先判当前问题属于 [[concepts/problem-focused-information-presentation]] 的哪类 lens。
2. 再判每张图片的职能：证据、示意、对比、导航、品牌、封面还是情绪。
3. 为 lens 选择空间骨架：单栏阅读、双栏图文、卡片网格、证据表、时间线、框图、主题地图或 print spread。
4. 写清图文绑定：caption、annotation、callout、overlay、旁注、脚注、证据表和回链各自承担什么。
5. 做媒介适配：桌面 / 移动 / 打印 / PDF / PNG 是否同源，是否需要 art direction、`srcset`、A4 / A3 和分页策略。
6. 最后才考虑 AI 或模板生成；生成物必须保持可编辑、可追溯、可访问和不重复入库。

## 常见误区

- 把网格当装饰，而不是用来控制对齐、层级和阅读路径。
- 把所有图片做成同等大小，导致证据、例子、封面和装饰失去层级。
- 让文字覆盖复杂图像，却没有对比、遮罩、主体避让或移动端裁切。
- 用瀑布流展示需要严格比较的证据。
- 用长图替代可追溯文档，导致无法链接、无法更新、无法验证来源。
- 把 caption 当 alt，或把 alt 当 caption；二者一个服务可访问替代，一个服务读者上下文。
- 把 AI 生成图文当最终设计稿，忽略响应式、打印、品牌、可编辑层和证据边界。

## 相关概念

- [[concepts/image-text-layout-system]]
- [[concepts/problem-focused-information-presentation]]
- [[concepts/ai-era-information-presentation]]
- [[skills/problem-focused-visual-presentation/SKILL]]

## 知识关联自检

- 上位概念 / owning page：[[concepts/problem-focused-information-presentation]]
- 邻接文章 / 案例：[[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]、[[articles/2026-06-05-ai-era-information-presentation-research]]
- 入口回链：[[articles/README]]、[[INDEX]]
- 是否需要新建或更新概念页：需要，已新增 [[concepts/image-text-layout-system]]

## 后续动作

- 如果后续要把它升级成执行能力，可更新 [[skills/problem-focused-visual-presentation/SKILL]]，加入“图片职能 -> 图文绑定 -> 媒介适配”的检查表。
- 如果某个项目开始实际生成 HTML 图文 lens，可在目标项目的 `views/` 或等价呈现层中引入本页模型，但不要把本页变成项目状态源。

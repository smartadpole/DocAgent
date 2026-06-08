---
type: concept
id: CONCEPT-IMAGE-TEXT-LAYOUT-SYSTEM-001
status: active
updated: 2026-06-08
tags: [information-architecture, presentation, layout, image-text, visual-design]
---

# 图片与图文排版体系

## 定义

图片与图文排版体系，是指把图片、标题、正文、说明、标注、证据、留白、网格、响应式规则和导出媒介组织成一条可读路径的方法。

它服务 [[concepts/problem-focused-information-presentation]]：问题聚焦式信息呈现负责选择当前 lens，图片与图文排版体系负责让这个 lens 的视觉结构、文字解释、证据边界和媒介适配成立。

## 核心判断

图文排版先问三件事：

1. **图片职能**：图片是证据、示意、对比、导航、品牌、封面还是情绪背景。
2. **图文绑定**：文字是在命名图片、解释图片、标注图片、和图片并列比较，还是覆盖在图片上形成主视觉。
3. **媒介适配**：这个图文关系在桌面、移动、打印、PDF / PNG、slide 或长图里是否仍然成立。

如果这三件事没有先定，网格、字体、颜色和模板都会变成表层装饰。

## 七层模型

| 层级 | 职责 | 产物 |
| --- | --- | --- |
| 意图层 | 确认图片为什么出现 | 证据 / 示意 / 对比 / 封面 / 品牌 / 情绪 |
| 素材层 | 确认图片质量和语义 | 来源、裁切、比例、alt、caption、版权 |
| 空间骨架层 | 规定页面承载方式 | 网格、列、沟槽、边距、基线、断点 |
| 视觉组织层 | 控制先后、分组和层级 | 对比、接近、相似、连续、留白、节奏 |
| 图文绑定层 | 绑定图片与解释 | 标题、说明、callout、旁注、overlay、证据表 |
| 媒介适配层 | 保证跨格式一致 | 响应式图片、art direction、print profile、snapshot |
| 治理生成层 | 保证可复用和可审计 | 模板、manifest、source pack、design tokens、AI 约束 |

## 图片职能分类

| 图片职能 | 默认处理 | 禁忌 |
| --- | --- | --- |
| 证据图 | 保留来源、时间、环境、caption、可放大入口 | 裁掉关键上下文或只做装饰展示 |
| 示意图 | 用简化结构帮助理解 | 冒充真实证据 |
| 对比图 | 统一比例、视角、裁切和标注 | 用不同尺度制造错觉 |
| 主图 / 封面 | 强焦点、标题避让、可响应裁切 | 用氛围替代真实对象 |
| 图库 / 素材集 | 统一 tile、筛选、分组和元数据 | 需要比较时使用瀑布流 |
| 图解 / 架构 | 保留节点、边界、方向和说明 | 只画好看，不说明证据边界 |
| 品牌 / 情绪图 | 控制色调和留白，不抢信息 | 让装饰影响判断 |

## 图文绑定模式

| 模式 | 适用 | 关键检查 |
| --- | --- | --- |
| `figure + caption` | 文章、报告、证据、教程 | caption 解释上下文，alt 服务可访问替代 |
| 图文并列 | 案例、方案、产品、before / after | 图和文的信息粒度是否对齐 |
| 图内标注 | 界面截图、地图、排障、证据定位 | callout 是否短；长解释是否外置 |
| 图上覆盖文字 | hero、海报、社交图、封面 | 对比度、主体避让、移动端裁切 |
| 卡片网格 | 资源、案例、人物、状态、产品 | 比例、槽位、元数据和交互是否统一 |
| 时间线图组 | 过程、事件链、教程 | 每个节点是否有时间、动作、证据 |
| 图表 + 文字 | 数据报告、验收、诊断 | 标题给结论，图表给证据，脚注给口径 |

## 和相邻概念的分工

- [[concepts/ai-era-information-presentation]] 回答信息记录、组织、处理、呈现和归档如何分层。
- [[concepts/problem-focused-information-presentation]] 回答围绕当前关注问题应选择什么 lens。
- [[concepts/image-text-layout-system]] 回答一个 lens 内部的图片、文字、标注、证据和媒介如何排。
- [[skills/problem-focused-visual-presentation/SKILL]] 回答 agent 实际生成图文 lens 时怎样识别关注合同、组 source pack、建立背景框和声明导出边界。

## 常见用法

- 设计知识文章中的图解、配图、图注和证据图。
- 设计 HTML lens、状态卡、验收报告、问题定位页和主题地图。
- 把截图、图片证据、标注和文字说明整理成可追溯证据链。
- 为同一图文内容设计桌面、移动、A4 / A3 PDF、PNG 或 slide 的同源版式。
- 评估 AI 生成图文设计是否可编辑、可访问、可追溯、可响应和不重复入库。

## 反模式

- 只追求“好看”，没有先定义图片的信息职能。
- 图片和文字各讲各的，读者无法知道哪段文字解释哪张图。
- 用长图压缩复杂知识，丢失链接、版本、来源和可更新性。
- 为了统一视觉，把证据图、示意图、封面图和装饰图处理成同一种视觉权重。
- 同一 lens 手工维护 HTML、PDF、PNG 多份不同内容，破坏 [[concepts/problem-focused-information-presentation|同源导出]] 边界。
- 把 AI 生成的扁平图片当作最终真相源，而不是可编辑、可追溯的呈现草稿。

## 相关页面

- [[articles/2026-06-08-image-text-layout-system-research]]
- [[concepts/problem-focused-information-presentation]]
- [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]
- [[articles/2026-06-05-ai-era-information-presentation-research]]
- [[skills/problem-focused-visual-presentation/SKILL]]

## 知识关联自检

- 上位概念 / owning page：[[concepts/problem-focused-information-presentation]]
- 邻接概念 / 案例：[[concepts/ai-era-information-presentation]]、[[articles/2026-06-08-image-text-layout-system-research]]
- 入口回链：[[concepts/README]]、[[INDEX]]
- 不进入的层级：本页不是执行技能，不直接规定每个项目必须生成图片或 HTML；具体执行看 [[skills/problem-focused-visual-presentation/SKILL]] 和目标项目呈现层。

## 维护说明

- 当新文章讨论图片、截图证据、图注、HTML lens、PDF 导出、AIGC layout 或视觉证据链时，把链接补回这里。
- 如果后续沉淀成 agent 执行步骤，应更新技能页而不是把本概念页改成操作手册。

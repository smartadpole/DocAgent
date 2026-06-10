---
type: concept
id: CONCEPT-COLOR-AESTHETIC-SYSTEM-001
status: active
updated: 2026-06-10
tags: [visual-design, color, aesthetics, accessibility, design-system]
---

# 配色与审美体系

## 定义

配色与审美体系，是指把颜色、明度、彩度、对比、留白、层级、材质、动效和品牌气质组织成可复用视觉规则的方法。

它不是单纯挑色板，而是服务 [[concepts/problem-focused-information-presentation]] 的视觉语义层：当一个 lens、知识页、状态矩阵或报告需要让读者快速判断时，颜色负责表达层级、行动、状态、数据和品牌；审美负责让这些信息之间形成稳定、克制、可信的秩序。

## 核心判断

配色和审美先问五件事：

1. **信息层级**：读者应该先看哪里，背景和辅助信息应该退到哪里。
2. **语义角色**：颜色是在表达行动、状态、品牌、数据，还是只是背景层。
3. **感知强度**：对比、明度、彩度和字号是否足够支持阅读和区分。
4. **场景气质**：当前对象需要专业、温和、前沿、克制、活泼还是仪式感。
5. **治理复用**：这些颜色是否能通过 token、主题、检查和模板长期复用。

如果这五件事没有先定，审美反馈就会退化成“喜欢 / 不喜欢”，配色也会退化成一组不可维护的 hex。

## 六层模型

| 层级 | 职责 | 典型产物 |
| --- | --- | --- |
| 感知层 | 保证可读、可辨、可访问 | 对比度、色弱安全、明暗关系 |
| 语义层 | 给颜色分配稳定含义 | brand、action、status、data、surface |
| 调和层 | 控制颜色之间的关系 | 单色、邻近、互补、三角色、中性底 |
| 结构层 | 用颜色强化布局和路径 | 背景层、卡片层、分割线、强调区 |
| 情绪层 | 形成符合场景的气质 | 专业、沉稳、温暖、科技、活力 |
| 治理层 | 让颜色可迁移和可检查 | design tokens、themes、WCAG、视觉 QA |

## 颜色角色

| 角色 | 用法 | 检查点 |
| --- | --- | --- |
| 背景 / 表面 | 组织页面层级和区域 | 是否抢正文，是否能支持暗色 / 打印 |
| 文本 | 表达正文、弱化、禁用和辅助说明 | 普通文本是否达到对比度要求 |
| 行动 | 表达可点击、可选择、当前焦点 | 主行动是否唯一且稳定 |
| 状态 | 表达成功、警告、危险、等待、禁用 | 是否有文字 / 图标 / 形状冗余 |
| 数据 | 表达分类、顺序、强弱、异常 | 色相和明度是否都支持区分 |
| 品牌 | 表达长期识别和气质 | 是否污染功能色和状态色 |

## 和相邻概念的分工

- [[concepts/ai-era-information-presentation]] 回答信息记录、组织、处理、呈现和归档如何分层。
- [[concepts/problem-focused-information-presentation]] 回答当前问题应该使用什么 lens。
- [[concepts/image-text-layout-system]] 回答 lens 内部的图片、文字、标注、证据和媒介如何排。
- [[concepts/color-aesthetic-system]] 回答 lens 和知识页面内部的颜色语义、审美秩序和视觉气质如何成立。
- [[skills/problem-focused-visual-presentation/SKILL]] 回答 agent 实际生成图文 lens 时怎样把这些视觉规则落实到产物和检查中。

## 常见用法

- 为知识库 HTML lens、状态卡、矩阵、热力图、验收报告和调研页面建立颜色角色。
- 判断一个页面“好看但不好用”或“信息正确但不可信”的原因。
- 把用户的审美反馈拆成层级、密度、对比、色彩语义、留白和气质几个可改点。
- 把具体配色从项目事实中抽象为可迁移的 token / theme / usage rule。
- 检查 AI 生成或模板生成的界面是否牺牲了可访问性、证据边界和信息层级。

## 反模式

- 把配色当装饰，而不是当信息系统。
- 用低对比和浅灰文字制造“高级感”。
- 只靠红绿表达状态，缺少文字、图标或形状。
- 一个品牌色承担所有行动、状态、图表和装饰职责。
- 只追逐流行风格，不考虑读者任务、媒介和场景气质。
- 用审美效果遮蔽真实可用性问题、证据缺口或验收边界。

## 相关页面

- [[articles/2026-06-10-color-aesthetic-system-research]]
- [[concepts/image-text-layout-system]]
- [[concepts/problem-focused-information-presentation]]
- [[articles/2026-06-08-image-text-layout-system-research]]
- [[skills/problem-focused-visual-presentation/SKILL]]

## 知识关联自检

- 上位概念 / owning page：[[concepts/problem-focused-information-presentation]]
- 邻接概念 / 案例：[[concepts/image-text-layout-system]]、[[articles/2026-06-08-image-text-layout-system-research]]
- 入口回链：[[concepts/README]]、[[INDEX]]
- 不进入的层级：本页不是具体项目设计系统，不规定固定品牌色、组件 token 名或某个项目必须采用的配色方案。

## 维护说明

- 当新文章讨论配色、审美、视觉风格、状态色、图表色、主题 token、暗色模式或可访问对比时，把链接补回这里。
- 如果后续沉淀成执行步骤，应优先更新 [[skills/problem-focused-visual-presentation/SKILL]] 或相关模板，而不是把本概念页改成完整设计系统手册。

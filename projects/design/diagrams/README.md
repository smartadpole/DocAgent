---
type: design_diagrams
id: DES-DIAGRAMS-001
project: PROJ-WIKI-001
status: active
stage: design
updated: 2026-05-28
tags: [design, diagrams, excalidraw, diagrams-net]
---

# 设计图资产

主入口：[[projects/design/README]]

这页是当前项目设计图资产的单一入口。它只管理图源文件、导出图和图工具规则，不替代 [[projects/design/architecture]]、[[projects/design/backend-frontend-structure]] 或 [[projects/service-registry]] 的正文职责。

## 工具分工

- **Excalidraw**：当前主力。用于全服务总览、业务到实现链路、服务拓扑草案、模块关系推演和需要频繁调整的大图。
- **Diagrams.Net**：正式交付版。只在架构关系已经稳定、需要汇报版 / 交付版 / 更正式制图时使用。
- **Mermaid**：只保留给局部小流程、状态机、短链路或代码块附近的轻量说明；不再承接大型系统架构图。
- **其他图工具**：当前不引入。D2、PlantUML、Graphviz 等只有用户重新拍板后才允许进入本项目规则。

## 存放规则

- 图源文件和可选导出图统一放在 `projects/design/diagrams/`。
- Excalidraw 源文件命名为 `*.excalidraw.md`。
- Diagrams.Net 源文件命名为 `*.drawio`。
- Markdown 正文默认嵌入 `*.svg` / `*.png` 作为可读预览，保证普通阅读页能直接看到完整图。
- 同一段落必须回链 Excalidraw 源文件，编辑时从源文件进入 Excalidraw View，拖拽节点并调整箭头。
- `*.svg` / `*.png` 是阅读、发布和汇报快照，不是源文件；修改图形结构时必须先改 Excalidraw 源文件，再按需要更新导出图。
- 大型图的 Markdown 正文必须同时满足“直接看得到图”和“直接定位到可编辑源文件”。

## 当前图资产

暂无正式图资产。新增正式架构图、服务拓扑图、业务到实现总览图或跨模块数据流图时，先在这里登记，再回链到对应设计正文。

| 图 | 用途 | 正文预览图 | 可编辑源文件 | 当前主入口 |
| --- | --- | --- | --- | --- |

## 维护规则

- 修改导出图时，必须同步更新源文件；不能只改 SVG / PNG。
- 修改源文件后，优先确认 Obsidian 中的 SVG / PNG 预览能显示完整图，并确认 Excalidraw 源文件能打开编辑；如果正文使用该导出图，必须同步重新导出或更新快照。
- 如果图里的服务、模块、实例或运行事实发生变化，只改图不够：还要同步对应的设计页、模块页或 [[projects/service-registry]]。
- 如果图还在推演阶段，优先使用 Excalidraw；不要过早转成 Diagrams.Net 正式图。
- 如果图已经成为对外汇报或交付材料，可以基于 Excalidraw 稳定版另做 Diagrams.Net 正式版，但必须保留二者的用途边界。

# 主题呈现

本页是 [[AGENTS]] 按需加载的唯一条件正文；只读取与当前任务相关的章节。

- 主题呈现先读 [[skills/topic-visual-presentation/SKILL]] 与目标事实 owner / 直接来源。默认快速生成结构清楚、显式表达关系的轻量 HTML；已有源层级时映射页面树，复杂单文档按语义模块组织。不得为了省流程压缩专业内容、隐去关键证据或把一切改成摘要卡。

- 需要持久 current / snapshot 时按 [[views/README]] 和 [[views/lens-registry]] 落位与登记。用户明确要求正式 PDF / PNG 导出、公开交付或治理级证据时，读取 [[templates/topic-presentation-template]] 的适用专业合同；导出缓存落在 `.gitignore` 忽略目录。普通 HTML 不强制生成导出件、source pack 全套表单或五门裁决。

- 正式持久 lens / 导出使用 v2 专业合同时，在 HTML meta、JSON script 或等价机器可读块中保留 `static_visual_qa`；实际请求的 PDF / PNG 必须来自同一 source manifest 或同一 render pipeline。没有真实导出和检查时不得声称“已导出”。轻量 HTML 同样需要核对真实内容、关系、链接与可读性，不能用未执行的视觉检查作为通过证据。

- 如果是问题聚焦式图文 lens、current / snapshot 视图或持久 HTML / print view，优先放 `views/`，并同步 [[views/lens-registry]]；不要放到仓库根目录、handoff、临时目录或把导出件提交成事实源。

- 大型架构图、服务拓扑图、业务到实现总览图和跨模块数据流图不得继续默认用 Mermaid 承载。当前图工具固定为 Excalidraw 和 Diagrams.Net：Excalidraw 负责当前主力推演图和持续维护图；Diagrams.Net 只负责架构冻结后的正式交付 / 汇报图；Markdown 正文默认嵌入 SVG / PNG 作为可读预览，并在同段落回链 Excalidraw 源文件用于编辑。Mermaid 只保留给局部小流程、状态机或短链路说明；不得新增 D2 或其他图工具，除非用户重新拍板。

- 用户要求正式导出、公开发布或治理级验收时，保留 v2 专业合同的 `admit / reject / clarify / abstain`、subject_package / source_pack、三轴、五门 evaluator、版本化 trace 和同源导出验证，按适用对象补齐。`problem-focus` 只是 content_scope；任何 lens 都不替代事实 owner、验收、状态或规则裁定。

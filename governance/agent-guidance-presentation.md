# 主题呈现

本页是 [[AGENTS]] 按需加载的唯一条件正文；只读取与当前任务相关的章节。

- 如果目标在 `views/`，先读 [[README]]、[[INDEX]]、[[views/README]]、[[skills/topic-visual-presentation/SKILL]]、[[templates/topic-presentation-template]] 和目标事实源；current / snapshot 必须同步 [[views/lens-registry]]，导出 PDF / PNG 缓存必须落在 `.gitignore` 忽略目录。

- 如果目标是持久 HTML lens，必须在 HTML meta、JSON script 或等价机器可读块中保留 `static_visual_qa`，并检查 PDF / PNG 是否来自同一 source manifest 或同一 render pipeline；没有真实导出和检查时不得声称“已导出”。

- 如果是问题聚焦式图文 lens、current / snapshot 视图或持久 HTML / print view，优先放 `views/`，并同步 [[views/lens-registry]]；不要放到仓库根目录、handoff、临时目录或把导出件提交成事实源。

- 大型架构图、服务拓扑图、业务到实现总览图和跨模块数据流图不得继续默认用 Mermaid 承载。当前图工具固定为 Excalidraw 和 Diagrams.Net：Excalidraw 负责当前主力推演图和持续维护图；Diagrams.Net 只负责架构冻结后的正式交付 / 汇报图；Markdown 正文默认嵌入 SVG / PNG 作为可读预览，并在同段落回链 Excalidraw 源文件用于编辑。Mermaid 只保留给局部小流程、状态机或短链路说明；不得新增 D2 或其他图工具，除非用户重新拍板。

- 当用户要求看主题、复杂关系、状态、风险、计划、验收、issue 或知识材料，先按 [[skills/topic-visual-presentation/SKILL]] 做 `admit / reject / clarify / abstain`，以即时 subject_package / source_pack、三轴和五门 evaluator 决定输出；admit 默认 HTML 并同源生成 PDF / PNG。`problem-focus` 只是 content_scope，lens 不替代 owner、验收、状态或规则裁定。

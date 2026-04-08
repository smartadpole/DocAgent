# Log

> append-only

## 2026-04-08

- 初始化 `wiki` vault。
- 配置 `Obsidian`、`Codex CLI`、`workspace-filesystem`、`workspace-memory`。
- 建立 `README.md`、`WORKFLOW.md`、`templates/`、`articles/`、`concepts/`、`indexes/`。
- 后续维护改为 `raw/ -> articles/concepts/indexes -> log.md` 的持续编译流程。
- 补充文件与目录操作流程：新建目录、新建文件、修改文件、处理已有目录。
- 将“新目录 / 新文件 / 修改文件 / 目录复用 / 链接影响 / 记录日志”等关键判断前置到 `README.md` 和 `INDEX.md`，避免总入口过于隐蔽。
- 在总入口补充了“怎么用这个 vault / 先看什么 / 常见操作对应关系 / 可直接复制的指令模板”，让 README 真正承担使用说明。
- 进一步明确 `raw/` 与 `inbox/` 的边界，补入 `assets/` 与 `archive/` 的生命周期规则，并把 `workspace-memory` 限定为稳定偏好而不是唯一规则源。
- 清理了根目录两个空的 `canvas` 占位文件，改用 `assets/` 作为支持性可视化文件落点。
- 增加 `projects/` 作为活跃软件研发项目层，明确知识库模式是底座、研发模式是叠加层，并补了项目模板与项目运行说明。
- 为 `projects/` 补了手动流控、项目主页优先和活跃项目汇总入口的约定。
- 进一步收紧为极简小项目模式：默认一页项目主页 + 总日志，其他项目文件按需添加，不预建空结构。
- 把新建目录规则进一步改成“README 先行，模板和索引按需创建”，避免极简模式被默认的重结构约束反向拉重。
- 进一步把模板定位为加速器而非门槛：项目主页可以直接手写，不必先复制模板。
- 把“研发推进的关键原则”单独沉淀到 `projects/README.md` 和 `WORKFLOW.md`，强调项目主页、代码仓库、问题定义、过程记录和知识回写这几条最重要的研发约束。

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

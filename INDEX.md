# 知识库入口

这是一套给 Obsidian + Codex 用的文档系统。

如果你不知道先看什么，按这个顺序：

1. 先看 [README.md](./README.md)，知道这个 vault 是干什么的、怎么启动、怎么选动作。
2. 要处理文件和目录细节，就看 [WORKFLOW.md](./WORKFLOW.md)。
3. 要知道 agent 的维护边界，就看 [AGENTS.md](./AGENTS.md)。
4. 要找入口分类和运行记录，就留在这页。

这页只做总导航，不承载细节。

先看这几个总入口判断：
- 这是新目录还是已有目录扩展
- 这是新文件还是修改已有文件
- 这份材料应该进哪一层
- 这次改动会不会影响链接和索引
- 这次处理要不要记进 `log.md`

当前工具：
- `Obsidian`：浏览、编辑、链接 Markdown
- `Codex CLI`：读写文件、批量整理、生成索引
- `workspace-filesystem` MCP：让 Codex 直接访问 `/Users/hai/Documents/Software`
- `workspace-memory` MCP：保存长期规则、偏好和稳定结论

层级：
- `raw/`：原始资料层，尽量只进不改
- `inbox/`：临时收口区，来源还没完全整理前先放这里
- `assets/`：截图、图片、导图、导出物和辅助附件
- `articles/`：每篇材料一张摘要卡片
- `concepts/`：每个工具或概念一个页面
- `indexes/`：全局索引、分类索引、时间线索引
- `archive/`：退役但仍需保留的页面和历史版本

运行记录：
- [log.md](./log.md)：按时间追加的 ingest / lint / decision 记录

更新原则：
- 工具名和概念名尽量用 `[[双向链接]]`
- 新内容先写成摘要卡片，再汇总到概念页和索引页
- 长期不变的规则和偏好写进 `workspace-memory`

# 知识库入口

这是一套给 Obsidian + Codex 用的文档系统。先看 [README.md](./README.md)，再看 [WORKFLOW.md](./WORKFLOW.md)。

当前工具：
- `Obsidian`：浏览、编辑、链接 Markdown
- `Codex CLI`：读写文件、批量整理、生成索引
- `workspace-filesystem` MCP：让 Codex 直接访问 `/Users/hai/Documents/Software`
- `workspace-memory` MCP：保存长期规则、偏好和稳定结论

推荐结构：
- `inbox/`：原始材料，先收进来，再整理
- `articles/`：每篇材料一张摘要卡片
- `concepts/`：每个工具或概念一个页面
- `indexes/`：全局索引、分类索引、时间线索引

更新原则：
- 工具名和概念名尽量用 `[[双向链接]]`
- 新内容先写成摘要卡片，再汇总到概念页和索引页
- 长期不变的规则和偏好写进 `workspace-memory`

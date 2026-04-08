# 文档系统说明

这个 vault 的目标很简单：把散乱资料变成能查、能连、能持续更新的知识网络。

## 这组工具怎么配合

- `Obsidian` 用来浏览、编辑和串联笔记。
- `Codex CLI` 用来读取、改写、批量生成 Markdown。
- `workspace-filesystem` 让 Codex 直接操作 `/Users/hai/Documents/Software` 下的文件。
- `workspace-memory` 记录长期规则、偏好、命名习惯和稳定结论。

## 最短工作流

1. 新材料先丢进 `inbox/`。
2. 让 Codex 把材料整理成一篇 `articles/` 摘要卡片。
3. 把反复出现的工具和概念抽到 `concepts/`。
4. 把入口、分类和时间线写到 `indexes/`。
5. 稳定下来的规则记到 `workspace-memory`，避免下次重复决定。

## 新建目录时

- 先建 `README.md` 说明用途。
- 再建一个最小模板文件，方便后续复制。
- 然后从 `INDEX.md` 补入口链接。

## 打开方式

- `open -a Obsidian /Users/hai/Documents/Software/wiki`
- `open 'obsidian:///Users/hai/Documents/Software/wiki/INDEX.md'`

## 更新原则

- 一篇材料只维护一张主摘要卡片。
- 一个概念只维护一个主页面。
- 索引页永远指向最新入口，不堆内容。
- 如果暂时不知道怎么归类，先放 `inbox/`。

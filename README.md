# 文档系统说明

这个 vault 的目标很简单：把散乱资料变成能查、能连、能持续更新的知识网络。

如果只记一件事，就记住这一层分法：

- `raw/` 放原始资料
- `inbox/` 放临时待处理内容
- `assets/` 放截图、图片、导出物和辅助附件
- `projects/` 放活跃软件研发项目
- `articles/`、`concepts/`、`indexes/` 放整理后的知识
- `archive/` 放退役但仍需保留的旧页面
- vault 根目录主要放入口、规则和总索引
- `AGENTS.md` 放维护规则

## 怎么用这个总入口

如果你第一次打开这个 vault，就按这个顺序走：

1. 先看这页，知道它是做什么的、怎么分层、怎么启动。
2. 如果你要新增或修改文档，去看 [WORKFLOW.md](./WORKFLOW.md)。
3. 如果你要知道 agent 能做什么、不能做什么，去看 [AGENTS.md](./AGENTS.md)。
4. 如果你只是想找入口，直接看 [INDEX.md](./INDEX.md)。

常见操作对应关系：

- 想知道“这个系统怎么用” -> 读这页
- 想知道“新建目录 / 新建文件 / 修改文件怎么做” -> 读 `WORKFLOW.md`
- 想知道“Codex 处理时有哪些约束” -> 读 `AGENTS.md`
- 想知道“入口页、索引页、层级在哪” -> 读 `INDEX.md`

如果你想直接让我做事，可以直接发这种话：

- `请把这份材料整理成 articles 摘要卡，并更新相关 concepts 和 indexes。`
- `请检查这个目录是否应该新建，还是复用已有目录。`
- `请把这个页面重命名，并同步更新所有内部链接。`
- `请帮我把这个目录按 raw / inbox / articles / concepts / indexes 重新归类。`

## 先看这些关键问题

如果你只从总入口判断要不要动文档，先看这 5 件事：

- 这是新目录，还是已有目录的扩展？
- 这是新文件，还是对已有文件的修改？
- 这份材料该进 `raw/`、`inbox/`、`articles/`、`concepts/` 还是 `indexes/`？
- 这次改动会不会影响链接、目录名或索引？
- 这次处理是不是有长期价值，需要写进 `log.md` 或 `workspace-memory`？

## 这组工具怎么配合

- `Obsidian` 用来浏览、编辑和串联笔记。
- `Codex CLI` 用来读取、改写、批量生成 Markdown。
- `workspace-filesystem` 让 Codex 直接操作 `/Users/hai/Documents/Software` 下的文件。
- `workspace-memory` 记录长期规则、偏好、命名习惯和稳定结论。

## 软件研发模式怎么叠加

可以把原有底座理解成只有知识库模式。

知识库模式默认负责这些事：

- 收集原始资料
- 编译成摘要卡片、概念页和索引页
- 把稳定结论沉淀为长期知识

如果当前在做一个活跃的软件项目，再叠加 `projects/` 作为项目运行层：

- 项目层负责需求、设计、任务、决策、发布和复盘
- 知识库层负责把可复用的稳定结论抽象出来
- 流程控制不做自动化，由人读项目主页和状态后手动推进
- 任何会重复使用的内容，最后都要回写到知识库层

如果你正在做研发，先看 [projects/README.md](./projects/README.md)。

如果是极简小项目，默认只需要：

- 一个项目主页 `projects/<项目名>/README.md`
- 一个总日志 `log.md`
- 必要时再补 `decisions.md`、`worklog.md` 这类文件

不要为了“结构完整”提前建一堆空文件。

## 最短工作流

1. 新材料先丢进 `inbox/` 或直接放进 `raw/`。
2. 让 Codex 把材料整理成一篇 `articles/` 摘要卡片。
3. 把反复出现的工具和概念抽到 `concepts/`。
4. 把入口、分类和时间线写到 `indexes/`。
5. 把过程和决策追加到 `log.md`。
6. 稳定下来的规则记到 `workspace-memory`，避免下次重复决定。

## 新建目录时

- 先建 `README.md` 说明用途。
- 模板和索引按需创建，不要为了完整性先铺满。
- 需要入口时，再从 `INDEX.md` 补链接。

## 为什么入口页不写太细

- `README.md` 负责让你快速判断方向，不负责承载所有细则。
- 详细的文件和目录流程放在 `WORKFLOW.md`。
- 维护约束和行为边界放在 `AGENTS.md`。
- 这样总入口不会变成长手册，但关键分流点仍然能一眼看到。

## 打开方式

- `open -a Obsidian /Users/hai/Documents/Software/wiki`
- `open 'obsidian:///Users/hai/Documents/Software/wiki/INDEX.md'`

## 更新原则

- 一篇材料只维护一张主摘要卡片。
- 一个概念只维护一个主页面。
- 索引页永远指向最新入口，不堆内容。
- `log.md` 只追加，不重写。
- 原始来源只进 `raw/`，临时待处理内容只进 `inbox/`，整理稿不要回塞 `raw/`。
- 支持性图片、截图、图表和 canvas 等辅助文件优先放 `assets/`。
- 不再作为默认入口但仍需保留的页面放 `archive/`。
- 如果暂时不知道怎么归类，先放 `inbox/`。

---
type: article
date: 2026-05-28
updated: 2026-05-28
---

# OpenClaw 记忆系统调研

- 来源：OpenClaw 官方文档与官方仓库文档源码
- 日期：2026-05-28
- 类型：研究

## 一句话总结

OpenClaw 的记忆系统不是“藏在框架里的黑盒向量库”，而是一套以本地 Markdown 为真相源、以检索和晋升机制为补充、并且显式受 prompt 预算约束的分层 memory 体系。

## 核心判断

### 1. 它把 memory 当成工作区，而不是单独插件

OpenClaw 把 agent workspace 直接当成记忆主场。`AGENTS.md`、`SOUL.md`、`USER.md`、`MEMORY.md`、`memory/YYYY-MM-DD.md`、`DREAMS.md`、`skills/` 都在同一个工作区里协同工作，而不是把“规则”“人格”“记忆”“技能”完全拆成互不相见的独立黑箱。

这意味着它的 memory 不是单点模块，而是三层叠加：

- 启动注入层：`AGENTS.md`、`SOUL.md`、`USER.md` 等 bootstrap 文件
- 可检索记忆层：`MEMORY.md` 和 `memory/*.md`
- 编译 / 提升层：`DREAMS.md`、active memory、dreaming、`memory-wiki`

### 2. 它的长期记忆是“文件优先”，不是“模型偷偷记住”

OpenClaw 官方写得很明确：模型只会记住被写到磁盘上的内容，没有隐藏状态。

这点很重要，因为它把“记忆是否存在”变成了可检查、可版本化、可迁移、可备份的问题，而不是一次对话里模型是否碰巧记住。

### 3. 它天然分成“工作层”和“提纯层”

它至少有两个非常清晰的记忆层：

- `memory/YYYY-MM-DD.md`：工作层，放日记、观察、会话摘要、原始上下文
- `MEMORY.md`：提纯层，放长期稳定事实、偏好、决策和短摘要

官方设计不是要求每次都手工维护 `MEMORY.md`，而是鼓励先把细节落到 daily memory，再逐步蒸馏到长期记忆。

### 4. 它把“记得住”和“调得出来”分开设计

OpenClaw 不靠把所有 memory 永远塞进 prompt，而是分成两步：

1. 只把少量高价值 bootstrap 文件注入上下文
2. 其他 memory 通过 `memory_search` / `memory_get` 按需召回

这让它比“全量塞 prompt”更可扩展，也比“只有数据库没有文档真相源”更可审计。

## 记忆系统结构

### 1. `MEMORY.md` 是长期记忆

- 放 durable facts、preferences、decisions、short summaries
- 默认只在 main private session 加载，不应在群聊或共享上下文泄露
- 如果文件太大，磁盘上的原文会保留，但注入 prompt 的版本会被截断

这说明 OpenClaw 把长期记忆视为“启动时就该知道的压缩版共识”，而不是无限增长的日志仓库。

### 2. `memory/YYYY-MM-DD.md` 是每日工作记忆

- 记录当天观察、运行上下文、会话摘要和仍可能有用的原始材料
- 会被索引给 `memory_search` / `memory_get`
- 默认不会每轮都整份注入 bootstrap prompt
- 今天和昨天的 daily memory 会自动进入启动上下文

这层非常像“运行中的工作台账”，既比长时记忆细，又不等于完整聊天记录。

### 3. `DREAMS.md` 是记忆晋升的人工审阅面

`DREAMS.md` 不是普通 long-term memory，而是 dreaming sweep 和 grounded backfill 的 review 面。它承接：

- 候选长期记忆的阶段性汇总
- 旧 daily memory 回放后的结构化结果
- 人工审阅 dreaming 是否提纯得合理

也就是说，OpenClaw 没把“记忆晋升”设计成静默黑盒，而是保留了可审阅的中间层。

### 4. Action-sensitive memory 是它很值得借鉴的一点

官方专门强调：有些记忆不只是“事实”，还会改变未来动作，所以必须连同 action boundary 一起记下，比如：

- 是否需要批准
- 临时限制是否还有效
- 何时可以安全执行
- 谁是 authority / owner
- 到何时过期

这和单纯“记住一条偏好”完全不同，更接近执行合同和操作边界。

## 检索与召回

### 1. 内建检索引擎是 SQLite + FTS + 向量混合

OpenClaw 默认的 builtin memory engine：

- 用 SQLite 存 per-agent index
- 对 `MEMORY.md` 和 `memory/*.md` 做 chunking
- 支持 BM25、向量检索和 hybrid search
- 默认 chunk 大约 400 tokens，80-token overlap
- 文件变化后会自动 reindex

这套默认引擎的优点是开箱即用，而且没有强依赖外部服务。

### 2. 检索层做了不少工程化细节

`memory_search` 不是简单向量搜一下，而是明确支持：

- hybrid merge
- MMR 去重
- temporal decay 时间衰减
- CJK trigram tokenizer
- multimodal memory
- 可选 session transcript recall

这说明 OpenClaw 认为记忆问题不只是“存下来”，更是“怎么避免旧内容、重复内容、错语义内容污染召回”。

### 3. QMD 是它的高级本地 sidecar

如果 builtin engine 不够，OpenClaw 还支持 QMD：

- 本地 sidecar
- BM25 + vector + reranking + query expansion
- 可索引工作区外部目录
- 可索引会话 transcript
- QMD 故障时能回退到 builtin SQLite engine

这让它从“记忆系统”扩展成“本地知识检索底座”。

### 4. Active Memory 解决的是“来不及想起”

OpenClaw 还专门做了一个 optional 的 active memory plugin：

- 在主回复前跑一次 blocking memory sub-agent
- 给系统一次 bounded 的 recall 机会
- 默认只对 direct-message、interactive、persistent session 开启
- 不在 heartbeat、one-shot、sub-agent helper 等路径乱开

这解决的不是存储问题，而是“主 agent 没有主动搜 memory 时，相关记忆根本不会自然浮现”的问题。

## 记忆晋升与压缩

### 1. Compaction 前会先做 memory flush

这是它非常实用的一层保护：

- 在 compaction 总结长对话前
- 先跑一轮 silent memory flush
- 提醒 agent 把重要上下文写回 memory 文件

这样 compaction 不会直接把还没落盘的重要信息吞掉。

### 2. Dreaming 是后台 consolidation，不是默认永远开

Dreaming 在 OpenClaw 里是 opt-in 的背景整理流程：

- 从短期信号里挑候选
- 经过 score、recall frequency、query diversity 等门槛
- 只有 qualified items 才晋升进 `MEMORY.md`
- 结果写到 `DREAMS.md` 供人审查

这比“每次都自动提炼到长期记忆”更克制，也更容易控制长期记忆污染。

### 3. Grounded backfill 让旧 daily memory 也能重放

它甚至支持把历史 `memory/YYYY-MM-DD.md` 当作独立 day files 回放，再把结果写进 `DREAMS.md` 或 stage 到短期 dreaming store。这个设计很适合“后来才开始认真做记忆治理”的场景。

## `memory-wiki`：从 memory 到知识库

`memory-wiki` 是我认为最接近当前文档库兴趣点的一层。

它不是替代 active memory，而是在旁边再加一个 compiled knowledge layer：

- 把 durable memory 编译成 wiki vault
- 有 deterministic page layout
- 有 structured claims / evidence
- 有 provenance、confidence、contradictions、open questions
- 有 dashboards 和 machine-readable digests
- 可以 bridge 到 active memory 的公共 artifacts

它本质上是在说：原始记忆、长期摘要、知识编译，这三层不该混成一层。

## 为什么它的 memory 系统强

### 1. 真相源是本地可读文件

不是只能通过 SDK 才能看到的内部状态，而是直接可读、可备份、可迁移、可 Git 化。

### 2. 分层自然

- raw / daily
- curated / long-term
- retrieved / active recall
- compiled / wiki

这比“一个 memory store 装所有东西”清楚得多。

### 3. prompt 预算意识很强

它明确区分“磁盘上保留”和“注入模型的版本会被截断”，并提供 `/context list` 等工具查看 raw vs injected size。

### 4. 它把召回、晋升、编译拆成不同职责

- recall：`memory_search` / active memory
- promotion：dreaming / memory flush
- knowledge compilation：`memory-wiki`

这种拆法很工程化。

## 它的局限和代价

### 1. 复杂度不低

OpenClaw 的 memory 不是一个文件，而是一整套 runtime、plugin、search backend、dreaming、wiki compilation 组合。能力强，但也意味着学习成本和运维面更大。

### 2. 默认路线仍然依赖治理习惯

虽然它是 file-first，但如果用户和 agent 不持续整理 `memory/*.md`、`MEMORY.md`、`DREAMS.md`，文件也会迅速膨胀。

### 3. Active memory 会引入额外延迟和隐式上下文

它通过 pre-reply sub-agent 提前召回很聪明，但也确实改变了 reply path，需要非常注意 rollout 范围、调试可见性和用户预期。

### 4. 安全边界仍然要靠别的机制兜底

官方也明确说过：memory 可以保存 approval context，但 memory 本身不负责 enforce policy；硬边界仍要靠 approval、sandbox、scheduled tasks 等机制。

## 对当前文档库最值得借鉴的点

### 1. 先把记忆做成“文件真相源”，再谈检索

OpenClaw 最强的不是向量检索，而是先把 durable memory 做成清晰文件层级。

### 2. 把 daily working memory 和 curated long-term memory 分开

这和当前 wiki 的 `log / BRAIN / projects/memory / articles` 分层思路高度一致，但 OpenClaw 更强调“daily working layer 先沉淀，再提纯”。

### 3. 补 action-sensitive memory

我们现在对“事实”和“规则”已经有分层，但对“可执行时机、审批上下文、owner authority、过期条件”这种 action-sensitive memory 还可以更显式。

### 4. 补 prompt-budget 可视化

OpenClaw 对 injected vs on-disk 的区分很实用。当前 wiki 如果继续增强 agent harness，也值得补类似的 context budget 可观测面。

### 5. 如果后续真做 compiled knowledge layer，可以参考 `memory-wiki`

尤其是：

- structured claims
- evidence metadata
- contradictions / stale dashboards
- compiled digests

这比单纯多写几篇总结页更接近“可供 agent 直接消费的知识层”。

## 当前结论

如果只看 memory 设计，OpenClaw 的真正特点不是“它也有长期记忆”，而是它把 memory 做成了：

- 文件优先
- 分层治理
- 检索增强
- compaction 前保护
- 背景晋升
- 知识编译

这套设计很适合长期运行的 agent，也很适合拿来对照当前 wiki 的 `BRAIN / POLICY / projects/memory / articles / concepts` 分层继续升级。

## 相关页面

- [[concepts/openclaw]]
- [[articles/2026-04-09-layered-memory-research]]
- [[concepts/layered-memory]]
- [[concepts/harness-engineering]]

## 参考链接

- [OpenClaw Memory overview](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw Agent workspace](https://docs.openclaw.ai/agent-workspace)
- [OpenClaw Active memory](https://docs.openclaw.ai/concepts/active-memory)
- [OpenClaw Builtin memory engine](https://docs.openclaw.ai/concepts/memory-builtin)
- [OpenClaw QMD memory engine](https://docs.openclaw.ai/concepts/memory-qmd)
- [OpenClaw Memory wiki](https://docs.openclaw.ai/plugins/memory-wiki)

## 后续动作

- 如果后续继续研究 agent memory，可单独补一页“OpenClaw memory vs 当前 wiki 分层 memory 对照表”
- 如果后续要吸收其机制，优先评估 action-sensitive memory、daily memory 提纯链和 compiled knowledge layer，而不是先照搬具体插件

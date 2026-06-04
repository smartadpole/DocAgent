---
type: concept
id: CONCEPT-AGENT-INSTRUCTION-SHARING-001
status: active
updated: 2026-06-04
tags: [ai-agent, codex, claude-code, agent-governance]
---

# Agent 指令共享

相关：[[concepts/agent-governance]]、[[concepts/harness-engineering]]、[[AGENTS]]

Agent 指令共享指的是让多个 coding agent 使用同一份项目规则、工作方式、代码规范和上下文说明，避免在 `AGENTS.md`、`CLAUDE.md`、`.codex/AGENTS.md` 或其他工具配置之间复制多份内容后逐渐漂移。

截至 2026-06-04，最稳的 Claude Code + Codex 最小方案是：**把根 `AGENTS.md` 作为唯一共享规则正文，Claude Code 通过 `CLAUDE.md` 导入它；Codex 直接读取根 `AGENTS.md`，如果工程需要保留 `.codex/AGENTS.md`，也只把它做成导入根规则的 thin adapter。**

## 推荐结构

```text
your-project/
├── AGENTS.md
├── CLAUDE.md
├── .codex/
│   ├── AGENTS.md     # 可选：只导入 ../AGENTS.md，不写第二份规则正文
│   └── agents/
└── .claude/
    └── agents/
```

- `AGENTS.md`：共享主规则正文，承接项目定位、工作方式、代码风格、验证要求和安全边界。
- `CLAUDE.md`：Claude Code 入口，只导入共享规则，并追加 Claude 专用补充。
- `.codex/AGENTS.md`：Codex 兼容入口，可选；如果存在，只导入 `../AGENTS.md` 并追加极少量 Codex Only 外壳说明，不承接独立规则。
- `.codex/agents/`：Codex 项目级自定义 agent，可选。
- `.claude/agents/`：Claude 项目级 subagent，可选。

项目级共享规则正文只保留根 `AGENTS.md`。`.codex/AGENTS.md` 可以被治理和保留，但只能是 thin adapter；不能复制根规则，也不能成为第二份项目级规则正文。

## Codex 适配入口处理

有些工程会同时出现根目录 `AGENTS.md` 和 `.codex/AGENTS.md`。这不一定冲突，关键看 `.codex/AGENTS.md` 的角色：

- 如果 `.codex/AGENTS.md` 复制了项目规则、响应路由、验证、写入边界或工作流正文，它就是重复规则源，必须收口。
- 如果 `.codex/AGENTS.md` 只通过 `@../AGENTS.md` 导入根规则，并保留极少量 Codex Only 外壳说明，它只是兼容入口，可以和根 `AGENTS.md` 同时治理。

默认迁移方式：

1. 读取根 `AGENTS.md` 和 `.codex/AGENTS.md`，只识别后者里仍有效、且根文件尚未覆盖的规则。
2. 把有效规则抽象后并入根 `AGENTS.md` 或对应 owning governance / skill / template 页面；根 `AGENTS.md` 只保留短入口和硬边界。
3. 如果不需要 Codex 兼容入口，可以删除 `.codex/AGENTS.md`。
4. 如果需要保留 Codex 兼容入口，把 `.codex/AGENTS.md` 改成 thin adapter：

```markdown
@../AGENTS.md

# Codex Only

This file is the thin Codex adapter for this repository.

- Treat `../AGENTS.md` as the single source of truth for shared project rules.
- Do not copy shared governance rules, response routing, validation rules, write boundaries, Goal Contract rules, or finalizer rules here.
- Keep Codex custom agent wrappers under `.codex/agents/*.toml`.
```

5. 跑项目自己的治理检查；在本库中对应 `python3 scripts/check_all.py --only harness-governance`。

判断口诀：**根 `AGENTS.md` 是规则正文；`CLAUDE.md` 和 `.codex/AGENTS.md` 是工具入口壳；`.codex/agents/` 是 Codex 子 agent 定义目录。**

## 最小实现

项目根目录创建共享主规则：

```bash
cat > AGENTS.md <<'EOF'
# AGENTS.md

## 项目定位

这是一个 AI 研发工程项目。你需要优先理解现有架构，不要在未确认影响面的情况下重构核心流程。

## 工作方式

- 修改代码前，先阅读相关文件并说明改动计划。
- 优先做最小可行修改，避免大范围无关重构。
- 修改后要给出验证方式，例如测试命令、启动命令、手动检查步骤。
- 不要擅自删除数据、迁移数据库、修改线上配置。
- 遇到不确定的业务规则，先标记假设，不要硬编码。

## 代码风格

- Python 代码保持类型清晰、函数职责单一。
- Web 后台优先保持原生 HTML/CSS/JS 轻量实现，不要随意引入重型前端框架。
- 数据处理逻辑要区分 raw / dwd / mart 等层级，不要混写。

## 输出格式

- 先给结论。
- 再给修改点。
- 最后给验证步骤。
EOF
```

再创建 Claude Code 入口：

```bash
cat > CLAUDE.md <<'EOF'
@AGENTS.md

## Claude Code Only

- 大改动前先列计划。
- 涉及批量文件修改时，先列出会影响的文件。
EOF
```

这样以后优先维护 `AGENTS.md`。Claude 专用偏好只追加在 `CLAUDE.md` 的 import 后面，不复制共享正文。

如果工程需要兼容 `.codex/AGENTS.md`，再创建 Codex thin adapter：

```bash
mkdir -p .codex
cat > .codex/AGENTS.md <<'EOF'
@../AGENTS.md

# Codex Only

This file is the thin Codex adapter for this repository.

- Treat `../AGENTS.md` as the single source of truth for shared project rules.
- Do not copy shared governance rules, response routing, validation rules, write boundaries, Goal Contract rules, or finalizer rules here.
- Keep Codex custom agent wrappers under `.codex/agents/*.toml`.
EOF
```

## 官方事实

- Codex 会在启动时构建 instruction chain：默认从 Codex home 读取全局 `AGENTS.md` / `AGENTS.override.md`，再从项目根到当前目录读取项目级 `AGENTS.md` / `AGENTS.override.md`，越靠近当前目录的指令越靠后，因此覆盖更早的指导。来源：[OpenAI Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md)。
- Codex 全局默认目录是 `~/.codex`，除非设置 `CODEX_HOME`；官方验证命令示例是 `codex --ask-for-approval never "Summarize the current instructions."`。来源：[OpenAI Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md)。
- Claude Code 读取 `CLAUDE.md` 而不是直接读取 `AGENTS.md`；如果仓库已有 `AGENTS.md`，官方建议创建导入它的 `CLAUDE.md`，也可以在导入后追加 Claude 专用规则。来源：[Claude Code memory](https://code.claude.com/docs/en/memory)。
- Claude Code 的 `CLAUDE.md` 支持 `@path/to/import` 语法，导入文件会在启动时展开并加载；首次遇到外部导入时会显示批准对话框。来源：[Claude Code memory](https://code.claude.com/docs/en/memory)。

## 全局共享

如果目标是全局共享，而不是每个项目维护一份，可以用 Codex 的全局 `AGENTS.md` 做主文件：

```bash
mkdir -p ~/.codex
cat > ~/.codex/AGENTS.md <<'EOF'
# Global AGENTS.md

## 我的通用偏好

- 回答先给结论，再给步骤。
- 修改代码前先理解现有结构。
- 不要默认引入新依赖。
EOF
```

Claude Code 用户级入口可以导入它：

```bash
mkdir -p ~/.claude
cat > ~/.claude/CLAUDE.md <<'EOF'
@~/.codex/AGENTS.md

## Claude Code 全局补充

- 对复杂任务先拆解。
- 对危险命令先说明风险。
EOF
```

全局共享适合个人偏好和通用工作方式；项目规则仍应优先放在项目根 `AGENTS.md`，让团队和版本控制一起维护。

## 子 Agent 边界

共享项目规则和共享自定义子 agent 不是一回事。

如果“agent 信息”指项目规则、工作方式、代码规范、上下文说明，用 `AGENTS.md` + `CLAUDE.md` import 就够了。

如果“agent 信息”指自定义 subagent / 子 agent，两边格式不同，不建议硬共享同一个文件：

- Claude Code subagent 使用 `.claude/agents/*.md` 或 `~/.claude/agents/*.md`，文件是带 YAML frontmatter 的 Markdown，`name` 和 `description` 必填。来源：[Claude Code subagents](https://code.claude.com/docs/en/sub-agents)。
- Codex 自定义 agent 使用 `~/.codex/agents/` 或项目内 `.codex/agents/` 下的独立 TOML 文件。来源：[OpenAI Codex subagents](https://developers.openai.com/codex/subagents)。

更稳的结构是共享核心 prompt 文案，再分别生成 Claude / Codex 包装文件：

```text
your-project/
├── agents-shared/
│   ├── code-reviewer.md
│   ├── bug-investigator.md
│   └── data-architect.md
├── .claude/
│   └── agents/
│       └── code-reviewer.md
└── .codex/
    └── agents/
        └── code-reviewer.toml
```

## 判断规则

- 只要是团队共同规则，优先进入项目根 `AGENTS.md`。
- 只要是 Claude Code 专用习惯，放在 `CLAUDE.md` 的 `@AGENTS.md` 之后。
- 只要是 Codex 项目兼容入口，`.codex/AGENTS.md` 只能 `@../AGENTS.md` 并写极少量 Codex Only 外壳说明。
- 只要是个人偏好，优先放用户级文件，例如 `~/.codex/AGENTS.md` 或 `~/.claude/CLAUDE.md`。
- 只要是子 agent 角色定义，不要混进主规则文件；维护共享 prompt 原文，再生成各工具专用格式。
- 只要发现项目内同时维护根 `AGENTS.md` 和 `.codex/AGENTS.md` 两份规则正文，优先合并回根 `AGENTS.md`；然后按项目需要删除 `.codex/AGENTS.md`，或把它改成 thin adapter。

## 常见误区

- 把 `AGENTS.md` 和 `CLAUDE.md` 维护成两份复制文本，最后两边漂移。
- 把 Claude 专用计划模式、工具权限或模型选择规则写进共享主文件，影响 Codex。
- 把自定义子 agent 的工具格式当成通用项目规则。
- 把 `.codex/AGENTS.md` 当作 Codex 项目规则副本长期维护；Codex 项目规则正文应回到根 `AGENTS.md`，`.codex/AGENTS.md` 最多只是 thin adapter，`.codex/agents/` 只放自定义 subagent。
- 把全局个人偏好写进团队项目规则，导致其他人继承不该继承的本机习惯。
- `AGENTS.md` 无限膨胀；共享主文件应该是短入口，细节优先链接到项目文档、技能或模板。

## 验证

Codex 可用：

```bash
codex --ask-for-approval never "Summarize the current instructions."
```

Claude Code 可在会话里运行 `/memory`，检查 `CLAUDE.md` 和导入的文件是否被加载。

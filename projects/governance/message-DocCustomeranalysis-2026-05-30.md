---
type: governance-message
target: DocCustomeranalysis
from: AcknowledgeBase 治理中控
date: 2026-05-30
purpose: 外部治理变更收尾
---

# 发给 DocCustomeranalysis 的治理消息

以下内容可直接粘贴进 DocCustomeranalysis 会话窗口。

---

## 消息正文

AcknowledgeBase 治理中控在 2026-05-30 对本工程做了两处外部治理变更，已直接提交到 master，commit `fe2ae81`。本轮目标是完成收尾：验证改动正确、补 log、补 ledger episode、提交。

**不需要重新分析问题**，根因和解法已经由治理中控完成。本轮只收尾。

---

### 已做的改动（commit fe2ae81）

改动文件：`governance/response-mode-routing.md`，共两处新增：

**改动一（PI-001）**：在"Issue Intake 分三层执行"之前，新增证据充分性判定段落。

> 核心内容：用户同时提供截图、可见入口路径和期望行为时，浏览器复现不需要做，直接进入最小落档层；三项中任一缺失时才做最小范围复现。

**改动二（PI-001 续）**：在同步预算段末尾，新增检查链分层规则。

> 核心内容：doc-only issue intake 只跑 `project-docs` + finalizer；涉及 TASK/EP 状态回退时补跑 `work-item-matrix`；只有规则/结构/多模块同步时才升级到全量 check_all.py。

**改动三（PI-002）**：在读取预算段的升级信号列表之后，新增子工程读取预算。

> 核心内容：主控读子工程默认只读 AGENTS.md + 直接点名的最多 3 个文件 + 命令输出；不读完整 codebase、governance 文件或历史报告；扩展前必须说明理由。

---

### 本轮需要你做的事

**第一步：验证改动**

```
git show fe2ae81
```

确认三处新增内容都在 `governance/response-mode-routing.md` 里，没有引入格式问题。

**第二步：跑专项检查**

```
python3 scripts/check_all.py --only harness-governance,project-docs
```

如果有报错，修复后再继续。

**第三步：在 `log.md` 顶部补一条记录**

```markdown
### 外部治理变更：Issue Intake 效率与跨工程读取预算

- **来源**：AcknowledgeBase 治理中控，2026-05-30
- **变更内容**：response-mode-routing.md 新增三处规则——Issue Intake 证据充分性判定（用户已提供截图+入口+期望行为时跳过复现）、doc-only intake 检查链分层、主控读取子工程默认读取预算（最多 3 个文件）
- **对应平台级问题**：PI-001（Issue Intake 缺证据充分性判定）、PI-002（跨工程读取模式无读取预算）
- **commit**：fe2ae81
```

**第四步：在 `governance/harness-feedback-ledger.md` 的 Episode Ledger 表里补两条**

```
| 2026-05-30 | Issue Intake 缺证据充分性判定，默认触发复现 | AcknowledgeBase 治理中控分析 ISSUE-024 实录（21 分钟），复现占约 6-8 分钟；用户已提供截图但仍触发浏览器复现 | 规则升级 | 可优化成本 | response-mode-routing.md 新增证据充分性判定 + doc-only 检查链分层（commit fe2ae81） | governance/response-mode-routing.md | promoted |
| 2026-05-30 | 子工程读取无预算，token 消耗过重 | AcknowledgeBase 治理中控分析 ISSUE-022 实录（14 分 53 秒）；读取 customeranalysis 子工程无深度约束 | 规则升级 | 可优化成本 | response-mode-routing.md 新增子工程读取预算（commit fe2ae81） | governance/response-mode-routing.md | promoted |
```

**第五步：提交**

```
git add governance/response-mode-routing.md governance/harness-feedback-ledger.md log.md
python3 scripts/check_all.py
python3 scripts/agent_finalizer.py
```

检查通过后提交，commit message 参考：

```
Complete governance handoff: issue intake + cross-project read budget

Verify and close out two harness improvements applied by AcknowledgeBase
governance hub (fe2ae81). Add ledger episodes and log entry.
PI-001: evidence sufficiency check before Issue Intake reproduction.
PI-002: sub-project read budget in response-mode-routing.
```

---

### 本轮边界

- 不分析其他问题
- 不修改 AGENTS.md、WORKFLOW、POLICY
- 不开新 issue 或 TASK
- 不处理 ledger 存量清理（PI-003，单独一轮）

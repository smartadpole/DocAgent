---
name: cross-project-governance-audit
description: 跨工程治理审计技能。定期或按需读取各工程关键治理文件，对照平台级标准评估成熟度，生成漂移报告和 handoff 包。支持全量审计（所有已注册工程）和单工程审计（"治理 X 工程"）两种模式。
trigger:
  - 用户说"审计 / 治理 [工程名]"
  - 用户说"生成漂移报告"
  - 定期调度任务（每周）自动触发
---

# 跨工程治理审计技能

## 定位

把注册表里的工程，逐一对照平台级标准评分，输出漂移清单和可直接转发的 handoff 包。

**不做**：直接修改其他工程的文件。所有产出留在 AcknowledgeBase 内，由用户确认后手动在目标工程执行。

---

## 读取顺序

1. [[governance/platform-standards]]（评分基线）
2. [[projects/governance/registry]]（工程列表、路径、当前状态）
3. 对每个目标工程，按以下优先级读取：
   - 根目录 `AGENTS.md`
   - `governance/harness-feedback-ledger.md` 或等价台账
   - `governance/response-mode-routing.md` 或等价文件
   - `scripts/check_*.py` 或等价 sensor 脚本列表
   - `governance/template-feedback-rules.md`（如有）

---

## 工作流

### 0. 判断审计模式

| 用户输入 | 模式 | 目标工程 |
|---|---|---|
| "审计所有工程" / 定期调度 | 全量审计 | 所有 non-reference 工程 |
| "治理 DocFilmCommunity" | 单工程审计 | 指定工程 |
| "生成 DocFilmCommunity handoff" | 只生成 handoff | 指定工程（跳过评分，直接用上次评分） |

### 1. 逐工程评分

对每个目标工程，按 [[governance/platform-standards]] 的 5 个维度打分：

```
维度1：执行约束文件
维度2：响应分流机制
维度3：Episode / Harness 反馈机制
维度4：Sensor / 自动检查覆盖
维度5：跨工程协作规则

整体等级 = min(维度1, ..., 维度5)
```

如果工程路径"待补充"，记录 `blocked - 路径未知`，跳过该工程，继续其他。

### 2. 生成漂移报告

输出到 `projects/governance/drift-report-YYYY-MM.md`（按年月命名，同月覆盖更新）。

报告结构：

```markdown
# 治理漂移报告 YYYY-MM

生成时间：YYYY-MM-DD
基准标准：governance/platform-standards.md vX

## 汇总

| 工程 | 整体等级 | 上次评级 | 变化 | 治理阶段 |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 各工程详情

### [工程名]

- **整体等级**：L2
- **各维度**：维度1=L2, 维度2=L1, 维度3=无, 维度4=无, 维度5=L2
- **主要缺口**：...
- **已有优势**：...
- **建议优先动作**：1. ... 2. ...
- **handoff 包**：[已生成 / 未生成]

## 平台级模式（2+ 工程共性问题）

...
```

### 3. 生成 handoff 包（按需）

对处于 `assessed` 阶段的工程，生成 `projects/governance/handoff-{project}-YYYY-MM.md`。

handoff 包结构：

```markdown
# 治理 handoff：[工程名] YYYY-MM

目标工程：[工程名]
当前成熟度：L2 → 目标 L3
生成时间：YYYY-MM-DD

## 本次治理范围

只做以下几件事（不扩展）：
1. ...
2. ...

## 逐条操作说明

### 操作 1：[简短标题]

**文件**：`governance/harness-feedback-ledger.md`  
**问题**：所有 episode 停在 active，没有 closed/deprecated 终态  
**操作**：...  
**验证**：...

## 不做的事（本轮边界）

- 不改 AGENTS.md 正文结构
- 不新增 sensor 脚本
- ...
```

### 4. 更新注册表

审计完成后，更新 [[projects/governance/registry]] 中的：
- 各工程整体成熟度
- 治理阶段（assessed / handoff-ready）
- 上次审计日期

### 5. 输出收尾

给用户一个简短总结：
- 本次审计了哪些工程
- 哪些工程有漂移（和上次相比）
- 哪些工程已生成 handoff 包，路径在哪
- 哪些工程因路径未知被跳过

---

## 输出约束

- 漂移报告和 handoff 包都留在 AcknowledgeBase 内，不写入目标工程
- 不自动执行 handoff 包里的操作，除非用户明确说"现在去 X 工程执行"
- 如果某工程路径"待补充"，不猜测路径，记录为 blocked 并继续
- 报告只写事实和建议，不写"应该"或"必须"这类断言语气
- 平台级模式（2+ 工程共性）单独成段，不埋在各工程详情里

---

## 定期调度说明

本技能每周一次由调度任务自动触发，默认执行全量审计。  
调度任务的 prompt 格式：

```
在 /Users/hai/Documents/Docs/AcknowledgeBase 执行跨工程治理审计。
读 skills/cross-project-governance-audit/SKILL.md 获取完整流程。
模式：全量审计（所有 non-reference 工程）。
输出漂移报告到 projects/governance/drift-report-YYYY-MM.md，并更新注册表。
```

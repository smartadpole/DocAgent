---
type: governance-standard
id: GOV-PLATFORM-STANDARDS-001
scope: cross-project
status: active
source_of_truth: true
updated: 2026-06-04
tags: [governance, standards, cross-project, maturity]
---

# 平台级治理标准

这页属于治理层，统一由 [[governance/README]] 收口。

**基准来源**：AcknowledgeBase 自身的治理体系。  
**用途**：作为跨工程治理审计的评分基线，由 [[skills/cross-project-governance-audit/SKILL]] 读取。

---

## 成熟度等级定义

| 等级 | 名称 | 含义 |
|---|---|---|
| L1 | 基础存在 | 有最小约束文件，agent 知道边界在哪 |
| L2 | 规范运作 | 有读取顺序、响应分流、跨工程写入边界 |
| L3 | 完整体系 | 有 episode 追踪、sensor 覆盖、写入边界自动检查 |
| L4 | 自演进 | 有规则晋升机制、跨工程反哺规则、定期治理巡检 |

---

## 各维度标准

### 维度 1：执行约束文件（根 AGENTS.md）

| 能力点 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| 文件存在 | ✓ | ✓ | ✓ | ✓ |
| 有工作目录声明 | ✓ | ✓ | ✓ | ✓ |
| 有基础角色边界 | ✓ | ✓ | ✓ | ✓ |
| 有明确读取顺序 | | ✓ | ✓ | ✓ |
| 有跨工程写入边界规则 | | ✓ | ✓ | ✓ |
| 项目级规则正文唯一；`.codex/AGENTS.md` 如存在只能是 thin adapter，不维护规则副本 | | ✓ | ✓ | ✓ |
| 写入边界有 sensor 强化（非纯自然语言） | | | ✓ | ✓ |
| 有 scope proof 要求（finalizer 级别） | | | ✓ | ✓ |
| 规则有闭环机制（deprecated/pruned） | | | | ✓ |

**AcknowledgeBase 当前**：L3（scope proof 已有 episode 但 sensor 待补，规则闭环待补）

---

### 维度 2：响应分流机制

| 能力点 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| 有快速诊断 vs 完整治理区分 | | ✓ | ✓ | ✓ |
| 有 response-mode-routing 或等价文件 | | ✓ | ✓ | ✓ |
| 路由规则有 sensor 检查 | | | ✓ | ✓ |
| 路由能自动识别场景并带假设推进 | | | | ✓ |

**AcknowledgeBase 当前**：L4（proactive-dialogue-system 已就位）

---

### 维度 3：Episode / Harness 反馈机制

| 能力点 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| 有 episode 记录（任何形式） | | | ✓ | ✓ |
| 有 harness-feedback-ledger 或等价台账 | | | ✓ | ✓ |
| Episode 有状态（observed / promoted） | | | ✓ | ✓ |
| Episode 有晋升路径（→ 规则 / sensor / 模板） | | | ✓ | ✓ |
| Episode 有终态（closed / deprecated） | | | | ✓ |
| 有跨工程 episode 对比机制 | | | | ✓ |

**AcknowledgeBase 当前**：L3（无终态，跨工程对比是本次建的新能力）

---

### 维度 4：Sensor / 自动检查覆盖

| 能力点 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| 有任何自动检查脚本 | | | ✓ | ✓ |
| 覆盖治理结构检查（文件存在、链接、模板字段） | | | ✓ | ✓ |
| 覆盖工作项矩阵检查（EP/TASK/FP/Gate 关系） | | | ✓ | ✓ |
| 覆盖写入边界检查（scope proof） | | | ✓ | ✓ |
| 覆盖跨工程漂移检查 | | | | ✓ |

**AcknowledgeBase 当前**：L3（check_all.py 已有多个 --only 模式）

---

### 维度 5：跨工程协作规则

| 能力点 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| 有"不修改其他工程"的自然语言规则 | | ✓ | ✓ | ✓ |
| 有主控 vs 子工程职责划分 | | ✓ | ✓ | ✓ |
| 有 handoff 包格式（向子工程传递建议的标准格式） | | | ✓ | ✓ |
| 有跨工程写入边界 sensor | | | ✓ | ✓ |
| 有模板反哺规则（template-feedback-rules） | | | | ✓ |
| 有治理中控定期巡检（本次建的能力） | | | | ✓ |

**AcknowledgeBase 当前**：L4（template-feedback-rules 已就位）

---

## 综合成熟度评分方法

审计时按 5 个维度分别打 L1-L4，取最低维度作为整体等级。

```
整体等级 = min(维度1, 维度2, 维度3, 维度4, 维度5)
```

主控工程目标：**L3**  
子工程目标：**L2**  
AcknowledgeBase 自身目标：**L4**

---

## 变更记录

| 日期 | 变更内容 |
|---|---|
| 2026-05-30 | 初版建立，基于 AcknowledgeBase 自身治理体系 |

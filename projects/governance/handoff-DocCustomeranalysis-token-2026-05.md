---
type: governance-handoff
target: DocCustomeranalysis
source: AcknowledgeBase 治理中控
issue: 主控读取子工程时 token 消耗过重
root-cause: 子工程读取模式无读取预算；episode ledger 60+ 条全 active 造成固定上下文成本
generated: 2026-05-30
status: ready
---

# 治理 handoff：DocCustomeranalysis — 跨工程读取 token 消耗

## 诊断依据

来源：2026-05-30 ISSUE-022 复开实录（14 分 53 秒）+ response-mode-routing.md 读取预算段审查

**核心发现**：

`response-mode-routing.md` 第 95 行的"读取预算"段落只为**快速诊断**定义了 budget（入口规则 + 1-3 个事实源）。`子工程实现/回传`模式的 Mode 表里写的最小读取是"主控裁决 + 子工程入口规则 + 目标代码上下文"，**"目标代码上下文"没有深度上限**，agent 自行决定读多少，实际会读入整个相关模块。

**两个独立成本来源**：

| 成本来源 | 每轮固定消耗 | 性质 |
|---|---|---|
| 子工程读取无 budget，深度不受控 | 按模块大小变化 | 可优化 |
| harness-feedback-ledger 60+ 条全 active | 每次读治理文件都扫入全表 | 可优化 |

---

## 本次治理范围

改 `governance/response-mode-routing.md` 一处，加一段跨工程读取预算。  
**不改** AGENTS.md、WORKFLOW、episode ledger（ledger 清理是独立工作，不在本 handoff 里）。

---

## 操作：补跨工程读取预算

**文件**：`governance/response-mode-routing.md`

**定位**：找到 `## 读取预算` 段落，当前内容是：

```
快速诊断的默认读取预算是：

1. 当前主控 / 子工程身份和写权限边界。
2. 当前仓库入口规则或目标子目录入口。
3. 和问题直接相关的 1 到 3 个事实源。
4. 能快速量化的命令输出。

触发以下任一信号时，必须升级读取：
...
```

**在这段末尾（"触发以下任一信号时，必须升级读取"那段之后）追加以下内容**：

---

追加内容：

```
主控读取子工程的默认读取预算是：

1. 子工程 AGENTS.md（了解写入边界和身份）。
2. 用户或主控 issue / TASK 直接点名的子工程文件，最多 3 个。
3. 能直接回答当前问题的命令输出或接口返回。

子工程读取默认不包含：子工程完整 codebase、子工程 WORKFLOW / governance 文件、子工程历史报告、子工程 ledger。只有满足以下条件之一时，才扩展子工程读取深度：

- 主控 issue / TASK 的关闭标准需要子工程代码层证据。
- 主控和子工程之间存在明确接口冲突或状态不一致。
- 用户明确要求"看子工程的 X 文件 / X 模块"。

扩展子工程读取时，先说明读取理由和预计读取范围，不默认全量展开。
```

---

**验证**：改完后问自己：下次主控需要验证子工程某个 API 行为时，是否只读 AGENTS.md + 相关接口文件，而不是读整个模块？

---

## 额外建议（不在本次 handoff，供参考）

**Episode ledger 瘦身**（独立工作）：60+ 条 active episode 是另一个固定 token 成本。每次读治理上下文时整张表都会进入上下文。建议单独开一轮：
- 把已被 sensor/模板覆盖的 episode 状态从 `active` 改为 `promoted`
- 把已有 `promoted` 标注但还写着 `active` 的条目对齐状态
- 参考 `train_platform` 的做法，补 `promoted-replaced` 终态

这件事本 handoff 不处理，是因为它需要逐条判断，和读取预算修改是独立工作，混在一起容易互相干扰。

---

## 预期收益

| 场景 | 改前 | 改后 |
|---|---|---|
| 主控验证子工程 API 行为 | 读入整个相关模块（数千 token） | 只读 AGENTS.md + 目标接口文件（几百 token） |
| 主控复现子工程 UI 问题 | 读 customeranalysis codebase + 历史报告 | 只读 AGENTS.md + 直接相关组件文件 |

---

## 执行后回传

在 DocCustomeranalysis 的 harness-feedback-ledger 补一条 episode：

```
| 2026-05-30 | 子工程读取无预算导致 token 消耗过重 | AcknowledgeBase 治理中控分析 ISSUE-022 实录 | 规则升级 | 可优化成本 | 补跨工程读取预算段落到 response-mode-routing.md | response-mode-routing.md | promoted |
```

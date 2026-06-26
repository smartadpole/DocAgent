# Goal Contract Transfer

## 能力目标

让目标工程具备长时任务完成契约能力：在复杂实现、排障、迁移、调研、验收或跨工程协作开始前，先固定目标、范围、证据层级、验证面、预算、停止条件和记录落点，防止目标漂移、证据漂移和无限探索。

## 可以吸收

- 启动条件：终点清楚、路径需探索、可能跨多轮执行、跨工程回传或证据边界敏感时启用。
- 合同字段：objective、expected final state、in scope、out of scope、source pack、acceptance criteria、evidence layers、verification surface、record landing、iteration budget、stop / blocked conditions、closure boundary。
- 证据分层：code-level / unit、functional、service-side、end-to-end、non-default / boundary、related regression、manual confirmation。
- 业务链路证据：functional / business-flow 证据必须说明用户可见行为、后台副作用、状态投影或持久化 readback 之间的对应关系。
- 三条防线：期望最终状态、验证面 / 证据边界、预算 / 阻塞停止条件。
- method-candidate 判断：长时任务结束后只把可复用方法候选分流到 log、ledger、skill、template、sensor 或 rule；不能把候选直接写成已生效规则。
- 并行 agent 边界：Worker 只能回传自身证据，主控按同一 contract 合流。
- 收口路由：no-op / log / harness ledger / retrospective / memory / skill / template / sensor / rule。

## 只能抽象吸收

- 源工程的 TASK、Issue、handoff、服务环境、项目状态和历史 Goal 案例只能映射到目标工程自己的 owning page。
- 目标工程没有模板目录时，可以先把字段写入 skill、AGENTS 或 workflow，不硬造平行模板体系。
- 下游工程的成熟度分数、leader 标记和一次性验收结果只能作为案例信号。

## 禁止复制

- 不复制项目状态、运行 ID、服务名、环境名、真实路径、本地 handoff 或一次性完成结论。
- 不把 Goal Contract 迁移成普通业务 skill、事项关闭模板或全局 memory。
- 不用 Goal Contract 替代目标工程的验收报告、发布准出、安全审查、人工确认或主控关闭裁决。

## 目标工程结构自检

1. 是否已有长时任务、issue、task、report、handoff、conversation record 或 Harness 入口？
2. 是否已有 completion contract 或验收合同字段？有则优先 recognize 并补缺口。
3. 合同应该落在 chat-level、TASK、Issue、AP、handoff、run capsule 还是其他 owning page？
4. 证据层级是否能区分完成证据、辅助证据、不能上推边界和人工确认？
5. 是否至少覆盖一个 non-default / boundary 条件；缺少非默认值、code-level、business-flow 或 manual-confirmation 时是否必须降级？
6. 是否需要 sensor 检查 skill、TRANSFER、template、workflow 或入口接线？

## 验证要求

- 用一个长时任务样例建立合同，检查字段齐全且有记录落点。
- 检查最终结论是否区分 passed / partial / blocked / failed，以及哪些 code-level、business-flow、non-default、manual-confirmation 证据不能上推。
- 跑目标工程已有检查或新增轻量 sensor。
- 最终回复写清合同落位、检查命令、未验证边界和不能替代的验收入口。

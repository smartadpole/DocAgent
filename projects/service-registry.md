---
type: service-registry
id: PROJ-SERVICE-REGISTRY-001
project: wiki
status: optional
stage: operations
source_of_truth: true
updated: 2026-05-25
tags: [project, operations, service-registry]
---

# 服务实例台账

主入口：[[projects/README]]

部署设计：[[projects/design/deployment]]

这页是研发模式里的运行 / 部署治理组件，用于统一记录已经确认过的服务实例事实。它只回答“真实服务现在在哪里运行、怎样验证、怎样复启和怎样追溯版本”，不替代部署设计、服务合同或密钥治理。

如果当前项目还没有长期运行服务，可以保留为空或不启用；一旦同一项目需要反复联调多个 API、UI、scheduler、worker、sidecar 或外部服务，就优先启用这页作为单一信息源。

## 维护边界

- 记录已经确认过的运行实例事实：机器或稳定别名、端口、服务名、代码版本、启动方式、健康检查、配置 profile、数据目录、日志位置和更新方式。
- 同一个代码工程 / 部署上下文下的 API、UI、scheduler、worker 或 sidecar 默认先作为一个服务组记录，再把进程写成组件；不要把同工程组件和其他独立服务平级并列。
- 同一服务组只要对外提供 UI，就必须记录并验证 UI / API 配对事实：UI origin、API origin、`/ui-settings` 或等价配置返回值、前端暴露 API URL，以及操作者机器实际访问时是否错误回落到 `127.0.0.1`、`localhost` 或其他环境。
- 所有工程、所有服务实例默认采用“代码主线 / 实例配置”分层：Git 管理源码、测试、模板和示例配置；服务器只记录当前运行版本和实例配置。服务器热修必须标为临时补丁，并写清回收到主线或被主线覆盖的动作。
- Git 忽略的实例本地配置是本页核心职责之一：记录路径或配置键、关键非密配置、profile 选择、启动 / 恢复步骤和最近验证结果。真实密钥只记录键名或 SecretStore 引用。
- 不记录真实 Token、账号密码、数据库 DSN、Authorization header、cookie 或其他可还原凭据。
- 一次性排障过程仍进 [[log]] 或 [[projects/development/execution/worklog]]；只有会被后续运维、调度、联调或服务治理复用的信息才沉淀到这页。
- 服务设计原则、部署阶段、密钥治理和发布 / 回滚策略仍维护在 [[projects/design/deployment]]；这页只保存实例事实。

## 字段口径

新增服务实例时，优先补齐这些字段。具体条目可以复制 [[templates/service-registry-template]]。

| 字段 | 含义 |
| --- | --- |
| `service_id` | 稳定服务或服务组标识，建议用 `服务名@主机别名` |
| `host` | 服务器 IP、主机名或稳定别名 |
| `endpoint` | 对外健康检查或调用入口 |
| `service_name` | `/health` 或等价接口返回的服务名 |
| `components` | 同一服务组内的 API、UI、scheduler、worker、sidecar 等组件 |
| `owner` | 当前维护人、团队或待确认 |
| `code_path_key` | 运行环境中的代码目录配置键；长期文档优先写键名，不写个人路径 |
| `git_remote` | 源码远程，写 URL 或待确认，不写凭据 |
| `git_revision` | 当前运行代码提交 |
| `start_command` | 脱敏后的启动命令或进程形态 |
| `config_profile` | credential、rate limit、feature flag 等 profile 标识 |
| `config_path_key` | Git 忽略的实例配置路径键名或非密路径 |
| `config_restore` | 配置丢失时的恢复来源、步骤、备份位置和 readback 证据 |
| `ui_api_contract` | 含 UI 服务组必须记录 UI / API origin、前端暴露 API URL 和最近一致性验证 |
| `data_root_key` | 业务产物或运行数据根目录配置键 |
| `status_store` | 状态文件、ledger、run registry 或数据库位置 |
| `log_path_key` | 日志路径配置键；长期文档优先写键名 |
| `health_check` | 最近一次确认的健康检查结论 |
| `preflight` | 最近一次预检结论 |
| `update_method` | 当前可用更新方式和限制 |
| `last_verified_at` | 最近确认时间 |
| `notes` | 重要边界、风险或待补信息 |

## 当前服务实例

当前暂无模板级服务实例事实。

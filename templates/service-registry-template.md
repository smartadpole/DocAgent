# 服务实例台账条目模板

使用位置：[[projects/service-registry]]

```md
## <service-id>

- `service_id`：
- `host`：
- `endpoint`：
- `service_name`：
- `components`：
- `owner`：
- `code_path_key`：
- `git_remote`：
- `git_revision`：
- `start_command`：
- `config_profile`：
- `config_path_key`：
- `config_restore`：
- `ui_api_contract`：
- `data_root_key`：
- `status_store`：
- `log_path_key`：
- `health_check`：
- `preflight`：
- `update_method`：
- `last_verified_at`：
- `notes`：
```

只写可长期复用的运行事实和脱敏后的配置键，不写真实密钥、临时进程号或一次性排障流水。含 UI 的服务组必须写 UI / API 配对事实；远程热修必须写回收主线计划。

"""Validate wiki staged-v1 work items and stage-specific evidence.

This checks declared structure, not truth of authorization or test evidence.
Semantic impact classification and actual acceptance remain owner duties.
"""
from __future__ import annotations

import re
from pathlib import Path

IMPACTS = {'local', 'interface', 'cross_repo', 'service', 'production',
           'data_write', 'irreversible', 'long_run'}
PLACEHOLDERS = {'', '待补', '待填写', 'todo', 'tbd', 'none', 'n/a'}


def contract_body(text: str) -> str:
    """Exclude fenced examples; inline backticks cannot hide current fields."""
    lines = []
    fence = ''
    for line in text.splitlines():
        if fence:
            if re.fullmatch(r' {0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}[ \t]*', line):
                fence = ''
            continue
        opening = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if opening and not (opening[1][0] == '`' and '`' in opening[2]):
            fence = opening[1]
            continue
        lines.append(line)
    return '\n'.join(lines)


def validate(text: str, *, require_contract: bool = False) -> list[str]:
    match = re.match(r'\A---\s*\n(.*?)\n---\s*\n', text, re.S)
    if not match:
        return ['work item requires complete frontmatter'] if require_contract else []
    metadata_pairs = re.findall(r'^([\w_]+):[ \t]*([^\n]*)$', match[1], re.M)
    metadata = dict(metadata_pairs)
    # Check before profile selection: a repeated empty profile must not disable validation.
    if 'contract_profile' in metadata:
        keys = [key for key, _ in metadata_pairs]
        duplicates = sorted({key for key in keys if keys.count(key) > 1})
        if duplicates:
            return ['duplicate metadata field: ' + key for key in duplicates]
    profile = metadata.get('contract_profile', '').strip()
    if 'contract_profile' not in metadata:
        return ['missing contract_profile'] if require_contract or metadata.get('type') in {'task', 'issue'} else []
    if profile != 'staged-v1':
        return ['unknown contract_profile']
    body = contract_body(text[match.end():])
    field_pairs = [(key.strip(), value) for key, value in re.findall(
        r'^-[ \t]+(?:\*\*)?([^：:\n*]+?)(?:\*\*)?[：:][ \t]*([^\n]*)$', body, re.M)]
    keys = [key for key, _ in field_pairs]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        return ['duplicate contract field: ' + key for key in duplicates]
    fields = dict(field_pairs)
    errors = []

    def need(keys, source=fields):
        for key in keys:
            if source.get(key, '').strip().lower() in PLACEHOLDERS:
                errors.append(f'missing concrete {key}')

    need(('id', 'owner', 'status', 'type'), metadata)
    kind, status = metadata.get('type'), metadata.get('status')
    task_states = {'planned', 'in_progress', 'implemented', 'review', 'done', 'blocked', 'archived'}
    issue_states = {'open', 'investigating', 'in_progress', 'resolved', 'review', 'closed', 'blocked', 'archived'}
    if kind not in {'task', 'issue'} or status not in (task_states if kind == 'task' else issue_states):
        errors.append('invalid work item type or stage')
        return errors
    closing = status in {'done', 'closed'}
    executing = status in {'in_progress', 'implemented', 'review', 'done', 'resolved', 'closed'}
    if kind == 'task':
        need(('parent_ep',), metadata)
        need(('目标', '范围', '完成条件', '验证计划'))
        if not re.match(r'^EP', metadata.get('parent_ep', '')):
            errors.append('formal TASK requires parent EP')
    else:
        need(('用户可见症状', '期望行为', '影响范围', '证据'))
    if executing:
        need(('授权依据', '执行范围', '下一动作'))
        impacts = {x.strip().strip('\'"') for x in metadata.get('impact', '').strip('[]').split(',') if x.strip()}
        if not impacts or impacts - IMPACTS:
            errors.append('execution requires known impact classification')
        if impacts & {'production', 'data_write', 'irreversible'}:
            need(('pre_action_check', '恢复方法'))
            if not re.match(r'^allowed\s*[:：]\s*\S', fields.get('pre_action_check', '')):
                errors.append('high-risk execution requires allowed: current action evidence')
        if 'cross_repo' in impacts:
            need(('Git preflight', '回传入口'))
        if closing and impacts & {'service', 'interface'}:
            need(('service-side validation', 'end-to-end validation', '非默认值 / 边界值'))
            for key in ('service-side validation', 'end-to-end validation', '非默认值 / 边界值'):
                if not re.match(r'^passed\s*[:：]\s*\S', fields.get(key, '')):
                    errors.append(f'{key}: requires passed: evidence reference')
        if 'long_run' in impacts:
            need(('运行合同',))
    if closing:
        need(('验证结果', '证据', '回归守卫'))
        if fields.get('验证结果', '').strip() != 'passed':
            errors.append('closure requires passed validation')
        need(('不上推边界',) if kind == 'task' else ('反向复验', '未验证边界', '关闭结论'))
    return errors


def check_repository(repo: Path) -> list[str]:
    errors = []
    for folder in ('projects/development/execution/tasks', 'projects/development/issues'):
        for path in sorted((repo / folder).rglob('*.md')):
            if path.name == 'README.md':
                continue
            text = path.read_text(encoding='utf-8')
            findings = validate(text, require_contract=True)
            errors.extend(f'{path.relative_to(repo)}: {error}' for error in findings)
    return errors

def _format_value(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def _stringify(value, depth):
    if not isinstance(value, dict):
        return _format_value(value)
    base_indent = '  ' + '    ' * depth
    lines = []
    for k, v in sorted(value.items()):
        if isinstance(v, dict):
            inner = _stringify(v, depth + 1)
            lines.append(f'{base_indent}    {k}: {inner}')
        else:
            lines.append(f'{base_indent}    {k}: {_format_value(v)}')
    body = '\n'.join(lines)
    if body:
        return '{\n' + body + f'\n{base_indent}  }}'
    return '{\n' + f'{base_indent}  }}'


def _walk(node, depth):
    base_indent = '  ' + '    ' * depth
    node_type = node['type']
    key = node['key']

    if node_type == 'nested':
        lines = [f'{base_indent}  {key}: {"{"}']
        for child in node['children']:
            lines.append(_walk(child, depth + 1))
        lines.append(f'{base_indent}  }}')
        return '\n'.join(lines)

    if node_type == 'updated':
        old_val = _stringify(node['old_value'], depth)
        new_val = _stringify(node['new_value'], depth)
        return f'{base_indent}- {key}: {old_val}\n{base_indent}+ {key}: {new_val}'

    symbol = {'added': '+', 'removed': '-', 'unchanged': ' '}[node_type]
    val = _stringify(node['value'], depth)
    return f'{base_indent}{symbol} {key}: {val}'


def format_stylish(tree):
    lines = [_walk(node, 0) for node in tree]
    return '{\n' + '\n'.join(lines) + '\n}'

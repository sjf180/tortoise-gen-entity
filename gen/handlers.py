from typing import Tuple, Dict, Any

from utils import tuple_to_str


def handle_char(field) -> str:
    tpl, kv = handle_common(field, 'CharField')

    try:
        kv['max_length'] = field['character_maximum_length']
    except IndexError:
        kv['max_length'] = 255

    return tpl.format(", ".join(map(tuple_to_str, kv.items()))) + "\n"


def handle_common(field, field_str) -> Tuple[str, Dict[str, Any]]:
    tpl = f'{field["column_name"]} = ' + 'fields.' + field_str + '({})'
    kv = {}
    kv['description'] = "'" + field['column_comment'] + "'"
    if field['column_key'] == 'PRI':
        kv['pk'] = True
    if field['is_nullable'] == 'NO':
        kv['null'] = False
    if field['column_default'] and field['column_default'] != 'NULL':
        kv['default'] = field['column_default']

    return tpl, kv


def handle_int(field) -> str:
    tpl, kv = handle_common(field, 'IntField')
    return tpl.format(", ".join(map(tuple_to_str, kv.items()))) + "\n"


def handle_float(field) -> str:
    tpl, kv = handle_common(field, 'FloatField')
    return tpl.format(", ".join(map(tuple_to_str, kv.items()))) + "\n"


def handle_bool(field) -> str:
    tpl, kv = handle_common(field, 'BooleanField')
    return tpl.format(", ".join(map(tuple_to_str, kv.items()))) + "\n"


def handle_datetime_field(field) -> str:
    tpl, kv = handle_common(field, 'DatetimeField')
    return tpl.format(", ".join(map(tuple_to_str, kv.items()))) + "\n"


def handle_date_field(field) -> str:
    tpl, kv = handle_common(field, 'DateField')
    return tpl.format(", ".join(map(tuple_to_str, kv.items()))) + "\n"


def handle_text_field(field) -> str:
    tpl, kv = handle_common(field, 'TextField')
    return tpl.format(", ".join(map(tuple_to_str, kv.items()))) + "\n"


parsers = {
    'int': handle_int,
    'float': handle_float,
    'double': handle_float,
    'decimal': handle_float,
    'char': handle_char,
    'varchar': handle_char,
    'text': handle_text_field,
    'bool': handle_bool,
    'date': handle_date_field,
    'datetime': handle_datetime_field
}

from tortoise import Tortoise, run_async, connections

from gen.handlers import parsers
from gen.utils import colors
from yaml_utils import YamlUtils


model_template = colors.yellow + """
from tortoise import models, fields
from entity.base import BaseModel
from utils.jsonModel import jsonModel

""" + colors.blue + """
@jsonModel()
class {model_name}(BaseModel):
{fields}

  class Meta:
    table = "{table_name}"
    
"""

async def init():
    yaml_dict = YamlUtils.update_yaml_model()

    await Tortoise.init(
        db_url=yaml_dict['connections']['default'],
        modules={'models': yaml_dict['apps']['ts']['models']}
    )
    # Generate the schema
    # await Tortoise.generate_schemas()

    # enable_sql_log()

    conn = connections.get('default')

    table_name = 'ds_t_vehpass'

    res = await conn.execute_query(
        "SELECT column_name, data_type, character_maximum_length, column_type, is_nullable, column_default, column_comment, column_key FROM information_schema.COLUMNS WHERE table_schema = %s AND table_name = %s",
        [conn.database, table_name]
    )
    if res:
        generated = model_template.format(model_name=table_name, table_name=table_name, fields=parse_field(res[1]))
        print(generated)


def parse_field(fields):
    _str = ''
    for field in fields:
        _type = field['data_type']
        if field['data_type'] in parsers:
            _str += "  " + parsers[_type](field)
        else:
            print(f"类型[{_type}]的解析器暂未定义")
    return _str


if __name__ == '__main__':
    run_async(init())

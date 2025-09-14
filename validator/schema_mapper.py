from common import utils
from common import constants as const
from common.obj.column_details import ColumnDetails
from common.obj.table_details import TableDetails


def get_schema_map():
    schema_json = utils.get_schema_json()
    tables = schema_json[const.c_str_tables]
    schema_details = []
    for table in tables:
        table_name = table[const.c_str_table_name]
        columns = table[const.c_str_datatype]
        columns_list = []
        for column in columns.keys():
            columns_list.append(ColumnDetails(name=column, datatype=columns[column]))
        schema_details.append(TableDetails(name=table_name, columns=columns_list).to_dict())
    return schema_details

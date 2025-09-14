import re

from common import constants as const

def sql_regex_validation(query) -> bool:
    """
    This function performs a regex validation of a SQL query
    :param query: The query to be validated
    :return: True if the SQL matches the regex, else False
    """
    select_pattern = re.compile(const.c_rp_sql_select_query)
    insert_pattern = re.compile(const.c_rp_sql_insert_query)
    update_pattern = re.compile(const.c_rp_sql_update_query)
    delete_pattern = re.compile(const.c_rp_sql_delete_query)
    if select_pattern.match(query) or insert_pattern.match(query) or update_pattern.match(query) or delete_pattern.match(query):
        return True
    return False

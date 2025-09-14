import re

from common import constants as const

def sql_regex_validation(query):
    pattern = re.compile(const.c_rp_sql_query)
    if pattern.match(query):
        return True
    return False

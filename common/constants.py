# Paths
c_path_schema_json = 'common\\res\simple_enterprise_schema.json'

# Request Constants
c_str_get = 'GET'
c_str_post = 'POST'

# Response Keys
c_str_message = 'message'
c_str_status = 'status'
c_str_error = 'error'
c_str_status_ok = 'OK'

# API specific response messages
c_resp_error = 'Error Occurred.'
c_resp_ping = 'Validator Ping!!'
c_resp_syntax_validation_success = 'Valid SQL Query'
c_resp_syntax_validation_failure = 'Invalid SQL Query'

# String constant
c_str_query = 'query'
c_str_tables = 'tables'
c_str_table_name = 'table_name'
c_str_columns = 'columns'
c_str_datatype = 'datatype'

# Regex Patterns
c_rp_sql_query_table = '\w+'
c_rp_sql_query_where = '\s+WHERE\s+.+'
c_rp_sql_query_semi_colon = '\s*;?\s*$'

c_rp_sql_select_query_select = '^SELECT\s+[\*\w,\s]+'
c_rp_sql_select_query_from = '\s+FROM\s+\w+'
c_rp_sql_select_query_basic = f'{c_rp_sql_select_query_select}{c_rp_sql_select_query_from}'
c_rp_sql_select_query_join = '\s+JOIN\s+\w+\s+'
c_rp_sql_select_query_on = '\s+ON\s+.+'
c_rp_sql_select_query_join_on = f'{c_rp_sql_select_query_join}{c_rp_sql_select_query_on}'
c_rp_sql_select_query_group_by = '\s+GROUP\s+BY\s+.+'
c_rp_sql_select_query_having = '\s+HAVING\s+.+'
c_rp_sql_select_query_order_by = '\s+ORDER\s+BY\s+.+'
c_rp_sql_select_query_limit = '\s+LIMIT\s+\d+'
c_rp_sql_select_query_offset = '\s+OFFSET\s+\d+'

c_rp_sql_insert_query_insert = '^INSERT\s+INTO\s+'
c_rp_sql_insert_query_columns = '\s*\(([\w\s,]+)\)'
c_rp_sql_insert_query_values = '\s*VALUES\s*\(.*\)'

c_rp_sql_update_query_update = '\s*UPDATE\s+'
c_rp_sql_update_query_set = '\s+SET\s+.+'

c_rp_sql_delete_query_delete = '\s*DELETE\s+FROM\s+'

c_rp_sql_select_query = (
    fr'{c_rp_sql_select_query_basic}'
    fr'({c_rp_sql_select_query_join_on})?'
    fr'({c_rp_sql_query_where})?'
    fr'({c_rp_sql_select_query_group_by})?'
    fr'({c_rp_sql_select_query_having})?'
    fr'({c_rp_sql_select_query_order_by})?'
    fr'({c_rp_sql_select_query_limit})?'
    fr'({c_rp_sql_select_query_offset})?'
    fr'{c_rp_sql_query_semi_colon}'
)
c_rp_sql_insert_query = (
    fr'{c_rp_sql_insert_query_insert}'
    fr'{c_rp_sql_query_table}'
    fr'{c_rp_sql_insert_query_columns}'
    fr'{c_rp_sql_insert_query_values}'
    fr'{c_rp_sql_query_semi_colon}'
)
c_rp_sql_update_query = (
    fr'{c_rp_sql_update_query_update}'
    fr'{c_rp_sql_query_table}'
    fr'{c_rp_sql_update_query_set}'
    fr'({c_rp_sql_query_where})?'
    fr'{c_rp_sql_query_semi_colon}'
)
c_rp_sql_delete_query = (
    fr'{c_rp_sql_delete_query_delete}'
    fr'{c_rp_sql_query_table}'
    fr'{c_rp_sql_query_where}'
    fr'{c_rp_sql_query_semi_colon}'
)



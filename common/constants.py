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

# Regex Patterns
c_rp_sql_query_select = '^SELECT\s+[\*\w,\s]+'
c_rp_sql_query_from = 'FROM\s+\w+'
c_rp_sql_query_join = 'JOIN\s+\w+\s+'
c_rp_sql_query_on = 'ON\s+.+'
c_rp_sql_query_join_on = f'[{c_rp_sql_query_join}{c_rp_sql_query_on}]?'
c_rp_sql_query_where = '[WHERE\s+]?'
c_rp_sql_query = fr'{c_rp_sql_query_select}{c_rp_sql_query_from}{c_rp_sql_query_join_on}{c_rp_sql_query_where}'

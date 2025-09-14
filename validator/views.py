from django.http import HttpRequest, JsonResponse

from common import utils as utils
from common import constants as const
from validator import syntax_validator, schema_mapper


def ping(_: HttpRequest) -> JsonResponse:
    """
    This function checks if the server is reachable
    :param _: The request, since it is not used anywhere, replaced with _
    :return: response confirming the server is reachable
    """
    return JsonResponse({
        const.c_str_message: const.c_resp_ping,
        const.c_str_status: const.c_str_status_ok
    })


def get_schema_json(_: HttpRequest) -> JsonResponse:
    """
    This function reads the schema JSON and returns that as a dict
    :param _: The request, since it is not used anywhere, replaced with _
    :return: The schema JSON in dict form
    """
    response = utils.get_schema_json()
    return JsonResponse(response)


def validate_sql_syntax(request) -> JsonResponse:
    """
    This function checks the syntax of the SQL auery
    :param request: The request that contains the SQL query
    :return: JsonResponse of the API
    """
    query = request.param_dict[const.c_str_query].upper().strip()
    is_valid_sql_syntax = syntax_validator.sql_regex_validation(query)
    return JsonResponse({
        const.c_str_message: const.c_resp_syntax_validation_success if is_valid_sql_syntax else const.c_resp_syntax_validation_failure,
        const.c_str_status: const.c_str_status_ok
    })


def get_schema_map(_) -> JsonResponse:
    """
    This function creates the schema map for each table and respective columns
    :param _: The request, since it is not used anywhere, replaced with _
    :return: The schema map as dict
    """
    schema_map = schema_mapper.get_schema_map()
    return JsonResponse({
        const.c_str_message: schema_map,
        const.c_str_status: const.c_str_status_ok
    })
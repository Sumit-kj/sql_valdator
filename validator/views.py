from django.http import HttpRequest, JsonResponse

from common import utils as utils
from common import constants as const


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

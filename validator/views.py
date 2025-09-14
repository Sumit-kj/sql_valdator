from django.http import HttpRequest, JsonResponse


def ping(_: HttpRequest) -> JsonResponse:
    """
    This function checks if the server is reachable
    :param _: The request, since it is not used anywhere, replaced with _
    :return: response confirming the server is reachable
    """
    return JsonResponse({'message': 'Validator Ping!!', 'status': 'ok'})

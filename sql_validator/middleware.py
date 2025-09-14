from django.http import JsonResponse

from common import constants as const

class RequestFormatter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        param_dict = dict()
        if request.method == const.c_str_get:
            param_dict = request.GET.dict()
        elif request.method == const.c_str_post:
            param_dict = request.POST.dict()
        request.param_dict = param_dict
        try:
            response = self.get_response(request)
        except Exception as e:
            return JsonResponse({
                const.c_str_message: e.__str__(),
                const.c_str_status: const.c_resp_error
            })
        return response

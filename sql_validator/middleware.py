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
        response = self.get_response(request)
        return response

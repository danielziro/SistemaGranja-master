from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class JSONResponseMixin(object):
    def render_to_json_response(self):
        return self.json_to_response()

    def json_to_response(self):
        data = self.get_data()
        return JsonResponse(data, safe=True)

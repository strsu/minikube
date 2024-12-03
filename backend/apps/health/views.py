from django.http import HttpResponse
from django.views import View


class HealthCheckView(View):
    def get(self, request):
        return HttpResponse(status=200)

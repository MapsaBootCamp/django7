from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))
    
    def process_response(self, request, response):
        print(response)
        return response
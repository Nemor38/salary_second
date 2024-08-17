from django.utils.deprecation import MiddlewareMixin
from django.db.models import F
from .models import RequestStatistics

class RequestStatisticsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # Код для обробки запиту
        pass

    def process_response(self, request, response):
        # Код для обробки відповіді
        return response

    def process_exception(self, request, exception):
        # Інкрементуємо лічильник виключень
        RequestStatistics.objects.update(exception=F('exception') + 1)


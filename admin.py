# admin.py

from django.contrib import admin
from .models import Employee, RequestStatistics

admin.site.register(Employee)
admin.site.register(RequestStatistics)

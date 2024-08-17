# models.py

from django.db import models

class RequestStatistics(models.Model):
    exception = models.PositiveIntegerField(default=0)
    # Інші поля статистики запитів

class Employee(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    # Інші поля співробітника

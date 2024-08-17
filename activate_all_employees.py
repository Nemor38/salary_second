from django.core.management.base import BaseCommand
from your_app.models import Employee

class Command(BaseCommand):
    help = 'Активує всіх співробітників (is_active=True)'

    def handle(self, *args, **kwargs):
        updated_count = Employee.objects.update(is_active=True)
        self.stdout.write(self.style.SUCCESS(f'{updated_count} співробітників було успішно активовано.'))

from django.core.management.base import BaseCommand

from authapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)

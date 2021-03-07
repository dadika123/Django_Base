from django.core.management.base import BaseCommand
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        ShopUser.objects.all().delete()
        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)

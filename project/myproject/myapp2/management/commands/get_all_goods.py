from django.core.management.base import BaseCommand
from myapp2.models import Goods


class Command(BaseCommand):
    help = "Get all goods."

    def handle(self, *args, **kwargs):
        goods = Goods.objects.all()
        self.stdout.write(f'{goods}')

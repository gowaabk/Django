from django.core.management.base import BaseCommand
from myapp2.models import Client, Goods, Orders


class Command(BaseCommand):
    help = "Generate fake data for Clients, Goods, Orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name_{i}', email=f'email_{i}@mail.ru',
                            phone=i + 900_000_00_00, address=f'address_{i}')
            goods = Goods(
                name=f'name_{i}', description=f'description_{i}', price=i * 100, amount=i)
            client.save()
            goods.save()
            for j in range(1, count + 1):
                order = Orders(client_id=client, goods_id=goods)
                order.save()

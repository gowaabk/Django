from django.core.management.base import BaseCommand
from myapp2.models import Client, Goods, Orders


class Command(BaseCommand):
    help = "Generate fake data for Clients, Goods, Orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(client_name=f'name_{i}', client_email=f'email_{i}@mail.ru',
                            client_phone=i + 900_000_00_00, client_address=f'address_{i}')
            goods = Goods(
                goods_name=f'name_{i}', goods_description=f'description_{i}', goods_price=i * 100, goods_amount=i)
            client.save()
            goods.save()
            for j in range(1, count + 1):
                order = Orders(order_client_id=client, order_goods_id=goods)
                order.save()

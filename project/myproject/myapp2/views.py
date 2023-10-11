import datetime
from django.shortcuts import render
from myapp2.models import Client, Goods, Orders

# Create your views here.


def get_clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'myapp2/clients.html', context=context)


def get_client_goods(request, client_id: int, count=7):
    start = datetime.date.today() - datetime.timedelta(days=count)
    client = Client.objects.get(id=client_id)
    orders = Orders.objects.filter(client_id=client_id, create_at__gte=start)
    context = {
        'count_days': count,
        'client': client,
        'orders': orders
    }
    return render(request, 'myapp2/client_goods.html', context=context)

import datetime
from django.shortcuts import render
from myapp2.models import Client, Goods, Orders
from myapp2.forms import GoodsForm
import logging


# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'myapp2/base.html')


def get_clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    logger.info("View all clients")
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
    logger.info(f"Get all goods for {count} days")
    return render(request, 'myapp2/client_goods.html', context=context)


def add_goods(request):
    message = ''
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            image = form.cleaned_data['image']
            logger.info(
                f'Получили {name=}, {description=}, {price=}, {amount=}, {image=}')
            goods = Goods(name=name, description=description,
                          price=price, amount=amount, image=image)
            goods.save()
            message = 'Товар сохранен'
    else:
        form = GoodsForm()
    return render(request, 'myapp2/goods_form.html',
                  {'form': form, 'message': message})

from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.get_clients, name='clients'),
    path('get_client_goods/<int:client_id>/<int:count>/',
         views.get_client_goods, name='get_client_goods'),
    path('add_goods/', views.add_goods, name='add_goods'),
    path('', views.index, name='index'),
]

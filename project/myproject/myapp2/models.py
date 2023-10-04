from django.db import models

# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.IntegerField()
    client_address = models.CharField(max_length=200)
    client_create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client_name} {self.client_email} {self.client_phone} {self.client_address} {self.client_create_at}'


class Goods(models.Model):
    goods_name = models.CharField(max_length=100)
    goods_description = models.CharField(max_length=200)
    goods_price = models.IntegerField()
    goods_amount = models.IntegerField()
    goods_create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.goods_name} {self.goods_description} {self.goods_price} {self.goods_amount} {self.goods_create_at}'


class Orders(models.Model):
    order_client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    order_create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.order_client_id} {self.order_goods_id} {self.order_create_at}'

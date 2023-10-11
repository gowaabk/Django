from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address} {self.create_at}'


class Goods(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    amount = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.amount} {self.create_at}'


class Orders(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client_id} {self.goods_id} {self.create_at}'

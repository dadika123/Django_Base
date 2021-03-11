from django.db import models
from django.db.models.deletion import CASCADE
from authapp.models import ShopUser
from mainapp.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"Корзина пользователя: {self.user.username} | Товар: {self.product.name}"

from django.db import models
from django.db.models.deletion import CASCADE


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='Название Категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория Продукта'
        verbose_name_plural = 'Категории Продуктов'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(
        verbose_name='Название Продукта', max_length=64, unique=True)
    category = models.ForeignKey(
        verbose_name='Категория', to=ProductCategory, on_delete=CASCADE)
    description = models.TextField(
        verbose_name='Описание Продукта', blank=True)
    short_description = models.CharField(
        verbose_name='Краткое Описание', max_length=64)
    price = models.DecimalField(
        verbose_name='Цена', decimal_places=2, max_digits=8, default=0)
    quantity = models.PositiveIntegerField(
        verbose_name='Количество', default=0)
    image = models.ImageField(
        verbose_name='Изображение', upload_to='products_images', blank=True)

    def __str__(self):
        return f'{self.category.name}:{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

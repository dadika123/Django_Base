from django.core.paginator import Paginator
from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page_num=1):
    context = {'title': 'Товары', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_num)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)

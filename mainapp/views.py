from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.


def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    print(pk)
    title = 'Товары'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    content = {'title': title, 'products': products, 'categories': categories}
    return render(request, 'mainapp/products.html', content)

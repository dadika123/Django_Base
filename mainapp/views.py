from django.shortcuts import render

from mainapp.models import Product, ProductCategory


# Create your views here.


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    title = 'Товары'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {'title': title, 'products': products, 'categories': categories}
    if category_id:
        context.update({'products': Product.objects.filter(category_id=category_id)})
    else:
        context.update({'products': Product.objects.all()})
    return render(request, 'mainapp/products.html', context)

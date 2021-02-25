from django.shortcuts import render
import json

# Create your views here.


def index(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    content = {
        'title': 'Продукты',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'img': '/vendor/img/products/Adidas-hoodie.png',
             'short_description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'price': 6090},
            {'name': 'Синяя куртка The North Face',
             'short_description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'img': '/vendor/img/products/Blue-jacket-The-North-Face.png',
             'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'img': '/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'short_description': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'price': 3390},
            {'name': 'Черный рюкзак Nike Heritage', 'short_description': 'Плотная ткань. Легкий материал.',
             'img': '/vendor/img/products/Black-Nike-Heritage-backpack.png',
             'price': 2340},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'img': '/vendor/img/products/Black-Dr-Martens-shoes.png',
             'short_description': 'Гладкий кожаный верх. Натуральный материал.',
             'price': 13590},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'img': '/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'short_description': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'price': 2890},
        ]
    }
    with open("mainapp/fixtures/products.json", "r") as file:
        dict_data = json.load(file)
    for product in dict_data:
        content['products'].append(dict_data[product])
    return render(request, 'mainapp/products.html', context=content)

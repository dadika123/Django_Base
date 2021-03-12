from mainapp.views import products
from django.shortcuts import HttpResponseRedirect, render
from mainapp.models import Product
from basketapp.models import Basket
from django.urls import reverse


def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, product_id=None):
    product = Product.objects.get(pk=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id=None):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

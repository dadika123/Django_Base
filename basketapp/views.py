from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from django.template.loader import render_to_string


from basketapp.models import Basket
from mainapp.models import Product


@login_required
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


@login_required
def basket_remove(request, id=None):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        user_product = Basket.objects.get(id=id)
        if quantity > 0:
            user_product.quantity = quantity
            user_product.save()
        else:
            user_product.delete()
        basket = Basket.objects.filter(user=request.user)
        context = {'basket': basket}
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})

from basketapp.models import Basket
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from django.conf import settings


def login(request):
    title = 'Вход'

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
        else:
            print(login_form.errors)
    else:
        login_form = ShopUserLoginForm()

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'Регистрация'

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def profile(request):
    title = 'Профиль'
    if request.method == 'POST':
        profile_form = ShopUserProfileForm(
            request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        profile_form = ShopUserProfileForm(instance=request.user)
        basket = Basket.objects.all()
        total_quantity = 0
        total_sum = 0
        for product in basket:
            total_quantity += product.quantity
            total_sum += product.sum()
        content = {'title': title, 'profile_form': profile_form, 'basket': basket, 'total_sum': total_sum, 'total_quantity': total_quantity,
                   'media_url': settings.MEDIA_URL}
        return render(request, 'authapp/profile.html', content)

from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from django.contrib import auth, messages
from django.urls import reverse


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
    pass

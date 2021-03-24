from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import NewAdminRegisterForm, NewAdminProfileForm, NewAdminProductCategoryForm
from authapp.models import ShopUser
from geekshop.settings import MEDIA_URL
from mainapp.models import ProductCategory


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users(request):
    context = {'users': ShopUser.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_create(request):
    if request.method == 'POST':
        register_form = NewAdminRegisterForm(
            data=request.POST, files=request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('new_admin:admin_users'))
    else:
        register_form = NewAdminRegisterForm()
    context = {'register_form': register_form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_update(request, user_id):
    user = ShopUser.objects.get(id=user_id)
    if request.method == 'POST':
        profile_form = NewAdminProfileForm(
            data=request.POST, files=request.FILES, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('new_admin:admin_users'))
    else:
        profile_form = NewAdminProfileForm(instance=user)
        context = {'profile_form': profile_form,
                   'user': user, 'media_url': MEDIA_URL}
        return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_delete(request, user_id):
    if request.user.id != user_id:
        user = ShopUser.objects.get(id=user_id)
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('new_admin:admin_users'))
    else:
        return HttpResponseRedirect(reverse('new_admin:admin_users'))


def admin_categories(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/categories_read.html', context)


def admin_category_create(request):
    if request.method == 'POST':
        category_form = NewAdminProductCategoryForm(data=request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('new_admin:admin_categories'))
    else:
        category_form = NewAdminProductCategoryForm()
    context = {'category_form': category_form}
    return render(request, 'adminapp/categories_create.html', context)

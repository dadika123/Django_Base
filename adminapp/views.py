from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import NewAdminRegisterForm, NewAdminProfileForm
from authapp.models import ShopUser


# Create your views here.
def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users(request):
    context = {'users': ShopUser.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        register_form = NewAdminRegisterForm(data=request.POST, files=request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('new_admin:admin_users'))
    else:
        register_form = NewAdminRegisterForm()
    context = {'register_form': register_form}
    return render(request, 'adminapp/admin-users-create.html', context)


def admin_users_update(request, user_id):
    user = ShopUser.objects.get(id=user_id)
    if request.method == 'POST':
        profile_form = NewAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('new_admin:admin_users'))
    else:
        profile_form = NewAdminProfileForm(instance=user)
        context = {'profile_form': profile_form, 'user': user}
        return render(request, 'adminapp/admin-users-update-delete.html', context)


def admin_users_delete(request, user_id):
    if request.user.id != user_id:
        user = ShopUser.objects.get(id=user_id)
        user.delete()
        return HttpResponseRedirect(reverse('new_admin:admin_users'))
    else:
        return HttpResponseRedirect(reverse('new_admin:admin_users'))

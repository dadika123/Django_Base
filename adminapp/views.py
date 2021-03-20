from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    return render(request, 'adminapp/admin-users-read.html')


def admin_users_create(request):
    return render(request, 'adminapp/admin-users-create.html')


def admin_users_update_delete(request):
    return render(request, 'adminapp/admin-users-update-delete.html')

from django.urls import path

from adminapp.views import admin_users_create, admin_users_read, admin_users_update, admin_users_delete, index

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('', admin_users_delete, name='index'),
    path('', admin_users_read, name='index'),
    path('', admin_users_create, name='index'),
    path('', admin_users_update, name='index'),
]

from django.urls import path

from adminapp.views import admin_users, admin_users_create, admin_users_update, admin_users_delete, index

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users-delete/<int:pk>/', admin_users_delete, name='admin_users_delete'),
    path('users/', index, name='index'),
    path('users-update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users-create/', admin_users_create, name='admin_users_create'),
]

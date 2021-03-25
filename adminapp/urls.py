from django.urls import path

from adminapp.views import admin_users_update, admin_users_delete, index, \
    admin_categories, admin_category_create, UserListView, UserCreateView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users-delete/<int:user_id>/', admin_users_delete, name='admin_users_delete'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('categories/', admin_categories, name='admin_categories'),
    path('categories-create/', admin_category_create, name='admin_category_create'),
    path('users-update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
]

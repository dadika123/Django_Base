from django.urls import path

from adminapp.views import UserUpdateView, UserDeleteView, index, UserListView, UserCreateView, ProductCreateView, \
    ProductDeleteView, ProductUpdateView, ProductListView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('product-create/', ProductCreateView.as_view(), name='admin_product_create'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_product_update'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_product_delete'),
    path('products/', ProductListView.as_view(), name='admin_products'),
]

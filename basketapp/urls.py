from django.urls import path

from basketapp import views as basketapp

app_name = "basketapp"

urlpatterns = [
    path('basket-add/<int:product_id>/',
         basketapp.basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basketapp.basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/',
         basketapp.basket_edit, name='basket_edit'),
]

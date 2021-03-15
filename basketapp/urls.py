from django.urls import path

from basketapp import views as basketapp

app_name = "basketapp"

urlpatterns = [
    path('basket-add/<int:product_id>/',
         basketapp.basket_add, name='add'),
    path('basket-remove/<int:id>/', basketapp.basket_remove, name='remove')
]

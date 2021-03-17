from django.contrib import admin

from mainapp.models import ProductCategory, Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'quantity', 'price',)
    list_display_links = ('name', 'short_description',)
    search_fields = ('name', 'short_description',)


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)

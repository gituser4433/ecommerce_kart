from django.contrib import admin
from store.models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug', 'sku', 'unit', 'price', 'stock')

admin.site.register(Product, ProductAdmin)

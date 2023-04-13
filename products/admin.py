from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    # Choose the fields to display on Admin panel for products
    list_display = (
        'name',
        'sku',
        'category',
        'price_kilo',
        'weight',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    # Choose the fields to display on Admin panel for categories
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

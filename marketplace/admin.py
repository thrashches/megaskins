from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'in_stock',
    ]
    list_filter = ['in_stock']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product',
        'status',
    ]
    list_filter = [
        'status',
    ]

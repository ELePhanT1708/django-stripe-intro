from django.contrib import admin
from .models import Item



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stripe_product_id', 'price')
    search_fields = ('name', 'price')
    ordering = ['price']


admin.site.register(Item, ProductAdmin)


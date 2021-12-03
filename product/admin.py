from django.contrib import admin
from .models import Category, Product

# Register your models here.
admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = ('name', 'price', 'quantity')
    fields = ('name', ('price', 'quantity'), 'description', 'category')
    # readonly_fields = ('description')
    ordering = ('price', 'quantity')
    search_fields = ('price', 'quantity')
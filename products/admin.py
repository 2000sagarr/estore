from django.contrib import admin
from .models import Products
from django.utils.html import format_html

class ProductsAdmin(admin.ModelAdmin):
    def myphoto(self, object):
       return format_html('<img src= {} width="40"/>'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'quantity', 'price', 'is_featured')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured', 'quantity')
    list_filter = ('brand', 'category', 'gender', 'occasion', 'size', )
    search_fields = ('name', 'brand')

# Register your models here.
admin.site.register(Products, ProductsAdmin)
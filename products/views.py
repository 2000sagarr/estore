from django.shortcuts import render
from .models import Products

# Create your views here.
def products(request):
    products = Products.objects.all()
    sidebar_products = Products.objects.all()[0:3]
    data = {
        'products' : products,
        'sidebar_products' : sidebar_products,
    }
    return render(request, 'products/products.html', data)
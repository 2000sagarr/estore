from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Products
from django.core.paginator import Paginator

# Create your views here.
def products(request):
    products = Products.objects.all().order_by('-created_date')
    # paginator object
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)


    sidebar_products = Products.objects.all().filter(is_featured=True).order_by('-created_date')[0:3]
    brand_names = Products.objects.values_list('brand', flat=True).distinct()
    tags = Products.objects.values_list('occasion', flat=True).distinct()
    data = {
        'page_object' : page_object,
        'sidebar_products' : sidebar_products,
        'brand_names' : brand_names,
        'tags' : tags,
    }
    return render(request, 'products/products.html', data)

def product_details(request, id):
    product = get_object_or_404(Products, pk = id)
    sidebar_products = Products.objects.all().filter(is_featured=True).order_by('-created_date')[0:3]
    brand_names = Products.objects.values_list('brand', flat=True).distinct()
    tags = Products.objects.values_list('occasion', flat=True).distinct()

    gender= product.gender
    related_data = Products.objects.all().filter(gender= gender)[:8]

    data = {
        'product' : product,
        'sidebar_products' : sidebar_products,
        'brand_names' : brand_names,
        'tags' : tags,
        'related_data' : related_data
    }
    return render(request, 'products/product_details.html', data)
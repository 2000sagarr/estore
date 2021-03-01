from django.shortcuts import render
from products.models import Products
# Create your views here.
def home(request):
    featured_product = Products.objects.filter(is_featured= True).order_by('-created_date')[:8]
    recent_product = Products.objects.all().order_by('-created_date')[:8]
    data = {
        'featured_products' : featured_product,
        'recent_products' : recent_product,
    }
    return render(request, 'mainpage/home.html', data)

def contactus(request):
    return render(request, 'mainpage/contactUs.html')
from django.urls import path
from django.urls.conf import include
from . import views
	
urlpatterns = [
	#this is home page url
    path('', views.products, name= 'products'),
    path('<int:id>', views.product_details, name = 'product_details'),
]

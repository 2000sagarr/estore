from django.urls import path
from django.urls.conf import include
from . import views
	
urlpatterns = [
	#this is home page url
    path('', views.home, name= 'home'),
    path('contactus', views.contactus, name="contactus"),
]

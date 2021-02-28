from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mainpage/home.html')

def contactus(request):
    return render(request, 'mainpage/contactUs.html')
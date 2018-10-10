from django.shortcuts import render

#from .models import Products

def home(request):
    #products = Products.objects
    #return render(request, 'products/home.html', {'products':products})
    return render(request, 'products/home.html')

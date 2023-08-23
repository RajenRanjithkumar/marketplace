from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    
    
    # products = Product.objects.all()
    # context = {"products": products}
    return render(request, 'market/products.html', context = {})

# def productDetails(request, pk):
    
#     product = Product.objects.get(id = pk)
    
#     address = Address.objects.get(product = product)
    
#     context = {"product": product, "address": address}
#     return render(request, 'market/products_details.html', context)
    
    

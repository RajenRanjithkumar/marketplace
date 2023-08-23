from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):
    
    
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'market/products.html', context)

def productDetails(request, pk):
    
    product = Product.objects.get(id = pk)
    
    address = Address.objects.get(product = product)
    
    context = {"product": product, "address": address}
    return render(request, 'market/products_details.html', context)

def registerUser(request):
    
    page = 'register'
    
    if request.method == "POST":
        
        
        form = CreateUserForm(request.POST)
        #CustomUser = get_user_model()
        if form.is_valid():
            
            user = form.save(commit=False)
            user = mUser.objects.create_user(email = user.email, password = user.password)
            print(user.email)
            print(user.username)
            print(user.password)
            
            # Check if the password matches (Django handles password hashing and comparison)
            #password_matches = user.check_password('secure_password')
            #print(f"Password matches: {password_matches}")  # Should print True
            
            # user.save()
            login(request, user)
            return redirect("home")
    else:
        
        form = CreateUserForm()
            
    
    context = {'page':page, 'form': form}
    return render(request, 'market/login.html', context)
    
def loginUser(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user.email)
            print(user.username)
            print(user.password)
            login(request, user)
            return redirect("home") 
    else:
        
        form = AuthenticationForm()
    
    
    
    context = {"form":form}
    return render(request, 'market/login.html', context)
    
    
    

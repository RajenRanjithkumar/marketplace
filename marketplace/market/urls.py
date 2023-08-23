from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    #path('product_details/<str:pk>', views.productDetails, name='product_details'),


]
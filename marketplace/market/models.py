from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class mUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100, blank=False)
    about = models.TextField(blank=True, null=True)
    profileImg = models.ImageField(null=True, blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    phEnable = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self) :
        return self.name
    
class Product(models.Model):

    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    condition = models.CharField(max_length=30, null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, null=True, blank=False)

    
class Address(models.Model):
    city = models.CharField(max_length=50, null=True)
    province = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    #data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.city)


from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class mUser(AbstractBaseUser, PermissionsMixin):

    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    about = models.TextField(blank=True, null=True)
    profileImg = models.ImageField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    phEnable = models.BooleanField(default=False, null=True, blank=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) :
        return self.email
    
class Product(models.Model):

    seller = models.ForeignKey(mUser, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    condition = models.CharField(max_length=30, null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, null=True, blank=False)

    
class Address(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField(max_length=50, null=True)
    province = models.CharField(max_length=40, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    #data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.city)


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import mUser

class CreateUserForm(UserCreationForm):
    
    # password = forms.CharField(widget=forms.PasswordInput)
    # Confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = mUser
        fields = ["email", "username",]
        
class LoginUserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    #Confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = mUser
        fields = ["email",]
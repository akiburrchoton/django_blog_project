from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This is my custom form where I added email field. If I want to add more fields or customise the form, I will have to it in here.
class UserRegisterForm(UserCreationForm):
    email   = forms.EmailField()

    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']
from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

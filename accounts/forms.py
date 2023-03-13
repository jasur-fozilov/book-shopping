from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control custom-width'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control custom-width'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control custom-width'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control custom-width'}))
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput(attrs={'class': 'form-control custom-width'}))
    class Meta:
        model=CustomUser
        fields=('email','first_name','last_name','password1','password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('email','first_name','last_name')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,'Foydalanuvchi muvaffaqiyatli yaratildi')
            return redirect('login')
    else:
        form=CustomUserCreationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user:
            login(request,user)
            
            return redirect('store')
        else:
            messages.error(request,'Parol yoki email noto\'g\'ri')
    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request,'accounts/profile.html')
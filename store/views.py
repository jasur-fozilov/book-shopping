from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def book_list(request):
    books=Book.objects.all()
    return render(request,'store/book_list.html',{'books':books})

def book_detail(request,slug):
    return render(request,'store/book_detail.html')
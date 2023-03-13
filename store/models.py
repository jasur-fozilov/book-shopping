from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify
from PIL import Image
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True,db_index=True)
    icon=models.FileField(upload_to="category/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Writer(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True,db_index=True)
    bio=models.TextField()
    pic=models.FileField(upload_to="writer/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    writer=models.ForeignKey(Writer,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True,db_index=True)
    price=models.IntegerField()
    stock=models.IntegerField()
    coverpage=models.FileField(upload_to="coverpage/")
    bookpage=models.FileField(upload_to="bookpage/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    totalreview=models.IntegerField(default=1)
    totalrating=models.IntegerField(default=5)
    status=models.IntegerField(default=0)
    description=models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    customer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    review_star=models.IntegerField()
    review_text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Slider(models.Model):
    title=models.CharField(max_length=150)
    slideimg=models.FileField(upload_to="slide/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
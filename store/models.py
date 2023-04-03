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
    price=models.DecimalField(max_digits=7,decimal_places=2)
    stock=models.IntegerField()
    digital=models.BooleanField(default=False,blank=True,null=True)
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
    
    @property
    def bookURL(self):
        try:
            url=self.coverpage.url
        except:
            url=''
        return url

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

class Order(models.Model):
    customer=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.book.digital==False:
                shipping=True
        return shipping

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    book=models.ForeignKey(Book,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.book.price * self.quantity

class ShippingAddress(models.Model):
    customer=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    zipcode=models.CharField(max_length=100,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.address)
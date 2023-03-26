from django.contrib import admin
from django.utils.text import slugify
from PIL import Image
# Register your models here.

from .models import Category, Writer, Book, Review, Slider, Order, OrderItem, ShippingAddress

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

    def save_model(self,request,obj,form,change):
        if not obj.slug:
            obj.slug=slugify(obj.name)
        super().save_model(request,obj,form,change)

class WriterAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

    def save_model(self,request,obj,form,change):
        if not obj.slug:
            obj.slug=slugify(obj.name)
        super().save_model(request,obj,form,change)

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

    def save_model(self,request,obj,form,change):
        if not obj.slug:
            obj.slug=slugify(obj.name)
        super().save_model(request,obj,form,change)

        image_path=obj.coverpage.path
        with Image.open(image_path) as image:
            image.thumbnail((400,500))
            image.save(image_path)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Writer,WriterAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Review)
admin.site.register(Slider)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
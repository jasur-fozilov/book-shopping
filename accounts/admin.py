from django.contrib import admin
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display=('email','first_name','last_name','is_staff')
    list_filter=('is_staff','is_superuser','is_active')
    search_fields=('email','first_name','last_name')
    ordering=('email',)
    filter_horizontal=()



admin.site.register(CustomUser,CustomUserAdmin)
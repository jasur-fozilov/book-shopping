from django.urls import path
from . import views

app_name='store'

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('book-detail/<slug:slug>/',views.book_detail,name='book_detail'),

]

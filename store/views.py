from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Order, OrderItem, ShippingAddress
from django.http import JsonResponse
from accounts.models import CustomUser
import json
import datetime
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from . utils import cookieCart, cartData, guestOrder

# Create your views here.

def store(request):

    data=cartData(request)
    cartItems=data['cartItems']

    books=Book.objects.all()
    context={'books':books,'cartItems':cartItems}

    return render(request,'store/store.html',context)

def cart(request):

    data=cartData(request)
    cartItems=data['cartItems']
    items=data['items']
    order=data['order']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)


def checkout(request):

    data=cartData(request)
    cartItems=data['cartItems']
    items=data['items']
    order=data['order']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)

def updateItem(request):
    data=json.loads(request.body)
    bookId=data['bookId']
    action=data['action']

    customer=request.user
    book=Book.objects.get(id=bookId)
    order, created=Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created=OrderItem.objects.get_or_create(order=order,book=book)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)
    
    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('Item was added',safe=False)


def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    print('data',request.body)
    if request.user.is_authenticated:
        customer=request.user
        order, created=Order.objects.get_or_create(customer=customer,complete=False)

    else:
        customer, order=guestOrder(data)

    total=float(data['form']['total'])
    order.transaction_id=transaction_id
    if total==order.get_cart_total:
        order.complete=True
    order.save()

    if order.shipping==True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode']
            )

    return JsonResponse('Payment completed',safe=False)
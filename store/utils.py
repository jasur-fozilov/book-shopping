import json
from . models import *


def cookieCart(request):
    try:
        cart=json.loads(request.COOKIES['cart'])
    except:
        cart={}
    print('Cart:',cart)
    items=[]
    order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    cartItems=order['get_cart_items']
    for i in cart:
        try:
            cartItems+=cart[i]['quantity']

            book=Book.objects.get(id=i)
            total=(book.price*cart[i]['quantity'])

            order['get_cart_total']+=total
            order['get_cart_items']+=cart[i]['quantity']

            item={
                'book':{
                    'id':book.id,
                    'name':book.name,
                    'price':book.price,
                    'bookURL':book.bookURL,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)

            if book.digital==False:
                order['shipping']=True
        except:
            pass
    return {'items':items,'order':order,'cartItems':cartItems}

def cartData(request):
    if request.user.is_authenticated:
        customer=request.user
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
        
    else:
        cookieData=cookieCart(request)
        cartItems=cookieData['cartItems']
        items=cookieData['items']
        order=cookieData['order']
    return {'items':items,'order':order,'cartItems':cartItems}

def guestOrder(request,data):
    print('User in not logged in..')
    print('COOKIES:',request.COOKIES)
    name=data['form']['name']
    email=data['form']['email']
    cookieData=cookieCart(request)
    items=cookieData['items']
    customer, created=CustomUser.objects.get_or_create(email=email,)
    customer.first_name=name
    customer.save()

    order=Order.objects.create(customer=customer,complete=False,)
    
    for item in items:
        book=Book.objects.get(id=item['book']['id'])
        orderItem=OrderItem.objects.create(book=book,order=order,quantity=item['quantity'])
    return customer,order
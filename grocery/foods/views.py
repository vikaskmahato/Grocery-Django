from django.shortcuts import render, redirect
from .models import Product, Category, Orders
from .forms import Orderform
from django.contrib.auth.models import User

         

# Create your views here.
def home (request):
    category=Category.objects.all()
    return render(request, 'foods/home.html', {'category':category})

def contact(request):
    return render(request, 'foods/contact.html')
    

def checkout(request):
    c=list(request.session.get('cart').keys())
    p=Product.objects.filter(id__in=c)
    if request.method=='POST':
        addr=request.POST.get('address')
        phone=request.POST.get('phone_no')
        c_user=User.objects.get(username=request.user.username)
        cart=request.session.get('cart')
        for i in p:
            ord=Orders(customer=c_user, product=i, price=i.price, quantity=cart.get(str(i.id)), address=addr, phone_no=phone)
            ord.save()
        request.session['cart']={}  
        return render(request, 'foods/placed.html')
    else:
        f=Orderform()  
        info={ 'products':p,
           'form':f,
          }    
    return render(request, 'foods/checkout.html', info)    

def showcart(request):
    cart=request.session.get('cart')
    if cart:
        c=list(request.session.get('cart').keys())
        p=Product.objects.filter(id__in=c)
        empty=False
        return render(request, 'foods/cart.html', {'products':p,'empty':empty})
    else:
        empty=True

    return render(request, 'foods/cart.html', {'empty':empty})    

def getproducts(request, cat_id):
    if request.method=='POST':
        product=request.POST.get('product')
        minus=request.POST.get('minus')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if minus:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1                  
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1    
            
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart   
        prod=Product.objects.filter(category=cat_id)
        return render(request, 'items/break.html', {'products':prod})  

    else:    
        
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        prod=Product.objects.filter(category=cat_id)
        return render(request, 'items/break.html', {'products':prod})  
              
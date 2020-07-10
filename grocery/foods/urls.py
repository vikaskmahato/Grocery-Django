from django.contrib import admin
from django.urls import path
from foods import views
from .authmiddleware import auth_middleware

urlpatterns = [
    
    path('category/<int:cat_id>/',views.getproducts,name="categories"),
    path('cart/',views.showcart,name="cart"),
    path('checkout/',auth_middleware(views.checkout),name="checkout"),
    
    
]

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=200, blank=True)
    image=models.ImageField(blank=True)
    objects=models.Manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=70)
    price=models.IntegerField(default=0)
    image=models.ImageField(blank=True)
    desc=models.CharField(max_length=200, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    objects=models.Manager()

    def __str__(self):
        return self.name

class Orders(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10)
    objects=models.Manager()

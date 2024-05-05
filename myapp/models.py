from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_work(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    address = models.TextField()
    pin = models.IntegerField(null=True)

    def __str__(self):
        return self.address,self.user

class Type_product(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Product(models.Model):
    type = models.ForeignKey(Type_product,on_delete=models.CASCADE,null=True)
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=30)
    des = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.item


class Cart(models.Model):
    no = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="")
    product_item = models.CharField(max_length=30)
    price = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_item, self.user

class OrderStatus(models.Model):
    order_status = models.CharField(max_length=40)

    def __str__(self):
        return self.order_status



class Values(models.Model):
    value = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Order(models.Model):
    order_status = models.ForeignKey(OrderStatus,on_delete=models.CASCADE,null=True,default=1)
    no = models.AutoField(primary_key=True)
    # item = models.TextField(max_length=100,null=True)
    item = models.ManyToManyField(Values)
    # img = models.ImageField(upload_to="")
    price = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Cart_list(models.Model):
    item = models.CharField(max_length=20)
    quantity = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    img = models.ImageField(upload_to='',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)













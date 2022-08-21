from distutils.command.upload import upload
from django.conf import settings
from django.contrib.auth import get_user_model

from django.urls import reverse


from sre_parse import CATEGORIES, State
from statistics import mode
from telnetlib import STATUS
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from email.policy import default
import datetime


from django.db import models




# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.DateField(max_length=2000)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    State = models.CharField(max_length=50)

    def __str__(self):
      return str(self.id)




# class Category(models.Model):
#     name = models.CharField(max_length=20)

#     @staticmethod
#     def get_all_categories():
#         return Category.objects.all()


#     def __str__(self):
#         return self.name





# class CustomerO(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     password = models.CharField(max_length=500)

#     def register(self):
#         self.save()

#     @staticmethod
#     def get_customer_by_email(email):
#         try:
#             return Customer.objects.get(email=email)
#         except:
#             return False


#     def isExists(self):
#         if Customer.objects.filter(email = self.email):
#             return True

#         return  False






# class Productpg(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.IntegerField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
#     description = models.CharField(max_length=200, default='' , null=True , blank=True)
#     image = models.ImageField(upload_to='uploads/products/')

#     @staticmethod
#     def get_products_by_id(ids):
#         return Productpg.objects.filter(id__in =ids)

#     @staticmethod
#     def get_all_products():
#         return Productpg.objects.all()

#     @staticmethod
#     def get_all_products_by_categoryid(category_id):
#         if category_id:
#             return Productpg.objects.filter(category = category_id)
#         else:
#             return Productpg.get_all_products();




# class Order(models.Model):
#     product = models.ForeignKey(Productpg,
#                                 on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer,
#                                  on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price = models.IntegerField()
#     address = models.CharField(max_length=50, default='', blank=True)
#     phone = models.CharField(max_length=50, default='', blank=True)
#     date = models.DateField(default=datetime.datetime.today)
#     status = models.BooleanField(default=False)

#     def placeOrder(self):
#         self.save()

#     @staticmethod
#     def get_orders_by_customer(customer_id):
#         return Order.objects.filter(customer=customer_id).order_by('-date')













    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)



CATEGORY_CHOICES =(
    ('T','Textile'),
    ('F','Footwear'),
    ('MN', 'Men'),
    ('WM','Women'),
    ('KD','Kids'),

)
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,null=True)
    category =models.CharField(choices=CATEGORY_CHOICES,max_length=2,null=True)
    subcategory=models.CharField(max_length=50,default="",null=True)
    price=models.IntegerField(default=0,null=True)
    desc=models.CharField(max_length=300,null=True)
   
    image=models.ImageField(upload_to="images" ,default="",null=True)

    def __str__(self):
        return self.product_name


CATEGORY_CHOICES =(
     ('T','Textile'),
     ('F','Footwear'),
     ('MN', 'Men'),
     ('WM','Women'),
     ('KD','Kids'),

 )

class Productpg(models.Model):
     product_id=models.AutoField
     product_name=models.CharField(max_length=50,null=True)
     category =models.CharField(choices=CATEGORY_CHOICES,max_length=2,null=True)
     subcategory=models.CharField(max_length=50,default="",null=True)
     price=models.IntegerField(default=0,null=True)
     desc=models.CharField(max_length=300,null=True)
   
     image=models.ImageField(upload_to="images" ,default="",null=True)

     def __str__(self):
        return self.product_name

        return reverse('mentex', args=[str(self.id)])




class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
class Cart(models.Model):

    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
      return str(self.id)

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)      



class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."
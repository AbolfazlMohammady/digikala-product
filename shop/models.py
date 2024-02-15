import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from djmoney.models.fields import MoneyField
from decimal import Decimal
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

class Category(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 11)
    email = models.EmailField(blank=True, max_length= 50)
    password = models.CharField(max_length = 50)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Product(models.Model):
    name = models.CharField(max_length =50)
    description = models.TextField(max_length= 500, blank= True, default='')
    price =MoneyField(
        max_digits=15, decimal_places=2, default=0, default_currency='IRR',
        validators=[
            MinMoneyValidator(Decimal(0)), MaxMoneyValidator(Decimal(999999999)),
        ]
        )
    category =models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
    image=models.ImageField(upload_to = 'upload/product/', blank=True)
    star = models.IntegerField(default= 0 , validators=[MinValueValidator(0),MaxValueValidator(5)] )
    is_sale = models.BooleanField(default = False)
    price_sale = MoneyField(
        max_digits=15, decimal_places=2, default=0, default_currency='IRR',
        validators=[
            MinMoneyValidator(Decimal(0)), MaxMoneyValidator(Decimal(999999999)),
        ]
        )


    def __str__(self):
        return self.name
    
class Order(models.Model):
    product =models.ForeignKey(Product, on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(blank = True, max_length= 50, default='')
    phone_number = models.CharField(max_length = 11, blank =True)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default= False)

    def __str__(self):
        return self.product
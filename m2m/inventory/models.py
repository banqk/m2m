from django.db import models
from accounts.models import Account
from product.models import Product
from fuel_class.models import Fuel_Class

class Inventory(models.Model):

    name = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=20)
    location = models.CharField(max_length=250)
    id_number = models.CharField(max_length=50)
    volumn = models.IntegerField(null=True, default=0)
#    price = models.FloatField(null=True, default=0)
    products = models.CharField(max_length=250)
    create_date = models.DateTimeField(null=True, auto_now=True)
    m2m_account = models.ForeignKey(Account)

class SellPrice(models.Model):
    inventory = models.ForeignKey(Inventory)
    product = models.ForeignKey(Product)
    phy_volume = models.IntegerField(null=True, default=0)
    hedge_volume = models.IntegerField(null=True, default=0)
    volume = models.IntegerField(null=True, default=0)
    price = models.FloatField(null=True, default=0)
    hedge_price = models.FloatField(null=True, default=0)
    hedge_avg_price = models.FloatField(null=True, default=0)
    avg_price = models.FloatField(null=True, default=0)

#hedge position
class HedgePos(models.Model):
    inventory = models.ForeignKey(Inventory)
#    fuel_class = models.ForeignKey(Fuel_Class)
    product = models.ForeignKey(Product)
    trans = models.IntegerField(null=True, default=0)
#    trans = models.CharField(max_length=250)
    position = models.IntegerField(null=True, default=0)
    last_price = models.FloatField(null=True, default=0)
    price = models.FloatField(null=True, default=0)
    create_date = models.DateTimeField(null=True, auto_now=True)
    status = models.CharField(max_length=20)

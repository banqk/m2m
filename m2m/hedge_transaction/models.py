from django.db import models
from hedge_account.models import Hedge_Account
from counter_party.models import Counter 
from hedge_instrument.models import Instrument
from inventory.models import Inventory
from product.models import Product

class Hedge_Tran(models.Model):

    name = models.CharField(max_length=100)
    hedge_type = models.CharField(max_length=100)
    hedge_account = models.ForeignKey(Hedge_Account)
    instrument = models.ForeignKey(Instrument)
    inventory = models.ForeignKey(Inventory)
    price = models.FloatField(null=True, default=0)
    volume = models.IntegerField(null=True, default=0)
    initial_pos = models.BooleanField(default=False)
    create_date = models.DateTimeField(null=True, auto_now=True)
    confirm_number = models.CharField(max_length=100)
    trader = models.CharField(max_length=100)
    status = models.CharField(max_length=20) 
    program = models.CharField(max_length=100)
    product = models.ForeignKey(Product)

class Hedge_Price(models.Model):
    h_date = models.CharField(max_length=100)
    h_open = models.FloatField(null=True, default=0)
    h_high = models.FloatField(null=True, default=0)
    h_low = models.FloatField(null=True, default=0)
    h_last = models.FloatField(null=True, default=0)
    h_change = models.FloatField(null=True, default=0)
    h_settle = models.FloatField(null=True, default=0)
    h_volume = models.IntegerField(null=True, default=0)
    h_interest = models.FloatField(null=True, default=0)
    h_type = models.CharField(max_length=20)
    

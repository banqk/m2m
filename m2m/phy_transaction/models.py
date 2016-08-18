from django.db import models
from inventory.models import Inventory
from hedge_account.models import Hedge_Account
from counter_party.models import Counter 
from product.models import Product
from accounts.models import Account

class Physical(models.Model):

    name = models.CharField(max_length=100)
    phy_type = models.CharField(max_length=20)
    inventory = models.ForeignKey(Inventory)
    product = models.ForeignKey(Product)
    counter_party = models.ForeignKey(Counter)
    price = models.FloatField(null=True, default=0)
    net_volume = models.IntegerField(null=True, default=0)
    gross_volume = models.IntegerField(null=True, default=0)
    program = models.CharField(max_length=50, null=True)
    create_date = models.DateTimeField(null=True, auto_now=True)
    to_m2m_account = models.CharField(max_length=100)
    to_inventory = models.CharField(max_length=100)

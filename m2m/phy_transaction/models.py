from django.db import models
from inventory.models import Inventory
from hedge_account.models import Hedge_Account
from counter_party.models import Counter 
from product.models import Product

class Physical(models.Model):

    name = models.CharField(max_length=100)
    phy_type = models.CharField(max_length=20)
    inventory = models.ForeignKey(Inventory)
    product = models.ForeignKey(Product)
    counter_party = models.ForeignKey(Counter)
    price = models.FloatField(null=True, default=0)
    volume = models.IntegerField(null=True, default=0)
    create_date = models.DateTimeField(null=True, auto_now=True)
from django.db import models
from inventory.models import Inventory
from hedge_account.models import Hedge_Account
from counter_party.models import Counter 
from hedge_instrument.models import Instrument

class Hedge_Tran(models.Model):

    name = models.CharField(max_length=100)
    hedge_type = models.CharField(max_length=100)
    hedge_account = models.ForeignKey(Hedge_Account)
    instrument = models.ForeignKey(Instrument)
    price = models.FloatField(null=True, default=0)
    volume = models.IntegerField(null=True, default=0)
    initial_pos = models.BooleanField(default=False)
    create_date = models.DateTimeField(null=True, auto_now=True)

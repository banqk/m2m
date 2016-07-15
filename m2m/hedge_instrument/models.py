from django.db import models
from counter_party.models import Counter

class Instrument(models.Model):
    name = models.CharField(max_length = 100)
    fuel_class = models.CharField(max_length = 100)
    contract_year = models.CharField(max_length=10)
    contract_month = models.CharField(max_length=10)
    expiration_date = models.DateTimeField(null=True)
    instrument = models.CharField(max_length = 20)
    put_call = models.CharField(max_length = 100)
    strike_price = models.CharField(max_length = 100)
    counter_party = models.ForeignKey(Counter)
    create_date = models.DateTimeField(null=True, auto_now=True)

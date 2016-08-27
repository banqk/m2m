from django.db import models
from accounts.models import Account

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

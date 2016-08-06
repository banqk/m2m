from django.db import models
from fuel_class.models import Fuel_Class
from accounts.models import Account
from inventory.models import Inventory

class Product(models.Model):
    name = models.CharField(max_length=250)
    fuel_class = models.ForeignKey(Fuel_Class)
    m2m_account = models.ForeignKey(Account)
    inventory = models.ForeignKey(Inventory)
    description = models.CharField(max_length=250, null=True)
    create_date = models.DateTimeField(
        auto_now=True,
        help_text='This is create date', )

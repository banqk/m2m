from django.db import models
from accounts.models import Account

class Inventory(models.Model):

    name = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=20)
    location = models.CharField(max_length=250)
    id_number = models.CharField(max_length=50)
    m2m_account = models.ForeignKey(Account)

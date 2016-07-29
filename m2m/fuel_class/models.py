from django.db import models
from accounts.models import Account

class Fuel_Class(models.Model):
    code = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True)
    m2m_account = models.ForeignKey(Account)

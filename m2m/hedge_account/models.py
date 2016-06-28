from django.db import models
from accounts.models import Account

class Hedge_Account(models.Model):
    name = models.CharField(max_length = 100)
    id_number = models.CharField(max_length=50)
    institution = models.CharField(max_length = 250)
    create_date = models.DateTimeField(null=True, auto_now=True)
    m2m_account = models.ForeignKey(Account)

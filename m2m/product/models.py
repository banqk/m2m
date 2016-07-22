from django.db import models
from fuel_class.models import Fuel_Class

class Product(models.Model):
    name = models.CharField(max_length=250)
    fuel_class = models.ForeignKey(Fuel_Class)
    create_date = models.DateTimeField(
        auto_now=True,
        help_text='This is create date', )

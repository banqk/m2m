from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    fuel_class = models.CharField(max_length=250)
    create_date = models.DateTimeField(
        auto_now=True,
        help_text='This is create date', )

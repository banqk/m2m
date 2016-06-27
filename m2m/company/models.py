from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now=True)

# Create your models here.

from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    


# Create your models here.

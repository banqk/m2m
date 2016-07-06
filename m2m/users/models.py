from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now=True)

# Create your models here.

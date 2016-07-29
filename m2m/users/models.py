from django.db import models
from user_privilages.models import User_Privilage

class User(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now=True)
    user_privilages = models.ForeignKey(User_Privilage)

# Create your models here.

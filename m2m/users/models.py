from django.db import models
from django.contrib.auth.models import AbstractUser
from user_privilages.models import User_Privilage

class User(AbstractUser):
    user_privilages = models.ForeignKey(User_Privilage)

# Create your models here.

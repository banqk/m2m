from django.db import models
from users.models import User

class Account(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250)
    create_date = models.DateTimeField(
        auto_now=True,
        help_text='When the account logined, will change the column', )
    user = models.ForeignKey(User)
    


# Create your models here.

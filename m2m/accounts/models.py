from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    last_login_date = models.DateTimeField(
        auto_now=True,
        help_text='When the account logined, will change the column', )
    


# Create your models here.

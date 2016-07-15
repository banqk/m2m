from django.db import models

class Counter(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250, null=True)
    counter_type = models.CharField(max_length=250)
    identifier = models.CharField(max_length=250)
    create_date = models.DateTimeField(
        auto_now=True,
        help_text='This is create date', )

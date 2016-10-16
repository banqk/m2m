# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_sellprice_avg_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedgepos',
            name='last_price',
            field=models.FloatField(default=0, null=True),
        ),
    ]

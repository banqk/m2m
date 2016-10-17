# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20161016_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellprice',
            name='hedge_avg_price',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='sellprice',
            name='hedge_price',
            field=models.FloatField(default=0, null=True),
        ),
    ]

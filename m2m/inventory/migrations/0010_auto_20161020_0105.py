# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_hedgepos_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hedgepos',
            name='position',
        ),
        migrations.AddField(
            model_name='hedgepos',
            name='status',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
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
        migrations.AddField(
            model_name='sellprice',
            name='hedge_volume',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='sellprice',
            name='phy_volume',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

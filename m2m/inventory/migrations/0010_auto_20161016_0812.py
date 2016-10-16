# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_hedgepos_create_date'),
    ]

    operations = [
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

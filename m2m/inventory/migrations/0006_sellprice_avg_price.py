# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_hedgepos_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellprice',
            name='avg_price',
            field=models.FloatField(default=0, null=True),
        ),
    ]

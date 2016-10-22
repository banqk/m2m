# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_transaction', '0002_hedge_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedge_price',
            name='h_type',
            field=models.CharField(default='HOZ2016', max_length=20),
            preserve_default=False,
        ),
    ]

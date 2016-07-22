# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20160712_1056'),
        ('hedge_transaction', '0002_auto_20160715_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedge_tran',
            name='inventory',
            field=models.ForeignKey(default=1, to='inventory.Inventory'),
            preserve_default=False,
        ),
    ]

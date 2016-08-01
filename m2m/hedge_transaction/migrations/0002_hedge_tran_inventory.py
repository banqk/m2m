# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('hedge_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedge_tran',
            name='inventory',
            field=models.ForeignKey(default=1, to='inventory.Inventory'),
            preserve_default=False,
        ),
    ]

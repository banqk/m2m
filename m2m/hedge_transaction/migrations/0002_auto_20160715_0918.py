# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_instrument', '0002_auto_20160715_0918'),
        ('hedge_transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hedge_tran',
            name='product',
        ),
        migrations.AddField(
            model_name='hedge_tran',
            name='instrument',
            field=models.ForeignKey(default=1, to='hedge_instrument.Instrument'),
            preserve_default=False,
        ),
    ]

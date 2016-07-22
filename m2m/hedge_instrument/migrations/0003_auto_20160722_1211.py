# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_instrument', '0002_auto_20160715_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='fuel_class',
            field=models.ForeignKey(to='fuel_class.Fuel_Class'),
        ),
    ]

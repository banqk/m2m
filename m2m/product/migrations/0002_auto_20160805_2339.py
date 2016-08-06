# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('accounts', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.ForeignKey(default=1, to='inventory.Inventory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='m2m_account',
            field=models.ForeignKey(default=1, to='accounts.Account'),
            preserve_default=False,
        ),
    ]

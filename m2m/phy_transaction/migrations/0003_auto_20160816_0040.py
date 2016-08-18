# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phy_transaction', '0002_physical_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='physical',
            name='to_inventory',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physical',
            name='to_m2m_account',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]

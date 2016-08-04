# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('phy_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='physical',
            name='product',
            field=models.ForeignKey(to='product.Product'),
        ),
    ]

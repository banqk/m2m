# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_inventory'),
        ('hedge_transaction', '0003_hedge_price_h_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedge_tran',
            name='product',
            field=models.ForeignKey(default=1, to='product.Product'),
            preserve_default=False,
        ),
    ]

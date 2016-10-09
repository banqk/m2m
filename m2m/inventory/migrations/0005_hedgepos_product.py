# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_inventory'),
        ('inventory', '0004_hedgepos'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedgepos',
            name='product',
            field=models.ForeignKey(default=1, to='product.Product'),
            preserve_default=False,
        ),
    ]

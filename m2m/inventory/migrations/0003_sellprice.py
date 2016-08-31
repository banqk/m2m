# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_inventory'),
        ('inventory', '0002_inventory_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.IntegerField(default=0, null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
                ('product', models.ForeignKey(to='product.Product')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='inventory',
        ),
    ]

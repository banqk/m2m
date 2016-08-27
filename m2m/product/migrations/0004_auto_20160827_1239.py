# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_volumn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='volumn',
            new_name='volume',
        ),
    ]

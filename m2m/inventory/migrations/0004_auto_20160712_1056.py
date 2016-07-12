# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventory_volumn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='volumn',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

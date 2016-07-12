# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventory_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='volumn',
            field=models.IntegerField(null=True),
        ),
    ]

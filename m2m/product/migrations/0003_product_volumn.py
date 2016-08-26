# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160805_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='volumn',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

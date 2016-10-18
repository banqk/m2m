# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20161017_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hedgepos',
            name='position',
        ),
        migrations.AlterField(
            model_name='hedgepos',
            name='trans',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20161020_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedgepos',
            name='position',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_hedgepos_last_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedgepos',
            name='trans',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

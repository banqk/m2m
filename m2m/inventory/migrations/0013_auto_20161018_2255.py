# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20161018_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedgepos',
            name='status',
            field=models.CharField(default='OPEN', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hedgepos',
            name='trans',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Account',
            name='fuel_type',
            field=models.CharField(default='ULSD,RBOB,BO,NG', max_length=250, null=True),
            preserve_default=False,
        ),
    ]

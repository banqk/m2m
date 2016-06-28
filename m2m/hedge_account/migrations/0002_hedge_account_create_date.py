# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedge_account',
            name='create_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

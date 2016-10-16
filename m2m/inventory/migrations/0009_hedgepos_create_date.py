# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_hedgepos_trans'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedgepos',
            name='create_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

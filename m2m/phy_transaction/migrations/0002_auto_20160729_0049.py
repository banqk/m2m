# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phy_transaction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='physical',
            old_name='volume',
            new_name='gross_volume',
        ),
        migrations.AddField(
            model_name='physical',
            name='net_volume',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='physical',
            name='program',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hedge_tran',
            name='inventory',
        ),
        migrations.AddField(
            model_name='hedge_tran',
            name='confirm_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hedge_tran',
            name='program',
            field=models.CharField(default='aaa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hedge_tran',
            name='status',
            field=models.CharField(default=11, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hedge_tran',
            name='trader',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hedge_Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h_date', models.CharField(max_length=100)),
                ('h_open', models.FloatField(default=0, null=True)),
                ('h_high', models.FloatField(default=0, null=True)),
                ('h_low', models.FloatField(default=0, null=True)),
                ('h_last', models.FloatField(default=0, null=True)),
                ('h_change', models.FloatField(default=0, null=True)),
                ('h_settle', models.FloatField(default=0, null=True)),
                ('h_volume', models.IntegerField(default=0, null=True)),
                ('h_interest', models.FloatField(default=0, null=True)),
            ],
        ),
    ]

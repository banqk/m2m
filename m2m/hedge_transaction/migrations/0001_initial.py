# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_account', '0001_initial'),
        ('hedge_instrument', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hedge_Tran',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('hedge_type', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0, null=True)),
                ('volume', models.IntegerField(default=0, null=True)),
                ('initial_pos', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now=True, null=True)),
                ('confirm_number', models.CharField(max_length=100)),
                ('trader', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('program', models.CharField(max_length=100)),
                ('hedge_account', models.ForeignKey(to='hedge_account.Hedge_Account')),
                ('instrument', models.ForeignKey(to='hedge_instrument.Instrument')),
            ],
        ),
    ]

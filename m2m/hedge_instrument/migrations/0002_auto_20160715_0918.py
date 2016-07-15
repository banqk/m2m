# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter_party', '0001_initial'),
        ('hedge_instrument', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('fuel_class', models.CharField(max_length=100)),
                ('contract_year', models.CharField(max_length=10)),
                ('contract_month', models.CharField(max_length=10)),
                ('expiration_date', models.DateTimeField(null=True)),
                ('instrument', models.CharField(max_length=20)),
                ('put_call', models.CharField(max_length=100)),
                ('strike_price', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now=True, null=True)),
                ('counter_party', models.ForeignKey(to='counter_party.Counter')),
            ],
        ),
        migrations.RemoveField(
            model_name='hedge_account',
            name='counter_party',
        ),
        migrations.DeleteModel(
            name='Hedge_Account',
        ),
    ]

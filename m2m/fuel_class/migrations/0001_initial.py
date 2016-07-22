# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160702_0541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel_Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250, null=True)),
                ('m2m_account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
    ]

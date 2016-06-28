# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160622_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hedge_Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=250)),
                ('m2m_account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hedge_Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=250)),
                ('create_date', models.DateTimeField(auto_now=True, null=True)),
                ('m2m_account', models.ForeignKey(to='accounts.Account')),
            ],
        ),
    ]

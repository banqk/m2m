# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_sellprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='HedgePos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(default=0, null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
            ],
        ),
    ]

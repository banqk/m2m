# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('counter_party', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('phy_type', models.CharField(max_length=20)),
                ('price', models.FloatField(default=0, null=True)),
                ('volume', models.IntegerField(default=0, null=True)),
                ('create_date', models.DateTimeField(auto_now=True, null=True)),
                ('counter_party', models.ForeignKey(to='counter_party.Counter')),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
                ('product', models.ForeignKey(to='product.Product')),
            ],
        ),
    ]

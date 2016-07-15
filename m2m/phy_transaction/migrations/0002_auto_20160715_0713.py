# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter_party', '0001_initial'),
        ('inventory', '0004_auto_20160712_1056'),
        ('product', '0001_initial'),
        ('phy_transaction', '0001_initial'),
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
            ],
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='counter_party',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='product',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.AddField(
            model_name='physical',
            name='inventory',
            field=models.ForeignKey(to='inventory.Inventory'),
        ),
        migrations.AddField(
            model_name='physical',
            name='product',
            field=models.ForeignKey(to='product.Product'),
        ),
    ]

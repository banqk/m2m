# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('create_date', models.DateTimeField(help_text=b'This is create date', auto_now=True)),
                ('fuel_class', models.ForeignKey(to='fuel_class.Fuel_Class')),
            ],
        ),
    ]

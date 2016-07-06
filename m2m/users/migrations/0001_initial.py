# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
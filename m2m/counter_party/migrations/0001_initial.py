# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250, null=True)),
                ('counter_type', models.CharField(max_length=250)),
                ('identifier', models.CharField(max_length=250)),
                ('create_date', models.DateTimeField(help_text=b'This is create date', auto_now=True)),
            ],
        ),
    ]

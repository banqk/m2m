# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Privilage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=250)),
                ('code', models.IntegerField(default=0, choices=[(0, b'USER'), (1, b'ADMIN')])),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
    ]

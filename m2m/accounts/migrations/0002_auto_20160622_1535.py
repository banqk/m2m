# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_login_date',
            field=models.DateTimeField(help_text=b'When the account logined, will change the column', null=True),
        ),
    ]

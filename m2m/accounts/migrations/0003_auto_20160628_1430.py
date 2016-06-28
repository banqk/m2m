# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160622_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_login_date',
            field=models.DateTimeField(help_text=b'When the account logined, will change the column', auto_now=True),
        ),
    ]

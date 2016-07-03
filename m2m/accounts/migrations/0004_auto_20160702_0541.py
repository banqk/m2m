# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160628_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='full_name',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='last_login_date',
            new_name='create_date',
        ),
        migrations.RemoveField(
            model_name='account',
            name='company',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
    ]

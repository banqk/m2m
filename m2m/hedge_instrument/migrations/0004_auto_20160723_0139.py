# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_instrument', '0003_auto_20160722_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrument',
            old_name='name',
            new_name='symbol',
        ),
    ]

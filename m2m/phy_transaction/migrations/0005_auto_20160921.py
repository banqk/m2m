
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phy_transaction', '0004_auto_20160827_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='physical',
            name='transaction_date',
            field=models.DateTimeField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phy_transaction', '0003_auto_20160816_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='physical',
            old_name='to_m2m_account',
            new_name='to_product',
        ),
    ]

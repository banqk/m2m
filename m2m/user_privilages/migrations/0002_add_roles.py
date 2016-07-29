# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from user_privilages.models import User_Privilage

def addRole(apps, schema_edtior):
    desc = "User"
    user_pri = User_Privilage(display_name="User", code = 0, description = desc) 
    user_pri.save()
    desc = "Admin permission"
    user_pri = User_Privilage(display_name="Admin", code = 1, description = desc) 
    user_pri.save()

class Migration(migrations.Migration):

    dependencies = [
        ('user_privilages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_privilage',
            name='code',
            field=models.IntegerField(default=0, choices=[(0, b'USER'), (1, b'ADMIN')]),
        ),
        migrations.RunPython(addRole),
    ]

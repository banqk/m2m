# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from users.models import User

def addUser(apps, schema_editor):
    user = User(username="admin", password="admin",is_active = 1, user_privilages_id=2)
    user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addUser),
    ]

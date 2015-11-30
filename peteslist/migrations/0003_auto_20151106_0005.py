# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0002_auto_20151105_2254'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubCategory',
            new_name='Category',
        ),
    ]

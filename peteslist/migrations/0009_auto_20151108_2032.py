# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0008_auto_20151108_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='post_type',
            new_name='type',
        ),
    ]

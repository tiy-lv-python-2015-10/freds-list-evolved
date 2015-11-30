# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0015_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='post',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]

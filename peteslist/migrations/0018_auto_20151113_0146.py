# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0017_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dimensions',
        ),
        migrations.RemoveField(
            model_name='post',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='post',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='serial_num',
        ),
    ]

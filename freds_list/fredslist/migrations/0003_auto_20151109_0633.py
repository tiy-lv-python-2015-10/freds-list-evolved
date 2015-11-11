# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fredslist', '0002_auto_20151109_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='location',
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.OneToOneField(to='fredslist.City'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]

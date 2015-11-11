# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fredslist', '0004_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='city',
        ),
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='images',
            name='post',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]

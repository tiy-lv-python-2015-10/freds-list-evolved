# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0018_auto_20151113_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='created_at',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
    ]

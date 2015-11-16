# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0006_auto_20151107_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='by_phone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='by_text',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('like new', 'Like New'), ('excellent', 'Excellent'), ('good', 'Good'), ('fair', 'Fair'), ('salvage', 'Salvage'), ('other', 'Other')], max_length=20, null=True),
        ),
    ]

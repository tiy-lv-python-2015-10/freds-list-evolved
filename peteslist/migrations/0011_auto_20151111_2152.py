# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0010_auto_20151108_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('like new', 'Like New'), ('excellent', 'Excellent'), ('good', 'Good'), ('fair', 'Fair'), ('salvage', 'Salvage'), ('other', 'Other')], null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(null=True, max_length=40),
        ),
    ]

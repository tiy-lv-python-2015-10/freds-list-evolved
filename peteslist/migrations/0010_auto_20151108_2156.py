# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0009_auto_20151108_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, to='peteslist.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.ForeignKey(null=True, to='peteslist.Type'),
        ),
    ]

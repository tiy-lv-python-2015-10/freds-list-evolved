# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0012_remove_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(to='peteslist.Location', null=True),
        ),
    ]

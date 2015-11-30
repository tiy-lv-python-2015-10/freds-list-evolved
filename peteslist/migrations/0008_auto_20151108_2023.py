# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peteslist', '0007_auto_20151107_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='type',
            new_name='post_type',
        ),
    ]

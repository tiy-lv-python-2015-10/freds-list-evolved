# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fredslist', '0003_auto_20151109_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('state', models.CharField(max_length=21)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
    ]

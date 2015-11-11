# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fredslist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('state', models.CharField(max_length=21)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='fredslist.State'),
        ),
        migrations.AddField(
            model_name='category',
            name='city',
            field=models.ForeignKey(to='fredslist.City', null=True, blank=True),
        ),
    ]

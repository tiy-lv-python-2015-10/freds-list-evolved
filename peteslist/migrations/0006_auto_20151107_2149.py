# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peteslist', '0005_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=5000)),
                ('location', models.CharField(max_length=40)),
                ('phone_number', models.CharField(null=True, max_length=15, blank=True)),
                ('contact_name', models.CharField(null=True, max_length=35, blank=True)),
                ('price', models.DecimalField(null=True, decimal_places=2, max_digits=10, blank=True)),
                ('specific_location', models.CharField(null=True, max_length=75, blank=True)),
                ('manufacturer', models.CharField(null=True, max_length=50, blank=True)),
                ('model_name', models.CharField(null=True, max_length=50, blank=True)),
                ('serial_num', models.CharField(null=True, max_length=50, blank=True)),
                ('dimensions', models.CharField(null=True, max_length=50, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(null=True, to='peteslist.Post'),
        ),
    ]

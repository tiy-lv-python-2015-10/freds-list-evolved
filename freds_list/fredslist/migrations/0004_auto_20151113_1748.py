# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fredslist', '0003_auto_20151113_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('favorited_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='fredslist.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='favorited_posts',
            field=models.ManyToManyField(through='fredslist.Favorite', to=settings.AUTH_USER_MODEL, related_name='favorited_posts'),
        ),
    ]

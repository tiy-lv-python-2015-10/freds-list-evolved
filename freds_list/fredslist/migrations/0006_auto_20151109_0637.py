# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fredslist', '0005_auto_20151109_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(blank=True, upload_to='fredslist_images', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('contact_name', models.CharField(max_length=255)),
                ('posting_title', models.CharField(max_length=255)),
                ('price', models.CharField(blank=True, max_length=10, null=True)),
                ('specific_location', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(max_length=255)),
                ('posting_body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('location', models.OneToOneField(to='fredslist.City')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('state', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='fredslist.Category')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='sub_category',
            field=models.ForeignKey(to='fredslist.SubCategory'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(to='fredslist.Post'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='fredslist.State'),
        ),
        migrations.AddField(
            model_name='category',
            name='city',
            field=models.ForeignKey(to='fredslist.City'),
        ),
    ]

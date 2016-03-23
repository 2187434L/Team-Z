# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0027_auto_20160320_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspost',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogspost',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='blogspost',
            name='title',
        ),
        migrations.AddField(
            model_name='blogspost',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogspost',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogspost',
            name='name',
            field=models.CharField(default='', unique=True, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogspost',
            name='picture',
            field=models.ImageField(upload_to=b'food_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogspost',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogspost',
            name='view',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0042_food_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]

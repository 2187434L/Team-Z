# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0051_delete_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]

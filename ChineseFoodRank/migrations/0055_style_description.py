# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0054_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
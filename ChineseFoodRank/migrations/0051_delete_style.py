# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0050_style'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Style',
        ),
    ]

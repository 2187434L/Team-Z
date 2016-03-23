# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0043_foodstyle'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='style',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ChineseFoodRank.foodStyle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodstyle',
            name='style',
            field=models.CharField(default=b'#', max_length=128, unique=True),
        ),
    ]

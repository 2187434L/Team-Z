# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0045_auto_20160321_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChineseFoodRank.Category2'),
        ),
        migrations.DeleteModel(
            name='foodStyle',
        ),
    ]

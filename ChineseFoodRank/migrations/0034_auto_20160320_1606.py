# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0033_page_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FoodName', models.CharField(max_length=128)),
                ('likes', models.IntegerField(default=0)),
                ('url', models.URLField()),
                ('picture', models.ImageField(upload_to=b'food_images', blank=True)),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='ChineseFoodRank.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]

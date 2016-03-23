# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0038_remove_food_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commodity_cover', models.ImageField(upload_to=b'food_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

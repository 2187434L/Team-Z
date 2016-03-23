# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0032_remove_category_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='picture',
            field=models.ImageField(upload_to=b'food_images', blank=True),
            preserve_default=True,
        ),
    ]

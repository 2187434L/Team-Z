# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0019_delete_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(upload_to=b'food_images', blank=True),
            preserve_default=True,
        ),
    ]

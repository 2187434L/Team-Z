# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0025_auto_20160320_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='model_pic',
            field=models.ImageField(upload_to=b'food_images'),
            preserve_default=True,
        ),
    ]

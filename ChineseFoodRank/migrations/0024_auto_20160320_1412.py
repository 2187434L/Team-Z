# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0023_auto_20160320_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='model_pic',
            field=models.ImageField(upload_to=b'../profile_images/'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0035_auto_20160320_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='views',
        ),
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]

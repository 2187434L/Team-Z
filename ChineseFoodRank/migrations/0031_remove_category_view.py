# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0030_auto_20160320_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='view',
        ),
    ]

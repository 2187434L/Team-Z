# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0031_remove_category_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='picture',
        ),
    ]

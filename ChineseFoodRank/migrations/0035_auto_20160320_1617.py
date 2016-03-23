# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0034_auto_20160320_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='FoodName',
            new_name='title',
        ),
    ]

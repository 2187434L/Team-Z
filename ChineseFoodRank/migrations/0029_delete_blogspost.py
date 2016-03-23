# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0028_auto_20160320_1540'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsPost',
        ),
    ]

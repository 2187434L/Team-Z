# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0006_category_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsPost',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0008_blogspost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsPost',
        ),
    ]

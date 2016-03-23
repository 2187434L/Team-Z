# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0022_page2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page2',
            name='category',
        ),
        migrations.DeleteModel(
            name='Page2',
        ),
    ]

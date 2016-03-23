# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0037_delete_examplemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='url',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0039_commodity'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0029_delete_blogspost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

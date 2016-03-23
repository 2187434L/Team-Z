# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0018_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]

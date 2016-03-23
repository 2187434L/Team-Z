# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0020_category_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_pic', models.ImageField(default=b'pic_folder/1.jpg', upload_to=b'profile_images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

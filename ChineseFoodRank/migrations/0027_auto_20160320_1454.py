# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChineseFoodRank', '0026_auto_20160320_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='examplemodel',
            name='model_pic',
            field=models.ImageField(default=b'pic_folder/1.jpg', upload_to=b'profile_images/'),
            preserve_default=True,
        ),
    ]

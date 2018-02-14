# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='round_video',
        ),
        migrations.AlterField(
            model_name='round',
            name='round_picture',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to=''),
        ),
    ]

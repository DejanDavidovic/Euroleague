# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-29 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_team',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-29 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_player_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat',
            old_name='field_goal_percentage',
            new_name='two_point_percentage',
        ),
    ]

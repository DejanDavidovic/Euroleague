# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='history',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-26 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20180126_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games_played', models.DecimalField(decimal_places=0, max_digits=2)),
                ('games_started', models.DecimalField(decimal_places=0, max_digits=2)),
                ('minutes', models.CharField(max_length=200)),
                ('points', models.DecimalField(decimal_places=2, max_digits=6)),
                ('two_point', models.CharField(max_length=200)),
                ('three_point', models.CharField(max_length=200)),
                ('free_throw', models.CharField(max_length=200)),
                ('rebounds', models.DecimalField(decimal_places=2, max_digits=6)),
                ('assists', models.DecimalField(decimal_places=2, max_digits=6)),
                ('steals', models.DecimalField(decimal_places=2, max_digits=6)),
                ('turnovers', models.DecimalField(decimal_places=2, max_digits=6)),
                ('blocks', models.DecimalField(decimal_places=2, max_digits=6)),
                ('index', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_stats',
        ),
        migrations.AddField(
            model_name='stat',
            name='stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player'),
        ),
    ]
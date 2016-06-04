# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docnotes', '0018_auto_20160604_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='interval',
        ),
        migrations.AddField(
            model_name='prescription',
            name='time_inverval',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=1, max_length=10),
        ),
    ]

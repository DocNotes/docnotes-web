# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 08:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docnotes', '0004_auto_20160604_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

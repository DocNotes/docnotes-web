# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 08:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docnotes', '0007_auto_20160604_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='duration',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

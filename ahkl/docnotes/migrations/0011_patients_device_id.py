# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docnotes', '0010_auto_20160604_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='device_id',
            field=models.CharField(default='1234', max_length=255),
        ),
    ]

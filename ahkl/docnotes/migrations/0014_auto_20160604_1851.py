# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docnotes', '0013_auto_20160604_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='device_id',
            new_name='deviceid',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docnotes', '0002_auto_20160604_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='medication',
            new_name='medication_type',
        ),
    ]
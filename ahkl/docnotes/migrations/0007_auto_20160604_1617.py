# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docnotes', '0006_auto_20160604_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

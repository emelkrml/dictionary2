# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-29 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0013_auto_20160829_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.User'),
        ),
    ]

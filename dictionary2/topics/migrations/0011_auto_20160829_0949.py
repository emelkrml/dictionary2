# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-29 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0010_auto_20160829_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userjunior',
            name='junior',
            field=models.BooleanField(default=True, verbose_name='User'),
        ),
    ]
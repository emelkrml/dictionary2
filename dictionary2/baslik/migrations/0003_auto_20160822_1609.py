# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-22 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baslik', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baslik.Baslik', verbose_name='Baslik'),
        ),
    ]

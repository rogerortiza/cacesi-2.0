# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 22:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_terceros', '0009_auto_20170224_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extintores',
            name='vencimiento',
            field=models.DateField(default=datetime.datetime(2018, 2, 24, 22, 34, 53, 13450, tzinfo=utc)),
        ),
    ]

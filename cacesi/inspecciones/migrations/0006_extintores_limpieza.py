# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0005_auto_20170205_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='extintores',
            name='limpieza',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

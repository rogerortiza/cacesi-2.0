# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-12 03:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0019_auto_20171112_0301'),
        ('planteles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areas',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Areas',
        ),
    ]

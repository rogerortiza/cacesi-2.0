# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-10 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_terceros', '0013_auto_20170225_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extintores',
            name='foto',
            field=models.ImageField(blank=True, upload_to='static/images/extintores'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0013_auto_20170221_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extintores',
            name='observaciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='extintores',
            name='ultima_reca',
            field=models.DateField(verbose_name='Ultima Recarga'),
        ),
    ]
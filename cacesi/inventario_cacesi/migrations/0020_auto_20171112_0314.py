# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-12 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_cacesi', '0019_auto_20171112_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='CategoriaProductos',
        ),
    ]

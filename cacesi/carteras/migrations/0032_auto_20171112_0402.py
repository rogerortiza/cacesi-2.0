# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-12 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0031_auto_20171112_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='giro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.GiroProveedores'),
        ),
    ]

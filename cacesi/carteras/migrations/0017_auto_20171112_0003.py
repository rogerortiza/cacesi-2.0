# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-12 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0016_auto_20171112_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='giro',
            field=models.CharField(choices=[('1', 'Maquinaria'), ('2', 'Equipos Contra Incendios'), ('3', 'Equipos de Seguridad')], max_length=100),
        ),
    ]

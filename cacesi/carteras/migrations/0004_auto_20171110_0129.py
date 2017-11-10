# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-10 01:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0003_proveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='giro',
            field=models.CharField(choices=[(1, 'Maquinaria'), (2, 'Equipos Contra Incendios'), (3, 'Equipos de Seguridad')], max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-10 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0005_auto_20171110_0231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactos_proveedores',
            options={'verbose_name_plural': 'Contactos del Proveedor'},
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='giro',
            field=models.CharField(choices=[('3', 'Equipos de Seguridad'), ('2', 'Equipos Contra Incendios'), ('1', 'Maquinaria')], max_length=100),
        ),
    ]

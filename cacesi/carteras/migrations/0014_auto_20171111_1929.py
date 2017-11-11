# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-11 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0013_auto_20171111_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='colonia',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='logo',
            field=models.ImageField(blank=True, upload_to='static/images/logosClientes'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='giro',
            field=models.CharField(choices=[('1', 'Maquinaria'), ('2', 'Equipos Contra Incendios'), ('3', 'Equipos de Seguridad')], max_length=100),
        ),
    ]
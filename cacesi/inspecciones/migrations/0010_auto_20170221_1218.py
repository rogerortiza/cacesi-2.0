# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0009_auto_20170217_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extintores',
            old_name='acciones',
            new_name='acciones_etiqueta',
        ),
        migrations.RenameField(
            model_name='extintores',
            old_name='condicion',
            new_name='condicion_etiqueta',
        ),
        migrations.RenameField(
            model_name='extintores',
            old_name='foto_antes',
            new_name='foto_etiqueta_antes',
        ),
        migrations.RenameField(
            model_name='extintores',
            old_name='foto_despues',
            new_name='foto_etiqueta_despues',
        ),
        migrations.AddField(
            model_name='extintores',
            name='arreglo_etiqueta_sitio',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extintores',
            name='motivos_etiqueta',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extintores',
            name='etiqueta',
            field=models.BooleanField(default=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0007_extintores_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='extintores',
            name='acciones',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extintores',
            name='condicion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extintores',
            name='foto_antes',
            field=models.ImageField(default=1, upload_to='static/images/inspecciones/reportes/antes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extintores',
            name='foto_despues',
            field=models.ImageField(default=1, upload_to='static/images/inspecciones/reportes/despues'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extintores',
            name='status',
            field=models.CharField(choices=[('En su lugar', 'En su lugar'), ('No Encontrado', 'No Encontrado'), ('Operable', 'Operable'), ('No Operable', 'No Operable'), ('Reemplazado por caducidad', 'Reemplazado por caducidad'), ('Reemplazado por falta de presion', 'Reemplazado por falta de presion')], default=1, max_length=140),
            preserve_default=False,
        ),
    ]
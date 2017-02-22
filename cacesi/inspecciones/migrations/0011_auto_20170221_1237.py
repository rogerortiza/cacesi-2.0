# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0010_auto_20170221_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='extintores',
            name='acciones_seguro',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='extintores',
            name='arreglo_seguro_sitio',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extintores',
            name='condicion_seguro',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='extintores',
            name='foto_seguro_antes',
            field=models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/seguro'),
        ),
        migrations.AddField(
            model_name='extintores',
            name='foto_seguro_despues',
            field=models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/seguro'),
        ),
        migrations.AddField(
            model_name='extintores',
            name='motivos_seguro',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='extintores',
            name='acciones_etiqueta',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='extintores',
            name='condicion_etiqueta',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='extintores',
            name='foto_etiqueta_antes',
            field=models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/etiqueta'),
        ),
        migrations.AlterField(
            model_name='extintores',
            name='foto_etiqueta_despues',
            field=models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/etiqueta'),
        ),
        migrations.AlterField(
            model_name='extintores',
            name='motivos_etiqueta',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='extintores',
            name='seguro',
            field=models.BooleanField(default=True),
        ),
    ]

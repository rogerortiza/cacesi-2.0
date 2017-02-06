# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0001_initial'),
        ('inventario_terceros', '0002_auto_20170127_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreasPorCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=140)),
                ('telefono', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteras.Clientes')),
            ],
        ),
        migrations.AlterField(
            model_name='extintores',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_terceros.AreasPorCliente'),
        ),
    ]

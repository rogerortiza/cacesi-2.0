# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_terceros', '0003_auto_20170131_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=140)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='areasporcliente',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='extintores',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_terceros.Areas'),
        ),
        migrations.DeleteModel(
            name='AreasPorCliente',
        ),
    ]
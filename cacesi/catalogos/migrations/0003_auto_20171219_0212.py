# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-19 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0004_remove_proveedores_giro'),
        ('catalogos', '0002_auto_20171114_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='areas',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carteras.Clientes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areas',
            name='responsable',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='areas',
            name='nombre',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterUniqueTogether(
            name='areas',
            unique_together=set([('cliente', 'nombre')]),
        ),
    ]

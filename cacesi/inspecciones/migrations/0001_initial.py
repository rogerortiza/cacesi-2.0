# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-12 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plantilla', '__first__'),
        ('inventario_terceros', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(choices=[('01', 'Enero'), ('02', 'Febero'), ('03', 'Marzo')], max_length=10)),
                ('año', models.CharField(default=2017, max_length=4)),
                ('fecha_asignacion', models.DateField(default=django.utils.timezone.now)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantilla.Empleados')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
            },
        ),
        migrations.CreateModel(
            name='Extintores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_revision', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('En su lugar', 'En su lugar'), ('No Encontrado', 'No Encontrado'), ('Reemplazado por caducidad', 'Reemplazado por caducidad'), ('Reemplazado por daño', 'Reemplazado por daño'), ('Reemplazado por falta de presion', 'Reemplazado por falta de presion'), ('Sin acceso al area', 'Sin acceso al area')], max_length=140)),
                ('etiqueta', models.BooleanField(default=True)),
                ('condicion_etiqueta', models.TextField(blank=True)),
                ('foto_etiqueta_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/etiqueta')),
                ('acciones_etiqueta', models.TextField(blank=True)),
                ('foto_etiqueta_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/etiqueta')),
                ('arreglo_etiqueta_sitio', models.BooleanField()),
                ('motivos_etiqueta', models.TextField(blank=True)),
                ('seguro', models.BooleanField(default=True)),
                ('condicion_seguro', models.TextField(blank=True)),
                ('foto_seguro_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/seguro')),
                ('acciones_seguro', models.TextField(blank=True)),
                ('foto_seguro_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/seguro')),
                ('arreglo_seguro_sitio', models.BooleanField()),
                ('motivos_seguro', models.TextField(blank=True)),
                ('pintura', models.BooleanField(default=True)),
                ('condicion_pintura', models.TextField(blank=True)),
                ('foto_pintura_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/pintura')),
                ('acciones_pintura', models.TextField(blank=True)),
                ('foto_pintura_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/pintura')),
                ('arreglo_pintura_sitio', models.BooleanField()),
                ('motivos_pintura', models.TextField(blank=True)),
                ('valvula', models.BooleanField(default=True)),
                ('condicion_valvula', models.TextField(blank=True)),
                ('foto_valvula_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/valvula')),
                ('acciones_valvula', models.TextField(blank=True)),
                ('foto_valvula_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/valvula')),
                ('arreglo_valvula_sitio', models.BooleanField()),
                ('motivos_valvula', models.TextField(blank=True)),
                ('nanometro', models.BooleanField(default=True)),
                ('condicion_nanometro', models.TextField(blank=True)),
                ('foto_nanometro_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/nanometro')),
                ('acciones_nanometro', models.TextField(blank=True)),
                ('foto_nanometro_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/nanometro')),
                ('arreglo_nanometro_sitio', models.BooleanField()),
                ('motivos_nanometro', models.TextField(blank=True)),
                ('peso', models.BooleanField(default=True)),
                ('condicion_peso', models.TextField(blank=True)),
                ('foto_peso_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/peso')),
                ('acciones_peso', models.TextField(blank=True)),
                ('foto_peso_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/peso')),
                ('arreglo_peso_sitio', models.BooleanField()),
                ('motivos_peso', models.TextField(blank=True)),
                ('manguera', models.BooleanField(default=True)),
                ('condicion_manguera', models.TextField(blank=True)),
                ('foto_manguera_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/manguera')),
                ('acciones_manguera', models.TextField(blank=True)),
                ('foto_manguera_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/manguera')),
                ('arreglo_manguera_sitio', models.BooleanField()),
                ('motivos_manguera', models.TextField(blank=True)),
                ('senalamiento', models.BooleanField(default=True)),
                ('condicion_senalamiento', models.TextField(blank=True)),
                ('foto_senalamiento_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/senalamiento')),
                ('acciones_senalamiento', models.TextField(blank=True)),
                ('foto_senalamiento_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/senalamiento')),
                ('arreglo_senalamiento_sitio', models.BooleanField()),
                ('motivos_senalamiento', models.TextField(blank=True)),
                ('altura', models.BooleanField(default=True)),
                ('condicion_altura', models.TextField(blank=True)),
                ('foto_altura_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/altura')),
                ('acciones_altura', models.TextField(blank=True)),
                ('foto_altura_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/altura')),
                ('arreglo_altura_sitio', models.BooleanField()),
                ('motivos_altura', models.TextField(blank=True)),
                ('proteccion', models.BooleanField(default=True)),
                ('condicion_proteccion', models.TextField(blank=True)),
                ('foto_proteccion_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/proteccion')),
                ('acciones_proteccion', models.TextField(blank=True)),
                ('foto_proteccion_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/proteccion')),
                ('arreglo_proteccion_sitio', models.BooleanField()),
                ('motivos_proteccion', models.TextField(blank=True)),
                ('limpieza', models.BooleanField(default=True)),
                ('condicion_limpieza', models.TextField(blank=True)),
                ('foto_limpieza_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/limpieza')),
                ('acciones_limpieza', models.TextField(blank=True)),
                ('foto_limpieza_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/limpieza')),
                ('arreglo_limpieza_sitio', models.BooleanField()),
                ('motivos_limpieza', models.TextField(blank=True)),
                ('operable', models.BooleanField(default=True)),
                ('condicion_operable', models.TextField(blank=True)),
                ('foto_operable_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/operable')),
                ('acciones_operable', models.TextField(blank=True)),
                ('foto_operable_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/operable')),
                ('arreglo_operable_sitio', models.BooleanField()),
                ('motivos_operable', models.TextField(blank=True)),
                ('obstruido', models.BooleanField(default=True)),
                ('condicion_obstruido', models.TextField(blank=True)),
                ('foto_obstruido_antes', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/antes/obstruido')),
                ('acciones_obstruido', models.TextField(blank=True)),
                ('foto_obstruido_despues', models.ImageField(blank=True, upload_to='static/images/inspecciones/reportes/despues/obstruido')),
                ('arreglo_obstruido_sitio', models.BooleanField()),
                ('motivos_obstruido', models.TextField(blank=True)),
                ('observaciones', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='static/images/inspecciones/observaciones')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantilla.Empleados')),
                ('extintor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_terceros.Extintores')),
            ],
            options={
                'verbose_name': 'Inspeccion a Extintor',
                'verbose_name_plural': 'Inspecciones a Extintores',
            },
        ),
    ]

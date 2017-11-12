# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-12 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planos_Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('plano', models.FileField(blank=True, upload_to='static/files/planos')),
                ('cliente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='carteras.Clientes')),
            ],
            options={
                'verbose_name': 'Plano de Cliente',
                'verbose_name_plural': 'Planos de Clientes',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-14 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteras', '0002_planos_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='cp',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
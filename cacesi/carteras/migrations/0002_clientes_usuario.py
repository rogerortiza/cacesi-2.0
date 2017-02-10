# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carteras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

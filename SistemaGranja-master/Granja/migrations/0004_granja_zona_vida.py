# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZonaVida', '0001_initial'),
        ('Granja', '0003_remove_granja_zona_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='granja',
            name='zona_vida',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_granja_zonavida', to='ZonaVida.ZonaVida'),
        ),
    ]
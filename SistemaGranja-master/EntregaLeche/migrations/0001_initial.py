# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Granja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntregaLeche',
            fields=[
                ('id_ent_leche', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificacion entrega de leche')),
                ('volumen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaEntrega', models.DateTimeField(default=None)),
                ('placaVehiculo', models.CharField(max_length=10)),
                ('nombreConductor', models.CharField(max_length=140)),
                ('responsableEntrega', models.CharField(max_length=140)),
                ('temperaturaLeche', models.DecimalField(decimal_places=2, max_digits=4)),
                ('id_granja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_entrega_granja', to='Granja.Granja')),
            ],
            options={
                'ordering': ('id_ent_leche',),
            },
        ),
    ]
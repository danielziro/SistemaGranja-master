# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bovino', '0005_auto_20161003_0034'),
        ('ControlMastitis', '0001_initial'),
        ('Medicamento', '0001_initial'),
        ('ViaAplicacion', '0001_initial'),
        ('EstadoSanidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sanidad',
            fields=[
                ('id_sanidad', models.AutoField(primary_key=True, serialize=False)),
                ('peso_vivo_prom', models.DecimalField(decimal_places=2, max_digits=10)),
                ('evento', models.CharField(max_length=50)),
                ('dosis', models.IntegerField()),
                ('tiempo_retiro', models.IntegerField()),
                ('fecha_aplicacion', models.DateTimeField()),
                ('id_bovino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sanidad_bovino', to='Bovino.Bovino')),
                ('id_control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sanidad_control', to='ControlMastitis.ControlMastitis')),
                ('id_estado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='id_sanidad_estado', to='EstadoSanidad.EstadoSanidad')),
                ('id_medicamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='id_sanidad_medicamento', to='Medicamento.Medicamento')),
                ('id_via_apli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sanidad_via', to='ViaAplicacion.ViaAplicacion')),
            ],
            options={
                'ordering': ('id_sanidad',),
            },
        ),
    ]

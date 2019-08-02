# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 00:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bovino', '0005_auto_20161003_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlMastitis',
            fields=[
                ('id_control', models.AutoField(primary_key=True, serialize=False)),
                ('cad', models.BooleanField()),
                ('cai', models.BooleanField()),
                ('cpd', models.BooleanField()),
                ('cpi', models.BooleanField()),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de control')),
                ('id_bovino', models.ManyToManyField(related_name='id_control_bovino', to='Bovino.Bovino')),
            ],
            options={
                'ordering': ('id_control',),
            },
        ),
    ]

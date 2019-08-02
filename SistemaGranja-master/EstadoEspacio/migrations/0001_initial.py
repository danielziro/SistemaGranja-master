# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoEspacio',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('id_estado',),
            },
        ),
    ]

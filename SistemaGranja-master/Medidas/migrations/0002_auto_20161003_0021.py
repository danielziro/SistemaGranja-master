# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 00:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medidas',
            options={'ordering': ('id_medida',)},
        ),
    ]

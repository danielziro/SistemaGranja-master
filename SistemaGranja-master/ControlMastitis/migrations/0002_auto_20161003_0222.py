# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bovino', '0005_auto_20161003_0034'),
        ('ControlMastitis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlmastitis',
            name='id_bovino',
        ),
        migrations.AddField(
            model_name='controlmastitis',
            name='id_bovino',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_control_bovino', to='Bovino.Bovino'),
        ),
    ]
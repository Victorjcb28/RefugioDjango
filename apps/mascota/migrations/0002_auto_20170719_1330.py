# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='vacunas',
            new_name='vacuna',
        ),
    ]
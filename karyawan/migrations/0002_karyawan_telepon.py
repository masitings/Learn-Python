# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='telepon',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('Jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Jabatan')),
            ],
        ),
        migrations.CreateModel(
            name='Pendidikan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='karyawan',
            name='Pendidikan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Pendidikan'),
        ),
    ]

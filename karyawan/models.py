# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pendidikan(models.Model):
	nama = models.CharField(max_length=50)
	keterangan = models.CharField(max_length=50)
	def __str__(self):
		return self.nama

class Jabatan(models.Model):
	nama = models.CharField(max_length=50)
	keterangan = models.CharField(max_length=50)
	def __str__(self):
		return self.nama

class Karyawan(models.Model):
	nama = models.CharField(max_length=50)
	Pendidikan = models.ForeignKey(Pendidikan, on_delete=models.CASCADE)
	Jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
	telepon = models.CharField(max_length=50)
	def __str__(self):
		return self.nama


		
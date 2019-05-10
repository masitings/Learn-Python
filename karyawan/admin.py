# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class KaryawanAdmin(admin.ModelAdmin):
	# Sesuai dengan class Karyawan (di model)
	list_display = ('nama', 'Jabatan', 'Pendidikan')

admin.site.register(Jabatan)
admin.site.register(Pendidikan)
admin.site.register(Karyawan, KaryawanAdmin)
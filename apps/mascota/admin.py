# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import #importarlo para las llaves foraneas

from django.contrib import admin
from apps.mascota.models import Vacuna,Mascota

# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Mascota)
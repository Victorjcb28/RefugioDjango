# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import #importarlo para las llaves foraneas

from django.contrib import admin
from apps.adopcion.models import Persona

# Register your models here.
admin.site.register(Persona)

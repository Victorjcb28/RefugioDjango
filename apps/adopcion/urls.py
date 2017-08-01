from __future__ import absolute_import #importarlo para las llaves foraneas
from django.conf.urls import url

from apps.adopcion.views import index_adopcion

urlpatterns = [
    url(r'^$',index_adopcion),
]
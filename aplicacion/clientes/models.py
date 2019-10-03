from django.db import models
from django.utils.translation import gettext_lazy as _

from aplicacion.geolocalizacion.models import Ciudad, Barrio
from aplicacion.utilidades.models import Auditoria, PersonaBase


class Cliente(Auditoria, PersonaBase):
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True, verbose_name=_('ciudad'), on_delete=models.SET_NULL)
    barrio = models.ForeignKey(Barrio, null=True, blank=True, verbose_name=_('barrio'), on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre_completo

from django.db import models
from django.utils.translation import gettext_lazy as _

from aplicacion.utilidades.models import Auditoria


class Pais(Auditoria):
    nombre = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('nombre'))

    class Meta:
        verbose_name = _('país')
        verbose_name_plural = _('países')

    def __str__(self):
        return self.nombre


class Departamento(Auditoria):
    nombre = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('nombre'))
    pais = models.ForeignKey(Pais, null=True, blank=False, verbose_name=_('país'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('departamento')
        verbose_name_plural = _('departamentos')

    def __str__(self):
        return self.nombre


class Ciudad(Auditoria):
    nombre = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('nombre'))
    departamento = models.ForeignKey(Departamento, null=True, blank=False, verbose_name=_('departamento'),
                                     on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('ciudad')
        verbose_name_plural = _('ciudades')

    def __str__(self):
        return self.nombre


class Barrio(Auditoria):
    nombre = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('nombre'))
    ciudad = models.ForeignKey(Ciudad, null=True, blank=False, verbose_name=_('ciudad'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('barrio')
        verbose_name_plural = _('barrios')

    def __str__(self):
        return self.nombre

from django.db import models

# Create your models here.
from aplicacion.clientes.models import Cliente
from aplicacion.utilidades.models import Auditoria


class Ruta(Auditoria):
    nombre_ruta = models.CharField(max_length=20, null=False, blank=False, verbose_name=('nombre de la ruta'))
    clientes = models.ManyToManyField(Cliente, related_name='ruta_cliente')

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'

    def __str__(self):
        return self.nombre_ruta


class Zona(Auditoria):
    nombre = models.CharField(max_length=20, null=False, blank=False, verbose_name=('nombre de la zona'))
    rutas = models.ManyToManyField(Ruta, related_name='zona_ruta')

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return self.nombre

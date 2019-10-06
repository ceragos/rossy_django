from django.db import models
from django.utils.translation import gettext_lazy as _

from aplicacion.utilidades.models import Auditoria


class UnidadMedida(Auditoria):
    nombre = models.CharField(max_length=10, null=False, blank=False, verbose_name=_('nombre'))
    abreviatura = models.CharField(max_length=3, null=False, blank=False, verbose_name=_('abreviatura'))

    class Meta:
        verbose_name = _('unidad de medida')
        verbose_name_plural = _('unidades de medida')

    def __str__(self):
        return self.abreviatura


class Insumo(Auditoria):
    nombre = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('nombre'))
    cantidad = models.IntegerField(null=True, blank=False, verbose_name=_('cantidad'))
    unidad_medida = models.ForeignKey(UnidadMedida, null=True, blank=False, verbose_name=_('unidad de medida'),
                                      on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('insumo')
        verbose_name_plural = _('insumos')

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.cantidad, self.unidad_medida.abreviatura)


class InventarioInsumo(Auditoria):
    insumo = models.ForeignKey(Insumo, null=False, blank=False, verbose_name=_('insumo'), on_delete=models.PROTECT)
    unidades = models.IntegerField(null=True, blank=True, verbose_name=_('unidades'))
    precio_unitario = models.IntegerField(null=True, blank=True, verbose_name=_('precio unitario'))


class Producto(Auditoria):
    nombre = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('nombre'))
    descripcion = models.TextField(null=True, blank=True, verbose_name=_('descripción'))


class InventarioProducto(Auditoria):
    producto = models.ForeignKey(Producto, null=False, blank=False, verbose_name=_('producto'),
                                 on_delete=models.PROTECT)
    unidades = models.IntegerField(null=True, blank=True, verbose_name=_('unidades'))
    unidad_medida = models.ForeignKey(UnidadMedida, null=True, blank=False, verbose_name=_('unidad de medida'),
                                      on_delete=models.SET_NULL)
    precio_costo = models.IntegerField(null=True, blank=True, verbose_name=_('precio de costo'))
    precio_venta = models.IntegerField(null=False, blank=False, verbose_name=_('precio de venta'))
    fecha_elaboracion = models.DateField(null=False, blank=False, verbose_name=_('fecha de elaboración'))
    fecha_vencimiento = models.DateField(null=False, blank=False, verbose_name=_('fecha de vencimiento'))
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

class Marca(Auditoria):
    nombre = models.CharField(max_length=10, null=False, blank=False, verbose_name=_('nombre'))

    class Meta:
        verbose_name = _('marca')
        verbose_name_plural = _('marcas')

    def __str__(self):
        return self.nombre


class Insumo(Auditoria):
    nombre = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('nombre'))
    descripcion = models.TextField(null=True, blank=True, verbose_name=_('descripción'))

    class Meta:
        verbose_name = _('insumo')
        verbose_name_plural = _('insumos')

    def __str__(self):
        return self.nombre


class InsumoDetallado(Auditoria):
    insumo = models.ForeignKey(Insumo, null=False, blank=False, verbose_name=_('insumo'), on_delete=models.PROTECT,
                               related_name='insumo_detallado_insumo')
    cantidad = models.IntegerField(null=False, blank=False, verbose_name=_('cantidad'))
    unidad_medida = models.ForeignKey(UnidadMedida, null=False, blank=False, verbose_name=_('unidad de medida'),
                                      on_delete=models.PROTECT, related_name='insumo_detallado_unidad_medida')
    marca = models.ForeignKey(Marca, null=False, blank=False, verbose_name=_('marca'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('producto detallado')
        verbose_name_plural = _('productos detallados')

    def __str__(self):
        return '{} {} {} {}'.format(self.insumo, self.marca, self.cantidad, self.unidad_medida)


class CompraInsumo(Auditoria):
    insumo_detallado = models.ForeignKey(InsumoDetallado, null=False, blank=False, verbose_name=_('insumo detallado'),
                                         on_delete=models.PROTECT, related_name='compra_insumo_insumo_detallado')
    unidades = models.IntegerField(null=False, blank=False, verbose_name=_('unidades'))
    precio_unitario = models.IntegerField(null=False, blank=False, verbose_name=_('precio unitario'))
    valor_compra = models.IntegerField(null=True, blank=True, verbose_name=_('valor de la compra'))

    class Meta:
        verbose_name = _('compra de insumo')
        verbose_name_plural = _('compras de insumos')

    def __str__(self):
        return self.insumo_detallado

    def save(self, *args, **kwargs):

        # El valor de la compra es la multiplicacion del precio unitario por el numero de unidades
        self.valor_compra = self.unidades * self.precio_unitario

        super(CompraInsumo, self).save(*args, **kwargs)


class Producto(Auditoria):
    nombre = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('nombre'))
    descripcion = models.TextField(null=True, blank=True, verbose_name=_('descripción'))

    class Meta:
        verbose_name = _('producto')
        verbose_name_plural = _('productos')

    def __str__(self):
        return self.nombre


class ProductoDetallado(Auditoria):
    producto = models.ForeignKey(Producto, null=False, blank=False, verbose_name=_('producto'),
                                 on_delete=models.PROTECT, related_name='producto_detallado_producto')
    cantidad = models.IntegerField(null=True, blank=True, verbose_name=_('cantidad'))
    unidad_medida = models.ForeignKey(UnidadMedida, null=True, blank=False, verbose_name=_('unidad de medida'),
                                      on_delete=models.SET_NULL, related_name='producto_detallado_unidad_medida')
    precio_venta = models.IntegerField(null=False, blank=False, verbose_name=_('precio de venta'))
    unidades_disponibles = models.IntegerField(null=True, blank=True, verbose_name=_('unidades disponibles'), default=0)

    class Meta:
        verbose_name = _('producto detallado')
        verbose_name_plural = _('productos detallados')

    def __str__(self):
        return '{} {} {}'.format(self.producto, self.cantidad, self.unidad_medida)


class ProduccionProducto(Auditoria):
    lote = models.IntegerField(null=False, blank=False, verbose_name=_('lote'))
    producto_detallado = models.ForeignKey(ProductoDetallado, null=False, blank=False, verbose_name=_('producto'),
                                           on_delete=models.PROTECT,
                                           related_name='produccion_producto_producto_detallado')
    unidades_producidas = models.IntegerField(null=True, blank=True, verbose_name=_('unidades producidas'))
    precio_costo = models.IntegerField(null=True, blank=True, verbose_name=_('precio de costo'))
    fecha_elaboracion = models.DateField(null=False, blank=False, verbose_name=_('fecha de elaboración'))
    fecha_vencimiento = models.DateField(null=False, blank=False, verbose_name=_('fecha de vencimiento'))

    class Meta:
        verbose_name = _('producción de producto')
        verbose_name_plural = _('producción de productos')

    def __str__(self):
        return self.producto_detallado

    def save(self, *args, **kwargs):
        # Si la producción se esta creando:
        if self._state.adding:

            # El numero de lote sera el consecutivo del anterior, del mismo producto
            self.lote = self.objects.all().order_by('-fecha_creacion').first().lote + 1

            # El guardado incrementa el numero de unidades, a el numero de productos disponibles
            self.producto_detallado.unidades_disponibles += self.unidades_producidas

        super(ProduccionProducto, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        # El eliminado descuenta el numero de unidades, del numero de productos disponibles
        self.producto_detallado.unidades_disponibles -= self.unidades_producidas

        super(ProduccionProducto, self).delete()

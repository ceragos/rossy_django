from datetime import date

from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
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
    cantidad = models.PositiveIntegerField(null=False, blank=False, verbose_name=_('cantidad'))
    unidad_medida = models.ForeignKey(UnidadMedida, null=False, blank=False, verbose_name=_('unidad de medida'),
                                      on_delete=models.PROTECT, related_name='insumo_detallado_unidad_medida')
    marca = models.ForeignKey(Marca, null=False, blank=False, verbose_name=_('marca'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('insumo detallado')
        verbose_name_plural = _('insumos detallados')

    def __str__(self):
        return '{} {} {} {}'.format(self.insumo, self.marca, self.cantidad, self.unidad_medida)


class CompraInsumo(Auditoria):
    insumo_detallado = models.ForeignKey(InsumoDetallado, null=False, blank=False, verbose_name=_('insumo detallado'),
                                         on_delete=models.PROTECT, related_name='compra_insumo_insumo_detallado')
    unidades = models.PositiveIntegerField(null=False, blank=False, verbose_name=_('unidades'))
    precio_unitario = models.PositiveIntegerField(null=False, blank=False, verbose_name=_('precio unitario'))
    valor_compra = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('valor de la compra'))

    class Meta:
        verbose_name = _('compra de insumo')
        verbose_name_plural = _('compras de insumos')

    def __str__(self):
        return '{}'.format(self.insumo_detallado)

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
    cantidad = models.PositiveIntegerField(null=False, blank=False, verbose_name=_('cantidad'))
    unidad_medida = models.ForeignKey(UnidadMedida, null=True, blank=False, verbose_name=_('unidad de medida'),
                                      on_delete=models.SET_NULL, related_name='producto_detallado_unidad_medida')
    precio_venta = models.PositiveIntegerField(null=False, blank=False, verbose_name=_('precio de venta'))
    unidades_disponibles = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('unidades disponibles'), default=0)

    class Meta:
        verbose_name = _('producto detallado')
        verbose_name_plural = _('productos detallados')

    def __str__(self):
        return '{} por {} {}'.format(self.producto, self.cantidad, self.unidad_medida)


class ProduccionProducto(Auditoria):
    lote = models.IntegerField(null=False, blank=False, verbose_name=_('lote'), default=0)
    producto_detallado = models.ForeignKey(ProductoDetallado, null=False, blank=False, verbose_name=_('producto'),
                                           on_delete=models.PROTECT,
                                           related_name='produccion_producto_producto_detallado')
    unidades_producidas = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('unidades producidas'))
    unidades_vendidas = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('unidades vendidas'),
                                                    default=0)
    unidades_vencidas = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('unidades vencidas'),
                                                    default=0)
    precio_costo = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('precio de costo'))
    fecha_elaboracion = models.DateField(null=False, blank=False, verbose_name=_('fecha de elaboración'))
    fecha_vencimiento = models.DateField(null=False, blank=False, verbose_name=_('fecha de vencimiento'))
    lote_agotado = models.BooleanField(default=False, verbose_name=_('lote agotado'))

    class Meta:
        verbose_name = _('producción de producto')
        verbose_name_plural = _('producción de productos')

    def __str__(self):
        return '{}'.format(self.producto_detallado)

    @property
    def vencido(self):
        if self.fecha_vencimiento < date.today():
            return True

    def save(self, *args, **kwargs):
        # Si la producción se esta creando:
        if self._state.adding:

            # El numero de lote sera el consecutivo del anterior, del mismo producto
            produccion = ProduccionProducto.objects\
                            .filter(producto_detallado=self.producto_detallado)\
                            .order_by('-lote')\
                            .first()

            self.lote = (produccion.lote + 1) if produccion else 1

            producto_detallado = ProductoDetallado.objects.get(id=self.producto_detallado.id)

            # El guardado incrementa el numero de unidades, a el numero de productos disponibles
            producto_detallado.unidades_disponibles += self.unidades_producidas
            producto_detallado.save()

        super(ProduccionProducto, self).save(*args, **kwargs)

@receiver(pre_delete, sender=ProduccionProducto)
def produccion_producto_delete_handler(sender, instance, **kwargs):
    producto_detallado = ProductoDetallado.objects.get(id=instance.producto_detallado.id)

    # El eliminado de producto venta incrementa el numero de unidades, a el numero de productos disponibles
    producto_detallado.unidades_disponibles -= instance.unidades_producidas
    producto_detallado.save()


@receiver(post_save, sender=ProduccionProducto)
def produccion_producto_save_handler(sender, instance, **kwargs):
    if instance.unidades_vendidas > instance.unidades_producidas:
        print("lote: {} estado: {}, unidades vendidas: {}, unidades producidas: {}".format(instance.lote,
                                                                                           instance.lote_agotado,
                                                                                           instance.unidades_vendidas,
                                                                                           instance.unidades_producidas))
        # Si la cantidad de unidades vendidas es mayor a la del lote, se toman las unidades disponibles del
        # siguiente lote y se marca el actual como agotado lote: 3 unidades vendidas: 4, unidades producidas: 3

        unidades_revasadas = instance.unidades_vendidas - instance.unidades_producidas
        instance.unidades_vendidas = instance.unidades_producidas

        proxima_produccion = ProduccionProducto.objects \
            .filter(producto_detallado=instance.producto_detallado, lote_agotado=False) \
            .order_by('fecha_vencimiento').first()

        proxima_produccion.unidades_vendidas = unidades_revasadas

        if proxima_produccion.unidades_vendidas >= proxima_produccion.unidades_producidas:
            proxima_produccion.lote_agotado = True

        proxima_produccion.save()
        instance.save()

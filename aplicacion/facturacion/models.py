from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

# Create your models here.
from aplicacion.bodega.models import ProductoDetallado
from aplicacion.clientes.models import Cliente
from aplicacion.utilidades.models import Auditoria


class Factura(Auditoria):
    fecha_compra = models.DateTimeField(null=False, blank=False, verbose_name=_('fecha de compra'))
    cliente = models.ForeignKey(Cliente, null=False, blank=False, verbose_name=_('cliente'), on_delete=models.PROTECT)
    contado = models.BooleanField(default=False, verbose_name=_('contado'))
    credito = models.BooleanField(default=False, verbose_name=_('credito'))
    pagada = models.BooleanField(default=False, verbose_name=_('pagada'))
    fecha_pago = models.DateField(null=True, blank=True, verbose_name=_('fecha de pago'),
                                  help_text=_('Uselo solo si selecciono crédito como método de pago.'))
    total = models.IntegerField(null=True, blank=True, verbose_name=_('total de la factura'), default=0)

    class Meta:
        verbose_name = _('factura')
        verbose_name_plural = _('facturas')

    def __str__(self):
        return "Factura: {} - Cliente: {} {} {} - Fecha: {}".format(self.factura_numero,
                                                                    self.cliente.numero_identificacion,
                                                                    self.cliente.primer_nombre,
                                                                    self.cliente.primer_apellido,
                                                                    self.fecha_compra)

    @property
    def factura_numero(self):
        completar_numero_factura = 6 - len(str(self.id))
        ceros = completar_numero_factura * '0'
        return '{}{}'.format(ceros, self.id)

    @property
    def abonos_pagados(self):
        if self.contado:
            return self.total
        elif self.credito:
            total_abonos = 0
            for abono in self.abono_credito_factura.all():
                total_abonos += abono.valor_abono
            return total_abonos

    def clean(self, *args, **kwargs):

        if self.contado and self.credito:
            raise ValidationError({'contado': ["Solo puede seleccionar una opcion (Credito / Contado)",],
                                   'credito': ["Solo puede seleccionar una opcion (Credito / Contado)", ]})

        if self.fecha_pago is not None and self.contado:
            raise ValidationError({'fecha_pago': ["Solo disponible para pagos a credito", ]})

    def save(self, *args, **kwargs):
        if self.contado:
            self.pagada = True
        super(Factura, self).save(*args, **kwargs)


class ProductoVenta(Auditoria):
    factura = models.ForeignKey(Factura, null=False, blank=False, verbose_name=_('factura'), on_delete=models.PROTECT,
                                related_name='producto_venta_factura')
    producto_detallado = models.ForeignKey(ProductoDetallado, null=False, blank=False,
                                           verbose_name=_('producto detallado'), on_delete=models.PROTECT,
                                           related_name='producto_venta_producto_detallado')
    unidades_vendidas = models.PositiveIntegerField(null=False, blank=False, verbose_name=_('unidades vendidas'))
    precio_venta = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('precio de venta'), default=0)
    valor_venta = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('valor de la venta'), default=0)

    class Meta:
        verbose_name = _('producto vendido')
        verbose_name_plural = _('productos vendidos')

    def __str__(self):
        return '{}'.format(self.producto_detallado)

    @property
    def factura_numero(self):
        completar_numero_factura = 6-len(str(self.factura.id))
        ceros = completar_numero_factura * '0'
        return '{}{}'.format(ceros, self.factura.id)

    def clean(self, *args, **kwargs):

        if self.producto_detallado.unidades_disponibles <= 0:
            raise ValidationError({'producto_detallado': ["Este producto se encuentra agotado en el sistema.",]})

        if self.producto_detallado.unidades_disponibles < self.unidades_vendidas:
            raise ValidationError({'producto_detallado': ["Solo hay {} {} disponibles.".format(
                self.producto_detallado.unidades_disponibles,
                self.producto_detallado.unidad_medida.nombre
            ), ]})

    def save(self, *args, **kwargs):
        if self._state.adding:
            # El precio de venta que quedara registrado en la factura es el precio de venta actual del producto
            self.precio_venta = self.producto_detallado.precio_venta

            # Valor de venta del producto
            self.valor_venta = self.precio_venta * self.unidades_vendidas

            producto_detallado = ProductoDetallado.objects.get(id=self.producto_detallado.id)

            # El guardado de producto venta decrementa el numero de unidades, a el numero de productos disponibles
            producto_detallado.unidades_disponibles -= self.unidades_vendidas
            producto_detallado.save()

            factura = Factura.objects.get(id=self.factura.id)
            factura.total += self.valor_venta
            factura.save()

        super(ProductoVenta, self).save(*args, **kwargs)


@receiver(pre_delete, sender=ProductoVenta)
def producto_venta_delete_handler(sender, instance, **kwargs):
    producto_detallado = ProductoDetallado.objects.get(id=instance.producto_detallado.id)

    # El eliminado de producto venta incrementa el numero de unidades, a el numero de productos disponibles
    producto_detallado.unidades_disponibles += instance.unidades_vendidas
    producto_detallado.save()


class FacturaCreditoManager(models.Manager):
    def get_queryset(self):
        return super(FacturaCreditoManager, self).get_queryset().filter(credito=True).exclude(pagada=True)


class FacturaCredito(Factura):
    class Meta:
        proxy = True
        verbose_name = 'Credito'
        verbose_name_plural = 'Creditos'

    objects = FacturaCreditoManager()


class AbonoCredito(Auditoria):
    factura = models.ForeignKey(Factura, null=False, blank=False, verbose_name=_('factura'), on_delete=models.PROTECT,
                                related_name='abono_credito_factura')
    fecha_abono = models.DateTimeField(null=False, blank=False, verbose_name=_('fecha del abono'))
    valor_abono = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('valor del abono'))

    class Meta:
        verbose_name = 'Abono del crédito'
        verbose_name_plural = 'Abonos del crédito'

    def __str__(self):
        return '{} {}'.format(self.factura.factura_numero,
                              self.factura.cliente.primer_nombre,
                              self.factura.cliente.primer_apellido)

    @property
    def factura_numero(self):
        completar_numero_factura = 6 - len(str(self.factura.id))
        ceros = completar_numero_factura * '0'
        return '{}{}'.format(ceros, self.factura.id)


@receiver(post_save, sender=AbonoCredito)
def abono_credito_save_handler(sender, instance, **kwargs):
    factura = Factura.objects.get(id=instance.factura.id)
    abonos = AbonoCredito.objects.filter(factura=instance.factura)

    total_abonos = 0
    for abono in abonos:
        total_abonos += abono.valor_abono

    if total_abonos == factura.total:
        factura.pagada = True
        factura.save()

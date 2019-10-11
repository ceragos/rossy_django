from django.contrib import admin

from aplicacion.facturacion.models import Factura, ProductoVenta, FacturaCredito, AbonoCredito
from aplicacion.utilidades.admin import AdminModel


class ProductoVentaInline(admin.StackedInline):
    model = ProductoVenta
    fk_name = 'factura'
    fieldsets = (
        ('', {
            'fields': ('producto_detallado', 'unidades_vendidas', 'precio_venta', 'valor_venta')
        }),
    )
    readonly_fields = ['precio_venta', 'valor_venta']
    extra = 1
    can_delete = False


class AbonoCreditoInline(admin.StackedInline):
    model = AbonoCredito
    fk_name = 'factura'
    fieldsets = (
        ('', {
            'fields': ('fecha_abono', 'valor_abono',)
        }),
    )
    extra = 1
    can_delete = False


@admin.register(Factura)
class FacturaAdmin(AdminModel):
    search_fields = ['cliente__numero_identificacion']
    list_filter = ['contado', 'credito', 'pagada']
    list_display = ['factura_numero', 'fecha_compra', 'cliente', 'contado', 'credito', 'pagada', 'total',
                    'abonos_pagados']
    fieldsets = (
        ('Forma de Pago', {
            'fields': ('contado', 'credito', 'fecha_pago')
        }),
        ('Información de la Factura', {
            'fields': ('fecha_compra', 'cliente', 'total')
        }),
    )
    readonly_fields = ['total',
                       'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']
    inlines = [ProductoVentaInline]


@admin.register(ProductoVenta)
class ProductoVentaAdmin(AdminModel):
    search_fields = ['factura__cliente__numero_identificacion']
    list_filter = ['producto_detallado', 'producto_detallado__producto']
    list_display = ['factura_numero', 'producto_detallado','unidades_vendidas', 'precio_venta', 'valor_venta']
    fieldsets = (
        ('Información de Venta del Producto', {
            'fields': ('factura', 'producto_detallado', 'unidades_vendidas', 'precio_venta', 'valor_venta')
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )
    readonly_fields = ['precio_venta', 'valor_venta',
                       'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']


@admin.register(FacturaCredito)
class FacturaCreditoAdmin(AdminModel):
    search_fields = ['cliente__numero_identificacion']
    list_display = ['factura_numero', 'fecha_pago', 'fecha_compra', 'cliente', 'total', 'abonos_pagados']
    fieldsets = (
        ('Forma de Pago', {
            'fields': ('credito', 'fecha_pago')
        }),
        ('Información de la Factura', {
            'fields': ('pagada', 'fecha_compra', 'cliente', 'total')
        }),
    )
    readonly_fields = ['credito', 'pagada', 'fecha_pago', 'fecha_compra', 'cliente', 'total',
                       'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']
    inlines = [AbonoCreditoInline]


@admin.register(AbonoCredito)
class AbonoCreditoAdmin(AdminModel):
    search_fields = ['factura__cliente__numero_identificacion']
    list_display = ['factura_numero', 'fecha_abono', 'valor_abono',]
    fieldsets = (
        ('Información del Abono', {
            'fields': ('fecha_abono', 'valor_abono',)
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )
    readonly_fields = ['creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']
from django.contrib import admin
from easy_select2 import select2_modelform

from aplicacion.bodega.models import Insumo, Producto, UnidadMedida, Marca, \
    InsumoDetallado, CompraInsumo, ProductoDetallado, ProduccionProducto
from aplicacion.utilidades.admin import AdminModel


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(AdminModel):
    list_display = ['nombre', 'abreviatura', 'creado_por', 'fecha_creacion', 'modificado_por', 'fecha_modificacion']
    fieldsets = (
        ('Unidad de Medida', {
            'fields': ('nombre', 'abreviatura')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Marca)
class MarcaAdmin(AdminModel):
    list_display = ['nombre', 'creado_por', 'fecha_creacion', 'modificado_por', 'fecha_modificacion']
    fieldsets = (
        ('Marca', {
            'fields': ('nombre',)
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Insumo)
class InsumoAdmin(AdminModel):
    search_fields = ['nombre']
    fieldsets = (
        ('Información del Insumo', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(InsumoDetallado)
class InsumoDetalladoAdmin(AdminModel):
    search_fields = ['insumo__nombre']
    list_display = ['insumo', 'marca', 'cantidad', 'unidad_medida']
    fieldsets = (
        ('Información del Insumo', {
            'fields': ('insumo', 'marca', 'cantidad', 'unidad_medida')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(CompraInsumo)
class CompraInsumoAdmin(AdminModel):
    search_fields = ['insumo_detallado__insumo__nombre']
    list_display = ['insumo_detallado', 'unidades', 'precio_unitario', 'valor_compra']
    fieldsets = (
        ('Información de la Compra', {
            'fields': ('insumo_detallado', 'unidades', 'precio_unitario', 'valor_compra')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )
    readonly_fields = ['valor_compra',
                       'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']


@admin.register(Producto)
class ProductoAdmin(AdminModel):
    search_fields = ['nombre',]
    list_display = ['nombre', 'creado_por', 'fecha_creacion', 'modificado_por', 'fecha_modificacion']
    fieldsets = (
        ('Información del Producto', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(ProductoDetallado)
class ProductoDetalladoAdmin(AdminModel):
    search_fields = ['producto__nombre']
    list_display = ['producto', 'cantidad', 'unidad_medida', 'precio_venta', 'unidades_disponibles']
    fieldsets = (
        ('Información del Producto', {
            'fields': ('producto', 'cantidad', 'unidad_medida', 'precio_venta', 'unidades_disponibles')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )
    readonly_fields = ['unidades_disponibles',
                       'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']
    form = select2_modelform(ProductoDetallado, attrs={'width': '220px'})


@admin.register(ProduccionProducto)
class ProduccionProductoAdmin(AdminModel):
    search_fields = ['producto_detallado__producto__nombre']
    list_display = ['producto_detallado', 'lote', 'unidades_producidas', 'unidades_vendidas', 'precio_costo', 'fecha_elaboracion',
                    'fecha_vencimiento']
    fieldsets = (
        ('Información de la Producción', {
            'fields': ('lote', 'producto_detallado', 'unidades_producidas', 'precio_costo', 'fecha_elaboracion',
                       'fecha_vencimiento')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )
    readonly_fields = ['lote',
                       'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']
    form = select2_modelform(ProduccionProducto, attrs={'width': '220px'})

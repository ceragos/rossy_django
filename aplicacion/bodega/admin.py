from django.contrib import admin

from aplicacion.bodega.models import Insumo, InventarioInsumo, Producto, InventarioProducto, UnidadMedida
from aplicacion.utilidades.admin import AdminModel


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(AdminModel):
    fieldsets = (
        ('Unidad de Medida', {
            'fields': ('nombre', 'abreviatura')
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Insumo)
class InsumoAdmin(AdminModel):
    search_fields = ['nombre']
    fieldsets = (
        ('Información del Insumo', {
            'fields': ('nombre', 'cantidad', 'unidad_medida')
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(InventarioInsumo)
class InventarioInsumoAdmin(AdminModel):
    search_fields = ['insumo__nombre']
    fieldsets = (
        ('Inventario de Insumos', {
            'fields': ('insumo', 'unidades', 'precio_unitario')
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Producto)
class ProductoAdmin(AdminModel):
    search_fields = ['nombre']
    fieldsets = (
        ('Información del Producto', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(InventarioProducto)
class InventarioProductoAdmin(AdminModel):
    search_fields = ['producto__nombre']
    fieldsets = (
        ('Inventario de Productos', {
            'fields': ('producto', 'unidades', 'unidad_medida', 'fecha_elaboracion',
                       'fecha_vencimiento')
        }),
        ('Precio y costo por unidad', {
            'fields': ('precio_costo', 'precio_venta')
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )

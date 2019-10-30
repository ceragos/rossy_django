from django.contrib import admin

from aplicacion.rutas.models import Ruta, Zona
from aplicacion.utilidades.admin import AdminModel


@admin.register(Ruta)
class RutaAdmin(AdminModel):
    filter_horizontal = ['clientes']
    list_filter = ['zona_ruta']
    fieldsets = (
        ('Información de la Ruta', {
            'fields': ('nombre_ruta', 'clientes',)
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Zona)
class ZonaAdmin(AdminModel):
    filter_horizontal = ['rutas']
    fieldsets = (
        ('Información de la Ruta', {
            'fields': ('nombre', 'rutas',)
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )

from django.contrib import admin

from aplicacion.geolocalizacion.models import Pais, Departamento, Ciudad, Barrio
from aplicacion.utilidades.admin import AdminModel


@admin.register(Pais)
class PaisAdmin(AdminModel):
    fieldsets = (
        ('País', {
            'fields': ('nombre',)
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Departamento)
class DepartamentoAdmin(AdminModel):
    fieldsets = (
        ('Departamento', {
            'fields': ('nombre', 'pais')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Ciudad)
class CiudadAdmin(AdminModel):
    fieldsets = (
        ('Ciudad', {
            'fields': ('nombre', 'departamento')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )


@admin.register(Barrio)
class BarrioAdmin(AdminModel):
    fieldsets = (
        ('Barrio', {
            'fields': ('nombre', 'ciudad')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )

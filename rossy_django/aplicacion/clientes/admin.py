from django.contrib import admin

from aplicacion.clientes.models import Cliente
from aplicacion.utilidades.admin import AdminModel


@admin.register(Cliente)
class ClienteAdmin(AdminModel):
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('tipo_identificacion', 'numero_identificacion', 'nombres', 'apellidos', 'fecha_nacimiento',
                       'celular', 'ciudad', 'barrio', 'direccion')
        }),
        ('Auditoria', {
            'fields': ('activo', 'creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )

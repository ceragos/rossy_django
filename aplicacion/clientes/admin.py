from django.contrib import admin

from aplicacion.clientes.models import Cliente
from aplicacion.utilidades.admin import AdminModel


@admin.register(Cliente)
class ClienteAdmin(AdminModel):
    search_fields = ['numero_identificacion', 'nombres', 'apellidos']
    list_filter = ['ruta_cliente', 'ruta_cliente__zona_ruta']
    list_display = ('abbr_tipo_identificacion', 'numero_identificacion', 'nombre_completo', 'celular', 'ciudad', 'barrio',
                    'direccion')
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('tipo_identificacion', 'numero_identificacion', 'nombres', 'apellidos', 'fecha_nacimiento',
                       'celular', 'ciudad', 'barrio', 'direccion')
        }),
        ('Auditoria', {
            'fields': ('creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion')
        }),
    )

    def abbr_tipo_identificacion(self, obj):
        return obj.tipo_identificacion
    abbr_tipo_identificacion.short_description = 'tipo de identificacion'

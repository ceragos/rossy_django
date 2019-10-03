from django.contrib import admin


class AdminModel(admin.ModelAdmin):
    readonly_fields = ['creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']

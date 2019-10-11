from django.contrib import admin
from django.contrib.admin.models import LogEntry


class AdminModel(admin.ModelAdmin):
    readonly_fields = ['creado_por', 'fecha_creacion', 'ip_creacion',
                       'modificado_por', 'fecha_modificacion', 'ip_modificacion']


class LogEntryAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user',)
    list_display = ('action_flag', 'object_repr', 'content_type', 'user', 'action_time',)
    readonly_fields = ('content_type',
                       'user',
                       'action_time',
                       'object_id',
                       'object_repr',
                       'action_flag',
                       'change_message'
                       )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(LogEntry, LogEntryAdmin)
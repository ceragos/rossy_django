from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from aplicacion.usuarios.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    search_fields = ('email',)
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    UserAdmin.fieldsets = [
        ('Información del usuario', {'fields': ('foto_perfil',)})] + list(UserAdmin.fieldsets)

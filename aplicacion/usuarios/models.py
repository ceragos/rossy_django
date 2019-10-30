from datetime import datetime

from crum import get_current_user, get_current_request
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Usuario(AbstractUser):

    foto_perfil = models.ImageField(null=True, blank=True, verbose_name=_('foto de perfil'),
                                    upload_to='usuarios/foto_perfil')
    # Auditoria de creación
    creado_por = models.ForeignKey("Usuario", null=True, blank=True, verbose_name='creado por',
                                   related_name='%(class)s_creado_por', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name=_('fecha de creación'))
    ip_creacion = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip de creación'))
    # Auditoria de modificación
    modificado_por = models.ForeignKey("Usuario", null=True, blank=True, verbose_name='modificado por',
                                       related_name='%(class)s_modificado_por', on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(null=True, blank=True, verbose_name=_('fecha de modificación'))
    ip_modificacion = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip de modificación'))

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):

        """
        Si el estado de la instancia es de creación se genera un registro de
        quien, cuando y desde donde se crea la instancia.
        De lo contrario el estado corresponde a una modificación, por lo cual
        se genera un registro de quien, cuando y desde donde se modifica la instancia.
        """
        if self._state.adding:
            if Usuario.objects.count() > 0:
                self.creado_por = get_current_user()
                self.ip_creacion = get_current_request().META['REMOTE_ADDR']
        else:
            self.modificado_por = get_current_user()
            self.fecha_modificacion = datetime.now()
            self.ip_modificacion = get_current_request().META['REMOTE_ADDR']
        super(Usuario, self).save(*args, **kwargs)

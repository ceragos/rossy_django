from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Usuario(AbstractUser):

    foto_perfil = models.ImageField(null=True, blank=True, verbose_name=_('foto de perfil'),
                                    upload_to='usuarios/foto_perfil')

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def __str__(self):
        return self.username

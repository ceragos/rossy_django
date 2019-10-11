from datetime import datetime

from crum import get_current_user, get_current_request
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aplicacion.usuarios.models import Usuario
from aplicacion.utilidades.funcionalidades import calcular_edad, convertir_valores_campos_capitalize

TIPO_IDENTIFICACION_CHOICES = (
    ('CC', _('CEDULA DE CIUDADANIA')),
    ('TI', _('TARJETA DE IDENTIDAD')),
    ('CE', _('CEDULA EXTRANJERA')),
    ('PS', _('PASAPORTE')),
)

def validar_cadenas_numericas(value):
    if not value.isdigit():
        raise ValidationError(
            _('No es un número valido'),
            params={'value': value},
        )


class Auditoria(models.Model):
    """
    Esta clase genera automáticamente un registro de los cambios que se realizan la información de una instancia
    de las clases que hereden de ella.
    """
    activo = models.BooleanField(default=True, verbose_name=_('registro activo'))
    # Auditoria de creación
    creado_por = models.ForeignKey(Usuario, null=True, blank=True, verbose_name='creado por',
                                   related_name='%(class)s_creado_por', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name=_('fecha de creación'))
    ip_creacion = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip de creación'))
    # Auditoria de modificación
    modificado_por = models.ForeignKey(Usuario, null=True, blank=True, verbose_name='modificado por',
                                       related_name='%(class)s_modificado_por', on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(null=True, blank=True, verbose_name=_('fecha de modificación'))
    ip_modificacion = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip de modificación'))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        """
        Si el estado de la instancia es de creación se genera un registro de
        quien, cuando y desde donde se crea la instancia.
        De lo contrario el estado corresponde a una modificación, por lo cual
        se genera un registro de quien, cuando y desde donde se modifica la instancia.
        """
        if self._state.adding:
            self.creado_por = get_current_user()
            self.ip_creacion = get_current_request().META['REMOTE_ADDR']
        else:
            self.modificado_por = get_current_user()
            self.fecha_modificacion = datetime.now()
            self.ip_modificacion = get_current_request().META['REMOTE_ADDR']

        convertir_valores_campos_capitalize(self)
        super(Auditoria, self).save(*args, **kwargs)


class PersonaBase(models.Model):
    tipo_identificacion = models.CharField(max_length=2, null=True, blank=True,
                                           verbose_name=_('tipo de identificación'),
                                           choices=TIPO_IDENTIFICACION_CHOICES)
    numero_identificacion = models.CharField(max_length=20, null=True, blank=True, unique=True,
                                             validators=[validar_cadenas_numericas],
                                             verbose_name=_('numero de identificación'))
    nombres = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('nombres'))
    apellidos = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('apellidos'))
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name=_('fecha de nacimiento'))
    celular_regex = RegexValidator(regex=r'\+?2?\d{10}$',
                                   message="""El numero celular debe ingresarse con el formato:
                                       +573152340969. Máximo 10 digitos""", )
    celular = models.CharField(max_length=13, null=True, blank=True, verbose_name='celular', validators=[celular_regex])
    direccion = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('dirección'))

    class Meta:
        abstract = True

    @property
    def nombre_completo(self):
        return "{} {}".format(self.nombres, self.apellidos)

    @property
    def primer_nombre(self):
        return self.nombres.split()[0]

    @property
    def primer_apellido(self):
        return self.apellidos.split()[0]

    @property
    def edad(self):
        return calcular_edad(self.fecha_nacimiento)

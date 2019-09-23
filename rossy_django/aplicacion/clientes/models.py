from django.db import models

from aplicacion.utilidades.models import Auditoria, PersonaBase


class Cliente(Auditoria, PersonaBase):
    pass

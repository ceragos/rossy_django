from datetime import date

from dateutil.relativedelta import relativedelta


def calcular_edad(fecha_nacimiento):
    if fecha_nacimiento:
        # Calcula la cantida de años entre la fecha actual y la fecha de nacimiento
        anios = date.today().year - fecha_nacimiento.year
        # Suma los años de diferencia a la fecha de nacimiento
        cumpleanios = fecha_nacimiento + relativedelta(years=anios)

        if cumpleanios > date.today():
            anios = anios - 1

        return anios

    return 0


def convertir_valores_campos_mayusculas(self):
    from django.db import models
    # Obtiene todos los campos de tipo charfield y genera una lista de campos
    char_fields = [field.name for field in self._meta.fields if
                   isinstance(field, models.CharField) and not getattr(field, 'choices')]
    # Recorrerla lista de campos
    for field in char_fields:
        valor = getattr(self, field, False)
        if valor:
            # Elimina los espacios en blanco que no son necesarios
            valor = " ".join(valor.split())
            # Cambia los caracteres a mayusculas
            setattr(self, field, valor.upper())

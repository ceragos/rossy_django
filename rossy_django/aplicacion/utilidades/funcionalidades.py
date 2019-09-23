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

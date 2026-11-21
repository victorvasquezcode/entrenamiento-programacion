import math


def convertir_entero(valor):
    if type(valor) not in (int, str):
        return None
    try:
        convertidor_entero = int(valor)
    except (TypeError,ValueError):
        return None
    return convertidor_entero

def dividir_seguro(a,b):
    if type(a) is bool or type(b) is bool:
        return None
    try:
        convertidor1 = float(a)
        convertidor2 = float(b)
        if not (math.isfinite(convertidor1) and math.isfinite(convertidor2)):
            return None
        division = convertidor1 / convertidor2
    except (ZeroDivisionError, ValueError, TypeError, OverflowError):
        return None
    return division if math.isfinite(division) else None


#
def convertir_entero(valor):
    if type(valor) is bool or type(valor) is float:
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
        division = convertidor1 / convertidor2
    except (ZeroDivisionError , ValueError, TypeError):
        return None
    return division


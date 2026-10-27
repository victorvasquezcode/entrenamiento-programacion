#Validación y transformación
def validar_codigo(codigo : str):
    codigo_limpio = codigo.strip().upper()
    if len(codigo_limpio) == 4 and codigo_limpio[:2].isalpha() and codigo_limpio[2:].isdigit():
        return codigo_limpio
    else:
        return None
def calcular_movimiento(tipo : str, unidades : int):
    normalizar_tipo = tipo.strip().upper()
    if normalizar_tipo == "VENTA" and isinstance(unidades,int)  and unidades > 0:
        return unidades
    elif normalizar_tipo == "DEVOLUCION" and isinstance(unidades,int)  and unidades > 0:
        return -unidades
    else:
        return None

print(validar_codigo(" ab01 "))
print(validar_codigo("A123"))
print(validar_codigo("CD99"))
print(calcular_movimiento("venta", 8))
print(calcular_movimiento("DEVOLUCION", 3))
print(calcular_movimiento("VENTA", 0))
print(calcular_movimiento("OTRO", 5))
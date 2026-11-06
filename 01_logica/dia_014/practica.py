import math
def aplicar_descuentos(productos, porcentaje):
    resultados = {}
    duplicados = set()
    if not type(productos) is dict:
        return None
    for nombre, precio in productos.items():
        if not type(nombre) is str:
            return None
        normalizar_nombres = nombre.strip()  
        if not normalizar_nombres:
            return None
        if normalizar_nombres in duplicados:
            return None
        else:
            duplicados.add(normalizar_nombres)
        if type(precio) is not int and type(precio) is not float:
            return None
        if not math.isfinite(precio) or not precio >= 0:
            return None
    if type(porcentaje) is not int and type(porcentaje) is not float:
        return None
    if not math.isfinite(porcentaje) or not 0 <= porcentaje <= 100:
        return None
    for nombre,precio in productos.items():
        normalizar_nombres = nombre.strip()
        precio_final = precio * (1-(porcentaje/100))
        resultados[normalizar_nombres] = precio_final
    return resultados

prueba_1 = aplicar_descuentos({"A": 100, "B": 200},0)
prueba_2 = aplicar_descuentos({"A": 100, "B": 200},100)
prueba_3 = aplicar_descuentos({"A": 100, "B": 200},-20)
prueba_4 = aplicar_descuentos({"A": float("inf")},20)
prueba_5 = aplicar_descuentos({"A": float("nan")},20)
prueba_6 = aplicar_descuentos({"A": True},20)
prueba_7 = aplicar_descuentos({},20)
prueba_8 = aplicar_descuentos({"A": 100, " A ": 200},20)
original = {" Teclado ": 100.0}
copia = original.copy()
prueba_9 = aplicar_descuentos(original,20)
assert prueba_1 == {"A": 100.0, "B": 200.0}
assert prueba_2 == {"A": 0.0, "B": 0.0}
assert prueba_3 is 	None
assert prueba_4 is 	None
assert prueba_5 is 	None
assert prueba_6 is 	None
assert prueba_7 == 	{}
assert prueba_8 is 	None
assert original == copia
assert prueba_9 == {"Teclado": 80.0}
assert prueba_9 is not original
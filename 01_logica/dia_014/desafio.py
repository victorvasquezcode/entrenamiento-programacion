import math
def transformar_ventas(ventas):
    productos = {}
    if not type(ventas) is list:
        return None
    for registro in ventas:
        if type(registro) is not dict:
            return None
        claves = ('producto','cantidad','precio')
        if not all(clave in registro for clave in claves):
            return None
        nombre = registro['producto']
        cantidad = registro['cantidad']
        precio = registro['precio']
        if not type(nombre) is str:
            return None
        normalizar_nombre = nombre.strip()
        if not normalizar_nombre:
            return None
        if type(cantidad) is not int or not cantidad > 0:
            return None
        if not type(precio) is float and not type(precio) is int:
            return None
        if not math.isfinite(precio) or not precio >= 0:
            return None
    if not ventas:
        return productos
    for registro in ventas:
        nombre = registro['producto']
        cantidad = registro['cantidad']
        precio = registro['precio']
        normalizar_nombre = nombre.strip()
        importe_total = cantidad * precio
        if normalizar_nombre in productos:
            productos[normalizar_nombre]['cantidad'] += cantidad
            productos[normalizar_nombre]['total'] += importe_total
        else:
            productos[normalizar_nombre] = {
                "cantidad": cantidad,
                "total": importe_total
            }
    return productos
#1. Lista vacía
prueba_1 = transformar_ventas([])
assert prueba_1 == {}
#2. Ventas repetidas del mismo producto
ventas = [
    {"producto": "Teclado", "cantidad": 2, "precio": 45.50},
    {"producto": "Mouse", "cantidad": 3, "precio": 25.00},
    {"producto": "Teclado", "cantidad": 1, "precio": 45.50}
]
prueba_2 = transformar_ventas(ventas)
assert prueba_2 == {'Teclado': {'cantidad': 3, 'total': 136.5}, 'Mouse': {'cantidad': 3, 'total': 75.0}}
#3. Nombres con espacios exteriores
prueba_3 = transformar_ventas([{"producto": " Teclado ", "cantidad": 2, "precio": 45.50}])
assert prueba_3 == {'Teclado': {'cantidad': 2, 'total': 91.0}}
#4. Cantidad negativa o cero
prueba_4 = transformar_ventas([{"producto": " Teclado ", "cantidad": -2, "precio": 45.50}])
assert prueba_4 is None
#5. Cantidad booleana
prueba_5 = transformar_ventas([{"producto": " Teclado ", "cantidad": True, "precio": 45.50}])
assert prueba_5 is None
#6. Precio infinito o NaN
prueba_6 = transformar_ventas([{"producto": " Teclado ", "cantidad": 3, "precio": float("nan")}])
assert prueba_6 is None
prueba_7 = transformar_ventas([{"producto": " Teclado ", "cantidad": 3, "precio": float("inf")}])
assert prueba_7 is None
#7. Registro incompleto
prueba_8 = transformar_ventas([{"producto": " Teclado ", "precio": float("inf")}])
assert prueba_8 is None
#8. Inmutabilidad de la lista y sus diccionarios
import copy
ventas = [
    {"producto": " Teclado ", "cantidad": 2, "precio": 45.50},
    {"producto": "Mouse", "cantidad": 3, "precio": 25.00}
]
ventas_originales = copy.deepcopy(ventas)
resultado = transformar_ventas(ventas)
assert ventas == ventas_originales
assert resultado is not ventas
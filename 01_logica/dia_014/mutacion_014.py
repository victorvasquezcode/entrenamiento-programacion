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
                "total": importe_total,
            }
    for nombre, datos in productos.items():
        cantidad = datos['cantidad']
        total = datos['total']
        promedio = total / cantidad
        datos['promedio'] = promedio
    return productos
#1. Dos ventas del mismo producto con distintos precios
prueba_1 = transformar_ventas([
    {"producto": "Teclado", "cantidad": 2, "precio": 40.0},
    {"producto": "Teclado", "cantidad": 3, "precio": 50.0}
])
assert prueba_1 == {
    "Teclado": {"cantidad": 5, "total": 230.0, "promedio": 46.0}
}
#2. Una venta de un producto
prueba_2 = transformar_ventas([
    {"producto": "Mouse", "cantidad": 2, "precio": 25.0}
])
assert prueba_2 == {
    "Mouse": {"cantidad": 2, "total": 50.0, "promedio": 25.0}
}
#3. Lista vacía
assert transformar_ventas([]) == {}
#4. Registro inválido después de uno válido
prueba_4 = transformar_ventas([
    {"producto": "Teclado", "cantidad": 2, "precio": 40.0},
    {"producto": "Mouse", "cantidad": 0, "precio": 20.0}
])
assert prueba_4 is None
#5. Nombres con espacios exteriores
prueba_5 = transformar_ventas([
    {"producto": " Teclado ", "cantidad": 2, "precio": 40.0},
    {"producto": "Teclado", "cantidad": 1, "precio": 40.0}
])
assert prueba_5 == {
    "Teclado": {"cantidad": 3, "total": 120.0, "promedio": 40.0}
}
#6. Inmutabilidad de la entrada
import copy
ventas_originales = [
    {"producto": " Teclado ", "cantidad": 2, "precio": 40.0},
    {"producto": "Mouse", "cantidad": 1, "precio": 20.0}
]
copia = copy.deepcopy(ventas_originales)

resultado = transformar_ventas(ventas_originales)

assert ventas_originales == copia
assert resultado is not ventas_originales
#7. Precio cero
prueba_7 = transformar_ventas([
    {"producto": "Mouse", "cantidad": 3, "precio": 0.0}
])
assert prueba_7 == {
    "Mouse": {"cantidad": 3, "total": 0.0, "promedio": 0.0}
}
#8. Cantidades diferentes entre registros
prueba_8 = transformar_ventas([
    {"producto": "Monitor", "cantidad": 1, "precio": 100.0},
    {"producto": "Monitor", "cantidad": 3, "precio": 200.0}
])
assert prueba_8 == {
    "Monitor": {"cantidad": 4, "total": 700.0, "promedio": 175.0}
}
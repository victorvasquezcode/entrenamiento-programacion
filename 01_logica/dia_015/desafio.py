from decimal import Decimal, InvalidOperation
def resumir_ventas_monetarias(ventas):
    resumen_ventas = {}
    if not type(ventas) is list:
        return None
    for registro in ventas:
        if not type(registro) is dict:
            return None
        claves = ("producto","cantidad","precio")
        if not all(clave in registro for clave in claves):
            return None
        producto = registro['producto']
        cantidad = registro['cantidad']
        precio = registro['precio']
        if not type(producto) is str:
            return None
        normalizar_nombre = producto.strip()
        if not normalizar_nombre:
            return None
        if not type(cantidad) is int:
            return None
        if cantidad <= 0:
            return None
        if not type(precio) is str:
            return None
        try:
            precios_decimal = Decimal(precio)
        except InvalidOperation:
            return None
        if not precios_decimal.is_finite():
            return None
        if precios_decimal < 0:
            return None
    for registro in ventas:
        producto = registro['producto']
        cantidad = registro['cantidad']
        precio = registro['precio']
        normalizar_nombre = producto.strip()
        precios_decimal = Decimal(precio)
        total = cantidad * precios_decimal
        if normalizar_nombre in resumen_ventas:
            resumen_ventas[normalizar_nombre]['cantidad'] += cantidad
            resumen_ventas[normalizar_nombre]['total'] += total
        else:
            resumen_ventas[normalizar_nombre] = {
                "cantidad": cantidad,
                "total": total
            }
    return resumen_ventas
#1. Lista vacía
assert resumir_ventas_monetarias([]) == {}
#2. Ventas repetidas del mismo producto.
ventas = [
    {"producto": "Teclado", "cantidad": 2, "precio": "19.90"},
    {"producto": "Teclado", "cantidad": 1, "precio": "19.90"}
]
assert resumir_ventas_monetarias(ventas) == {
        "Teclado": {
            "cantidad": 3,
            "total": Decimal("59.70")
        }
    }
#3. Nombres con espacios.
assert resumir_ventas_monetarias([
    {"producto": " Teclado ", "cantidad": 2, "precio": "19.90"}
    ]) == {
        "Teclado": {
            "cantidad": 2,
            "total": Decimal("39.8")
        }
    }
#4. Cantidad cero, negativa o booleana.
assert resumir_ventas_monetarias([
    {"producto": "A", "cantidad": -1, "precio": "10.00"}
]) is None

assert resumir_ventas_monetarias([
    {"producto": "A", "cantidad": True, "precio": "10.00"}
]) is None

for precio in ("NaN", "Infinity", "abc"):
    assert resumir_ventas_monetarias([
        {"producto": "A", "cantidad": 1, "precio": precio}
    ]) is None
#5. Precio NaN, Infinity o texto inválido.
assert resumir_ventas_monetarias([{"producto": " Teclado ", "cantidad": 20, "precio": "NaN"}]) is None
assert resumir_ventas_monetarias([{"producto": " Teclado ", "cantidad": 20, "precio": "Infinity"}]) is None
assert resumir_ventas_monetarias([{"producto": " Teclado ", "cantidad": 20, "precio": "abc"}]) is None
#6. Precio de tipo float.
assert resumir_ventas_monetarias([{"producto": " Teclado ", "cantidad": 20, "precio": 19.6}]) is None
#7. Registro incompleto.
assert resumir_ventas_monetarias([{"producto": " Teclado ", "precio": "19.90"}]) is None
#8. Importes con "0.10" y "0.20".
ventas = [
    {"producto": "Teclado", "cantidad": 1, "precio": "0.10"},
    {"producto": "Teclado", "cantidad": 1, "precio": "0.20"}
]
assert resumir_ventas_monetarias(ventas) == {'Teclado': {'cantidad': 2, 'total': Decimal('0.30')}}
#9. Inmutabilidad de la lista y sus diccionarios
import copy
ventas_originales = [
    {"producto": " Teclado ", "cantidad": 2, "precio": "40.0"},
    {"producto": "Mouse", "cantidad": 1, "precio": "20.0"}
]
copia = copy.deepcopy(ventas_originales)
resultado = resumir_ventas_monetarias(ventas_originales)
assert ventas_originales == copia
assert resultado is not ventas_originales
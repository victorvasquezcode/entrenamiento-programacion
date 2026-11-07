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
    for clave, datos in resumen_ventas.items():
        cantidad = datos['cantidad']
        total = datos['total']
        promedio = total / cantidad
        datos['precio_promedio'] = promedio
    return resumen_ventas
#1. Promedio de un registro
assert resumir_ventas_monetarias([
    {"producto": "Teclado",
    "cantidad": 2,
    "precio": "10.00"}
    ]) == {
        "Teclado": {
            "cantidad": 2,
            "total": Decimal("20.00"),
            "precio_promedio": Decimal("10.00")
        }
    }
#2. Promedio ponderado con precios distintos.
assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"}
]) == {
        "Teclado": {
            "cantidad": 5,
            "total": Decimal("80.00"),
            "precio_promedio": Decimal("16.00")
        }
    }
#3. Dos productos independientes
assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"}
    ]) == {
    "Teclado": {
        "cantidad": 3,
        "total": Decimal("60.00"),
        "precio_promedio": Decimal("20.00")
    },
    "Mouse": {
        "cantidad": 1,
        "total": Decimal("5.00"),
        "precio_promedio": Decimal("5.00")
    }
}
#4. Precio cero.
assert resumir_ventas_monetarias([
    {"producto": "Teclado",
    "cantidad": 2,
    "precio": "0"}
    ]) == {
        'Teclado': 
            {'cantidad': 2, 
             'total': Decimal('0'), 
             'precio_promedio': Decimal('0')
             }
        }
#5. Lista vacía.
assert resumir_ventas_monetarias([]) == {}
#6. Registro inválido.
assert resumir_ventas_monetarias([{"producto": "Teclado", "cantidad": 3}]) is None
#7. Inmutabilidad.
import copy
ventas_original = [
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"}
]
copia = copy.deepcopy(ventas_original)
resultado = resumir_ventas_monetarias(ventas_original)
assert copia == ventas_original
assert resultado is not ventas_original
#8. Cantidad cero rechazada.
assert resumir_ventas_monetarias([
    {"producto": "Teclado",
    "cantidad": 0,
    "precio": "10.00"}
    ]) is None
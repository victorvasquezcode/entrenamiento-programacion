from decimal import Decimal, InvalidOperation
def validar_cantidad(cantidad):
    if type(cantidad) is int and cantidad > 0:
        return True
    else:
        return False
def convertir_precio(precio):
    if type(precio) is str:
        try:
            precio_decimal = Decimal(precio)
            if not precio_decimal.is_finite() or precio_decimal < 0:
                return None
        except InvalidOperation:
            return None
    else:
        return None
    return precio_decimal
def calcular_importe(cantidad, precio):
    if not validar_cantidad(cantidad):
        return None
    precio_decimal = convertir_precio(precio)
    if precio_decimal is None:
        return None
    total = cantidad * precio_decimal
    return total
def normalizar_producto(producto):
    if type(producto) is str:
        normalizar_producto = producto.strip()
        if not normalizar_producto:
            return None
        return normalizar_producto
    else:
        return None
def resumir_ventas_monetarios(ventas):
    if type(ventas) is not list:
        return None
    ventas_validadas = []
    for venta in ventas:
        if type(venta) is not dict:
            return None
        claves = ("producto","cantidad","precio")
        if not all(clave in venta for clave in claves):
            return None
        producto = normalizar_producto(venta["producto"])
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        if producto is None:
            return None
        importe = calcular_importe(cantidad, precio)
        if importe is None:
            return None
        ventas_validadas.append({
            "producto": producto,
            "cantidad": cantidad,
            "importe": importe
        })
    resumen_ventas = {}
    for venta in ventas_validadas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        importe = venta["importe"]
        if producto in resumen_ventas:
            resumen_ventas[producto]['cantidad'] += cantidad
            resumen_ventas[producto]['total'] += importe
        else:
            resumen_ventas[producto] ={
                "cantidad": cantidad,
                "total": importe
            }
    for clave, datos in resumen_ventas.items():
        cantidad = datos['cantidad']
        total = datos['total']
        promedio = total / cantidad
        datos['precio_promedio'] = promedio
    return resumen_ventas
from copy import deepcopy
# PRUEBA 1: Lista vacía
assert resumir_ventas_monetarios([]) == {}
# PRUEBA 2: Producto repetido con espacios
assert resumir_ventas_monetarios([
    {"producto": " Teclado ", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"}
]) == {
    "Teclado": {
        "cantidad": 5,
        "total": Decimal("80.00"),
        "precio_promedio": Decimal("16.00")
    }
}
# PRUEBA 3: Dos productos independientes
assert resumir_ventas_monetarios([
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"}
]) == {
    "Teclado": {
        "cantidad": 2,
        "total": Decimal("20.00"),
        "precio_promedio": Decimal("10.00")
    },
    "Mouse": {
        "cantidad": 1,
        "total": Decimal("5.00"),
        "precio_promedio": Decimal("5.00")
    }
}
# PRUEBA 4: Precio cero
assert resumir_ventas_monetarios([
    {"producto": "Teclado", "cantidad": 2, "precio": "0"}
]) == {
    "Teclado": {
        "cantidad": 2,
        "total": Decimal("0"),
        "precio_promedio": Decimal("0")
    }
}
# PRUEBA 5: Cantidad booleana
assert resumir_ventas_monetarios([
    {"producto": "Teclado", "cantidad": True, "precio": "10.00"}
]) is None
# PRUEBA 6: Precios especiales e inválidos
for precio in ("NaN", "Infinity", "-Infinity", "abc"):
    assert resumir_ventas_monetarios([
        {"producto": "Teclado", "cantidad": 2, "precio": precio}
    ]) is None
# PRUEBA 7: Registro incompleto
assert resumir_ventas_monetarios([
    {"producto": "Mouse", "cantidad": 2}
]) is None
# PRUEBA 8: Inmutabilidad
ventas_originales = [
    {"producto": " Teclado ", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"}
]
copia_original = deepcopy(ventas_originales)
resultado = resumir_ventas_monetarios(ventas_originales)
assert ventas_originales == copia_original
assert resultado is not None
# PRUEBA 9: Promedio ponderado
assert resumir_ventas_monetarios([
    {"producto": "Monitor", "cantidad": 2, "precio": "100.00"},
    {"producto": "Monitor", "cantidad": 3, "precio": "200.00"}
]) == {
    "Monitor": {
        "cantidad": 5,
        "total": Decimal("800.00"),
        "precio_promedio": Decimal("160.00")
    }
}
# PRUEBA 10: Registro inválido después de uno válido
assert resumir_ventas_monetarios([
    {"producto": "Mouse", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 1, "precio": "incorrecto"}
]) is None
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
            resumen_ventas[producto]['operaciones'] += 1
        else:
            resumen_ventas[producto] ={
                "cantidad": cantidad,
                "total": importe,
                "operaciones": 1
            }
    for clave, datos in resumen_ventas.items():
        cantidad = datos['cantidad']
        total = datos['total']
        promedio = total / cantidad
        datos['precio_promedio'] = promedio
    return resumen_ventas
# PRUEBA 1: Una venta de 10 unidades = 1 operación
assert resumir_ventas_monetarios([
    {"producto": "Teclado", "cantidad": 10, "precio": "15.00"}
]) == {
    "Teclado": {
        "cantidad": 10,
        "total": Decimal("150.00"),
        "operaciones": 1,
        "precio_promedio": Decimal("15.00")
    }
}
# PRUEBA 2: Tres registros del mismo producto = 3 operaciones
assert resumir_ventas_monetarios([
    {"producto": "Mouse", "cantidad": 2, "precio": "10.00"},
    {"producto": " Mouse ", "cantidad": 3, "precio": "20.00"},
    {"producto": "Mouse", "cantidad": 5, "precio": "30.00"}
]) == {
    "Mouse": {
        "cantidad": 10,
        "total": Decimal("230.00"),
        "operaciones": 3,
        "precio_promedio": Decimal("23.00")
    }
}
# PRUEBA 3: Dos productos con contadores independientes
assert resumir_ventas_monetarios([
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"}
]) == {
    "Teclado": {
        "cantidad": 5,
        "total": Decimal("80.00"),
        "operaciones": 2,
        "precio_promedio": Decimal("16.00")
    },
    "Mouse": {
        "cantidad": 1,
        "total": Decimal("5.00"),
        "operaciones": 1,
        "precio_promedio": Decimal("5.00")
    }
}
# PRUEBA 4: Registro inválido después de uno válido
assert resumir_ventas_monetarios([
    {"producto": "Mouse", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": True, "precio": "15.00"}
]) is None
# PRUEBA 5: Lista vacía
assert resumir_ventas_monetarios([]) == {}
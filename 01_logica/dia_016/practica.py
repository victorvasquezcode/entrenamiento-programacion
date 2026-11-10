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

assert validar_cantidad(3) is True
assert validar_cantidad(True) is False
assert validar_cantidad(0) is False
assert validar_cantidad(-2) is False

assert convertir_precio("0.10") == Decimal("0.10")
assert convertir_precio("abc") is None
assert convertir_precio("NaN") is None
assert convertir_precio("Infinity") is None
assert convertir_precio(10.5) is None

assert calcular_importe(3, "19.90") == Decimal("59.70")
assert calcular_importe(2, "0.10") == Decimal("0.20")
assert calcular_importe(0, "10.00") is None
assert calcular_importe(True, "10.00") is None

assert convertir_precio("-0.10") is None
assert convertir_precio("0") == Decimal("0")
assert convertir_precio("") is None
assert validar_cantidad(3.0) is False
assert calcular_importe(1,"0.001") == Decimal("0.001")
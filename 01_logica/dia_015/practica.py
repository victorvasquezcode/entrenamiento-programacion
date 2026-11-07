from decimal import Decimal, InvalidOperation
def calcular_importe(cantidad, precio_unitario):
    if not type(cantidad) is int:
        return None
    if cantidad <= 0:
        return None
    if not type(precio_unitario) is str:
        return None
    try:
        precio_decimal = Decimal(precio_unitario)
    except InvalidOperation:
        return None
    if not precio_decimal.is_finite():
        return None
    if precio_decimal < 0:
        return None
    resultado = cantidad * precio_decimal
    return resultado
#1. Precio válido: 3 × "19.90"
assert calcular_importe(3, "19.90") == Decimal("59.70")
#2. Precio "0.10" sin error de representación.
assert calcular_importe(2, "0.10") == Decimal("0.20")
#3. Precio cero
assert calcular_importe(1, "0") == Decimal("0")
#4. Cantidad cero
assert calcular_importe(0, "10.00") is None
#5. Cantidad negativa.
assert calcular_importe(-20, "10.00") is None
#6. Cantidad booleana
assert calcular_importe(True, "10.00") is None
#7. Precio "abc".
assert calcular_importe(2, "abc") is None
#8. Precio "NaN".
assert calcular_importe(2, "NaN") is None
#9. Precio "Infinity".
assert calcular_importe(2, "Infinity") is None
#10. Precio de tipo float en lugar de str.
assert calcular_importe(2, 12.6) is None
#11. Comprobar que el resultado sea Decimal.
resultado = calcular_importe(3,"19.90")
assert type(resultado) is Decimal

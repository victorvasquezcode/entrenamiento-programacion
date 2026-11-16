def convertir_stock(valor):
    if type(valor) is not str:
        return None
    normalizar_valor = valor.strip()
    if not normalizar_valor:
        return None
    valores_validos = ("0","1","2","3","4","5","6","7","8","9")
    if not all(valor in valores_validos for valor in normalizar_valor):
        return None
    try:
        normalizar_valor = int(normalizar_valor)
        return normalizar_valor
    except ValueError:
        return None
def calcular_stock_final(stock_inicial, entradas, salidas):
    convertir_stock_inicial = convertir_stock(stock_inicial)
    convertir_entradas = convertir_stock(entradas)
    convertir_salidas = convertir_stock(salidas)
    if convertir_stock_inicial is None:
        return None
    if convertir_entradas is None:
        return None
    if convertir_salidas is None:
        return None
    stock_disponible = convertir_stock_inicial + convertir_entradas
    if convertir_salidas > stock_disponible:
        return None
    stock_final = stock_disponible - convertir_salidas
    return stock_final

assert convertir_stock("15") == 15
assert convertir_stock(" 20 ") == 20
assert convertir_stock("0") == 0
assert convertir_stock("0007") == 7

assert convertir_stock("-5") is None
assert convertir_stock("+5") is None
assert convertir_stock("2.5") is None
assert convertir_stock("") is None
assert convertir_stock("abc") is None
assert convertir_stock(True) is None
assert convertir_stock(15) is None
assert convertir_stock("１２") is None

assert calcular_stock_final("10", "5", "3") == 12
assert calcular_stock_final("0", "10", "10") == 0
assert calcular_stock_final("5", "0", "8") is None
assert calcular_stock_final("abc", "2", "1") is None

assert convertir_stock(" 0009 ") == 9
assert convertir_stock("  ") is None
assert convertir_stock("１ ２") is None
assert convertir_stock("1\n2") is None
assert convertir_stock("٣") is None
assert convertir_stock(None) is None
assert convertir_stock("999999999999999999999999999999") == 999999999999999999999999999999
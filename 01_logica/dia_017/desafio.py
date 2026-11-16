from  practica import convertir_stock
def procesar_movimientos_stock(stock_inicial, movimientos):
    cantidad_operaciones = 0
    if type(movimientos) is not list:
        return None
    convertir_stock_inicial = convertir_stock(stock_inicial)
    if convertir_stock_inicial is None:
        return None
    for movimiento in movimientos:
        if type(movimiento) is not dict:
            return None
        claves_validas = ("tipo","cantidad")
        if not all(clave in claves_validas for clave in movimiento):
            return None
        if len(movimiento) != 2:
            return None
        tipo = movimiento["tipo"]
        cantidad = movimiento["cantidad"]
        if type(tipo) is not str:
            return None
        if tipo not in ("entrada", "salida"):
            return None
        convertir_cantidad = convertir_stock(cantidad)
        if convertir_cantidad is None:
            return None
        if tipo == "entrada":
            convertir_stock_inicial += convertir_cantidad
        elif tipo == "salida":
            if convertir_cantidad > convertir_stock_inicial:
                return None
            convertir_stock_inicial -= convertir_cantidad
        cantidad_operaciones += 1
    resultado = {
        "stock_final": convertir_stock_inicial,
        "operaciones": cantidad_operaciones
    }
    return resultado

assert procesar_movimientos_stock("5", [
    {"tipo": "entrada", "cantidad": "10"},
    {"tipo": "salida", "cantidad": "4"},
    {"tipo": "entrada", "cantidad": "2"}
]) == {"stock_final": 13, "operaciones": 3}

assert procesar_movimientos_stock("10", []) == {
    "stock_final": 10,
    "operaciones": 0
}

assert procesar_movimientos_stock("5", [
    {"tipo": "salida", "cantidad": "6"}
]) is None

assert procesar_movimientos_stock("5", [
    {"tipo": "entrada", "cantidad": "10"},
    {"tipo": "salida", "cantidad": "20"}
]) is None

assert procesar_movimientos_stock("5", [
    {"tipo": "entrada", "cantidad": "abc"}
]) is None

assert procesar_movimientos_stock("5", [
    {"tipo": "ajuste", "cantidad": "2"}
]) is None

assert procesar_movimientos_stock("5", [
    {"tipo": "entrada", "cantidad": "2", "extra": 1}
]) is None

assert procesar_movimientos_stock("abc", []) is None
assert procesar_movimientos_stock("5", "entrada") is None
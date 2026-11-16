from  practica import convertir_stock
def procesar_movimientos_stock(stock_inicial, movimientos):
    total_entradas = 0
    total_salidas = 0
    cantidad_operaciones = 0
    if type(movimientos) is not list:
        return None
    convertir_stock_inicial = convertir_stock(stock_inicial)
    if convertir_stock_inicial is None:
        return None
    mayor = convertir_stock_inicial
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
            total_entradas += convertir_cantidad
        elif tipo == "salida":
            if convertir_cantidad > convertir_stock_inicial:
                return None
            convertir_stock_inicial -= convertir_cantidad
            total_salidas += convertir_cantidad
        cantidad_operaciones += 1
        if convertir_stock_inicial > mayor:
            mayor = convertir_stock_inicial
    resultado = {
        "stock_final": convertir_stock_inicial,
        "operaciones": cantidad_operaciones,
        "total_entradas": total_entradas,
        "total_salidas": total_salidas,
        "stock_maximo": mayor
    }
    return resultado

assert procesar_movimientos_stock("5", [
    {"tipo": "entrada", "cantidad": "10"},
    {"tipo": "salida", "cantidad": "4"},
    {"tipo": "entrada", "cantidad": "2"}
]) == {
    "stock_final": 13,
    "operaciones": 3,
    "total_entradas": 12,
    "total_salidas": 4,
    "stock_maximo": 15
}

assert procesar_movimientos_stock("10", []) == {
    "stock_final": 10,
    "operaciones": 0,
    "total_entradas": 0,
    "total_salidas": 0,
    "stock_maximo": 10
}

assert procesar_movimientos_stock("20", [
    {"tipo": "salida", "cantidad": "5"},
    {"tipo": "entrada", "cantidad": "3"}
]) == {
    "stock_final": 18,
    "operaciones": 2,
    "total_entradas": 3,
    "total_salidas": 5,
    "stock_maximo": 20
}

assert procesar_movimientos_stock("0", [
    {"tipo": "entrada", "cantidad": "10"},
    {"tipo": "salida", "cantidad": "10"}
]) == {
    "stock_final": 0,
    "operaciones": 2,
    "total_entradas": 10,
    "total_salidas": 10,
    "stock_maximo": 10
}

assert procesar_movimientos_stock("5", [
    {"tipo": "entrada", "cantidad": "10"},
    {"tipo": "salida", "cantidad": "20"}
]) is None
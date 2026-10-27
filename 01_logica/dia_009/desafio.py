#Procesador de transacciones
movimientos = [
    ["AB01", "DEVOLUCION", 5],
    ["CD02", "DEVOLUCION", 2],
    ["AB01", "VENTA", 2],
    ["CD02", "VENTA"    , 1],
    ["XY03", "DEVOLUCION", 1]
]
def validar_codigo(codigo : str):
    codigo_limpio = codigo.strip().upper()
    if len(codigo_limpio) == 4 and codigo_limpio[:2].isalpha() and codigo_limpio[2:].isdigit():
        return codigo_limpio
    else:
        return None
def calcular_movimiento(tipo : str, unidades : int):
    normalizar_tipo = tipo.strip().upper()
    if normalizar_tipo == "VENTA" and isinstance(unidades,int)  and unidades > 0:
        return unidades
    elif normalizar_tipo == "DEVOLUCION" and isinstance(unidades,int)  and unidades > 0:
        return -unidades
    else:
        return None
def consolidar_movimientos(movimientos):
    mov={}
    for movimiento in movimientos:
        if len(movimiento) != 3:
            continue
        codigo_validado = validar_codigo(movimiento[0])
        movimiento_validado = calcular_movimiento(movimiento[1],movimiento[2])
        if codigo_validado != None and movimiento_validado != None:
            if codigo_validado in mov:
                mov[codigo_validado] += movimiento_validado
            else:
                mov[codigo_validado] = movimiento_validado
    return mov
def calcular_total(saldos):
    total = 0
    for saldo in saldos:
        total += saldos[saldo]
    return total
def buscar_mayor(saldos):
    contar = 0
    producto_mayor = None
    saldo_mayor = 0
    for saldo in saldos:
        contar += 1
        if contar == 1:
            producto_mayor = saldo
            saldo_mayor = saldos[saldo]
        else:
            if saldos[saldo] > saldo_mayor:
                producto_mayor = saldo
                saldo_mayor = saldos[saldo]
    return producto_mayor, saldo_mayor
saldos = consolidar_movimientos(movimientos)
producto_mayor , saldo_mayor = buscar_mayor(saldos)
for saldo in saldos:
    print(f"{saldo} : {saldos[saldo]}")
print(f"\nProducto diferentes: {len(saldos)}\nSaldo neto total: {calcular_total(saldos)}\nProducto con mayor saldo: {producto_mayor}\nSaldo maximo: {saldo_mayor}")
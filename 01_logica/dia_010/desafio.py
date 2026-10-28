#
transacciones = [
    ["AB01", "VENTA", "5"],
    ["CD02", "DEVOLUCION", "2"],
    ["AB01", "DEVOLUCION", "3"],
    ["CD02", "VENTA", "x"],
    ["A123", "VENTA", "4"],
    [" XY03 ", "venta", " 2 "],
    ["AB01", "VENTA", "0"],
    ["CD02", "VENTA"]
]
def validar_codigo(codigo):
    if type(codigo) is str:
        codigo_limpio = codigo.strip().upper()
    else:
        return None
    if len(codigo_limpio) == 4 and codigo_limpio[:2].isalpha() and codigo_limpio[-2:].isdigit():
        return codigo_limpio

def convertir_entero(valor):
    if type(valor) is bool or type(valor) is float:
        return None
    try:
        convertidor_entero = int(valor)
    except (TypeError,ValueError):
        return None
    return convertidor_entero

def procesar_transacciones(transacciones):
    saldos = {}
    rechazados = 0
    for transaccion in transacciones:
        if len(transaccion) != 3:
            rechazados += 1
            continue
        codigo_validado = validar_codigo(transaccion[0])
        if codigo_validado is None:
            rechazados += 1
            continue
        if type(transaccion[1]) is str:
            normalizar = transaccion[1].strip().upper()
            if normalizar not in ("VENTA","DEVOLUCION"):
                rechazados +=1
                continue
        else:
            rechazados += 1
            continue 
        convertidor_entero = convertir_entero(transaccion[2])
        if convertidor_entero is not None:
            if convertidor_entero > 0:
                if codigo_validado in saldos:
                    if normalizar == "VENTA":
                        saldos[codigo_validado] += convertidor_entero
                    elif normalizar == "DEVOLUCION":
                        saldos[codigo_validado] -= convertidor_entero
                else:
                    if normalizar == "VENTA":
                        saldos[codigo_validado] = convertidor_entero
                    elif normalizar == "DEVOLUCION":
                        saldos[codigo_validado] = - convertidor_entero
            else:
                rechazados += 1
                continue
        else:
            rechazados += 1
            continue
    return saldos, rechazados

def resumen_saldos(saldos):
    total = 0
    codigo_mayor = None
    saldo_mayor = 0
    contador = 0
    if not saldos:
        return total, codigo_mayor, saldo_mayor
    for saldo in saldos:
        total += saldos[saldo]
        contador += 1
        if contador == 1:
            codigo_mayor = saldo
            saldo_mayor = saldos[saldo]
        else:
            if saldos[saldo] > saldo_mayor:
                codigo_mayor = saldo
                saldo_mayor = saldos[saldo]
    return total,codigo_mayor,saldo_mayor

saldos , rechazados = procesar_transacciones(transacciones)
total, codigo_mayor, saldo_mayor = resumen_saldos(saldos)
for saldo in saldos:
    print(f"{saldo}: {saldos[saldo]}")
print(f"\nRegistros rechazados: {rechazados}")
print(f"Saldo total: {total}")
print(f"Producto con mayor saldo: {codigo_mayor}")
print(f"Saldo máximo: {saldo_mayor}")
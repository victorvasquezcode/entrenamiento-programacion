#Consolidación de transacciones
transaccion = {}
while True:
    cantidad_movimiento = int(input("Ingrese la cantidad de movimientos: "))
    if cantidad_movimiento > 0:
        break
    print("Ingrese una cantidad valida")
for movimiento in range(1, cantidad_movimiento + 1):
    while True:
        codigo_producto = input("Ingresar el codigo de producto: ").strip().upper()
        if len(codigo_producto) == 4 and codigo_producto[:2].isalpha() and codigo_producto[-2:].isdigit():
            break
        print("Codigo invalido")
    while True:
        tipo_movimiento = input("Ingresar el tipo de movimiento: ").strip().upper()
        if tipo_movimiento in ["VENTA","DEVOLUCION"]:
            break
        print("tipo movimiento invalido")
    while True:
        unidades = int(input(f"Ingresar las unidades para el producto {codigo_producto}: "))
        if unidades > 0:
            break
        print("unidad invalida")
    if codigo_producto in transaccion and tipo_movimiento == "VENTA":
        transaccion[codigo_producto] += unidades
    elif codigo_producto in transaccion and tipo_movimiento == "DEVOLUCION":
        transaccion[codigo_producto] -= unidades
    elif tipo_movimiento == "VENTA":
        transaccion[codigo_producto] = unidades
    elif tipo_movimiento == "DEVOLUCION":
        transaccion[codigo_producto] = -unidades
print(f"Productos diferentes: {len(transaccion)}")
total = 0
contador = 0
producto_mayor = 0
saldo_mayor = 0
for movimiento in transaccion:
    print(f"{movimiento} : {transaccion[movimiento]}")
    total += transaccion[movimiento]
    contador += 1
    if contador == 1:
        producto_mayor = movimiento
        saldo_mayor = transaccion[movimiento]
    else:
        if transaccion[movimiento] > saldo_mayor:
            producto_mayor = movimiento
            saldo_mayor = transaccion[movimiento]
print(f"Saldo neto total: {total}")
print(f"Producto con mayor saldo: {producto_mayor}\nSaldo maximo: {saldo_mayor}")

#Consolidación de ventas
ventas = {}
while True:
    operaciones = int(input("Ingresa el numero de operaciones: "))
    if operaciones > 0:
        break
    print("Numero invalido")
for operacion in range(1, operaciones + 1):
    while True:
        codigo_producto = input(f"Ingresa el codigo del producto {operacion}: ").strip().upper()
        if len(codigo_producto) == 4 and codigo_producto[:2].isalpha() and codigo_producto[-2:].isdigit():
            break
        print("Codigo invalido")
    while True:
        unidades = int(input(f"Ingrese la unidad para el codigo {codigo_producto}: "))
        if unidades > 0:
            break
        print("Unidad invalida")
    if codigo_producto in ventas:
        ventas[codigo_producto] += unidades
    else:
        ventas[codigo_producto] = unidades
contador = 0
mayor = 0
cant_mayor = 0
for producto in ventas:
    print(f"{producto} : {ventas[producto]}")
    contador += 1
    if contador == 1:
        mayor = producto
        cant_mayor = ventas[producto]
    else:
        if ventas[producto] > cant_mayor:
            mayor = producto
            cant_mayor = ventas[producto]
print(f"{len(ventas)} productos")
print(f"Mayor {mayor} con {cant_mayor} unidades")



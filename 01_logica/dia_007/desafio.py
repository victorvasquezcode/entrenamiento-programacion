#Identificadores de ventas
codigo = "VT1200"

print(codigo[:2])
print(codigo[2:4])
print(codigo[-2:])
registro = []
contador_ventas = 0
contador_nota_credito = 0
contador_00 = 0
while True:
    operaciones = int(input("Ingrese cuantas operaciones se realizara: "))
    if operaciones > 0:
        break
    print("Ingrese un numero valido")

for operacion in range(1, operaciones + 1):
    while True:
        identificador = input(f"Ingrese el identificador de la operacion {operacion}:").strip().upper()
        if identificador in registro:
            print("Duplicado")
            continue

        if len(identificador) == 6 and (identificador[:2] == "VT" or identificador[:2] == "NC") and identificador[2:].isdigit():
            registro.append(identificador)
            print("Se registro correctamente")
            break
        else:
            print("Error al registrar")

for identificador in registro:
    if identificador[:2] == "VT":
        contador_ventas += 1
    elif identificador[:2] == "NC":
        contador_nota_credito += 1
    if identificador[4:] == "00":
        contador_00 += 1

print(registro)
print(f"Identificadores registrados: {len(registro)}, {contador_ventas} ventas, {contador_nota_credito} notas de credito y {contador_00} identificadores terminados en 00")

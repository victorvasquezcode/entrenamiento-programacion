#Limpieza de datos de clientes
nombres_validos = []
contador_a = 0
largo = 0
corto = 0
nombre_largo = None
nombre_corto = None
contador = 0
while True:
    cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))
    if cantidad_clientes > 0:
        break
    print("Cantidad no valida")
for cantidad in range(1, cantidad_clientes + 1):
    while True:
        caracter_validos = True
        nombre = input(f"Ingrese el nombre {cantidad}: ").strip().upper()
        if not nombre:
            print("Vacio")
            continue
        if nombre in nombres_validos:
            print("Duplicado")
            continue
        for caracter in nombre:
            if not caracter.isalpha() and caracter != " ":
                caracter_validos = False
                break
        if 3 <= len(nombre) <= 20 and caracter_validos:
            print("Registrado")
            break
        print("Rechazado")
    nombres_validos.append(nombre)
for nombre in nombres_validos:
    contador += 1
    if contador == 1:
        largo = len(nombre)
        nombre_largo = nombre 
        corto = len(nombre)
        nombre_corto = nombre
    if len(nombre) > largo:
        largo = len(nombre)
        nombre_largo = nombre 
    elif len(nombre) <corto:
        corto = len(nombre)
        nombre_corto = nombre
    if nombre[:1] == "A":
        contador_a += 1
print(f"Lista de clientes registrados: {nombres_validos}\nCantidad total de clientes: {len(nombres_validos)}\nNombre mas largo y su longitud: {nombre_largo},{largo}\nNombre mas corto y su longitud: {nombre_corto},{corto}\nCantidad de nombres que comienzan con A: {contador_a}")
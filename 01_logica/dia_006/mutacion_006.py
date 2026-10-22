#Gestión de inventario con listas
inventario_inicial = []
while True:
    cantidad_productos = int(input("Ingresar cantidad de productos: "))
    if cantidad_productos > 0:
        break
    print("Cantidad invalida")

for producto in range(1, cantidad_productos + 1):
    while True:
        stock = int(input(f"Ingresar stock inicial del producto {producto}: "))
        if stock >= 0:
            break
        print("Stock invalido")
    inventario_inicial.append(stock)
    
while True:
    print("\n ===== GESTION DE INVENTARIO =====")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Consultar inventario")
    print("4. Mostrar estadisticas")
    print("5. Salir")

    opcion = input("Ingresar opcion valida: ")

    if opcion == "1":
        producto = int(input("Número del producto: "))

        if 1 <= producto <= len(inventario_inicial):
            cantidad = int(input("Cantidad a ingresar: "))

            if cantidad > 0:
                indice = producto - 1
                inventario_inicial[indice] += cantidad
                print(f"Stock del producto {producto}: {inventario_inicial[indice]}")
            else:
                print("Cantidad invalida")
        else:
            print("Producto inexistente")

    elif opcion == "2":
        producto = int(input("Numero del producto a modificar: "))

        if 1 <= producto <= len(inventario_inicial):
            cantidad = int(input("Cantidad a retirar: "))

            if cantidad > 0:
                indice = producto - 1
                if inventario_inicial[indice] >= cantidad:
                    inventario_inicial[indice] -= cantidad
                    print(f"Stock del producto {producto}: {inventario_inicial[indice]}")
                else:
                    print("Stock insuficiente")
            else:
                print("Cantidad invalida")
        else:
            print("Producto inexistente")

    elif opcion == "3":
        print(f"\nLista de inventario: {inventario_inicial}")

    elif opcion == "4":
        total_unidades = 0
        producto_sin_stock = 0
        contador = 0

        mayor = inventario_inicial[0]
        menor = inventario_inicial[0]

        producto_mayor = 1
        producto_menor = 1

        for stock in inventario_inicial:
            contador += 1
            total_unidades += stock

            if stock == 0:
                producto_sin_stock += 1

            if stock > mayor:
                mayor = stock
                producto_mayor = contador

            if stock < menor:
                menor = stock
                producto_menor = contador

        print("\n===== ESTADÍSTICAS =====")
        print(f"Total de unidades: {total_unidades}")
        print(f"Producto con mayor stock: {producto_mayor} ({mayor} unidades)")
        print(f"Producto con menor stock: {producto_menor} ({menor} unidades)")
        print(f"Productos sin existencias: {producto_sin_stock}")

    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opcion invalida.")
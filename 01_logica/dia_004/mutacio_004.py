# Sistema de control de inventario

cantidad_producto = 100
contador_entrada = 0
contador_salida = 0
unidades_ingresadas = 0
unidades_retiradas = 0

while True:
    print("===== CONTROL DE INVENTARIO =====")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Consultar inventario")
    print("4. Salir")
    opcion = input("Ingresar opcion valida (1-4): ")
    if opcion == "1":
        entrada = int(input("Ingresar nueva entrada al almacen: "))
        if entrada > 0:
            cantidad_producto += entrada
            unidades_ingresadas += entrada
            contador_entrada += 1
            print("Cantidad ingresada al almacen")
        else:
            print("No se ingreso cantidad porque es cero o negativo")
    elif opcion == "2":
        salida = int(input("Ingresar salida de almacen: "))
        if cantidad_producto >= salida:
            if salida > 0:
                cantidad_producto -= salida
                unidades_retiradas += salida
                contador_salida += 1
                print("Cantidad retirada del almacen")
            else:
                print("No se retiro cantidad porque es cero o negativo")
        else:
            print("No hay suficiente cantidad en el almacen")
    elif opcion == "3":
        print(f"Unidades disponibles: {cantidad_producto}")
    elif opcion == "4":
        print(f"Inventario final: {cantidad_producto}")
        print(f"Operaciones de entrada: {contador_entrada}")
        print(f"Operaciones de salida: {contador_salida}")
        print(f"Unidades ingresadas: {unidades_ingresadas}")
        print(f"Unidades retiradas: {unidades_retiradas}")
        print("¡Hasta luego!")
        break
    else:
        print("Opcion invalida")
    
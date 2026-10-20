# Registro de ventas

suma_total = 0
contador = 0
while True:
    importe_ventas = float(input("Ingrese el importe de ventas o 0 si desea terminar el proceso: "))
    if importe_ventas > 0:
        contador += 1
        suma_total += importe_ventas
    elif importe_ventas == 0: 
        break
    
if contador > 0:
    promedio = suma_total / contador
    print(f"Total vendido: S/. {suma_total}")
    print(f"Ventas registradas: {contador}")
    print(f"Promedio por venta: S/. {promedio}")
else:
    print("No se registraron ventas")

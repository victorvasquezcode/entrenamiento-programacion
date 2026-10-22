#Análisis de ventas por sucursal
while True:
    cantidad_sucursales = int(input("Ingrese la cantidad de sucursales: "))
    if cantidad_sucursales > 0:
        break
    print("No se puede ingresar 0 o numeros negativos")
total_vendido = 0
mayor = 0
mayor_ventas = 0
conteo = 0
resumen_sucursales = ""
for sucursal in range(1, cantidad_sucursales + 1):
    total_vendido_sucursal = 0

    while True:
        cantidad_ventas = int(input(f"Ingrese la cantidad de ventas de la sucursal {sucursal}: "))
        if cantidad_ventas > 0:
            break
        print("No se puede ingresar 0 o numeros negativos")

    for importe in range(1, cantidad_ventas + 1):
        while True:
            importe_venta = float(input(f"Ingrese el {importe} importe: "))
            if importe_venta > 0:
                break
            print("No se puede ingresar 0 o numeros negativos.")

        total_vendido_sucursal += importe_venta
        total_vendido += importe_venta
        conteo += 1

    if sucursal == 1:
        mayor_ventas = total_vendido_sucursal
        mayor = sucursal
    elif total_vendido_sucursal > mayor_ventas:
            mayor_ventas = total_vendido_sucursal
            mayor = sucursal
    
    resumen_sucursales += f"Total sucursal {sucursal}: {total_vendido_sucursal}\n"

print(f"\n{resumen_sucursales}")
promedio = total_vendido / conteo
print(f"Total sucursal general: {total_vendido}\nVentas registradas: {conteo}\nPromedio general: {promedio:.2f}\nSucursal con mayor facturacion: {mayor}")
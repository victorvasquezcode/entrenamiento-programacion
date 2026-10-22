#Analisis de ventas diarias
lista_ventas = []
total_vendido = 0
mayor = 0
dia_mayor = 0
contador_dias = 0
contador = 0
while True:
    dias = int(input("Ingrese los dias que desea registrar las ventas: "))
    if dias > 0:
        break
    print("Dias incorrectos")
for dia in range(1, dias + 1):
    while True:
        ventas_diarias = float(input(f"Ingrese la venta del dia {dia}: "))
        if ventas_diarias >= 0:
            break
        print("Venta invalida")
    lista_ventas.append(ventas_diarias)
for venta in lista_ventas:
    total_vendido += venta
    contador += 1
    if contador == 1:
        mayor = venta
        dia_mayor = contador
    else:
        if venta > mayor:
            mayor = venta
            dia_mayor = contador
promedio = total_vendido / len(lista_ventas)
for venta in lista_ventas:
    if promedio < venta:
        contador_dias += 1    
print(f"\nLista de ventas registradas: {lista_ventas}")
print(f"\nTotal vendido: {total_vendido}\nPromedio diario: {promedio}\nMayor venta: {mayor}\nDía con mayor venta: {dia_mayor}\nDías superiores al promedio: {contador_dias}")
lista_ventas[20]
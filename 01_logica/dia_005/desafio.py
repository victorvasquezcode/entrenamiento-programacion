#Análisis de temperaturas
while True:
    cantidad_mediciones = int(input("Cantidad de mediciones: "))
    if cantidad_mediciones > 0:
        break
    print("Cantidad no puede ser 0 o negativo")
contador_valido = 0
contador_invalido = 0
suma_temperaturas = 0
mayor = 0
menor = 0
for medicion in range(1, cantidad_mediciones + 1):
    temperatura = float(input(f"Ingresa Temperatura {medicion}: "))
    if -50 <= temperatura <= 60:
        contador_valido += 1
        suma_temperaturas += temperatura
        if contador_valido == 1:
            mayor = temperatura
            menor = temperatura
        else:
            if temperatura > mayor:
                mayor = temperatura
            if temperatura < menor:
                menor = temperatura
    else:
        contador_invalido += 1
print(f"\nMediciones validas: {contador_valido}\nMediciones invalidas: {contador_invalido}")
if contador_valido == 0:
    print("No existen temperaturas válidas para calcular estadísticas.")
else:
    promedio = suma_temperaturas / contador_valido
    print(f"Suma de temperaturas: {suma_temperaturas}\nTemperatura promedio: {promedio:.2f}\nTemperatura maxima: {mayor}\nTemperatura minima: {menor}")

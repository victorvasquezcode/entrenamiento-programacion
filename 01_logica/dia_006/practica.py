#Registro de calificaciones
calificaciones = []
suma_calificaciones = 0
contador = 0
maxima = 0
minima = 0

for estudiante in range(1, 6):
    while True:
        calificacion = int(input(f"Calificación del estudiante {estudiante}: "))
        if 0 <= calificacion <= 20:
            break
        print("Calificación inválida")
        
    calificaciones.append(calificacion)

for cali in calificaciones:
    suma_calificaciones += cali
    contador += 1
    if contador == 1:
        maxima = cali
        minima = cali
    elif cali > maxima:
        maxima = cali
    elif cali < minima:
        minima = cali

promedio = suma_calificaciones / len(calificaciones)
print(f"\nLista completa: {calificaciones}")
print(f"\nSuma de calificacion: {suma_calificaciones}\nPromedio: {promedio}\nMaximo: {maxima}\nMinima: {minima}")
# Clasificación de temperaturas

temperatura = float(input("Ingrese la temperatura: "))

if temperatura < -50:
    estado = "Lectura invalida"
elif temperatura < 0:
    estado = "Congelacion"
elif temperatura < 15:
    estado = "Frio"
elif temperatura < 30:
    estado = "Templado"
elif temperatura <= 60:
    estado = "Caluroso"
else:
    estado = "Lectura invalida"

print(estado)
# Clasificador de notas

nota = float(input("Ingrese la nota: "))

if 0 <= nota < 11:
    print("Desaprobado")
elif 11 <= nota < 14:
    print("Regular")
elif 14 <= nota < 18:
    print("Bueno")
elif 18 <= nota <= 20:
    print("Excelente")
else:
    print("Nota invalida")
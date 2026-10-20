# Suma de números consecutivos

while True:
    n = int(input("Ingrese cuantos numeros se calculara su suma: "))
    if n > 0: break

contador = 1
suma_numero = 0
while contador <= n:
    suma_numero += contador
    contador += 1

print(suma_numero)
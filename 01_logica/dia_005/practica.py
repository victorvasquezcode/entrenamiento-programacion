# Suma de números pares

while True:
    n = int(input("Numero para la suma de numeros pares: "))
    if n > 0: 
        break
    print("No se permite 0 o numero negativo")

contador = 0
suma_numeros = 0
for numero in range(1, n + 1):
    if numero % 2 == 0:
        contador += 1
        suma_numeros += numero

print(f"La suma es: {suma_numeros}\nLa cantidad es: {contador}")
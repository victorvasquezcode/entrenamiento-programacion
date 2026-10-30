#
def leer_numeros(ruta):
    numeros = []
    rechazados = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    convertidor = int(linea)
                    numeros.append(convertidor)
                except ValueError:
                    rechazados += 1
    except FileNotFoundError:
        return None
    return numeros, rechazados

resultado = leer_numeros("numeros.txt")
print(resultado)
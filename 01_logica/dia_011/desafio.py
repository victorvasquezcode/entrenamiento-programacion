# Procesador de temperaturas por ciudad.
import math
def validar_temperatura(valor):
    try:
        convertir = float(valor)
        if math.isfinite(convertir) and -50 <= convertir <= 60:
            return convertir
        else:
            return None
    except (ValueError,TypeError):
        return None
def procesar_temperaturas(ruta):
    datos = {}
    rechazados = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                campos = linea.split(";")
                if len(campos) != 2:
                    rechazados += 1
                    continue
                ciudad, temperatura = campos
                normalizar_temperatura = validar_temperatura(temperatura)
                normalizar_ciudad = ciudad.strip().title()
                if not normalizar_ciudad:
                    rechazados += 1
                    continue
                if normalizar_temperatura is not None:
                    if normalizar_ciudad in datos:
                        datos[normalizar_ciudad].append(normalizar_temperatura)
                    else:
                        datos[normalizar_ciudad] = [normalizar_temperatura]
                else:
                    rechazados += 1
    except FileNotFoundError:
        return None
    return datos, rechazados
def calcular_promedios(datos):
    promedio = {}
    total = 0
    if not datos:
        return promedio
    for dato in datos:
        cantidad = len(datos[dato])
        total = sum(datos[dato])
        promedio[dato] = total / cantidad
    return promedio
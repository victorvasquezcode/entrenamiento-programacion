#Sistema de control de calidad de datos
registros = [
    ["TEMP01", 25],
    ["TEMP02", -5],
    ["TEMP01", 30],
    ["TEMP03", 18],
    ["TEMP02", 10],
    ["TEMP01", 100],
    ["TEMP04", -60]
]
def validar_sensor(codigo):
    codigo_limpio = codigo.strip().upper()
    if len(codigo_limpio) == 6 and codigo_limpio[:4].isalpha() and codigo_limpio[-2:].isdigit():
        return codigo_limpio
    else:
        return None
def validar_temperatura(temperatura):
    if type(temperatura) is int and -50 <= temperatura <= 60:
        return True
    else:
        return False
def agrupar_temperatura(registros):
    diccionario_registro = {}
    for registro in registros:
        if len(registro) != 2:
            continue
        sensor_validado = validar_sensor(registro[0])
        temperatura_validada = validar_temperatura(registro[1])
        if sensor_validado is not None and temperatura_validada:
            if sensor_validado in diccionario_registro:
                diccionario_registro[sensor_validado].append(registro[1])
            else:
                diccionario_registro[sensor_validado] = [registro[1]]
    return diccionario_registro
def calcular_promedios(datos):
    promedio = {}
    for dato in datos:
        acumulador = 0
        contador = 0
        for numero in datos[dato]:
            acumulador += numero
            contador += 1
        promedio[dato] = acumulador / contador
    return promedio
def buscar_sensor_mayor(promedios):
    contador = 0
    sensor_mayor = None
    promedio_mayor = 0
    for promedio in promedios:
        contador += 1
        if contador == 1:
            sensor_mayor = promedio
            promedio_mayor = promedios[promedio]
        else:
            if promedios[promedio] > promedio_mayor:
                sensor_mayor = promedio
                promedio_mayor = promedios[promedio]
    return sensor_mayor, promedio_mayor
registros = agrupar_temperatura(registros)
promedio = calcular_promedios(registros)
sensor_mayor , promedio_mayor = buscar_sensor_mayor(promedio)
for registro in registros:
    print(f"{registro}: {registros[registro]}")
print(f"\nPromedios: ")
for prom in promedio:
    print(f"{prom}: {promedio[prom]}")
print(f"\nSensor con mayor promedio: {sensor_mayor}\nPromedio maximo: {promedio_mayor}")
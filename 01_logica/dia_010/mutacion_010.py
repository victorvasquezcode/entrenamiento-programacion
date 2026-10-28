#Limpieza de datos de empleados
import math
empleados = [
    ["EMP01", "Ana", "25", "2500.50"],
    ["EMP02", "Luis", "30", "3200"],
    ["EMP03", "Maria", "abc", "2800"],
    ["EMP04", "Pedro", "45", "x"],
    ["EMP05", "Sofia", "22", "1800"],
    ["EMP06", "Juan", "17", "1500"],
    ["EMP07", "Elena", "35", "4000"],
    ["EMP08", "Carlos", "40"]
]
def validar_empleado(codigo):
    if type(codigo) is str:
        codigo_limpio = codigo.strip().upper()
    else:
        return None
    if len(codigo_limpio) == 5 and codigo_limpio[:3].isalpha() and codigo_limpio[-2:].isdigit():
        return codigo_limpio
    return None

def convertir_edad(valor):
    if type(valor) is bool or type(valor) is float:
        return None
    try:
        convertir_entero = int(valor)
        if 18 <= convertir_entero <= 65:
            return convertir_entero
        else:
            return None
    except (TypeError, ValueError):
        return None

def convertir_salario(valor):
    if type(valor) is bool:
        return None
    try:
        convertir_decimal = float(valor)
        if convertir_decimal > 0 and math.isfinite(convertir_decimal):
            return convertir_decimal
        else:
            return None
    except(TypeError, ValueError):
        return None

def procesar_empleados(empleados):
    datos = {}
    rechazados = 0
    for empleado in empleados:
        if type(empleado) is not list and type(empleado) is not tuple:
            rechazados += 1
            continue
        if len(empleado) != 4:
            rechazados += 1
            continue
        validar_emp = validar_empleado(empleado[0])
        if validar_emp is None:
            rechazados += 1
            continue
        if type(empleado[1]) is str:
            validar_nombre = empleado[1].strip()
        else:
            rechazados += 1
            continue
        if not validar_nombre:
            rechazados += 1
            continue
        validar_edad = convertir_edad(empleado[2])
        if validar_edad is None:
            rechazados += 1
            continue
        validar_salario = convertir_salario(empleado[3])
        if validar_salario is None:
            rechazados += 1
            continue
        if validar_emp in datos:
            rechazados += 1
            continue
        datos[validar_emp] = {
            "nombre": validar_nombre,
            "edad": validar_edad,
            "salario": validar_salario
        }
    return datos, rechazados

def calcular_estadisticas(datos):
    cantidad = 0
    promedio_salarial = 0
    suma_salarial = 0
    codigo_mayor = None
    salario_maximo = 0
    if not datos:
        promedio_salarial = None
        salario_maximo = None
        return cantidad, promedio_salarial,codigo_mayor,salario_maximo
    for dato in datos:
        cantidad += 1
        suma_salarial += datos[dato]["salario"]
        if cantidad == 1:
            codigo_mayor = dato
            salario_maximo = datos[dato]["salario"]
        else:
            if datos[dato]["salario"] > salario_maximo:
                codigo_mayor = dato
                salario_maximo = datos[dato]["salario"]
    promedio_salarial = suma_salarial / cantidad
    return cantidad, promedio_salarial, codigo_mayor, salario_maximo

datos,rechazados = procesar_empleados(empleados)
cantidad, promedio_salarial, codigo_mayor, salario_maximo = calcular_estadisticas(datos)
print(cantidad,promedio_salarial,codigo_mayor,salario_maximo)
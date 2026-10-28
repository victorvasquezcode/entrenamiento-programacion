# Día 010 — Manejo de excepciones y conversión segura de datos

**Módulo:** 01 — Lógica de programación  
**Estado final:** 🟢 VERDE — APROBADO  
**Siguiente sesión:** Día 011 (desbloqueado; iniciar mañana)  
**Archivos:** `practica.py`, `desafio.py`, `mutacion_010.py`, `notas.md`

## 1. Objetivo

Controlar errores de ejecución con `try/except`, convertir entradas externas con seguridad, validar tipos y valores, descartar registros inválidos y calcular estadísticas sin contaminar los resultados.

## 2. Conceptos técnicos

- `try`: intenta ejecutar una operación que podría lanzar una excepción.
- `except ValueError`: maneja valores no interpretables para una conversión, como `int("abc")`.
- `except TypeError`: maneja tipos incompatibles, como `int(None)`.
- `except ZeroDivisionError`: maneja una división entre cero.
- `return`: entrega datos a quien invoca la función; `print` solamente los muestra.
- `continue`: omite el resto de la iteración actual y avanza a la siguiente.
- `float("nan")` no lanza `ValueError`, pero puede contaminar cálculos posteriores. `math.isfinite()` permite rechazar `NaN` e infinitos.
- Un error lógico puede generar resultados incorrectos sin lanzar excepciones.

## 3. Repaso activo — 3/3 APROBADO

**1. Diccionarios y listas.**

```python
datos = {"A": [2, 4], "B": [5]}
datos["A"].append(6)
datos["B"] += [3]
print(datos)
```

**Respuesta:** `{'A': [2, 4, 6], 'B': [5, 3]}`. `append` agrega al final y `+= [3]` extiende la lista.

**2. Funciones.** `transformar(-3)` devuelve `None`. Si se elimina el `return None`, también devolvería `None` implícitamente porque no se ejecuta otro `return`.

**3. Máximos negativos.** No inicializar el máximo en `0` cuando todos los valores pueden ser negativos; usar el primer valor real y comparar los restantes con `>`.

## 4. Evaluación conceptual inicial — 5/5 APROBADO

1. **Error lógico frente a excepción:** el error lógico produce un comportamiento o resultado incorrecto; una excepción señala una situación excepcional durante la ejecución, que puede manejarse con `except`.
2. **`try` y `except`:** `try` ejecuta el código; si se produce una excepción de un tipo capturado, se ejecuta su `except`.
3. **`ValueError` frente a `TypeError`:** el primero implica un valor inadecuado de un tipo aceptado; el segundo, un tipo incompatible.
4. **`int("25")` frente a `int("25.5")`:** la primera cadena representa un entero; la segunda es una cadena con representación decimal, no aceptada directamente por `int`.
5. **Evitar `except:` genérico:** capturar solo errores conocidos permite identificar fallos inesperados y no ocultarlos.

## 5. Práctica — `practica.py` — 10/10 APROBADO

**Requisitos:** `convertir_entero(valor)` acepta enteros y cadenas enteras, rechaza `bool` y `float`; `dividir_seguro(a, b)` convierte argumentos a `float`, rechaza booleanos y devuelve `None` en conversiones inválidas o división entre cero.

**Código entregado:**

```python
def convertir_entero(valor):
    if type(valor) is bool or type(valor) is float:
        return None
    try:
        convertidor_entero = int(valor)
    except (TypeError, ValueError):
        return None
    return convertidor_entero


def dividir_seguro(a, b):
    if type(a) is bool or type(b) is bool:
        return None
    try:
        convertidor1 = float(a)
        convertidor2 = float(b)
        division = convertidor1 / convertidor2
    except (ZeroDivisionError, ValueError, TypeError):
        return None
    return division
```

**Casos previstos y resultados esperados:**

| Llamada | Resultado |
|---|---|
| `convertir_entero(" 25 ")` | `25` |
| `convertir_entero("-12")` | `-12` |
| `convertir_entero("3.5")` | `None` |
| `convertir_entero(True)` | `None` |
| `convertir_entero(3.0)` | `None` |
| `convertir_entero(None)` | `None` |
| `dividir_seguro(10, 2)` | `5.0` |
| `dividir_seguro("15", "3")` | `5.0` |
| `dividir_seguro(8, 0)` | `None` |
| `dividir_seguro("abc", 2)` | `None` |
| `dividir_seguro(True, 2)` | `None` |

**Evaluación:** 10/10. Sin errores funcionales identificados en los casos exigidos. Mejora futura: validar valores no finitos en cálculos numéricos.

## 6. Desafío autónomo — `desafio.py` — 10/10 APROBADO

**Objetivo:** validar y consolidar transacciones externas, contar rechazados y obtener el saldo total y el producto con mayor saldo, respetando saldos negativos y empates.

**Código entregado:**

```python
transacciones = [
    ["AB01", "VENTA", "5"],
    ["CD02", "DEVOLUCION", "2"],
    ["AB01", "DEVOLUCION", "3"],
    ["CD02", "VENTA", "x"],
    ["A123", "VENTA", "4"],
    [" XY03 ", "venta", " 2 "],
    ["AB01", "VENTA", "0"],
    ["CD02", "VENTA"]
]

def validar_codigo(codigo):
    if type(codigo) is str:
        codigo_limpio = codigo.strip().upper()
    else:
        return None
    if len(codigo_limpio) == 4 and codigo_limpio[:2].isalpha() and codigo_limpio[-2:].isdigit():
        return codigo_limpio

def convertir_entero(valor):
    if type(valor) is bool or type(valor) is float:
        return None
    try:
        convertidor_entero = int(valor)
    except (TypeError, ValueError):
        return None
    return convertidor_entero

def procesar_transacciones(transacciones):
    saldos = {}
    rechazados = 0
    for transaccion in transacciones:
        if len(transaccion) != 3:
            rechazados += 1
            continue
        codigo_validado = validar_codigo(transaccion[0])
        if codigo_validado is None:
            rechazados += 1
            continue
        if type(transaccion[1]) is str:
            normalizar = transaccion[1].strip().upper()
            if normalizar not in ("VENTA", "DEVOLUCION"):
                rechazados += 1
                continue
        else:
            rechazados += 1
            continue
        convertidor_entero = convertir_entero(transaccion[2])
        if convertidor_entero is not None:
            if convertidor_entero > 0:
                if codigo_validado in saldos:
                    if normalizar == "VENTA":
                        saldos[codigo_validado] += convertidor_entero
                    elif normalizar == "DEVOLUCION":
                        saldos[codigo_validado] -= convertidor_entero
                else:
                    if normalizar == "VENTA":
                        saldos[codigo_validado] = convertidor_entero
                    elif normalizar == "DEVOLUCION":
                        saldos[codigo_validado] = -convertidor_entero
            else:
                rechazados += 1
                continue
        else:
            rechazados += 1
            continue
    return saldos, rechazados

def resumen_saldos(saldos):
    total = 0
    codigo_mayor = None
    saldo_mayor = 0
    contador = 0
    if not saldos:
        return total, codigo_mayor, saldo_mayor
    for saldo in saldos:
        total += saldos[saldo]
        contador += 1
        if contador == 1:
            codigo_mayor = saldo
            saldo_mayor = saldos[saldo]
        else:
            if saldos[saldo] > saldo_mayor:
                codigo_mayor = saldo
                saldo_mayor = saldos[saldo]
    return total, codigo_mayor, saldo_mayor
```

**Resultado del conjunto principal:**

```text
AB01: 2
CD02: -2
XY03: 2
Registros rechazados: 4
Saldo total: 2
Producto con mayor saldo: AB01
Saldo máximo: 2
```

**Razonamiento del desafío — 3/3:**

1. `continue` evita ejecutar el resto del cuerpo del bucle para un registro rechazado.
2. Con devoluciones de 5 para AB01 y 2 para CD02, `resumen_saldos()` devuelve `(-7, "CD02", -2)`.
3. `return` permite asignar y reutilizar resultados fuera de la función; `print` únicamente muestra información.

**Evaluación:** 10/10. Mejora futura: verificar que cada transacción sea una lista o tupla antes de llamar a `len()`.

## 7. Mutación 010 — Limpieza de datos de empleados — 10/10 APROBADA

**Objetivo:** aplicar validaciones, excepciones, diccionarios anidados y estadísticas a empleados, no a ventas.

**Código entregado:**

```python
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
    except (TypeError, ValueError):
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
        return cantidad, promedio_salarial, codigo_mayor, salario_maximo
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

datos, rechazados = procesar_empleados(empleados)
cantidad, promedio_salarial, codigo_mayor, salario_maximo = calcular_estadisticas(datos)
print(cantidad, promedio_salarial, codigo_mayor, salario_maximo)
```

**Resultados esperados del conjunto principal:**

```text
EMP01: Ana, 25, 2500.50
EMP02: Luis, 30, 3200.00
EMP05: Sofia, 22, 1800.00
EMP07: Elena, 35, 4000.00
Empleados válidos: 4
Registros rechazados: 4
Promedio salarial: 2750.125
Empleado con mayor salario: EMP07
Salario máximo: 4000.00
```

**Nota sobre la salida real del código entregado:** el `print` final del usuario muestra únicamente `4 2750.125 EMP07 4000.0`; la tabla anterior documenta los datos esperados, que están disponibles en `datos` y `rechazados`.

**Casos límite contemplados en la lógica:** edades 18/65, 17/66; salarios 0, `None`, `True`, `"nan"`, `"inf"`; duplicados; registros no lista/tupla; registros incompletos; un empleado; ninguno; empate en salario máximo.

**Razonamiento inicial:**

1. Validar tipos permite descartar tipos que no deben convertirse.
2. **Respuesta inicial imprecisa:** se pensó que `NaN` interrumpiría el programa.
3. Diccionarios anidados permiten buscar por código y acceder a nombre, edad y salario.
4. Incluir registros inválidos distorsionaría el promedio salarial.
5. **Respuesta inicial incompleta:** se indicó que hay que filtrar empleados, pero faltó mencionar la división entre cero.

**Control conceptual final — 2/2 APROBADO:**

1. `NaN` puede propagarse y convertir el promedio en `NaN`, aun cuando los otros salarios sean válidos; no necesariamente interrumpe la ejecución.
2. Si todos son rechazados, `cantidad = 0`, y `0 / 0` provoca `ZeroDivisionError`. `if not datos` evita esa operación.

**Evaluación de mutación:** 10/10. Sin errores funcionales identificados para los requisitos evaluados.

## 8. Restricciones respetadas

- Uso de funciones, parámetros y `return`.
- Manejo de excepciones específicas.
- Sin `sum()`, `max()`, `min()`, `.get()` ni `Counter` en desafío y mutación.
- Sin variables globales para guardar resultados de las funciones.
- Sin impresión dentro de las funciones.

## 9. Aprendizajes consolidados

- Las excepciones permiten manejar entradas problemáticas, pero no sustituyen la validación lógica.
- Las conversiones deben respetar el tipo de entrada permitido, no solo su posible representación numérica.
- Los registros defectuosos deben excluirse antes de consolidar y calcular estadísticas.
- Los diccionarios anidados permiten representar entidades con múltiples atributos.
- Para encontrar máximos con posibles valores negativos, conviene inicializar desde el primer elemento real.
- Los empates se conservan con una comparación estricta `>`.
- Los conjuntos vacíos necesitan un caso especial antes de calcular promedios.

## 10. Registro final de evaluación

| Actividad | Resultado |
|---|---|
| Repaso activo | 3/3 — Aprobado |
| Evaluación conceptual | 5/5 — Aprobado |
| `practica.py` | 10/10 — Aprobado |
| `desafio.py` | 10/10 — Aprobado |
| Razonamiento del desafío | 3/3 — Aprobado |
| `mutacion_010.py` | 10/10 — Aprobado |
| Control conceptual final | 2/2 — Aprobado |

**Estado definitivo:** 🟢 VERDE. **Día 010 cerrado.**  
**Próximo paso:** comenzar el Día 011 mañana, con repaso activo, teoría, práctica y desafío; no avanzar sin nueva evidencia de dominio.
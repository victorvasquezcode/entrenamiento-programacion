# Día 009 — Funciones en Python

**Ruta:** Python desde cero → Ciencia e Ingeniería de Datos  
**Estado final:** 🟢 VERDE — APROBADO  
**Archivos:** `practica.py`, `desafio.py`, `mutacion_009.py`, `notas.md`

## 1. Objetivo del día

Dividir problemas en funciones pequeñas y reutilizables, utilizar parámetros y argumentos, devolver resultados con `return` y evitar depender de variables globales para almacenar resultados.

## 2. Repaso activo — Temas VERDES

**Pregunta 1 — Listas**

```python
numeros = [2, 4, 6]
numeros.append(numeros[0] + numeros[-1])
print(numeros)
```

**Mi respuesta:** `[2, 4, 6, 8]`. **Correcta.**

**Pregunta 2 — Cadenas**

```python
codigo = "  ab12  ".strip().upper()
print(codigo[:2].isalpha())
print(codigo[2:].isdigit())
```

**Mi respuesta:** `codigo` queda como `"AB12"` y se imprime `True` y `True`. **Correcta.**

**Pregunta 3 — Diccionarios**

```python
ventas = {"AB01": 5, "CD02": 3}
ventas["AB01"] -= 7
print(ventas)
print(len(ventas))
```

**Mi respuesta:** `{'AB01': -2, 'CD02': 3}` y `2`. **Correcta.** La cantidad de claves no cambia al actualizar un valor.

**Resultado del repaso:** **3/3 — APROBADO.**

## 3. Concepto técnico breve

Una **función** es un bloque de código reutilizable que realiza una tarea concreta.

```python
def duplicar(numero):
    resultado = numero * 2
    return resultado

valor = duplicar(5)
print(valor)
```

- `def`: define una función.
- **Parámetro:** nombre definido en la firma de la función (`numero`).
- **Argumento:** valor proporcionado al llamar la función (`5`).
- `return`: devuelve un resultado a quien llamó la función y finaliza su ejecución.
- `print()`: muestra información, pero no equivale a devolverla.
- Una función sin `return` explícito devuelve `None`.
- Recibir dependencias por parámetros hace más fácil probar y reutilizar funciones.

## 4. Ejercicio práctico — Validación y transformación

**Archivo:** `practica.py`  
**Estado:** APROBADO — **10/10**

### Problema

Implementar dos funciones independientes para validar códigos de producto y transformar movimientos comerciales.

### Entrada

- `codigo`: cadena de texto.
- `tipo`: cadena de texto.
- `unidades`: entero positivo.

### Proceso

- Normalizar el código con `strip().upper()`.
- Comprobar que el código tenga cuatro caracteres: dos letras y dos dígitos.
- Normalizar el tipo de movimiento.
- Validar que las unidades sean enteras positivas.
- Devolver unidades positivas para `VENTA`, negativas para `DEVOLUCION` y `None` para entradas inválidas.

### Salida

- `validar_codigo`: código normalizado válido o `None`.
- `calcular_movimiento`: unidades con signo o `None`.

### Código desarrollado

```python
# Validación y transformación
def validar_codigo(codigo: str):
    codigo_limpio = codigo.strip().upper()
    if len(codigo_limpio) == 4 and codigo_limpio[:2].isalpha() and codigo_limpio[2:].isdigit():
        return codigo_limpio
    else:
        return None


def calcular_movimiento(tipo: str, unidades: int):
    normalizar_tipo = tipo.strip().upper()
    if normalizar_tipo == "VENTA" and isinstance(unidades, int) and unidades > 0:
        return unidades
    elif normalizar_tipo == "DEVOLUCION" and isinstance(unidades, int) and unidades > 0:
        return -unidades
    else:
        return None


print(validar_codigo(" ab01 "))
print(validar_codigo("A123"))
print(validar_codigo("CD99"))
print(calcular_movimiento("venta", 8))
print(calcular_movimiento("DEVOLUCION", 3))
print(calcular_movimiento("VENTA", 0))
print(calcular_movimiento("OTRO", 5))
```

### Casos de prueba

| Función | Argumentos | Retorno esperado |
|---|---|---|
| `validar_codigo` | `" ab01 "` | `"AB01"` |
| `validar_codigo` | `"A123"` | `None` |
| `validar_codigo` | `"CD99"` | `"CD99"` |
| `calcular_movimiento` | `"venta", 8` | `8` |
| `calcular_movimiento` | `"DEVOLUCION", 3` | `-3` |
| `calcular_movimiento` | `"VENTA", 0` | `None` |
| `calcular_movimiento` | `"OTRO", 5` | `None` |

**Evaluación:** siete casos correctos según la revisión del código.  
**Observación:** `isinstance(True, int)` es `True`; para rechazar booleanos se requiere una comprobación más estricta. No era requisito de esta práctica.

## 5. Desafío autónomo — Procesador de transacciones

**Archivo:** `desafio.py`  
**Estado:** APROBADO — **10/10**

### Problema

Procesar registros comerciales, ignorar los inválidos, consolidar saldos netos por producto y calcular estadísticas mediante funciones reutilizables.

### Entrada

```python
movimientos = [
    ["AB01", "DEVOLUCION", 5],
    ["CD02", "DEVOLUCION", 2],
    ["AB01", "VENTA", 2],
    ["CD02", "VENTA", 1],
    ["XY03", "DEVOLUCION", 1]
]
```

### Proceso

- Validar códigos y movimientos usando funciones reutilizables.
- Omitir registros que no tengan tres campos o cuyos valores sean inválidos.
- Acumular los movimientos válidos en un diccionario por producto.
- Calcular el saldo neto total recorriendo el diccionario.
- Buscar el mayor saldo tomando el primer valor real como referencia y conservando el primero ante empates.

### Salida esperada

```text
AB01: -3
CD02: -1
XY03: -1
Productos diferentes: 3
Saldo neto total: -5
Producto con mayor saldo: CD02
Saldo máximo: -1
```

### Código desarrollado

```python
# Procesador de transacciones
movimientos = [
    ["AB01", "DEVOLUCION", 5],
    ["CD02", "DEVOLUCION", 2],
    ["AB01", "VENTA", 2],
    ["CD02", "VENTA", 1],
    ["XY03", "DEVOLUCION", 1]
]


def validar_codigo(codigo: str):
    codigo_limpio = codigo.strip().upper()
    if len(codigo_limpio) == 4 and codigo_limpio[:2].isalpha() and codigo_limpio[2:].isdigit():
        return codigo_limpio
    else:
        return None


def calcular_movimiento(tipo: str, unidades: int):
    normalizar_tipo = tipo.strip().upper()
    if normalizar_tipo == "VENTA" and isinstance(unidades, int) and unidades > 0:
        return unidades
    elif normalizar_tipo == "DEVOLUCION" and isinstance(unidades, int) and unidades > 0:
        return -unidades
    else:
        return None


def consolidar_movimientos(movimientos):
    mov = {}
    for movimiento in movimientos:
        if len(movimiento) != 3:
            continue
        codigo_validado = validar_codigo(movimiento[0])
        movimiento_validado = calcular_movimiento(movimiento[1], movimiento[2])
        if codigo_validado != None and movimiento_validado != None:
            if codigo_validado in mov:
                mov[codigo_validado] += movimiento_validado
            else:
                mov[codigo_validado] = movimiento_validado
    return mov


def calcular_total(saldos):
    total = 0
    for saldo in saldos:
        total += saldos[saldo]
    return total


def buscar_mayor(saldos):
    contar = 0
    producto_mayor = None
    saldo_mayor = 0
    for saldo in saldos:
        contar += 1
        if contar == 1:
            producto_mayor = saldo
            saldo_mayor = saldos[saldo]
        else:
            if saldos[saldo] > saldo_mayor:
                producto_mayor = saldo
                saldo_mayor = saldos[saldo]
    return producto_mayor, saldo_mayor


saldos = consolidar_movimientos(movimientos)
producto_mayor, saldo_mayor = buscar_mayor(saldos)
for saldo in saldos:
    print(f"{saldo} : {saldos[saldo]}")
print(f"\nProducto diferentes: {len(saldos)}\nSaldo neto total: {calcular_total(saldos)}\nProducto con mayor saldo: {producto_mayor}\nSaldo maximo: {saldo_mayor}")
```

### Casos límite requeridos

- Un solo registro.
- Todos los saldos negativos.
- Productos empatados.
- Registros inválidos que deben ignorarse.

**Evaluación:** lógica aprobada; resultados del caso principal correctos.  
**Mejora opcional:** validar tipos de código y movimiento antes de aplicar `.strip()` cuando se reciban datos externos heterogéneos.

## 6. Evaluación conceptual

**1. ¿Cuál es la diferencia entre un parámetro y un argumento?**  
**Mi respuesta:** El parámetro es la referencia al valor que se le da a la función; el argumento es ese valor que se proporciona para ejecutarla. **Correcta.**

**2. ¿Qué diferencia existe entre `print()` y `return`?**  
**Mi respuesta:** `print()` muestra el valor en consola; `return` devuelve un valor para usarlo fuera de la función. **Correcta.**

**3. ¿Qué sucede cuando una función no tiene `return`?**  
**Mi respuesta:** Devuelve `None`. **Correcta.**

**4. ¿Por qué conviene dividir un programa grande en funciones pequeñas?**  
**Mi respuesta:** Para que sea más fácil de entender y reutilizar. **Correcta.**

**5. ¿Qué ventaja tiene una función con parámetros frente a variables globales?**  
**Mi respuesta:** Los parámetros permiten manejar los datos con mayor facilidad; las variables globales crean dependencias externas. **Correcta con precisión:** una función puede leer una variable global directamente, pero recibir sus dependencias como parámetros facilita reutilizarla y probarla.

**Resultado:** **5/5 — APROBADO.**

## 7. Plan de estudio — Bloques de 50 minutos

| Bloque | Objetivo | Actividad |
|---|---|---|
| 1 — 50 min | Comprender funciones | Repaso activo, concepto y preguntas conceptuales |
| 2 — 50 min | Aplicar funciones | Desarrollar y comprobar `practica.py` |
| 3 — 50 min | Resolver autónomamente | Desarrollar `desafio.py` y probar casos límite |

## 8. Mutación 009 — Sistema de control de calidad de datos

**Archivo:** `mutacion_009.py`  
**Estado:** APROBADO — **10/10**

### Problema

Validar registros de sensores de temperatura, ignorar los inválidos, agrupar las mediciones válidas por sensor y calcular promedios mediante funciones reutilizables.

### Entrada

```python
registros = [
    ["TEMP01", 25],
    ["TEMP02", -5],
    ["TEMP01", 30],
    ["TEMP03", 18],
    ["TEMP02", 10],
    ["TEMP01", 100],
    ["TEMP04", -60]
]
```

### Proceso

- Normalizar y validar cada código de sensor: cuatro letras seguidas de dos dígitos.
- Aceptar solo temperaturas de tipo `int` entre `-50` y `60`, inclusive; rechazar booleanos.
- Omitir registros inválidos y agrupar temperaturas por sensor en listas.
- Calcular el promedio de cada lista mediante acumulador y contador.
- Buscar el mayor promedio conservando el primer sensor en caso de empate.

### Salida esperada

```text
TEMP01: [25, 30]
TEMP02: [-5, 10]
TEMP03: [18]
Promedios:
TEMP01: 27.5
TEMP02: 2.5
TEMP03: 18.0
Sensor con mayor promedio: TEMP01
Promedio máximo: 27.5
```

### Código desarrollado

```python
# Sistema de control de calidad de datos
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
sensor_mayor, promedio_mayor = buscar_sensor_mayor(promedio)
for registro in registros:
    print(f"{registro}: {registros[registro]}")
print(f"\nPromedios: ")
for prom in promedio:
    print(f"{prom}: {promedio[prom]}")
print(f"\nSensor con mayor promedio: {sensor_mayor}\nPromedio maximo: {promedio_mayor}")
```

### Preguntas de razonamiento

**1. ¿Por qué utilizar una lista por sensor?**  
**Mi respuesta:** Porque cada clave puede almacenar varias mediciones. **Correcta.**

**2. ¿Cómo calcular el promedio sin `sum()`?**  
**Mi respuesta:** Recorrer las mediciones, acumularlas y dividir entre un contador. **Correcta.**

**3. ¿Por qué iniciar el máximo en `0` puede ser incorrecto?**  
**Mi respuesta inicial:** Es mejor `None` porque será una cadena. **Corrección conceptual:** `sensor_mayor` es una cadena, pero `promedio_mayor` es numérico. Si todos los promedios son negativos, compararlos directamente contra cero produce un máximo incorrecto. En mi código sí tomo el primer promedio real antes de comparar.

**4. ¿Qué diferencia hay entre validar y agrupar?**  
**Mi respuesta:** Validar comprueba el tipo y rango de la temperatura; agrupar utiliza esa validación para construir el diccionario. **Correcta.**

**5. ¿Cómo evitar que temperaturas inválidas alteren el promedio?**  
**Mi respuesta:** Excluirlas durante la agrupación para que no lleguen al cálculo. **Correcta.**

**Resultado conceptual de la mutación:** **4/5**, con la confusión corregida.

### Casos límite exigidos

- Un sensor con una medición válida.
- Todos los promedios negativos.
- Dos sensores empatados en el promedio máximo.
- Un sensor con varias mediciones.
- Registros inválidos.
- Temperaturas límite `-50` y `60`.
- Valores booleanos `True` y `False` rechazados.

**Resultado de evaluación:** código **10/10 — APROBADO**. La revisión confirmó la lógica del caso principal y de los requisitos. No se aportó un registro independiente de ejecuciones de todos los casos límite.

**Mejoras opcionales:** respetar el nombre solicitado `agrupar_temperaturas` (el código usa `agrupar_temperatura`); validar que los códigos sean cadenas antes de `.strip()`; considerar listas vacías si `calcular_promedios` se utilizara con datos externos.

## 9. Aprendizajes del Día 009

- Definir funciones con `def` y parámetros.
- Distinguir parámetros de argumentos.
- Diferenciar mostrar con `print()` y devolver con `return`.
- Conectar funciones mediante los valores devueltos.
- Validar, transformar, agrupar y analizar datos por etapas.
- Utilizar diccionarios de listas para conservar múltiples mediciones por clave.
- Calcular totales y promedios sin funciones agregadas incorporadas.
- Encontrar máximos correctamente con números negativos y empates.
- Rechazar booleanos cuando se requieren enteros exactos.
- Diseñar funciones que no dependan de variables globales para guardar resultados.

## 10. Errores identificados y correcciones

1. **Concepto de máximos:** confusión entre el identificador del elemento máximo (`sensor_mayor`) y el valor numérico máximo (`promedio_mayor`). **Corrección:** tomar el primer valor real como referencia antes de comparar, especialmente si puede ser negativo.
2. **Tipos en validaciones:** `isinstance(True, int)` devuelve `True`. **Aprendizaje:** `type(valor) is int` permite excluir booleanos cuando es necesario.
3. **Robustez:** `.strip()` supone que la entrada es una cadena; para fuentes externas conviene comprobar el tipo antes de usar métodos de texto.
4. **Nombres de funciones:** utilizar exactamente los nombres requeridos por el enunciado para facilitar su reutilización y evaluación automática.

## 11. Semáforo y progreso final

| Actividad | Resultado |
|---|---|
| Días 001–008 | 🟢 VERDE |
| Repaso activo 009 | 3/3 — APROBADO |
| Evaluación conceptual 009 | 5/5 — APROBADO |
| `practica.py` | 10/10 — APROBADO |
| `desafio.py` | 10/10 — APROBADO |
| `mutacion_009.py` | 10/10 — APROBADO |
| **Día 009 — Funciones** | **🟢 VERDE** |
| Día 010 | Desbloqueado; pendiente de iniciar |

**Cierre del día:** nueve días completados. Mañana corresponde iniciar el Día 010 en 🔴 ROJO, con un nuevo tema y repaso activo de conocimientos anteriores.
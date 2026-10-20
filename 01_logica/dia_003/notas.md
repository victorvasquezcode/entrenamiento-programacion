# Día 003 — Condicionales y control de flujo

**Módulo:** 01 — Lógica de programación  
**Estado:** 🟢 VERDE  
**Concepto:** `if`, `elif`, `else`, rangos, orden de evaluación y simplificación de condiciones.

---

## 1. Concepto aprendido

Las estructuras condicionales permiten ejecutar distintos bloques de código según una condición:

- `if`: comprueba la primera condición.
- `elif`: comprueba otra condición solo si las anteriores fueron falsas.
- `else`: se ejecuta si ninguna condición anterior fue verdadera.

En una cadena `if / elif / else`, **solo se ejecuta la primera rama cuya condición sea verdadera**. En cambio, varios `if` independientes pueden ejecutar más de un bloque.

El orden de las condiciones depende de la lógica del problema, no de su complejidad. Además, cada condición falsa descarta valores, lo que permite simplificar las siguientes. Por ejemplo, después de comprobar `temperatura < -50`, un `elif temperatura < 0` ya implica que la temperatura es al menos -50.

---

## 2. Ejercicio práctico — Clasificador de notas

**Archivo:** `practica.py`

### Problema

Solicitar una nota decimal y clasificarla según su rango.

### Entrada

- `nota`: número decimal.

### Proceso

1. De 0 a menos de 11: `Desaprobado`.
2. De 11 a menos de 14: `Regular`.
3. De 14 a menos de 18: `Bueno`.
4. De 18 a 20: `Excelente`.
5. Fuera del rango de 0 a 20: `Nota invalida`.

### Condiciones utilizadas

```python
0 <= nota < 11
11 <= nota < 14
14 <= nota < 18
18 <= nota <= 20
```

### Código desarrollado

```python
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
```

### Salida

Una clasificación: `Desaprobado`, `Regular`, `Bueno`, `Excelente` o `Nota invalida`.

### Casos de prueba

| Nota | Resultado esperado |
|---:|---|
| 8 | Desaprobado |
| 12 | Regular |
| 16 | Bueno |
| 19 | Excelente |
| -1 | Nota invalida |
| 21 | Nota invalida |

### Aprendizajes

- Puedo clasificar números usando rangos y operadores de comparación.
- Una cadena condicional ejecuta solo la primera rama verdadera.
- Conviene probar valores límite y valores fuera del rango permitido.
- Algunas comparaciones son redundantes si las condiciones previas ya descartaron esos valores.

**Evaluación:** Aprobado.

---

## 3. Desafío autónomo — Sistema de tarifas de estacionamiento

**Archivo:** `desafio.py`

### Problema

Determinar la tarifa fija de un estacionamiento según las horas utilizadas.

### Entrada

- `numero_horas`: número entero.

### Proceso

1. De 1 a 2 horas: S/ 5.
2. De 3 a 5 horas: S/ 10.
3. De 6 a 10 horas: S/ 20.
4. Más de 10 horas: S/ 30.
5. Cero o menos horas: `Error`.

### Condiciones utilizadas

```python
1 <= numero_horas <= 2
3 <= numero_horas <= 5
6 <= numero_horas <= 10
numero_horas > 10
numero_horas <= 0
```

### Código desarrollado

```python
numero_horas = int(input("Ingrese el numero de horas de estacionamiento: "))

total = 0

if 1 <= numero_horas <= 2:
    total += 5
    print(f"S/{total}")
elif 3 <= numero_horas <= 5:
    total += 10
    print(f"S/{total}")
elif 6 <= numero_horas <= 10:
    total += 20
    print(f"S/{total}")
elif numero_horas > 10:
    total += 30
    print(f"S/{total}")
elif numero_horas <= 0:
    print("Error")
```

### Salida

Tarifa en soles o mensaje de error.

### Casos de prueba

| Horas | Resultado esperado |
|---:|---|
| 0 | Error |
| 1 | S/ 5 |
| 2 | S/ 5 |
| 3 | S/ 10 |
| 5 | S/ 10 |
| 7 | S/ 20 |
| 10 | S/ 20 |
| 13 | S/ 30 |

### Aprendizajes

- Una cadena `if / elif / else` permite seleccionar una tarifa según el rango.
- `total = 10` asigna un valor fijo; `total += 10` acumula sobre el valor anterior.
- Para tarifas fijas, una asignación directa expresa mejor la intención.
- Repetir `print()` en cada rama es válido, pero puede simplificarse guardando primero el resultado.

**Evaluación:** Aprobado.

---

## 4. Mutación 003 — Clasificación de temperaturas

**Archivo:** `mutacion_003.py`

### Problema

Clasificar una temperatura decimal según rangos definidos por una estación meteorológica.

### Entrada

- `temperatura`: número decimal.

### Proceso

1. Menor de -50 °C: lectura inválida.
2. Desde -50 °C hasta menos de 0 °C: congelación.
3. Desde 0 °C hasta menos de 15 °C: frío.
4. Desde 15 °C hasta menos de 30 °C: templado.
5. Desde 30 °C hasta 60 °C: caluroso.
6. Mayor de 60 °C: lectura inválida.

### Condiciones finales

```python
temperatura < -50
temperatura < 0
temperatura < 15
temperatura < 30
temperatura <= 60
```

### Restricciones

- Utilizar `if`, `elif` y `else`.
- No anidar condiciones.
- No repetir límites inferiores ya garantizados por condiciones previas.
- Guardar el resultado en `estado`.
- Utilizar un solo `print()` al final.

### Código desarrollado

```python
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
```

### Salida

El texto guardado en `estado`.

### Casos de prueba

| Temperatura | Resultado esperado |
|---:|---|
| -51 | Lectura invalida |
| -50 | Congelacion |
| -1 | Congelacion |
| 0 | Frio |
| 14.9 | Frio |
| 15 | Templado |
| 30 | Caluroso |
| 60 | Caluroso |
| 61 | Lectura invalida |

### Error identificado

En la evaluación conceptual inicial pensé que las condiciones más complicadas debían colocarse primero. Corregí ese criterio: **las condiciones se ordenan según los rangos y la lógica del problema**.

### Aprendizajes

- Una condición falsa reduce el conjunto de valores posibles para las siguientes.
- Puedo omitir comparaciones redundantes si el orden garantiza el límite inferior.
- Guardar la clasificación en una variable permite usar un único `print()`.
- Simplificar condiciones no significa omitir validaciones necesarias.

**Evaluación:** Mutación aprobada. 🟢

---

## 5. Control verde — Repaso activo

### Control 001 — Pensamiento algorítmico

**Problema:** Un trabajador gana S/ 12 por hora normal y S/ 18 por cada hora que exceda 40 horas.

- **Entrada:** horas trabajadas.
- **Proceso:** pagar las primeras 40 horas a S/ 12 y las adicionales a S/ 18.
- **Salida:** remuneración semanal.

**Caso de 43 horas:** `40 × 12 + 3 × 18 = 480 + 54 = S/ 534`.

**Aprendizaje:** Conviene resolver y explicar el algoritmo antes de programar.

**Estado:** 🟢 Aprobado.

### Control 002 — Operadores lógicos

```python
edad = 17
autorizado = True
suspendido = False

resultado = (
    (edad >= 18 or autorizado)
    and not suspendido
)

print(resultado)
```

**Razonamiento:** `(False or True) and not False` → `True and True` → `True`.

**Salida:** `True`.

**Estado:** 🟢 Aprobado.

---

## 6. Errores y lecciones importantes

1. **Orden de condiciones:** no colocar primero la condición aparentemente más compleja, sino la que corresponda a la lógica de los rangos.
2. **Comparaciones redundantes:** revisar qué valores ya fueron descartados antes de escribir el siguiente `elif`.
3. **Asignación frente a acumulación:** usar `=` para establecer un valor y `+=` cuando deba sumarse al existente.
4. **Repetición de código:** guardar un resultado y mostrarlo al final puede ser más claro que imprimirlo en cada rama.

---

## 7. Reflexión personal

Aprendí a tomar decisiones con `if`, `elif` y `else`, a organizar correctamente los rangos y a comprender por qué una condición puede simplificarse cuando las anteriores ya descartaron ciertos valores. También reforcé la diferencia entre asignar y acumular, y la importancia de escribir código claro, no solo funcional.

**Resultado final:** Día 003 🟢 VERDE.  
**Próximo tema:** Día 004 — Bucles `while` y repetición controlada.
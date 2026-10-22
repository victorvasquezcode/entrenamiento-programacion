# Día 004 — Bucles `while` y repetición controlada

**Módulo:** 01 — Lógica de programación  
**Estado:** 🟢 VERDE  
**Concepto:** bucles `while`, condiciones de terminación, `break`, contadores, acumuladores y validación de operaciones.

---

## 1. Concepto aprendido

Un bucle `while` repite un bloque de instrucciones **mientras su condición sea verdadera**. La condición se evalúa antes de cada iteración, por lo que el bloque puede ejecutarse cero veces.

En un bucle controlado por contador suelen intervenir:

1. **Inicialización:** establecer el valor inicial del contador.
2. **Condición:** determinar si el bucle continúa.
3. **Actualización:** cambiar el contador para avanzar hacia la terminación.

```python
contador = 1
while contador <= 3:
    print(contador)
    contador += 1
```

El resultado es `1`, `2` y `3`. Cuando `contador` llega a 4, la condición es falsa y el bucle termina.

`while True` crea un bucle cuya condición es siempre verdadera; puede finalizar mediante `break`. Si la condición nunca se vuelve falsa y no se ejecuta una salida como `break`, se produce un bucle infinito.

**Contador:** registra cuántas veces ocurre algo (`contador += 1`).  
**Acumulador:** suma cantidades (`suma_total += importe`).

---

## 2. Ejercicio práctico — Suma de números consecutivos

**Archivo:** `practica.py`

### Problema

Solicitar un entero positivo `n` y sumar los números desde 1 hasta `n`.

### Entrada

- `n`: número entero positivo.

### Proceso

1. Solicitar `n` repetidamente hasta que sea mayor que cero.
2. Inicializar `contador = 1` y `suma_numero = 0`.
3. Mientras `contador <= n`, sumar el contador al acumulador.
4. Aumentar el contador en una unidad por iteración.
5. Mostrar la suma final.

### Condiciones utilizadas

```python
if not n <= 0:
    break

while contador <= n:
    ...
```

La expresión `not n <= 0` equivale a `n > 0`.

### Salida

La suma de todos los enteros desde 1 hasta `n`.

### Casos de prueba

| Entrada | Resultado esperado |
|---|---:|
| 1 | 1 |
| 3 | 6 |
| 5 | 15 |
| 10 | 55 |
| 0 → 4 | 10, después de volver a solicitar |
| -3 → 2 | 3, después de volver a solicitar |

### Aprendizajes

- **Variable de control:** `contador`.
- **Acumulador:** `suma_numero`.
- **Actualización:** `suma_numero` y `contador` cambian en cada iteración.
- **Sin actualizar el contador:** el segundo `while` no termina para una entrada positiva.
- Puedo utilizar un `while` para validar entradas y otro para realizar un cálculo.
- `if n > 0` es más legible que `if not n <= 0`.

**Evaluación:** Aprobado.

---

## 3. Desafío autónomo — Registro de ventas

**Archivo:** `desafio.py`

### Problema

Registrar importes de ventas hasta que el usuario introduzca `0`, ignorar importes negativos y calcular estadísticas.

### Entrada

- `importe_ventas`: número decimal.

### Proceso

1. Inicializar `suma_total` y `contador` en cero.
2. Solicitar importes dentro de un `while True`.
3. Si el importe es positivo, sumarlo al total y aumentar el contador.
4. Si el importe es cero, terminar el bucle con `break`.
5. Si el importe es negativo, ignorarlo y continuar.
6. Si hay ventas válidas, calcular `suma_total / contador`.
7. Si no hay ventas válidas, mostrar el mensaje correspondiente sin dividir entre cero.

### Condiciones utilizadas

```python
if importe_ventas > 0:
    ...
elif importe_ventas == 0:
    break

if contador > 0:
    ...
else:
    ...
```

### Salida

Total vendido, cantidad de ventas válidas y promedio; o `No se registraron ventas`.

### Casos de prueba

| Entradas | Total | Ventas válidas | Promedio |
|---|---:|---:|---:|
| `10, 20, -5, 30, 0` | S/ 60 | 3 | S/ 20 |
| `0` | — | 0 | Mensaje: No se registraron ventas |
| `-10, -20, 50, 0` | S/ 50 | 1 | S/ 50 |

### Aprendizajes

- **¿Cómo solicitar ventas sin conocer cuántas habrá?** Con `while True`, hasta recibir el valor centinela `0`.
- **¿Cómo distinguir negativo de cero?** Los positivos se registran, el cero termina y los negativos se ignoran.
- **¿Cuándo aumentar el contador?** Solo después de comprobar que el importe es positivo.
- **¿Cómo evitar dividir entre cero?** Calcular el promedio únicamente si `contador > 0`.
- En aplicaciones monetarias reales, `Decimal` suele ser preferible a `float` para cálculos exactos.

**Evaluación:** Aprobado.

---

## 4. Mutación 004 — Sistema de control de inventario

**Archivo:** `mutacion_004.py`

### Problema

Un almacén inicia con 100 unidades. Debe permitir registrar entradas, registrar salidas, consultar inventario y salir mediante un menú repetitivo.

### Entrada

- `opcion`: texto correspondiente a una opción del menú (`"1"` a `"4"`).
- `entrada`: entero solicitado al registrar una entrada.
- `salida`: entero solicitado al registrar una salida.
- `cantidad_producto`: inventario actual; comienza en 100 y se actualiza internamente.

### Proceso

1. Mostrar el menú dentro de un `while True`.
2. Opción `1`: si la cantidad es positiva, agregarla al inventario, sumar unidades ingresadas y contar una operación válida.
3. Opción `2`: si la cantidad es positiva y no supera el stock, descontarla, sumar unidades retiradas y contar una operación válida.
4. Opción `3`: mostrar el inventario actual.
5. Opción `4`: mostrar el resumen y salir con `break`.
6. Cualquier otra opción: mostrar `Opcion invalida` y repetir el menú.
7. Las operaciones rechazadas no modifican el inventario ni los contadores.

### Condiciones finales

```python
opcion == "1"
opcion == "2"
opcion == "3"
opcion == "4"
entrada > 0
cantidad_producto >= salida
salida > 0
```

### Restricciones

- Utilizar `while` para repetir el menú.
- Utilizar `if`, `elif` y `else`.
- No utilizar `for`, listas ni funciones propias.
- No permitir inventario negativo.
- Contar solo operaciones exitosas.
- Acumular las unidades ingresadas y retiradas.
- Finalizar únicamente mediante la opción 4.

### Salida

Inventario final, número de operaciones válidas de entrada y salida, total de unidades ingresadas y total de unidades retiradas.

### Caso de prueba principal

| Acción | Cantidad | Inventario esperado |
|---|---:|---:|
| Inventario inicial | — | 100 |
| Entrada | 30 | 130 |
| Salida | 20 | 110 |
| Salida rechazada | 150 | 110 |
| Entrada inválida | -5 | 110 |
| Salida | 10 | 100 |
| Salir | — | 100 |

**Resumen esperado:**

```text
Inventario final: 100
Operaciones de entrada: 1
Operaciones de salida: 2
Unidades ingresadas: 30
Unidades retiradas: 30
```

### Error identificado

En la respuesta conceptual inicial mencioné que el inventario debía ser mayor que la salida. La condición correcta permite también la igualdad: `cantidad_producto >= salida`. Mi código ya utilizaba esta comparación correctamente.

### Aprendizajes

- Una operación rechazada no debe modificar los contadores porque no fue exitosa.
- El inventario actual representa las unidades disponibles; `unidades_ingresadas` acumula todas las unidades que entraron durante la sesión.
- Para retirar unidades, debe cumplirse `0 < salida <= cantidad_producto`.
- Una opción inválida ejecuta el `else`, muestra el mensaje y vuelve al menú.
- Puedo combinar `while`, `break`, condiciones, contadores y acumuladores en un programa interactivo.
- Para opciones de menú, comparar cadenas como `"1"` es válido.

**Evaluación:** Mutación aprobada. 🟢

---

## 5. Control verde — Repaso activo

### Control 001 — Pensamiento algorítmico

**Problema:** Un almacén tiene 120 productos, recibe 35 y vende 48.

- **Entrada:** 120, 35 y 48 productos.
- **Proceso:** `120 + 35 - 48`.
- **Salida:** **107 productos**.

**Estado:** 🟢 Aprobado.

### Control 002 — Operadores lógicos

```python
edad = 20
cuenta_activa = True
suspendido = True
autorizacion = True

acceso = (
    edad >= 18
    and cuenta_activa
    and (not suspendido or autorizacion)
)

print(acceso)
```

**Razonamiento:** `True and True and (False or True)` → `True`.

**Salida:** `True`.

**Estado:** 🟢 Aprobado.

### Control 003 — Condicionales

```python
numero = 25

if numero >= 10:
    print("A")
elif numero >= 20:
    print("B")
else:
    print("C")
```

**Salida original:** `A`, porque la primera condición ya es verdadera.

**Corrección para imprimir `B` con 25:**

```python
if numero >= 20:
    print("B")
elif numero >= 10:
    print("A")
else:
    print("C")
```

**Estado:** 🟢 Aprobado.

---

## 6. Evaluación conceptual de `while`

1. **`if` frente a `while`:** `if` decide si se ejecuta un bloque; `while` repite el bloque mientras su condición sea verdadera.
2. **Tres elementos:** inicialización, condición y actualización.
3. **Bucle infinito:** repetición que no termina; se evita haciendo que la condición llegue a ser falsa o utilizando una salida controlada como `break`.
4. **Contador y acumulador:** `contador += 1` cuenta eventos; `suma_total += importe` acumula cantidades.
5. **Cero iteraciones:** `while` comprueba su condición antes de entrar; si es falsa desde el inicio, no ejecuta el bloque.

### Comprobación adicional

**Pregunta A:**

```python
numero = 5
while numero > 5:
    print("Python")
print("Fin")
```

El bucle se ejecuta **0 veces** y solo imprime `Fin`.

**Pregunta B:**

```python
contador = 3
while contador <= 5:
    print(contador)
    contador += 1
```

Realiza **3 iteraciones** e imprime `3`, `4`, `5`.

**Evaluación conceptual:** Aprobada.

---

## 7. Errores y lecciones importantes

1. **Cero iteraciones:** inicialmente no comprendía por qué un `while` podía no ejecutarse. Aprendí que la condición se verifica antes de entrar al bloque.
2. **Comparación de límites:** debo distinguir `>` de `>=`. En inventario se puede retirar exactamente todo el stock disponible.
3. **Legibilidad:** `if n > 0` es más claro que `if not n <= 0`.
4. **Validación de operaciones:** solo debo actualizar inventario, contadores y acumuladores cuando una operación es válida.
5. **Entradas no numéricas:** `int()` y `float()` pueden producir `ValueError` si reciben texto inválido; su manejo queda para una sesión posterior.

---

## 8. Reflexión personal

Aprendí a construir bucles `while` para repetir operaciones sin conocer previamente cuántas veces serán necesarias. Practiqué la validación de entradas, el uso de `break`, los contadores y los acumuladores. Comprendí cómo evitar bucles infinitos y por qué un `while` puede ejecutarse cero veces. En el sistema de inventario combiné estos conceptos con condiciones y reglas de negocio, asegurando que las operaciones inválidas no modificaran los resultados.

**Resultado final:** Día 004 🟢 VERDE.  
**Próximo tema:** Día 005 — Bucles `for` y `range()`.
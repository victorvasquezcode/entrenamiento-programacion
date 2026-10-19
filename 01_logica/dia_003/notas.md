# Día 003 — Condicionales y control de flujo

**Módulo:** 01 — Lógica de programación  
**Estado:** 🟢 VERDE  
**Concepto:** Estructuras condicionales `if`, `elif` y `else`, orden de evaluación, rangos y simplificación de condiciones.

---

## 1. Concepto aprendido

Las estructuras condicionales permiten que un programa tome decisiones dependiendo de si una condición es verdadera o falsa.

En Python existen tres instrucciones principales:

- **`if`:** Evalúa una condición y ejecuta su bloque si es verdadera.
- **`elif`:** Evalúa una condición adicional solamente cuando las condiciones anteriores fueron falsas.
- **`else`:** Ejecuta su bloque cuando ninguna condición anterior se cumple.

### Diferencia entre `if` independientes y `if/elif/else`

Cuando utilizamos varios `if` independientes, Python evalúa cada condición por separado y puede ejecutar varios bloques.

En una cadena `if/elif/else`, Python evalúa las condiciones de arriba hacia abajo y ejecuta únicamente el primer bloque cuya condición sea verdadera.

### Importancia del orden

El orden de las condiciones debe responder a la lógica del problema, no a su complejidad.

Si una condición general aparece antes de otra más específica, puede impedir que la segunda se ejecute.

### Simplificación de condiciones

En una cadena `if/elif/else`, cada condición falsa descarta un conjunto de valores.

Por ejemplo:

```python
if temperatura < -50:
    estado = "Lectura inválida"
elif temperatura < 0:
    estado = "Congelación"
```

Cuando Python llega al `elif`, ya sabe que `temperatura >= -50`, porque la primera condición fue falsa.

Por eso, no es necesario escribir:

```python
elif -50 <= temperatura < 0:
```

**Aprendizaje principal:** Las condiciones anteriores permiten simplificar las siguientes, siempre que estén correctamente ordenadas.

---

## 2. Ejercicio práctico — Clasificador de notas

**Archivo:** `practica.py`

### Problema

Solicitar una nota numérica y clasificarla según el rango correspondiente.

### Entrada

- `nota`: número decimal.

### Proceso

1. Si la nota está entre 0 y menos de 11, clasificar como `Desaprobado`.
2. Si está entre 11 y menos de 14, clasificar como `Regular`.
3. Si está entre 14 y menos de 18, clasificar como `Bueno`.
4. Si está entre 18 y 20, clasificar como `Excelente`.
5. Si está fuera de 0 a 20, clasificar como `Nota inválida`.

### Condiciones utilizadas

```python
0 <= nota < 11
11 <= nota < 14
14 <= nota < 18
18 <= nota <= 20
```

### Salida

Una de las siguientes clasificaciones:

- Desaprobado
- Regular
- Bueno
- Excelente
- Nota inválida

### Casos de prueba

| Nota | Resultado esperado |
|---|---|
| 8 | Desaprobado |
| 12 | Regular |
| 16 | Bueno |
| 19 | Excelente |
| -1 | Nota inválida |
| 21 | Nota inválida |

### Aprendizajes

- Aprendí a utilizar `if`, `elif` y `else` para clasificar valores numéricos.
- Comprendí cómo definir rangos con operadores de comparación.
- Aprendí que una cadena condicional ejecuta únicamente la primera rama verdadera.
- Identifiqué que algunas comparaciones pueden simplificarse aprovechando las condiciones anteriores.
- Comprendí la importancia de comprobar valores límite y entradas fuera del rango permitido.

---

## 3. Desafío autónomo — Sistema de tarifas de estacionamiento

**Archivo:** `desafio.py`

### Problema

Calcular la tarifa total de un estacionamiento según la cantidad de horas utilizadas.

### Entrada

- `numero_horas`: número entero.

### Proceso

1. Entre 1 y 2 horas: tarifa de S/ 5.
2. Entre 3 y 5 horas: tarifa de S/ 10.
3. Entre 6 y 10 horas: tarifa de S/ 20.
4. Más de 10 horas: tarifa de S/ 30.
5. Cero horas o valores negativos: mostrar `Error`.

### Condiciones utilizadas

```python
1 <= numero_horas <= 2
3 <= numero_horas <= 5
6 <= numero_horas <= 10
numero_horas > 10
numero_horas <= 0
```

### Salida

- Tarifa total en soles.
- Mensaje de error para horas no válidas.

### Casos de prueba

| Horas | Resultado esperado |
|---|---|
| 0 | Error |
| 1 | S/ 5 |
| 2 | S/ 5 |
| 3 | S/ 10 |
| 5 | S/ 10 |
| 7 | S/ 20 |
| 10 | S/ 20 |
| 13 | S/ 30 |

### Aprendizajes

- Aprendí a resolver un problema de tarifas utilizando una cadena de condiciones.
- Comprendí que `total += 10` acumula un valor, mientras que `total = 10` realiza una asignación directa.
- Identifiqué que, para tarifas fijas, es más claro asignar directamente el valor correspondiente.
- Aprendí que repetir `print()` en varias ramas puede generar código redundante.
- Comprendí que puedo separar el cálculo de la tarifa de su presentación.
- Reforcé la importancia de comprobar los límites entre rangos.

### Oportunidades de mejora

El programa es correcto para las entradas especificadas, pero puede simplificarse mediante asignaciones directas y una única impresión final para los casos válidos.

---

## 4. Mutación 003 — Clasificación de temperaturas

**Archivo:** `mutacion_003.py`

### Problema

Una estación meteorológica debe clasificar una temperatura de acuerdo con diferentes rangos.

### Entrada

- `temperatura`: número decimal.

### Proceso

1. Menor de -50 °C: `Lectura inválida`.
2. Desde -50 °C hasta menos de 0 °C: `Congelación`.
3. Desde 0 °C hasta menos de 15 °C: `Frío`.
4. Desde 15 °C hasta menos de 30 °C: `Templado`.
5. Desde 30 °C hasta 60 °C: `Caluroso`.
6. Mayor de 60 °C: `Lectura inválida`.

### Condiciones finales

```python
temperatura < -50
temperatura < 0
temperatura < 15
temperatura < 30
temperatura <= 60
```

### Salida

- Clasificación almacenada en la variable `estado`.

### Restricciones

- Utilizar `if`, `elif` y `else`.
- No utilizar condiciones anidadas.
- Evitar límites inferiores redundantes.
- Guardar la clasificación en `estado`.
- Utilizar un único `print()` al final.

### Casos de prueba

| Temperatura | Resultado esperado |
|---|---|
| -51 | Lectura inválida |
| -50 | Congelación |
| -1 | Congelación |
| 0 | Frío |
| 14.9 | Frío |
| 15 | Templado |
| 30 | Caluroso |
| 60 | Caluroso |
| 61 | Lectura inválida |

### Error identificado

En la evaluación conceptual anterior, inicialmente consideré que las condiciones más complicadas debían colocarse primero.

Comprendí que el orden no depende de la complejidad, sino de los rangos y de cómo cada condición descarta valores.

En esta mutación apliqué correctamente ese aprendizaje.

### Aprendizajes

- Aprendí a ordenar condiciones para clasificar rangos sin superposiciones incorrectas.
- Comprendí que una condición falsa proporciona información para las evaluaciones siguientes.
- Aprendí a eliminar comparaciones redundantes.
- Utilicé una variable para almacenar el resultado antes de imprimirlo.
- Aprendí a separar la lógica de decisión de la presentación del resultado.
- Comprendí que simplificar código no significa eliminar validaciones necesarias.

---

## 5. Control verde — Repaso activo



---

## 6. Errores y lecciones importantes

### Lección 001 — Orden incorrecto de condiciones

**Aspecto identificado:** Inicialmente consideré que las condiciones más complicadas debían ir primero.

**Corrección:** Las condiciones deben ordenarse según la lógica del problema y los valores que se desean clasificar.

**Regla preventiva:** Antes de escribir una cadena condicional, revisar qué valores acepta cada rama y cuáles descartan las anteriores.

### Lección 002 — Comparaciones redundantes

**Aspecto identificado:** En el clasificador de notas escribí límites inferiores y superiores en cada condición, aunque algunos ya estaban garantizados.

**Corrección:** En la mutación de temperaturas utilicé condiciones más simples, como `elif temperatura < 15`.

**Regla preventiva:** Preguntarme qué valores ya quedaron descartados antes de agregar una comparación.

### Lección 003 — Diferencia entre asignar y acumular

**Aspecto identificado:** En el estacionamiento utilicé `+=` para asignar tarifas fijas.

**Corrección conceptual:**

- `total = 10` asigna directamente el valor 10.
- `total += 10` suma 10 al valor anterior de `total`.

**Regla preventiva:** Utilizar asignación directa cuando quiero establecer un valor fijo y acumulación cuando necesito sumar al valor existente.

### Lección 004 — Evitar repetición de código

**Aspecto identificado:** En el estacionamiento repetí la instrucción `print()` en diferentes ramas.

**Corrección:** En la mutación almacené la clasificación en `estado` y utilicé un solo `print()` al final.

**Regla preventiva:** Identificar operaciones comunes que pueden realizarse después de la estructura condicional.

---

## 7. Reflexión personal

Durante el Día 003 aprendí a utilizar estructuras condicionales para resolver problemas que requieren tomar decisiones según diferentes rangos.

Al principio podía construir condiciones correctas, pero todavía repetía comparaciones y no comprendía completamente cómo influía el orden de evaluación.

Con la mutación de temperaturas entendí que cada condición anterior descarta valores, lo que permite simplificar las siguientes sin perder precisión.

También aprendí a distinguir entre asignar y acumular valores, y a evitar repetir instrucciones cuando puedo almacenar primero un resultado.
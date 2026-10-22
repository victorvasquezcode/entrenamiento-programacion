# Día 005 — Bucles `for` y `range()`

**Módulo:** 01 — Lógica de programación  
**Estado:** 🟢 VERDE — Aprobado  
**Concepto:** Iteración con `for`, `range()`, bucles anidados, contadores, acumuladores y análisis básico de datos.

---

## 1. Concepto aprendido

Un bucle `for` recorre los elementos de un iterable. `range()` genera una secuencia de enteros cuyo límite final es exclusivo.

```python
for numero in range(5):
    print(numero)
```

**Salida:** `0`, `1`, `2`, `3`, `4` (uno por línea).

- `range(fin)`: empieza en 0 y excluye `fin`.
- `range(inicio, fin)`: comienza en `inicio` y excluye `fin`.
- `range(inicio, fin, paso)`: avanza según `paso` y excluye el límite final.
- `while` repite mientras una condición sea verdadera; `for` recorre elementos de una secuencia o iterable.
- Los bucles anidados permiten procesar grupos y elementos dentro de cada grupo.

---

## 2. Ejercicio práctico — Suma de números pares

**Archivo:** `practica.py`  
**Estado:** ✅ Aprobado

### Problema
Solicitar un entero positivo `n` y calcular la suma y cantidad de números pares entre 1 y `n`, incluyéndolo si es par.

### Entrada
- `n`: número entero positivo.

### Proceso
1. Solicitar `n` hasta que sea mayor que cero.
2. Recorrer de 1 a `n` inclusive con `for numero in range(1, n + 1)`.
3. Comprobar si `numero % 2 == 0`.
4. Incrementar el contador y acumular el número cuando sea par.

### Restricciones
- Utilizar `for` y `range()` para la suma.
- Se permite `while` para validar.
- No utilizar listas, `sum()` ni fórmulas directas.

### Salida
- Suma de los números pares.
- Cantidad de números pares.

### Casos de prueba
| Entrada | Suma esperada | Cantidad de pares |
|---|---:|---:|
| 1 | 0 | 0 |
| 2 | 2 | 1 |
| 5 | 6 | 2 |
| 10 | 30 | 5 |
| 15 | 56 | 7 |
| 0 → 6 | 12 | 3 |
| -3 → 4 | 6 | 2 |

### Preguntas previas y respuestas
1. **¿Cómo recorrer de 1 a `n`?** `range(1, n + 1)` para incluir `n`.
2. **¿Cómo identificar un par?** `numero % 2 == 0`, porque el residuo al dividir entre 2 es cero.
3. **¿Qué variables usar?** `contador = 0` y `suma_numeros = 0`.
4. **¿Por qué `n + 1`?** Porque el límite superior de `range()` es exclusivo.

### Aprendizajes
- El límite superior de `range()` es exclusivo: no significa simplemente «contar un número menos» en todos los casos.
- `break` se lee mejor en una línea independiente.
- El `continue` al final de ese `while` era innecesario; el ciclo vuelve a empezar por sí solo.

---

## 3. Desafío autónomo — Análisis de temperaturas

**Archivo:** `desafio.py`  
**Estado:** ✅ Aprobado

### Problema
Registrar una cantidad determinada de temperaturas y calcular estadísticas únicamente con las mediciones válidas.

### Entrada
- `cantidad_mediciones`: entero positivo.
- `temperatura`: número decimal.

### Proceso
1. Validar que la cantidad de mediciones sea positiva.
2. Solicitar cada temperatura con `for`.
3. Aceptar valores entre -50 y 60 °C, inclusive.
4. Contar mediciones válidas e inválidas; sumar solo las válidas.
5. Inicializar máximo y mínimo con la primera temperatura válida y actualizarlos cuando corresponda.
6. Mostrar estadísticas solo si existe al menos una medición válida.

### Restricciones
- Usar `for`, `range()`, condiciones, contadores y acumuladores.
- No usar listas, diccionarios, funciones propias, `sum()`, `min()` ni `max()`.
- Evitar dividir entre cero.

### Salida
- Mediciones válidas e inválidas.
- Suma, promedio, máximo y mínimo de las temperaturas válidas.

### Casos de prueba
- `20, 40, -60, 30, 70`: 3 válidas, 2 inválidas, suma 90, promedio 30, máximo 40, mínimo 20.
- `-50, 0, 60`: 3 válidas, 0 inválidas, suma 10, promedio ≈ 3.33, máximo 60, mínimo -50.
- `-80, 100`: 0 válidas, 2 inválidas; mensaje de ausencia de datos válidos.

### Preguntas de razonamiento y respuestas
1. **¿Cómo solicitar varias temperaturas sin repetir `input()`?** Con `for` y `range()` según la cantidad indicada.
2. **¿Cuándo aumenta el contador válido?** Cuando `-50 <= temperatura <= 60`.
3. **¿Cómo calcular el promedio?** Suma de temperaturas válidas dividida entre cantidad de mediciones válidas.
4. **¿Cómo identificar máximo y mínimo sin listas?** Asignar ambos a la primera medición válida; luego comparar cada nueva temperatura válida y actualizar si supera el máximo o es menor que el mínimo.
5. **¿Y si todas son inválidas?** Comprobar que el contador válido sea cero y mostrar un mensaje sin dividir.

### Aprendizajes
- Máximo y mínimo deben tomar como referencia la primera **temperatura válida**, no necesariamente la primera entrada.
- El promedio puede calcularse una sola vez al final, si `contador_valido > 0`.
- Las condiciones de máximo y mínimo pueden ser independientes.

---

## 4. Controles verdes — Repaso activo

**Estado:** ✅ 3/3 aprobados; respuestas dadas antes de ejecutar.

1. **Operadores lógicos:** `edad >= 18 and activo and not bloqueado` con 19, `True`, `False` → `True and True and True` → **`True`**.
2. **Condicionales:** con `numero = 15`, `if numero > 20`, `elif numero >= 10` → imprime **`B`**.
3. **`while`:** `contador` comienza en 2, aumenta de 2 en 2 hasta 6 → **3 iteraciones**, `total = 12`, `contador = 8` al terminar.

---

## 5. Evaluación conceptual — Día 005

**Estado:** ✅ 6/6 aprobadas.

1. **`for` frente a `while`:** `for` recorre elementos de un iterable, como los valores de `range()`; `while` se ejecuta mientras se cumpla una condición. Para validar una entrada usaría `while`; para recorrer una secuencia, `for`.
2. **`range(3, 8)`:** `3, 4, 5, 6, 7`.
3. **`range(1, 6)`:** recorre de 1 a 5 porque el límite superior es exclusivo.
4. **`range(2, 12, 3)`:** `2, 5, 8, 11`; cuatro iteraciones.
5. **Suma con `range(1, 5)`:** `0 + 1 = 1`; `1 + 2 = 3`; `3 + 3 = 6`; `6 + 4 = 10`. Resultado: **10**.
6. **¿Puede ejecutarse cero veces?** Sí, por ejemplo `range(1, 1)` no genera valores.

---

## 6. Mutación 005 — Análisis de ventas por sucursal

**Archivo:** `mutacion_005.py`  
**Estado:** ✅ Aprobada

### Problema
Analizar ventas de varias sucursales, calcular estadísticas generales e identificar la sucursal con mayor facturación.

### Entrada
- `cantidad_sucursales`: entero positivo.
- `cantidad_ventas`: entero positivo por sucursal.
- `importe_venta`: número decimal positivo.

### Proceso
1. Validar la cantidad de sucursales.
2. Recorrer sucursales con `for`.
3. Reiniciar `total_vendido_sucursal` para cada sucursal.
4. Validar la cantidad de ventas de cada sucursal.
5. Recorrer sus ventas con otro `for`, validando cada importe con `while` hasta que sea positivo.
6. Acumular el total de la sucursal y el general; contar solo ventas válidas.
7. Comparar el total de la sucursal con el máximo registrado y guardar el número de sucursal correspondiente.
8. Mostrar totales individuales, total general, número de ventas, promedio y sucursal de mayor facturación.

### Restricciones
- Dos bucles `for` anidados y `while` para validaciones.
- Sin listas, diccionarios, funciones propias, `sum()`, `max()` ni `min()`.
- No contar importes rechazados.
- No depender de una cantidad fija de sucursales.

### Salida
- Total por sucursal.
- Total general de ventas.
- Cantidad total de ventas válidas.
- Promedio general por venta.
- Número de sucursal con mayor facturación.

### Caso de prueba
| Sucursal | Importes | Total |
|---|---|---:|
| 1 | 100, 200 | S/ 300 |
| 2 | 50, 150, 300 | S/ 500 |
| 3 | 250, 100 | S/ 350 |

**Esperado:** total general S/ 1,150; 7 ventas; promedio S/ 164.29; sucursal mayor: 2.

### Preguntas de razonamiento y respuestas
1. **¿Por qué dos `for` anidados?** El externo recorre sucursales y el interno recorre las ventas de cada sucursal.
2. **¿Qué reiniciar por sucursal?** `total_vendido_sucursal = 0`.
3. **¿Qué conservar entre sucursales?** `total_vendido`, `conteo`, `mayor_ventas` y `mayor`.
4. **¿Cómo identificar el máximo sin listas?** Inicializar el máximo con el total de la primera sucursal; comparar los siguientes **totales por sucursal** con `mayor_ventas` y actualizar también el identificador `mayor`.
5. **¿Por qué no avanzar tras un importe rechazado?** Porque se debe registrar exactamente la cantidad de ventas válidas solicitada; un intento inválido no cuenta como venta.

### Aprendizajes
- Los bucles anidados permiten procesar sucursales y sus ventas sin repetir código.
- El acumulador individual se reinicia en cada sucursal; los acumuladores generales conservan su valor.
- Para encontrar la sucursal mayor se compara `total_vendido_sucursal` con `mayor_ventas`, **no** `total_vendido` (total general).
- El `while` de validación garantiza que un intento inválido no avance a la siguiente venta.
- Acumular el resumen en una cadena funciona, aunque imprimir al terminar cada sucursal también es válido.

---

## 7. Errores identificados y correcciones

- **Precisión sobre `range()`:** el límite superior es exclusivo.
- **Legibilidad:** escribir `break` en una línea propia y evitar `continue` redundante.
- **Eficiencia:** calcular el promedio una vez después del bucle, cuando existan datos válidos.
- **Máximo y mínimo:** inicializar con el primer dato válido; no asumir que cero sirve para cualquier conjunto de datos.
- **Comparación correcta en la mutación:** comparar el total individual de la sucursal, no el total general acumulado.
- **Validación de ventas:** los intentos rechazados no incrementan el número de ventas ni avanzan a la siguiente posición.

**Nota para más adelante:** la conversión con `int()` y `float()` puede generar `ValueError` si el usuario escribe texto; el manejo de excepciones todavía no forma parte de este día.

---

## 8. Reflexión de cierre

- **¿Qué entendí mejor?** Cómo recorrer valores con `for` y `range()`, incluir límites con `n + 1` y utilizar bucles anidados para agrupar datos.
- **¿Qué fue más desafiante?** Mantener estadísticas independientes y generales, así como determinar máximos y mínimos sin listas.
- **¿Qué puedo explicar sin mirar código?** Contadores, acumuladores, límite exclusivo de `range()`, validación con `while` y comparación de máximos.
- **¿Qué debo seguir practicando?** Casos límite, nombres de variables claros y separación entre cálculos dentro y fuera de los bucles.

---

## 9. Evaluación final

- Ejercicio práctico: ✅ Aprobado.
- Desafío autónomo: ✅ Aprobado.
- Controles verdes: ✅ 3/3.
- Evaluación conceptual: ✅ 6/6.
- Mutación 005: ✅ Aprobada.

**Semáforo final:** 🟢 VERDE.  
**Próxima sesión:** Día 006 (pendiente; no iniciado).
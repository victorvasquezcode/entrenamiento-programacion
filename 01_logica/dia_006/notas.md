# Día 006 — Listas en Python

**Módulo:** 01 — Lógica de programación  
**Estado:** 🟢 VERDE — Práctica, desafío, evaluación conceptual y mutación aprobados.

## 1. Concepto aprendido

Una lista almacena varios valores y permite acceder a ellos mediante índices que empiezan en cero.

```python
numeros = [10, 20, 30]
numeros.append(40)       # Agrega al final
print(numeros[0])       # 10
print(len(numeros))     # 4
numeros[1] = 25        # Reemplaza el valor en índice 1
for numero in numeros:
    print(numero)
```

**Mi explicación:** Una lista guarda varios elementos en una variable. `append()` agrega al final; `[indice]` accede o modifica una posición; `len()` indica cuántos elementos hay; `for` recorre los valores.

## 2. Ejercicio práctico — Registro de calificaciones

**Archivo:** `practica.py` — ✅ Aprobado

**Problema:** Registrar cinco calificaciones y calcular estadísticas.

**Entrada:** Cinco calificaciones enteras entre 0 y 20.

**Proceso:**
1. Solicitar exactamente cinco calificaciones; repetir la entrada si está fuera de rango.
2. Guardar cada calificación con `append()`.
3. Recorrer la lista para acumular el total y encontrar máximo y mínimo.
4. Calcular el promedio con `total / len(calificaciones)`.

**Salida:** Lista, suma, promedio, máxima y mínima.

| Calificaciones | Suma | Promedio | Máxima | Mínima |
|---|---:|---:|---:|---:|
| 12, 16, 18, 14, 20 | 80 | 16 | 20 | 12 |
| 10, 10, 10, 10, 10 | 50 | 10 | 10 | 10 |
| 0, 5, 10, 15, 20 | 50 | 10 | 20 | 0 |

**Aprendizajes:** Usar listas, `append()`, `for` y `len()`; calcular estadísticas sin `sum()`, `max()` ni `min()`; evitar reutilizar una variable para propósitos diferentes.

## 3. Desafío autónomo — Análisis de ventas diarias

**Archivo:** `desafio.py` — ✅ Aprobado

**Problema:** Registrar ventas de varios días y analizarlas.

**Entrada:** Cantidad positiva de días y ventas diarias no negativas (se permite cero).

**Proceso:**
1. Validar la cantidad de días y cada venta.
2. Almacenar las ventas en una lista.
3. Recorrerla para calcular el total y localizar el primer día con mayor venta.
4. Calcular el promedio y recorrer de nuevo para contar días que lo superan.

**Salida:** Lista, total, promedio, venta máxima, día de la venta máxima y cantidad de días por encima del promedio.

| Ventas | Total | Promedio | Mayor | Día | Días sobre promedio |
|---|---:|---:|---:|---:|---:|
| 100, 200, 0, 300 | 600 | 150 | 300 | 4 | 2 |
| 0, 0, 0 | 0 | 0 | 0 | 1 | 0 |

**Aprendizajes:** Recorrer una lista varias veces cuando las estadísticas dependen de resultados anteriores; usar `>` para conservar el primer día en caso de empate.

## 4. Controles verdes — Repaso activo

- **Control 001:** `range(2, 11, 2)` suma **30**. ✅
- **Control 002:** Para `numero = 15`, imprime **"A"** porque es múltiplo de 3 y 5. ✅
- **Control 003:** El acumulador de una sucursal se reinicia para cada sucursal; el total general se mantiene fuera del bucle. ✅

**Resultado:** 3/3.

## 5. Evaluación conceptual — Día 006

**Resultado:** 6/6 — ✅ Aprobada.

1. `append()` agrega al final; `lista[0] = 10` reemplaza un elemento existente.
2. Tras agregar `20` a `[5, 10, 15]`, se imprime `4` y `15`.
3. Acceder a un índice inexistente produce `IndexError`.
4. Modificar `datos[1] = 10` en `[2, 4, 6]` produce `[2, 10, 6]`.
5. `for valor in lista` recorre valores; `for indice in range(len(lista))` recorre posiciones y permite acceder por índice.
6. Inicializar el máximo con el primer valor evita resultados incorrectos si todos los valores son negativos.

## 6. Mutación 006 — Gestión de inventario con listas

**Archivo:** `mutacion_006.py` — ✅ Aprobada

**Problema:** Registrar stocks de productos y procesar entradas, salidas, consultas y estadísticas.

**Entrada:** Cantidad positiva de productos; stock inicial no negativo; opción de menú; número de producto y cantidad de movimiento.

**Proceso:**
1. Solicitar y validar la cantidad de productos.
2. Registrar el stock inicial de cada producto en una lista.
3. Mostrar el menú hasta que se seleccione salir.
4. Validar el número de producto y la cantidad antes de registrar entradas o salidas.
5. Actualizar directamente el elemento correspondiente de la lista.
6. Consultar el inventario o calcular estadísticas usando los stocks actuales.
7. Finalizar únicamente con la opción 5.

**Menú:** 1. Entrada · 2. Salida · 3. Consultar · 4. Estadísticas · 5. Salir.

**Salida:** Inventario actualizado; total de unidades; producto con mayor stock; producto con menor stock; número de productos sin existencias.

**Caso de prueba:** Partiendo de `[10, 0, 25]`, ingresar 5 al producto 1 y retirar 10 del producto 3 deja `[15, 0, 15]`. Retirar 20 del producto 1 y agregar -3 al producto 2 se rechazan. Total: **30**; máximo: **producto 1**; mínimo: **producto 2**; sin stock: **1**.

**Respuestas clave:**
- El producto 1 corresponde al índice 0 porque los índices empiezan en cero.
- Un producto existe si `1 <= producto <= len(inventario)`.
- `append()` agrega un elemento; `inventario[indice]` permite modificar uno existente.
- Para retirar unidades, comprobar `cantidad > 0` y `inventario[indice] >= cantidad`.
- Las estadísticas deben calcularse sobre el inventario actualizado.

**Aprendizajes:** Modificar elementos por índice; convertir el número del producto a `producto - 1`; impedir stocks negativos; recalcular estadísticas actuales; conservar el primer producto en empates.

## 7. Errores identificados y correcciones

- **Reutilización de variables:** evitar usar la misma variable para número de estudiante y calificación.
- **Asignación por índice:** `lista[0] = valor` reemplaza; no añade elementos.
- **Salida exacta de stock:** usar `>=`, no `>`, para permitir retirar todas las unidades.
- **Validación de productos:** basta comprobar el rango con `len(lista)`; no hace falta recorrer la lista.
- **Entradas no numéricas:** `int()` y `float()` generan `ValueError` ante texto; manejo de excepciones queda como tema futuro.

## 8. Reflexión personal

**¿Qué entendí mejor hoy?** Cómo guardar datos en listas, recorrerlos y actualizar elementos mediante índices.

**¿Qué me costó más y cómo lo resolví?** Identificar máximos, mínimos y sus posiciones; lo resolví comparando valores y manteniendo el primer elemento en empates.

**¿Qué puedo explicar sin mirar el código?** `append()`, `len()`, índices desde cero, recorridos con `for` y validación de movimientos de inventario.

**¿Qué necesito practicar de nuevo?** Acceso y modificación por índices, diferencias entre `>` y `>=`, y validación de entradas.

---
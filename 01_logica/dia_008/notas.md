# Día 008 — Diccionarios en Python

**Ruta:** Python desde cero → Ciencia e Ingeniería de Datos  
**Estado final:** 🟢 VERDE — Día completado  
**Archivos:** `practica.py`, `desafio.py`, `mutacion_008.py`

## 1. Objetivo de aprendizaje

Utilizar diccionarios para almacenar datos mediante pares clave–valor, consultar y actualizar claves, contar frecuencias y consolidar operaciones comerciales, incluyendo saldos negativos y empates.

## 2. Concepto técnico

Un diccionario almacena pares **clave: valor**. Cada clave es única. La instrucción `clave in diccionario` permite comprobar si existe antes de acceder o incrementar su valor.

```python
ventas = {}
ventas["AB01"] = 3
ventas["AB01"] += 4  # Ahora AB01 tiene 7 unidades

for codigo in ventas:
    print(codigo, ventas[codigo])
```

- `len(diccionario)` devuelve el número de **claves diferentes**, no el número de operaciones ni la suma de valores.
- `diccionario[clave] += cantidad` exige que la clave ya exista; si no existe, se produciría `KeyError`.
- Un acumulador de totales puede empezar en `0`; para buscar el máximo de valores que podrían ser negativos, se debe tomar el **primer valor real** como referencia.

## 3. Repaso activo de temas verdes — APROBADO (3/3)

**Pregunta 1 — Listas:** `datos = [5, 10, 15]`, `datos[0] += datos[2]`, `datos.append(20)` → `[20, 10, 15, 20]`.

**Pregunta 2 — Cadenas:** `"  maria jose  ".strip().upper()` → `"MARIA JOSE"`; `[:5]` → `MARIA`; longitud → `10`; `" " in nombre` → `True`.

**Pregunta 3 — Bucles:** suma de los impares entre 1 y 7 → `1 + 3 + 5 + 7 = 16`.

## 4. Ejercicio práctico — Registro de incidencias

**Archivo:** `practica.py`  
**Evaluación:** APROBADO — 10/10

### Problema
Registrar exactamente cinco incidencias válidas de las categorías `RED`, `DATOS` o `APP`, normalizar la entrada y contar sus apariciones en un diccionario.

### Entrada
- `categoria`: cadena introducida por el usuario.

### Proceso
1. Solicitar cinco incidencias con `for`.
2. Normalizar cada entrada con `strip().upper()`.
3. Repetir con `while` si la categoría no es válida.
4. Si la clave existe, incrementar su contador; si no, crearla con valor `1`.
5. Recorrer el diccionario e imprimir las frecuencias.

### Salida
- Frecuencia por categoría.
- Número de categorías diferentes.

### Pruebas
- `red`, `datos`, `RED`, `APP`, `RED` → RED: 3, DATOS: 1, APP: 1; tres categorías.
- Cinco entradas `red` → RED: 5; una categoría.

**Errores funcionales:** ninguno.  
**Mejora de presentación:** cambiar `Categoria diferentes` por `Categorías diferentes`.

## 5. Desafío autónomo — Consolidación de ventas

**Archivo:** `desafio.py`  
**Evaluación:** APROBADO — 10/10

### Problema
Registrar operaciones y acumular las unidades vendidas por producto. Cada código contiene dos letras y dos dígitos. Identificar el producto con más unidades, conservando el primero en empates.

### Entrada
- `operaciones`: entero positivo.
- `codigo_producto`: cadena de cuatro caracteres.
- `unidades`: entero positivo.

### Proceso
1. Validar una cantidad positiva de operaciones.
2. Normalizar y validar cada código.
3. Solicitar unidades positivas.
4. Acumular unidades en un diccionario según el código.
5. Recorrer los productos para mostrar totales y hallar el máximo.

### Salida
- Unidades por producto.
- Cantidad de productos diferentes.
- Producto con más unidades y su total.

### Pruebas
- AB01: 3, CD02: 5, AB01: 4, XY03: 2, CD02: 1 → AB01: 7, CD02: 6, XY03: 2; tres productos; máximo AB01.
- Empate AB01: 7 y CD02: 7 → conserva AB01 si fue el primero registrado.

**Errores funcionales:** ninguno.  
**Precisión conceptual:** `len(ventas)` representa **productos diferentes**, no operaciones realizadas.

## 6. Evaluación conceptual final — APROBADA (5/5)

1. `{"A": 2, "B": 4}` y `datos["A"] += datos["B"]` → `{"A": 6, "B": 4}`; longitud `2`.
2. Incrementar `inventario["BORRADOR"]` cuando no existe provoca `KeyError`; hay que comprobar o crear la clave.
3. Contar `AB01`, `CD02`, `AB01` → `{"AB01": 2, "CD02": 1}`.
4. **Operaciones:** registros procesados; **productos diferentes:** claves únicas; **unidades totales:** suma de las cantidades.
5. Un diccionario permite consultar y acumular cantidades por clave directamente, sin recorrer una lista para localizar cada producto.

## 7. Mutación 008 — Consolidación de transacciones

**Archivo:** `mutacion_008.py`  
**Evaluación del código:** APROBADO — 10/10  
**Preguntas de razonamiento:** 4/5; una precisión conceptual corregida.

### Problema
Procesar ventas y devoluciones por producto. Las ventas suman unidades y las devoluciones las restan; el saldo neto puede ser negativo. Calcular los saldos individuales, el total neto y el producto con mayor saldo, conservando el primero en empates.

### Entrada
- `cantidad_movimiento`: entero positivo.
- `codigo_producto`: dos letras y dos dígitos.
- `tipo_movimiento`: `VENTA` o `DEVOLUCION`.
- `unidades`: entero positivo.

### Proceso
1. Solicitar una cantidad positiva de movimientos.
2. Normalizar y validar códigos y tipos de movimiento.
3. Validar unidades positivas sin avanzar con entradas inválidas.
4. Crear o actualizar cada clave del diccionario sumando ventas y restando devoluciones.
5. Recorrer el diccionario para calcular el saldo total y encontrar el máximo, inicializado con el primer producto.

### Salida
- Saldo neto por producto.
- Cantidad de productos diferentes.
- Saldo neto total.
- Producto con mayor saldo y su cantidad.

### Caso de prueba

| Código | Movimiento | Unidades | Efecto |
|---|---|---:|---:|
| AB01 | VENTA | 10 | +10 |
| CD02 | VENTA | 8 | +8 |
| AB01 | DEVOLUCION | 3 | -3 |
| XY03 | DEVOLUCION | 2 | -2 |
| CD02 | VENTA | 4 | +4 |
| AB01 | VENTA | 5 | +5 |

**Resultado:** AB01: 12, CD02: 12, XY03: -2; tres productos; saldo total 22; máximo AB01 con 12.

### Preguntas de razonamiento y corrección

1. Primera devolución de cinco unidades para un producto nuevo → `-5`. **Correcto.**
2. ¿Por qué iniciar el máximo en cero puede fallar? **Corrección:** `total = 0` es adecuado para sumar; `saldo_mayor = 0` no sirve como referencia general si todos los saldos son negativos. En el programa se corrige al sustituirlo por el saldo del primer producto antes de comparar.
3. Entre `-3` y `-7`, el mayor es `-3`. **Correcto.**
4. Sumar saldos con `total += transaccion[movimiento]` al recorrer las claves. **Correcto.**
5. El saldo neto total suma los saldos; los productos diferentes son las claves del diccionario. **Correcto.**

**Errores funcionales:** ninguno.  
**Mejoras opcionales:** usar `producto` en lugar de `movimiento` en el último bucle; inicializar `producto_mayor` en `None` por claridad.

## 8. Aprendizajes del Día 008

- Crear, consultar y actualizar diccionarios mediante claves únicas.
- Validar entradas antes de incorporarlas a los datos.
- Contar frecuencias y consolidar unidades por producto.
- Diferenciar operaciones, productos únicos y unidades acumuladas.
- Procesar movimientos positivos y negativos.
- Calcular totales manualmente y encontrar máximos sin funciones auxiliares.
- Conservar el primer registro en caso de empate utilizando `>`.
- Reconocer la diferencia entre iniciar un **acumulador** en cero e iniciar la referencia para un **máximo**.

## 9. Progreso y siguiente sesión

| Actividad | Resultado |
|---|---|
| Repaso activo | 3/3 — Aprobado |
| `practica.py` | 10/10 — Aprobada |
| `desafio.py` | 10/10 — Aprobado |
| Evaluación conceptual final | 5/5 — Aprobada |
| `mutacion_008.py` | 10/10 — Aprobada |
| Preguntas de la mutación | 4/5 — Precisión corregida |

**Semáforo final:** 🟢 VERDE.  
**Próxima sesión:** Día 009 — tema nuevo, con repaso activo de los días anteriores.
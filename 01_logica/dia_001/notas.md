# Día 001 — Pensamiento algorítmico

**Módulo:** 01 — Lógica de programación  
**Estado:** 🟢 VERDE  
**Concepto:** Entrada, proceso y salida

---

## 1. Concepto aprendido

Un algoritmo es una secuencia finita de instrucciones para resolver un problema.

- **Entrada:** Datos que recibe el programa.
- **Proceso:** Operaciones realizadas con esos datos.
- **Salida:** Resultado que produce el programa.
- **Variable:** Nombre asociado a un valor que puede utilizarse durante la ejecución.

### Conceptos de Python utilizados
- `input()` recibe información del usuario como texto.
- `int()` convierte un valor compatible a entero.
- `float()` convierte un valor compatible a número decimal.
- `print()` muestra información.
- `if` y `else` permiten tomar decisiones.
- `*` multiplica valores.

---

## 2. Ejercicio práctico — Costo total

**Archivo:** `practica.py`

### Problema
Solicitar el precio de un producto y la cantidad comprada para calcular el costo total.

### Entrada
- Precio del producto.
- Cantidad comprada.

### Proceso
Multiplicar el precio por la cantidad.

`total = precio * cantidad`

### Salida
Costo total de la compra.

### Caso de prueba
- Precio: 15
- Cantidad: 3
- Resultado esperado: 45

### Aprendizaje
Para precios con decimales, `float()` admite entradas como `15.50`, mientras que `int()` no admite directamente esa representación.

---

## 3. Desafío autónomo — Descuento fijo

**Archivo:** `desafio.py`

### Problema
Calcular el costo de una compra aplicando un descuento fijo de S/ 10, sin permitir un total negativo.

### Entrada
- Precio unitario.
- Cantidad.

### Proceso
1. Calcular el subtotal.
2. Restar el descuento de S/ 10.
3. Evitar que el total sea negativo.

### Salida
Total final de la compra.

### Casos de prueba

| Precio | Cantidad | Total esperado |
|---|---|---|
| 20 | 3 | 50 |
| 5 | 1 | 0 |
| 10 | 1 | 0 |

### Error o mejora identificada
Inicialmente corregía el resultado solamente al imprimirlo. Sin embargo, la variable `total` podía seguir almacenando un número negativo.

**Aprendizaje:** Es mejor corregir el valor de la variable para que pueda utilizarse de manera segura en operaciones posteriores.

---

## 4. Mutación 001 — Descuento condicionado

**Archivo:** `mutacion_001.py`

### Problema
Aplicar un descuento de S/ 10 únicamente cuando el subtotal sea de S/ 50 o más.

### Entrada
- Precio unitario.
- Cantidad.

### Proceso
1. Validar que la cantidad sea mayor que cero.
2. Validar que el precio no sea negativo.
3. Calcular el subtotal.
4. Si el subtotal es menor que 50, mantenerlo sin descuento.
5. En caso contrario, descontar S/ 10.

### Salida
- Total con o sin descuento.
- Mensaje de error si los datos numéricos incumplen las restricciones.

### Casos de prueba

| Precio | Cantidad | Resultado |
|---|---|---|
| 20 | 3 | 50 |
| 10 | 3 | 30 |
| 25 | 2 | 40 |
| 5 | 0 | Error |
| -10 | 3 | Error |

### Aprendizaje
No es necesario utilizar `elif subtotal >= 50` cuando el `if subtotal < 50` ya cubre la primera posibilidad y solo queda la alternativa contraria.

Se puede utilizar `else` para simplificar la lógica.

---

## 5. Control verde — Horas trabajadas

### Problema
Un trabajador gana S/ 15 por hora normal y S/ 20 por cada hora que exceda las 40 semanales.

### Entrada
Cantidad de horas trabajadas.

### Proceso
- Hasta 40 horas: multiplicar las horas por 15.
- Más de 40 horas: calcular 40 × 15 y sumar las horas adicionales × 20.

### Salida
Remuneración semanal.

### Pruebas
- 35 horas: S/ 525.
- 45 horas: S/ 700.

### Aprendizaje
Un problema puede resolverse primero mediante razonamiento y cálculos manuales, sin necesidad de escribir Python inmediatamente.

---

## 6. Errores y lecciones importantes

- Ejecutar un programa una sola vez no garantiza que funcione para todas las entradas.
- Debo comprobar resultados esperados, valores límite y entradas inválidas.
- Las variables deben contener valores coherentes, no solo producir una salida visualmente correcta.
- Primero debo entender las reglas y después escribir código.

## 7. Reflexión personal

**¿Qué aprendí?**  
A dividir problemas en entrada, proceso y salida, y a transformar ese razonamiento en instrucciones de Python.

**¿Qué debo mejorar?**  
Realizar más pruebas, especialmente con valores límite.

**¿Qué debo recordar?**  
Un programa correcto no solo funciona con un ejemplo: también debe comportarse según las reglas ante diferentes entradas.

# 🐛 Registro de Errores y Aprendizajes

## Objetivo

Identificar errores de razonamiento, implementación y validación para evitar repetirlos.

---

## Error 001 — No cumplir todas las restricciones

**Tema:** Operadores lógicos — Día 002

**Situación:**

En la Mutación 002 debía utilizar `and`, `or` y `not`.

**Error:**

Mi primera solución funcionaba para los casos propuestos, pero olvidé utilizar explícitamente `not`.

**Causa:**

Me concentré en que el programa funcionara y no comprobé todas las restricciones antes de entregarlo.

**Corrección:**

Representé el estado de suspensión mediante una variable booleana y utilicé `not` para negarla.

**Aprendizaje:**

Un programa no está completamente terminado solo porque produzca resultados correctos. También debe cumplir las restricciones del problema.

**Regla preventiva:**

Antes de entregar, revisar una lista de requisitos y verificar cada uno.

**Estado:** Corregido.

---

## Error 002 — Corregir solamente la salida

**Tema:** Pensamiento algorítmico — Día 001

**Situación:**

En el primer desafío debía impedir que el total de una compra fuera negativo.

**Error:**

Mostré `0` cuando el total era negativo, pero la variable `total` conservaba el valor negativo.

**Causa:**

Me enfoqué en el resultado mostrado en pantalla y no en el valor almacenado.

**Corrección:**

En la mutación siguiente almacené el resultado correcto directamente en la variable `total`.

**Aprendizaje:**

Es importante mantener valores correctos en las variables, no solamente mostrar resultados correctos.

**Regla preventiva:**

Comprobar tanto los resultados impresos como los valores que utiliza el programa.

**Estado:** Corregido.

---

## Error 003 — Pruebas insuficientes

**Tema:** Pensamiento algorítmico — Día 001

**Situación:**

Al explicar cómo comprobé mi primer programa, indiqué que lo había ejecutado en la terminal.

**Aspecto por mejorar:**

Ejecutar un programa una vez no demuestra que funcione para todas las entradas relevantes.

**Corrección:**

Comencé a trabajar con casos de prueba que incluyen valores normales, límites y entradas inválidas.

**Aprendizaje:**

Probar significa comparar el resultado obtenido con el resultado esperado.

**Regla preventiva:**

Antes de entregar un ejercicio, comprobar al menos un caso normal, un caso límite y un caso inválido cuando corresponda.

**Estado:** En seguimiento.

**Tema:** Orden de condiciones.

**Aspecto por reforzar:**

El orden de las condiciones debe responder a la lógica de los rangos, no a su complejidad aparente.

**Regla preventiva:** 

Antes de escribir una cadena if/elif, comprobar qué valores quedan descartados después de cada condición.

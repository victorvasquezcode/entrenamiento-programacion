# Registro de errores y aprendizajes

**Objetivo:** identificar fallos de razonamiento y mejorar la calidad de mis soluciones. No registrar errores triviales de escritura salvo que se repitan.

## Error 001 — Cumplimiento de restricciones (Día 002)

- **Situación:** en la primera solución de la mutación de operadores lógicos omití el uso explícito de `not`.
- **Causa:** comprobé el comportamiento, pero no revisé todos los requisitos.
- **Corrección:** definí una variable booleana para la suspensión y apliqué `not`.
- **Regla preventiva:** verificar cada restricción antes de entregar.
- **Estado:** corregido.

## Lección 002 — Orden de condiciones (Día 003)

- **Situación:** inicialmente pensé que las condiciones más complicadas debían ir primero.
- **Corrección:** ordenarlas según la lógica de los rangos y recordar que `if/elif/else` ejecuta la primera rama verdadera.
- **Regla preventiva:** probar límites y detectar condiciones que vuelvan inalcanzables las siguientes.
- **Estado:** consolidado en la Mutación 003.

## Lección 003 — Comparaciones redundantes (Día 003)

- **Situación:** en el clasificador de notas repetí límites inferiores que ya quedaban descartados.
- **Corrección:** en la mutación de temperaturas utilicé `elif temperatura < 0`, `elif temperatura < 15`, etc.
- **Regla preventiva:** antes de escribir cada `elif`, identificar qué valores ya fueron excluidos.
- **Estado:** consolidado.

## Lección 004 — Asignación frente a acumulación (Día 003)

- **Situación:** utilicé `total += 5` para una tarifa fija; funciona si `total` empieza en cero, pero no expresa tan claramente la intención.
- **Corrección:** utilizar `total = 5` para asignar una tarifa fija; reservar `+=` para acumular.
- **Regla preventiva:** distinguir entre reemplazar un valor y sumarlo al anterior.
- **Estado:** comprendido.

## Lección 005 — Límites inclusivos en inventario (Día 004)

- **Situación:** al explicar la validación de salidas mencioné que el inventario debía ser mayor que la salida.
- **Corrección:** la condición correcta admite igualdad: `cantidad_producto >= salida`. El código entregado ya utilizaba `>=`.
- **Regla preventiva:** comprobar casos de igualdad, cero y valores superiores al stock.
- **Estado:** corregido conceptualmente.

## Aspectos futuros — No son fallos de los ejercicios aprobados

- **Entradas no numéricas:** `int()` y `float()` producen `ValueError` ante texto no convertible. Practicar manejo de excepciones cuando corresponda al temario.
- **Repetición de impresiones:** almacenar el resultado en una variable y mostrarlo una sola vez cuando mejore la claridad.
- **Pruebas:** distinguir entre resultados esperados y casos efectivamente ejecutados.

## Rutina breve de revisión

1. Elegir una lección sin mirar su corrección.
2. Explicar qué salió mal y cómo evitarlo.
3. Crear un caso límite pequeño que demuestre la solución.
4. Marcar para repaso futuro cualquier concepto que no pueda explicar.
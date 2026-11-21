# Día 018 — Errores de validación con contexto

**Tema propuesto para la sesión.** Las notas del Día 017 anuncian un concepto nuevo sin especificar cuál.

## Repaso activo

1. ¿Por qué una salida inválida sigue siendo inválida aunque luego llegue una entrada que la habría cubierto?
2. ¿Qué información se pierde al devolver solo `None` para todos los movimientos inválidos?

## Concepto

Un error de validación puede describir qué falló y dónde. En un lote de movimientos, el número de registro permite encontrar la entrada problemática. Se conserva el orden de procesamiento del Día 017. Si un movimiento es inválido, se informa el primer error y se evita publicar un resultado parcial.

## Práctica — `practica.py`

Implementa `validar_movimiento(movimiento)`. Recibe un diccionario con las claves exactas `tipo` y `cantidad`. Acepta los tipos `entrada` y `salida`. La cantidad debe ser una cadena con dígitos ASCII, admite espacios exteriores y debe representar un entero mayor que cero. Devuelve una tupla con el tipo y la cantidad entera. Si el movimiento es inválido, lanza `ValueError` con un mensaje que indique el campo o la estructura que falló.

Prueba una salida con cantidad `" 03 "`, una cantidad `"0"`, un tipo desconocido y un diccionario con una clave faltante.

## Desafío — `desafio.py`

Implementa `procesar_lote(stock_inicial, movimientos)`. Valida el stock inicial con las reglas del Día 017 y reutiliza `validar_movimiento`. Devuelve `{"stock_final": ..., "operaciones": ...}` si procesa toda la lista. Ante el primer movimiento inválido o una salida sin stock suficiente, lanza `ValueError` e incluye la posición del movimiento, empezando en 1. Un stock inicial inválido o un lote que no sea lista debe identificarse por separado. La entrada debe quedar intacta.

Prueba un lote válido, una lista vacía y un lote en el que la segunda operación agote más stock del disponible.

## Mutación — `mutacion_018.py`

Conserva el contrato del desafío y añade `stock_maximo` al resultado, incluyendo el stock inicial. Prueba que una salida seguida de una entrada que no supere el stock de partida conserva ese máximo y que un error intermedio sigue indicando la posición correcta.

**Estado:** ejercicios listos para resolver. Evaluación pendiente.

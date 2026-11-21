# Día 018 — Validación estricta de registros

## Concepto

Validar la estructura de un registro antes de leer sus campos. Normalizar los valores aceptados y devolver un registro nuevo, manteniendo intacta la entrada.

## Práctica habilitada

Implementa `validar_registro(registro)` en `practica.py`.

- Acepta únicamente un `dict` exacto con las claves `codigo` y `cantidad`.
- `codigo` debe ser `str`. Aplica `strip()` y `upper()`. El valor normalizado debe ser no vacío y contener exclusivamente caracteres ASCII de `A` a `Z` o de `0` a `9`.
- Pasa `cantidad` a `convertir_stock()` del [Día 017](../dia_017/practica.py). Ese contrato acepta una cadena exacta con dígitos ASCII y espacios exteriores opcionales, y devuelve un entero no negativo o `None`. Conserva el cero como cantidad válida.
- Si el registro es válido, devuelve un diccionario nuevo con `codigo` normalizado y `cantidad` entera. Devuelve `None` si algún requisito falla. Conserva intacta la entrada en ambos casos.

## Pruebas funcionales

| Caso | Entrada o variación sobre un registro válido | Resultado esperado |
|---|---|---|
| 1 | `{"codigo": "A1", "cantidad": "5"}` | `{"codigo": "A1", "cantidad": 5}` |
| 2 | `{"codigo": " ab12 ", "cantidad": " 003 "}` | `{"codigo": "AB12", "cantidad": 3}` |
| 3 | `{"codigo": "9", "cantidad": "0"}` | `{"codigo": "9", "cantidad": 0}` |
| 4 | Lista con los pares `codigo` y `cantidad` | `None` |
| 5 | Subclase de `dict` con ambas claves válidas | `None` |
| 6 | Falta la clave `cantidad` | `None` |
| 7 | Ambas claves válidas y una clave adicional | `None` |
| 8 | `codigo` igual a `123` como entero | `None` |
| 9 | `codigo` igual a `"   "` | `None` |
| 10 | `codigo` igual a `"AÑ1"` | `None` |
| 11 | `codigo` igual a `"A-1"` | `None` |
| 12 | `cantidad` igual a `"-1"` | `None` |

**Inmutabilidad.** Guarda una copia del registro del caso 2. Después de validar, comprueba que la entrada sigue siendo igual a la copia y que el resultado es otro objeto. Repite la comprobación de la entrada con un registro inválido cuyo código se pueda normalizar y cuya cantidad falle.

Entrega el código, los resultados de las pruebas y una explicación breve del orden de validación, el tratamiento del cero y la reutilización de `convertir_stock()`.

El desafío y la mutación se habilitan según las [reglas de mentoría](../../INSTRUCCIONES_MENTOR.md). El [borrador histórico](notas.md) conserva la propuesta anterior.

## Desafío autónomo — Procesar un lote de inventario

Implementa `procesar_lote(stock_inicial, movimientos)` en `desafio.py`. Cada lote corresponde a un solo producto y se procesa en el orden recibido.

### Entradas y validaciones

- `stock_inicial` sigue el contrato de `convertir_stock()` del Día 017. El cero es válido.
- `movimientos` debe ser una lista exacta (`list`). Puede estar vacía.
- Cada movimiento debe ser un diccionario exacto con solo dos claves: `tipo` y `registro`. El tipo debe ser una cadena con el valor literal `"entrada"` o `"salida"`. Los espacios exteriores y las variantes de mayúsculas son inválidos en este campo.
- `registro` es el diccionario de la práctica, con solo `codigo` y `cantidad`. Su aceptación y normalización se rigen por `validar_registro(registro)`, que se debe reutilizar.
- El código normalizado del primer movimiento establece el producto del lote. Los demás movimientos deben tener ese mismo código normalizado.
- Una entrada incrementa el stock y una salida lo reduce. La salida puede dejar el stock en cero. Una cantidad cero es válida y cuenta como una operación.

### Resultado y errores

- Si el lote completo es válido, devuelve un diccionario nuevo de la forma `{"stock_final": entero, "operaciones": entero}`. Para un lote vacío, devuelve el stock inicial convertido y cero operaciones.
- Valida primero el stock inicial y después el tipo del lote. Si alguno falla, lanza `ValueError` con el mensaje exacto `"Stock inicial inválido"` o `"Lote inválido"`, respectivamente.
- Detén el procesamiento ante el primer movimiento inválido o la primera salida que supere el stock disponible en ese momento. Lanza `ValueError` con el mensaje exacto `"Movimiento inválido en posición N"` o `"Stock insuficiente en posición N"`, según corresponda. `N` empieza en 1. Un código distinto dentro del lote se considera un movimiento inválido. Para cada movimiento, comprueba su validez antes de evaluar si hay stock suficiente.
- La lista, sus movimientos y los registros internos deben conservar su contenido, orden e identidad, tanto si la llamada devuelve un resultado como si lanza una excepción.

### Pruebas del desafío

En la tabla, `E(c, q)` representa `{"tipo": "entrada", "registro": {"codigo": c, "cantidad": q}}`. `S(c, q)` representa la misma estructura con tipo `"salida"`. Esta notación describe datos de prueba.

| Stock inicial | Lote | Resultado esperado |
|---|---|---|
| `" 005 "` | `[E(" ab12 ", " 003 "), S("AB12", "2")]` | `{"stock_final": 6, "operaciones": 2}` |
| `" 007 "` | `[]` | `{"stock_final": 7, "operaciones": 0}` |
| `"0"` | `[S("A1", "0"), E("A1", "0")]` | `{"stock_final": 0, "operaciones": 2}` |
| `"5"` | `[S("A1", "5")]` | `{"stock_final": 0, "operaciones": 1}` |
| `"5"` | `[E("A1", "1"), S("A1", "7"), E("A1", "10")]` | `ValueError("Stock insuficiente en posición 2")` |
| `"0"` | `[S("A1", "1"), E("A1", "1")]` | `ValueError("Stock insuficiente en posición 1")` |
| `"-1"` | `None` | `ValueError("Stock inicial inválido")` |
| `5` como entero | `[]` | `ValueError("Stock inicial inválido")` |
| `"5"` | Tupla vacía y, en otra prueba, instancia de una subclase de `list` | `ValueError("Lote inválido")` en ambas |
| `"5"` | `[E("A1", "2"), None, S("A1", "99")]` | `ValueError("Movimiento inválido en posición 2")` |
| `"5"` | Un movimiento de entrada con una clave adicional | `ValueError("Movimiento inválido en posición 1")` |
| `"5"` | Un movimiento con `tipo=" Entrada "` y registro válido | `ValueError("Movimiento inválido en posición 1")` |
| `"5"` | `[E("A1", "2"), S("A1", "-1")]` | `ValueError("Movimiento inválido en posición 2")` |
| `"5"` | `[E("A1", "2"), S("B2", "99")]` | `ValueError("Movimiento inválido en posición 2")` |

**Inmutabilidad.** Comprueba el contenido y el orden frente a una copia profunda y conserva referencias a los movimientos y registros originales para verificar su identidad. Hazlo con el primer lote válido y con el lote cuya segunda operación tiene stock insuficiente.

**Entrega.** Comparte tu intento y los resultados de las pruebas. Explica cómo interpretaste el orden del lote y la prioridad de errores, cómo verificaste la inmutabilidad y qué coste tiene tu solución en tiempo y memoria. La mutación sigue bloqueada.

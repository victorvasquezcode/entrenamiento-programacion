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

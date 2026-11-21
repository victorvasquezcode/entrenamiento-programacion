# Progreso de entrenamiento de programación

**Objetivo:** desarrollar pensamiento algorítmico y fundamentos de Python para avanzar progresivamente hacia Ciencia de Datos e Ingeniería de Datos.

## Semáforo

- 🔴 **Rojo:** tema nuevo, pendiente de práctica y evaluación conceptual.
- 🟡 **Amarillo:** concepto inicial y práctica aprobados, con desafío y mutación en curso.
- 🟢 **Verde:** repaso, práctica, desafío, mutación y evaluación conceptual aprobados. Requiere recuperación activa periódica.

## Registro de sesiones

Las notas enlazadas conservan las evaluaciones históricas. A partir del Día 018, registrar aquí cada evaluación con su evidencia y consultar el punto de reanudación en [estado actual](memoria/estado_actual.md).

| Día | Tema | Registro |
|---|---|---|
| 001 | Pensamiento algorítmico | [Notas de la sesión](01_logica/dia_001/notas.md) |
| 002 | Operadores y expresiones lógicas | [Notas de la sesión](01_logica/dia_002/notas.md) |
| 003 | Condicionales y control de flujo | [Notas de la sesión](01_logica/dia_003/notas.md) |
| 004 | Bucles `while` y repetición controlada | [Notas de la sesión](01_logica/dia_004/notas.md) |
| 005 | Bucles `for` y `range()` | [Notas de la sesión](01_logica/dia_005/notas.md) |
| 006 | Listas en Python | [Notas de la sesión](01_logica/dia_006/notas.md) |
| 007 | Cadenas de texto en Python | [Notas de la sesión](01_logica/dia_007/notas.md) |
| 008 | Diccionarios en Python | [Notas de la sesión](01_logica/dia_008/notas.md) |
| 009 | Funciones en Python | [Notas de la sesión](01_logica/dia_009/notas.md) |
| 010 | Manejo de excepciones y conversión segura de datos | [Notas de la sesión](01_logica/dia_010/notas.md) |
| 011 | Lectura y procesamiento de archivos de texto | [Notas de la sesión](01_logica/dia_011/notas.md) |
| 012 | Escritura de archivos y persistencia de datos | [Notas de la sesión](01_logica/dia_012/notas.md) |
| 013 | Escritura segura de archivos | [Notas de la sesión](01_logica/dia_013/notas.md) |
| 014 | Funciones puras y transformación de datos | [Notas de la sesión](01_logica/dia_014/notas.md) |
| 015 | Precisión numérica y cálculos monetarios | [Notas de la sesión](01_logica/dia_015/notas.md) |
| 016 | Modularización y reutilización de funciones | [Notas de la sesión](01_logica/dia_016/notas.md) |
| 017 | Excepciones, validación estricta y procesamiento de inventario | [Notas de la sesión](01_logica/dia_017/notas.md) |
| 018 | Validación estricta de registros | [Práctica pendiente](01_logica/dia_018/enunciado.md) · [Borrador histórico](01_logica/dia_018/notas.md) |

## Verificación técnica reciente

- Día 006: la corrección del autor superó las pruebas de 1, 4, 20 y 21 días.
- Días 009, 010 y 014–016: se verificaron las regresiones de validación y límites numéricos.
- Días 012–013: 20 comprobaciones aisladas de guardado, escritura, cierre y reemplazo superadas.
- Día 018: los tres archivos Python publicados contienen descripciones. El repaso aprobado consta en la evaluación registrada más abajo.

## Controles de retención

| Tema | Última evidencia | Próximo control |
|---|---|---|
| Pensamiento algorítmico | Control verde del Día 004 aprobado | Próximas sesiones |
| Operadores lógicos | Control verde del Día 004 aprobado | Próximas sesiones |
| Condicionales | Control verde del Día 004 aprobado | Próximas sesiones |
| Bucles `while` | Mutación 004 aprobada | Día 005 o posterior |

## Rutina de repaso

- **Inicio del entrenamiento (10 min):** responder preguntas de un tema verde sin consultar notas.
- **Cierre (5–10 min):** registrar aprendizajes y errores importantes.
- **Noche (opcional, 5–10 min):** leer una lección de `errores.md` o una sección de `notas.md`, sin retrasar el sueño.
- **Cada semana:** intentar resolver un problema corto de un tema verde sin ver el código anterior.

## Próximo objetivo

Consultar el [estado actual](memoria/estado_actual.md) para retomar la etapa habilitada.

## Reflexión semanal

**Fortalezas actuales:** resolución autónoma de problemas con condiciones, validación de rangos, contadores, acumuladores y bucles `while`.

**Aspectos a vigilar:** precisión al explicar límites inclusivos, evitar condiciones redundantes y documentar casos de prueba ejecutados.

## Evidencia histórica

| Días | Aprobaciones registradas | Tipo y alcance de la evidencia |
|---|---|---|
| 001–002 | VERDE histórico y controles posteriores aprobados | Confirmación documental en notas y controles de retención. Sin veredictos individuales de práctica, desafío y mutación. |
| 003–004 | VERDE, práctica, desafío, mutación y controles de repaso | Veredictos en las notas. El 004 registra además la evaluación conceptual de `while`. |
| 005–011 | VERDE, práctica, desafío y mutación, con repaso y controles de razonamiento | Veredictos y puntuaciones en notas. El 009 documenta inspección y carece de registro independiente de ejecución de todos los límites. |
| 012 | VERDE, práctica, desafío y mutación | Inspección explícita del desafío y confirmación histórica de las pruebas complementarias. |
| 013 | VERDE, práctica, desafío y mutación | Veredictos en notas. Inspección explícita de la mutación. |
| 014–015 | VERDE, repaso, práctica, desafío, mutación y evaluación conceptual | Inspección o revisión estática según las notas. |
| 016 | VERDE, repaso, práctica, desafío, mutación y evaluación conceptual | Veredictos documentados en las notas y corroboración en el estado conversacional anterior. |
| 017 | VERDE, repaso, práctica, desafío, mutación y evaluación conceptual | Registro histórico de resultados, incluidos 23/23 en práctica y 5/5 en mutación. La auditoría ejecutó los scripts publicados, con 23, 9 y 5 aserciones en práctica, desafío y mutación, respectivamente. |

La auditoría del commit [`28fc6124`](https://github.com/victorvasquezcode/entrenamiento-programacion/commit/28fc6124fcea83b980b16c5898af56a8c6cdc73b) comprobó la sintaxis de 52 archivos Python de los días 001–017 y ejecutó los 28 scripts de los días 009–017 en copias temporales, todos con salida 0. Esta ejecución acredita los casos incorporados a esos scripts. Las verificaciones técnicas anteriores permanecen registradas arriba y en [errores.md](errores.md).

## Día 018

| Fecha de registro | Etapa | Veredicto | Evidencia |
|---|---|---|---|
| 2026-11-21 | Repaso activo | Aprobado | Confirmación histórica en la conversación y el [estado versionado en `28fc6124`](https://github.com/victorvasquezcode/entrenamiento-programacion/blob/28fc6124fcea83b980b16c5898af56a8c6cdc73b/memoria/estado_actual.md). Tres respuestas correctas y dos correctas en lo esencial, con precisiones sobre `Decimal` y `ValueError`. |
| 2026-11-21 | Práctica | Pendiente | Inspección de `practica.py` en `28fc6124`. Falta la implementación, las pruebas y el razonamiento. |
| 2026-11-21 | Desafío y mutación | Bloqueados | Inspección de ambos archivos en `28fc6124`. Contienen descripciones. Se requiere aprobar la práctica para habilitar el desafío. |
| 2026-11-21 | Evaluación conceptual | Pendiente | Falta un veredicto para el concepto del Día 018. El repaso acreditó conocimientos previos. |

### Evaluación de la práctica — 21 de noviembre de 2026

- **Veredicto:** Práctica requiere corrección. Concepto inicial aprobado por inspección de la explicación entregada en conversación. Se conserva el repaso aprobado.
- **Intento:** [`8d063842`](https://github.com/victorvasquezcode/entrenamiento-programacion/commit/8d06384278d5d138844965f10f06457da5828b12).
- **Ejecución directa:** Python 3.12.14, con `01_logica` en la ruta de importación. Pasaron los 12 casos funcionales y las dos comprobaciones de inmutabilidad. Una subclase simple de `str` con código `" ab12 "` y cantidad `"3"` devolvió `None`. El enunciado pide que el código sea `str` y reserva la exigencia de tipo exacto para el diccionario y la cadena de cantidad. El código `"ß"` se normalizó a `"SS"`, conforme al orden fijado. Cantidades booleanas y con dígitos no ASCII se rechazaron. Una cadena de 5000 ceros fue rechazada por el conversor del Día 017 con el límite de Python, comportamiento heredado de la dependencia exigida.
- **Inspección:** Orden de validación, conservación de cero, reutilización y construcción de un diccionario nuevo correctos. El script de pruebas imprime el resultado y no falla por sí mismo cuando un caso devuelve un resultado incorrecto. La ejecución del mentor añadió aserciones a los indicadores del script.
- **Rúbrica:** Corrección 20/25, pruebas 17/20, diseño 18/20, razonamiento 15/15, autonomía 10/10, rendimiento 10/10. Total 90/100. El incumplimiento de tipo bloquea el avance.
- **Próxima acción:** Aceptar una subclase simple de `str` para el código cuando el resultado normalizado cumpla el contrato. Agregar el caso de regresión y reevaluar la práctica.

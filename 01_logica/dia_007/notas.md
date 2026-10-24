# Día 007 — Cadenas de texto en Python

**Estado final:** 🟢 VERDE — Aprobado  
**Fecha de cierre:** 24 de octubre de 2026  
**Archivos:** `practica.py`, `desafio.py`, `mutacion_007.py`

## 1. Conceptos técnicos

- `strip()` elimina espacios al inicio y al final de una cadena.
- `upper()` convierte letras a mayúsculas y `lower()` a minúsculas.
- `len(texto)` devuelve la cantidad de caracteres.
- `texto[:2]` obtiene los primeros dos caracteres; `texto[2:]` obtiene desde el índice 2 hasta el final; `texto[-2:]` obtiene los últimos dos.
- `isalpha()` verifica que todos los caracteres sean letras; los espacios hacen que el resultado sea `False`.
- `isdigit()` comprueba que los caracteres sean dígitos.
- `in` comprueba pertenencia, útil para detectar duplicados.
- Las cadenas (`str`) son **inmutables**: no se pueden modificar caracteres por asignación de índice.
- `continue` salta a la siguiente iteración; `break` termina el bucle más cercano.

## 2. Controles de repaso activo

**Resultado:** 3/3 correctos.

- Modificación de lista: `[20, 10, 15, 25]`, longitud 4.
- Suma de impares 1, 3, 5 y 7: 16, en 4 iteraciones.
- Retirar exactamente 10 unidades de un stock de 10: operación permitida, stock final 0.

## 3. Práctica — Códigos de productos

**Archivo:** `practica.py`  
**Estado:** Aprobada.

### Entrada
Cinco códigos de producto ingresados por el usuario.

### Proceso
1. Solicitar cada código y normalizar con `strip().upper()`.
2. Validar que tenga exactamente cinco caracteres, dos letras iniciales y tres dígitos finales.
3. Repetir la solicitud hasta obtener un código válido.
4. Guardar los cinco códigos en una lista.
5. Contar los códigos que empiezan con `AB`.

### Salida
Lista de códigos válidos y cantidad de códigos con prefijo `AB`.

**Observación:** comprobar la longitud primero puede facilitar la lectura, aunque el código original funciona.

## 4. Desafío autónomo — Identificadores de ventas

**Archivo:** `desafio.py`  
**Estado:** Aprobado.

### Entrada
- `operaciones`: entero positivo.
- `identificador`: cadena introducida por el usuario.

### Proceso
1. Solicitar una cantidad positiva de operaciones.
2. Normalizar cada identificador con `strip().upper()`.
3. Rechazar duplicados mediante `identificador in registro`.
4. Validar seis caracteres: prefijo `VT` o `NC` y cuatro dígitos.
5. Repetir las entradas rechazadas sin avanzar el registro.
6. Guardar los identificadores válidos y contar ventas, notas de crédito y terminaciones `00`.

### Salida
Lista de identificadores, total registrado, cantidad de `VT`, cantidad de `NC` y cantidad terminada en `00`.

**Caso probado:** `VT0001`, `NC0100`, duplicado `VT0001` rechazado, `VT0200`, `NC0003`. Resultado: 4 registros; 2 ventas, 2 notas de crédito y 2 terminados en `00`.

### Preguntas de razonamiento

1. **¿Por qué normalizar antes de buscar duplicados?** Porque los espacios exteriores y las diferencias entre mayúsculas y minúsculas podrían impedir reconocer el mismo identificador.
2. **¿Cómo verificar si ya está almacenado?** `identificador in registro`. `append()` agrega un elemento; no comprueba su existencia.
3. **¿Cómo extraer los últimos dos caracteres?** `identificador[-2:]` o, si siempre tiene seis caracteres, `identificador[4:]`.
4. **¿Por qué una entrada inválida no aumenta el registro?** Porque se solicita otra entrada para la misma operación.
5. **¿Qué pasa sin normalizar `vt0001` y `VT0001`?** Python los considera cadenas diferentes.

## 5. Evaluación conceptual final

**Resultado:** 5/5 — Aprobado.

1. `"  pyTHON  ".strip().upper()[:3]` → `PYT`.
2. `" vt0001 ".strip().upper() in ["VT0001", "NC0002"]` → `True`.
3. `codigo[0] = "X"` en una cadena produce `TypeError` porque `str` es inmutable.
4. Para `"VT1200"`: `[:2]` → `VT`; `[2:4]` → `12`; `[-2:]` → `00`.
5. `continue` salta a la siguiente iteración; `break` finaliza el bucle.

## 6. Mutación 007 — Limpieza de datos de clientes

**Archivo:** `mutacion_007.py`  
**Estado:** Aprobada — 🟢 VERDE.

### Problema
Registrar nombres únicos de clientes, normalizados y validados, y calcular estadísticas de longitud y prefijo.

### Entrada
- `cantidad_clientes`: entero positivo.
- `nombre`: cadena de texto ingresada por el usuario.

### Proceso
1. Solicitar una cantidad positiva de clientes.
2. Normalizar cada nombre con `strip().upper()`.
3. Rechazar nombres vacíos, duplicados o cuya longitud no esté entre 3 y 20 caracteres.
4. Validar carácter por carácter: permitir únicamente letras o espacios interiores.
5. Repetir la solicitud sin avanzar cuando el nombre sea inválido.
6. Guardar nombres válidos en una lista.
7. Recorrer la lista para obtener el más largo, el más corto y el número de nombres que comienzan con `A`.
8. Conservar el primer nombre en caso de empate de longitud.

### Restricciones
- Usar listas, `append()`, `for`, `while`, `len()`, `strip()`, `upper()`, `isalpha()` e `in`.
- No usar diccionarios, conjuntos, expresiones regulares ni funciones propias.
- No usar `sum()`, `max()` ni `min()`.
- Debe funcionar con un solo cliente.
- Los espacios interiores cuentan para la longitud; no es necesario eliminar espacios interiores repetidos.

### Salida
Lista de clientes, cantidad total, nombre más largo y longitud, nombre más corto y longitud, y cantidad de nombres que empiezan con `A`.

### Casos de prueba

| Entrada | Resultado esperado |
|---|---|
| `" ana "` | Aceptar `ANA` |
| `"LUIS"` | Aceptar `LUIS` |
| `"ana"` | Rechazar duplicado |
| `"MARIA JOSE"` | Aceptar `MARIA JOSE` |
| `"ALBERTO"` | Aceptar `ALBERTO` |

**Estadísticas:** 4 clientes; más largo `MARIA JOSE` (10); más corto `ANA` (3); 2 nombres que comienzan con `A`.

| Entrada | Resultado esperado |
|---|---|
| `"  "` | Rechazar |
| `"JO"` | Rechazar |
| `"ANA123"` | Rechazar |
| `"MARIA-JOSE"` | Rechazar |
| `"JUAN PEREZ"` | Aceptar |
| `"ANA MARIA"` | Aceptar |

### Preguntas de razonamiento

1. **¿Por qué `"ANA"` y `" ana "` son duplicados?** Tras `strip().upper()`, ambos se convierten en `ANA`.
2. **¿Por qué `isalpha()` no basta para `"MARIA JOSE"`?** Porque el espacio no es una letra y hace que `isalpha()` sobre toda la cadena devuelva `False`.
3. **¿Cómo validar letras o espacios?** Recorrer cada carácter y rechazar si `not caracter.isalpha() and caracter != " "`.
4. **¿Cómo encontrar el más largo y el más corto?** Inicializar ambos con el primer nombre y comparar `len(nombre)` con las longitudes guardadas; actualizar también el nombre asociado. Usar `>` y `<` para conservar el primero en empates.
5. **¿Por qué revisar duplicados antes de agregar?** Para evitar almacenar dos veces el mismo nombre normalizado.

### Aprendizajes

- Validé cadenas carácter por carácter con `for`, `isalpha()` y condiciones.
- Comprendí que los espacios interiores requieren una comprobación adicional a `isalpha()`.
- Normalicé nombres con `strip()` y `upper()` antes de comparar duplicados.
- Encontré el nombre más largo y más corto con variables auxiliares, sin `max()` ni `min()`.
- Conservé el primer nombre en empates utilizando `>` y `<`.
- Diferencié `continue` y `break` en bucles anidados.

### Errores identificados y correcciones

- **`continue` innecesario en la revisión de caracteres:** puede sustituirse por `break` al detectar el primer carácter inválido para evitar revisiones adicionales. El código entregado funciona igualmente.
- **Respuesta conceptual incompleta:** no basta con comparar longitudes; hay que conservar también los nombres correspondientes.
- **Comprobación de existencia:** `in` verifica duplicados; `append()` agrega elementos.

## 7. Cierre del día

**Semáforo final:** 🟢 VERDE.

- Práctica: aprobada.
- Desafío autónomo: aprobado.
- Evaluación conceptual: 5/5.
- Mutación 007: aprobada.

**Próxima sesión:** Día 008 — nuevo contenido, con repaso activo de los días anteriores.
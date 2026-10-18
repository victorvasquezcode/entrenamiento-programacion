# Día 002 — Operadores y expresiones lógicas

**Módulo:** 01 — Lógica de programación  
**Estado:** 🟢 VERDE
**Concepto:** Operadores de comparación y operadores lógicos

---

## 1. Concepto aprendido

Los operadores de comparación permiten comparar valores y producen un resultado booleano: `True` o `False`.

### Operadores de comparación

| Operador | Significado | Ejemplo |
|---|---|---|
| `>` | Mayor que | `8 > 5` |
| `<` | Menor que | `3 < 7` |
| `>=` | Mayor o igual | `10 >= 10` |
| `<=` | Menor o igual | `5 <= 8` |
| `==` | Igualdad | `5 == 5` |
| `!=` | Diferente | `5 != 3` |

### Operadores lógicos

- **`and`:** Todas las condiciones deben ser verdaderas.
- **`or`:** Al menos una condición debe ser verdadera.
- **`not`:** Invierte un valor booleano.

### Tabla de verdad

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

### Precedencia lógica

En Python, los operadores lógicos se evalúan en este orden:

1. `not`
2. `and`
3. `or`

Los paréntesis permiten expresar agrupaciones explícitas y mejorar la legibilidad.

### Ejemplo de razonamiento

`edad >= 18 or autorizacion`

Si `edad = 16` y `autorizacion = True`:

- `edad >= 18` → False.
- `autorizacion` → True.
- `False or True` → True.

**Aprendizaje:** Con `or`, basta con que una condición sea verdadera.

---

## 2. Ejercicio práctico — Control de acceso

**Archivo:** `practica.py`

### Problema

Una plataforma permite el ingreso cuando el usuario tiene al menos 18 años y su cuenta está activa.

### Entrada

- Edad: número entero.
- Estado de cuenta: `si` o `no`.

### Proceso

1. Comprobar si la edad es mayor o igual a 18.
2. Comprobar si la cuenta está activa.
3. Combinar ambas condiciones mediante `and`.

**Condición:**

`edad >= 18 and estado == "si"`

### Salida

- Acceso permitido.
- Acceso denegado.

### Casos de prueba

| Edad | Estado | Resultado |
|---|---|---|
| 20 | si | Permitido |
| 17 | si | Denegado |
| 25 | no | Denegado |
| 18 | si | Permitido |

### Aprendizajes

- `and` exige que ambas condiciones sean verdaderas.
- `==` compara valores, mientras que `=` realiza una asignación.
- Las comparaciones de texto distinguen mayúsculas y minúsculas.
- Una entrada como `Si` no es igual a `si`.

---

## 3. Desafío autónomo — Sistema de becas

**Archivo:** `desafio.py`

### Problema

Una institución otorga una beca cuando el estudiante tiene promedio mayor o igual a 16 y asistencia mayor o igual al 80%, o cuando obtuvo el primer puesto.

### Entrada

- Promedio: número decimal.
- Asistencia: porcentaje entero.
- Primer puesto: `si` o `no`.

### Proceso

1. Comprobar si el promedio es mayor o igual a 16.
2. Comprobar si la asistencia es mayor o igual al 80%.
3. Verificar si obtuvo el primer puesto.
4. Combinar las condiciones mediante `and` y `or`.

**Condición:**

`(promedio >= 16 and asistencia >= 80) or primer_puesto == "si"`

### Salida

- Aprobado.
- Desaprobado.

### Casos de prueba

| Promedio | Asistencia | Primer puesto | Resultado |
|---|---|---|---|
| 17 | 90 | no | Aprobado |
| 15 | 95 | no | Desaprobado |
| 12 | 60 | si | Aprobado |
| 18 | 70 | no | Desaprobado |
| 16 | 80 | no | Aprobado |

### Aprendizajes

- `and` tiene mayor precedencia que `or`.
- Los paréntesis permiten expresar claramente las reglas.
- Una condición alternativa puede permitir un resultado aunque otras condiciones no se cumplan.
- Las condiciones deben reflejar exactamente las reglas del problema.

---

## 4. Mutación 002 — Acceso a sala de servidores

**Archivo:** `mutacion_002.py`

### Problema

Una empresa permite el acceso a una sala de servidores si el trabajador cumple todas las condiciones obligatorias y, además, tiene autorización especial o es administrador.

### Entrada

- Edad: entero.
- Cuenta activa: `si` o `no`.
- Suspendido: `si` o `no`.
- Autorización especial: `si` o `no`.
- Administrador: `si` o `no`.

### Proceso

**Grupo A — Condiciones obligatorias**

1. Edad mayor o igual a 18.
2. Cuenta activa.
3. No estar suspendido.

Todas deben cumplirse mediante `and`.

**Grupo B — Condiciones alternativas**

1. Tener autorización especial.
2. Ser administrador.

Basta con cumplir una mediante `or`.

**Condición final**

`grupo_a and grupo_b`

### Salida

- Permitido.
- Denegado.

### Restricciones

- Utilizar `and`, `or` y `not`.
- Utilizar una sola condición `if` para decidir el acceso.
- No utilizar condiciones `if` anidadas.
- Se permiten variables auxiliares.

### Casos de prueba

| Edad | Activa | Suspendido | Autorizado | Admin | Resultado |
|---|---|---|---|---|---|
| 25 | si | no | si | no | Permitido |
| 30 | si | no | no | si | Permitido |
| 17 | si | no | si | si | Denegado |
| 25 | si | si | si | si | Denegado |
| 25 | no | no | si | si | Denegado |
| 25 | si | no | no | no | Denegado |

### Error identificado

En mi primera solución utilicé correctamente `and` y `or`, pero olvidé utilizar explícitamente `not`.

**Corrección que debo aplicar:**

1. Crear una variable booleana que represente si el trabajador está suspendido.
2. Utilizar `not` para comprobar que no esté suspendido.
3. Mantener el comportamiento correcto de los casos de prueba.

### Aprendizajes

- Las variables auxiliares permiten dividir condiciones complejas.
- Agrupar condiciones mejora la lectura y el mantenimiento.
- Un administrador suspendido no puede ingresar.
- Debo revisar todas las restricciones antes de entregar.
- Que un programa produzca resultados correctos no significa necesariamente que cumpla todas las restricciones solicitadas.

---

## 5. Evaluación conceptual

### ¿Cuál es la diferencia entre `=` y `==`?

`=` se utiliza para asignar un valor a una variable. `==` compara dos valores y devuelve un booleano.

### ¿Por qué `True and False` produce `False`?

Porque `and` requiere que ambas condiciones sean verdaderas.

### ¿Por qué `True or False` produce `True`?

Porque `or` requiere que al menos una condición sea verdadera.

### ¿Qué hace `not`?

Invierte un valor booleano: `True` se convierte en `False` y viceversa.

### ¿Por qué utilizar paréntesis?

Para expresar claramente cómo se agrupan las condiciones y evitar interpretaciones equivocadas.

### ¿Qué sucede si cambio el `and` principal por `or`?

Bastaría con cumplir uno de los grupos para permitir el acceso, lo que incumpliría las reglas de seguridad.

### ¿Puede ingresar un administrador suspendido?

No. Estar libre de suspensión es una condición obligatoria para todos.

### ¿Qué ventaja tienen las variables auxiliares?

Permiten organizar reglas complejas, darles nombres significativos y facilitar la comprensión del código.

---

## 6. Errores y lecciones importantes

- Debo revisar que utilicé todos los operadores solicitados.
- Debo distinguir condiciones obligatorias de alternativas.
- Debo comprender la precedencia de operadores.
- Los paréntesis mejoran la legibilidad.
- Las entradas de texto pueden requerir normalización.
- Las pruebas deben incluir combinaciones que permitan y denieguen el acceso.

---

## 7. Reflexión personal

**¿Qué aprendí?**

A utilizar operadores de comparación y operadores lógicos para transformar reglas en decisiones de Python.

**¿Qué hice bien?**

Separé correctamente las condiciones en grupos y utilicé variables auxiliares para representar la lógica.

**¿Qué debo mejorar?**

Verificar todas las restricciones del enunciado y practicar el uso de `not`.

**¿Qué debo recordar?**

Antes de escribir una condición compleja, debo identificar qué reglas son obligatorias y cuáles son alternativas.
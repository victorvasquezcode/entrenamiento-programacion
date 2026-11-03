# Día 013 — Escritura segura de archivos

**Módulo:** 01 — Lógica de Programación con Python  
**Estado:** 🟢 VERDE  
**Archivos:** `practica.py`, `desafio.py`, `mutacion_013.py`

---

## 1. Objetivo

Aprender a guardar información en archivos sin sobrescribir directamente el contenido original, utilizando archivos temporales, validación previa, reemplazo atómico y manejo de errores.

## 2. Conceptos aprendidos

### Escritura segura

El proceso consiste en:

1. Validar todos los datos.
2. Crear un archivo temporal en el mismo directorio del destino.
3. Escribir la nueva información.
4. Cerrar correctamente el temporal.
5. Reemplazar el original mediante `os.replace()`.
6. Intentar limpiar el temporal si ocurre un error.

**Principio:** no modificar el archivo original mientras se prepara la nueva versión.

### `tempfile.NamedTemporaryFile()`

Permite crear archivos temporales con nombres únicos.

Argumentos utilizados:

- `mode="w"`: escritura de texto.
- `encoding="utf-8"`: codificación.
- `dir=directorio`: ubicación del temporal.
- `delete=False`: permite conservar el temporal después de cerrarlo para reemplazar el destino.

### `os.replace()`

Reemplaza el archivo de destino por el temporal.

Cuando se realiza dentro del mismo sistema de archivos y la operación tiene éxito, proporciona un reemplazo atómico.

**Atomicidad no significa durabilidad:** un reemplazo atómico no garantiza por sí solo la persistencia de los datos ante un corte de energía.

### `try`, `except` y `finally`

- `try`: ejecuta operaciones que pueden fallar.
- `except OSError`: captura errores del sistema de archivos.
- `finally`: permite ejecutar tareas de limpieza incluso cuando ocurre una excepción o un retorno.

La limpieza también debe manejar sus propios errores para evitar que estos oculten el resultado principal.

### `unittest.mock.patch`

Permite sustituir temporalmente funciones para simular fallos controlados.

Ejemplo:

```python
with patch("os.replace", side_effect=OSError("Fallo simulado")):
    resultado = guardar_inventario_seguro(ruta, inventario)
```

Se puede comprobar que una operación no fue ejecutada:

```python
mock_temporal.assert_not_called()
```

## 3. Ejercicio práctico — `practica.py`

Implementé `guardar_seguro(ruta, lineas)`.

Características:

- Validación de lista y cadenas.
- Escritura en archivo temporal.
- Reemplazo del archivo original.
- Manejo de `OSError`.
- Limpieza del temporal.

**Resultado:** 🟢 Aprobado.

## 4. Desafío autónomo — `desafio.py`

Implementé `guardar_inventario_seguro(ruta, inventario)`.

Validaciones:

- Inventario de tipo diccionario.
- Códigos y nombres válidos.
- Campos obligatorios.
- Stock entero no negativo, excluyendo booleanos.
- Precio numérico, finito y no negativo.
- Rechazo de separadores prohibidos.
- Detección de códigos duplicados después de `.strip()`.

Persistencia:

- Ordenamiento por código normalizado.
- Precio con dos decimales.
- Temporal con nombre único.
- Reemplazo mediante `os.replace()`.
- Limpieza en `finally`.

Valores de retorno:

| Valor | Significado |
|---|---|
| `True` | Guardado correcto |
| `None` | Datos inválidos |
| `False` | Error de escritura o reemplazo |

**Resultado:** 🟢 Aprobado.

## 5. Mutación — `mutacion_013.py`

Diseñé pruebas utilizando `tempfile.TemporaryDirectory()`, `patch()` y `assert`.

Pruebas implementadas:

1. Fallo simulado de `os.replace()`.
2. Stock negativo.
3. Precio infinito.
4. Códigos duplicados después de normalizar.
5. Nombre con separador prohibido.
6. Fallo simulado al crear el temporal.

Las pruebas comprueban, según corresponda:

- El valor de retorno.
- La conservación del contenido original.
- La ausencia de temporales residuales.
- Que no se invoquen operaciones de escritura o reemplazo cuando los datos son inválidos.

**Resultado:** 🟢 Aprobado en revisión de código.

## 6. Errores y correcciones importantes

**Error 1: ordenamiento por claves originales.**

Se corrigió utilizando:

```python
sorted(inventario, key=lambda codigo: codigo.strip())
```

**Error 2: comprobación del temporal fuera del bloque protegido.**

Se corrigió protegiendo tanto `os.path.exists()` como `os.remove()` frente a `OSError`.

**Precisión 3: fallo de creación frente a fallo de escritura.**

Simular un error en `NamedTemporaryFile()` prueba la creación del temporal, pero no una escritura fallida después de crearlo.

Queda pendiente practicar este último escenario con un objeto de archivo simulado que falle durante `write()`.

## 7. Repaso activo

Temas reforzados:

- Copias superficiales y referencias mutables.
- Diferencias entre `type()` e `isinstance()`.
- Modo de escritura `"w"`.
- Normalización con `.strip()`.
- Conjuntos para detectar duplicados.
- Manejo de excepciones.
- Atomicidad y durabilidad.

## 8. Aprendizajes principales

- Primero se valida; después se escribe.
- Un archivo temporal no equivale a una copia de seguridad.
- Los nombres temporales únicos evitan colisiones.
- El archivo original debe conservarse si falla la preparación de la nueva versión.
- Las pruebas deben comprobar tanto el resultado como los efectos secundarios.
- Los fallos del sistema operativo pueden simularse para verificar comportamientos difíciles de reproducir.

## 9. Autoevaluación

**Semáforo:** 🟢 VERDE

Logros:

- Implementación de escritura segura.
- Validación completa de inventarios.
- Detección de duplicados normalizados.
- Manejo de errores y limpieza.
- Introducción a pruebas con mocks.
- Explicación de atomicidad y durabilidad.

**Pendiente de repaso futuro:** simular un fallo durante `write()` y estudiar pruebas de fallos más complejos.

## 10. Próxima sesión

**Día 014:** nuevo tema, sujeto al repaso activo inicial.

Mantener la metodología:

1. Concepto técnico breve.
2. Ejercicio práctico.
3. Desafío autónomo.
4. Mutación y casos límite.
5. Evaluación de dominio antes de avanzar.

**Cierre:** Día 013 completado. 🟢

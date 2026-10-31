# Día 012 — Escritura de archivos y persistencia de datos

**Fecha:** 31/10/2026  
**Módulo:** 01 — Lógica de Programación  
**Lenguaje:** Python  
**Estado:** 🟢 VERDE  
**Tema:** Escritura, validación y persistencia de archivos

---

## 1. Objetivo del día

Aprender a escribir archivos de texto, validar información antes de guardarla y actualizar datos persistentes utilizando funciones independientes.

Aplicar estos conocimientos a un generador de reportes de ventas y a un sistema de inventario.

## 2. Conceptos aprendidos

### Escritura de archivos

```python
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola\n")
```

- `"r"`: lectura.
- `"w"`: escritura; crea o sobrescribe el archivo.
- `"a"`: agrega contenido al final.
- `write()`: escribe cadenas de texto.
- `\n`: salto de línea.
- `with`: gestiona el cierre del archivo.

### Manejo de errores

```python
try:
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("Datos\n")
except OSError:
    return False
```

`OSError` permite capturar errores de entrada y salida, pero no revierte las operaciones que ya se realizaron.

### Validación de datos

- `type(valor) is int`: comprueba el tipo exacto y excluye booleanos.
- `strip()`: elimina espacios exteriores.
- `split(";")`: separa campos.
- `math.isfinite()`: comprueba que un número sea finito.
- `sorted()`: permite recorrer claves ordenadas.
- `:.2f`: representa un número con dos decimales.

### Persistencia

La persistencia permite conservar información después de finalizar el programa.

Los cambios realizados en un diccionario permanecen en memoria hasta que se guardan en un medio persistente.

## 3. Ejercicio práctico — practica.py

**Problema:** guardar nombres válidos en un archivo.

Implementé una función que:

- Valida que la entrada sea una lista.
- Rechaza elementos que no sean cadenas.
- Normaliza nombres con `strip().title()`.
- Cuenta nombres aceptados y rechazados.
- Escribe un nombre por línea.
- Maneja errores mediante `OSError`.

**Resultado:** aprobado.

## 4. Desafío autónomo — desafio.py

**Problema:** generar un reporte de ventas.

Funciones desarrolladas:

### validar_ventas()

- Valida productos e importes.
- Excluye valores inválidos y booleanos.
- Consolida productos con nombres equivalentes después de eliminar espacios.
- Devuelve un diccionario nuevo sin modificar el original.

### calcular_resumen()

- Calcula cantidad, total y promedio.
- Evita divisiones entre cero.
- Conserva productos sin ventas válidas.

### guardar_reporte()

- Ordena los productos alfabéticamente.
- Genera un archivo de texto.
- Presenta importes con dos decimales.
- Calcula el total general.
- Devuelve el estado de la escritura.

**Resultado:** aprobado por revisión del código.

## 5. Mutación 012 — mutacion_012.py

**Problema:** cargar, modificar y guardar un inventario persistente.

Funciones desarrolladas:

### cargar_inventario()

- Lee archivos con campos separados por punto y coma.
- Valida código, nombre, stock y precio.
- Rechaza registros incorrectos.
- Conserva la primera aparición válida de cada código.
- Comprueba que los precios sean finitos.
- Devuelve `None` ante errores de lectura.

### actualizar_stock()

- Procesa entradas y salidas.
- Rechaza cantidades inválidas.
- Evita stock negativo.
- Mantiene los datos sin cambios cuando una operación es rechazada.

### guardar_inventario()

- Ordena los productos por código.
- Guarda los cuatro campos requeridos.
- Escribe precios con dos decimales.
- Devuelve `True` o `False` según el resultado de escritura.

**Resultado:** código aprobado y pruebas complementarias confirmadas como completadas.

## 6. Errores y riesgos identificados

### Sobrescritura de archivos

Abrir un archivo con `"w"` elimina su contenido anterior.

Si ocurre un error durante la escritura, el archivo puede quedar incompleto.

**Aprendizaje:** capturar una excepción no significa recuperar automáticamente los datos anteriores.

### División entre cero

Cuando una lista de ventas está vacía, el promedio debe manejarse mediante una condición previa.

### Tipos booleanos

`bool` es un subtipo de `int` en Python.

Por eso, cuando se necesita aceptar exclusivamente enteros, `type(valor) is int` puede ser adecuado.

### Ejecuciones repetidas

Si un programa carga un inventario, modifica el stock y guarda los cambios, volver a ejecutarlo puede aplicar las mismas modificaciones otra vez.

**Aprendizaje:** una operación no siempre es idempotente.

### Escritura segura

Una copia de respaldo puede ayudar a recuperar datos. Una estrategia más robusta consiste en escribir primero un archivo temporal y reemplazar el original después de completar correctamente la escritura.

## 7. Principios de programación reforzados

1. Validar antes de procesar.
2. Separar responsabilidades mediante funciones.
3. No modificar datos ante operaciones inválidas.
4. Diferenciar resultados válidos de errores.
5. Probar casos normales y casos límite.
6. Evitar pérdidas de información durante la persistencia.
7. Mantener separadas la lógica de negocio y la presentación.

## 8. Relación con Ingeniería de Datos

Los ejercicios aplicaron una versión básica del proceso ETL:

- **Extract:** leer información desde archivos.
- **Transform:** validar, limpiar, normalizar y calcular.
- **Load:** escribir los resultados procesados.

También introdujeron los conceptos de integridad de datos, persistencia, manejo de errores e idempotencia.

## 9. Autoevaluación

| Actividad | Estado |
|---|---|
| Repaso activo | 🟢 |
| Ejercicio práctico | 🟢 |
| Desafío autónomo | 🟢 |
| Mutación 012 | 🟢 |
| Razonamiento técnico | 🟢 |
| Pruebas complementarias | Completadas según confirmación |

**Semáforo final: 🟢 VERDE**

## 10. Próxima sesión

**Día 013 — Pendiente**

Continuar con el siguiente tema del Módulo 01, incorporando repaso activo de los conocimientos anteriores.

No avanzar sin comprobar comprensión, implementación y autonomía.

---

**Conclusión personal:** aprendí a transformar información en memoria y conservarla en archivos, comprendiendo que validar los datos y protegerlos frente a errores son responsabilidades diferentes.
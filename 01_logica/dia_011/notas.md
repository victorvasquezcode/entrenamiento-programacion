# Día 011 — Lectura y procesamiento de archivos de texto

**Estado final:** 🟢 VERDE — APROBADO  
**Módulo:** 01 — Lógica de programación  
**Próxima sesión:** Día 012 (aún no iniciado)

## 1. Objetivo

Leer archivos `.txt` con `with open()`, recorrer líneas, validar datos, gestionar errores específicos, agrupar registros y calcular estadísticas sin mezclar responsabilidades.

## 2. Conceptos técnicos

- `with open(ruta, "r", encoding="utf-8")` abre el archivo para lectura y gestiona su cierre.
- `for linea in archivo` permite procesar cada línea sin cargar el archivo completo en memoria.
- El contenido leído es `str`; `int()` y `float()` convierten valores cuando su formato lo permite.
- `ValueError` captura conversiones inválidas y `FileNotFoundError` permite tratar una ruta inexistente.
- `strip()` elimina espacios exteriores; `title()` normaliza nombres según las reglas del ejercicio.
- `math.isfinite()` rechaza `nan`, `inf` y `-inf`, aunque `float()` los acepte.
- Los diccionarios de listas permiten agrupar observaciones por clave.

## 3. Repaso activo — 3/3

**A.** `int(" +25 ")` → `25`.  
**B.** Media de `[10, 20, 30]` → `20.0`.  
**C.** `int("12.5")` produce `ValueError`; el bloque `except` asigna `None`. No todas las cadenas son inválidas: `int("25")` funciona.

## 4. Práctica — `practica.py` — 10/10

**Objetivo:** leer enteros de un archivo, devolver `(numeros, rechazados)` y `None` si no existe.

```python
def leer_numeros(ruta):
    numeros = []
    rechazados = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    convertidor = int(linea)
                    numeros.append(convertidor)
                except ValueError:
                    rechazados += 1
    except FileNotFoundError:
        return None
    return numeros, rechazados
```

**Archivo de ejemplo:** líneas `10`, ` 20`, `abc`, `-3`, línea vacía y `5`.  
**Resultado esperado:** `([10, 20, -3, 5], 2)`.

| Caso | Resultado esperado |
|---|---|
| `10`, `20`, `30` | `([10, 20, 30], 0)` |
| `abc`, `xyz` | `([], 2)` |
| Archivo vacío | `([], 0)` |
| `+7`, `-2`, `3.5` | `([7, -2], 1)` |
| Archivo inexistente | `None` |

**Control conceptual — 4/4:** `with` cierra el archivo incluso ante excepciones; `linea` es `str`; archivo inexistente genera `FileNotFoundError`; cadenas como `abc` no representan enteros convertibles.

## 5. Desafío — `desafio.py` — 10/10

**Objetivo:** leer `ciudad;temperatura`, validar temperaturas finitas en `[-50, 60]`, normalizar ciudades, agrupar observaciones y calcular promedios.

```python
import math

def validar_temperatura(valor):
    try:
        convertir = float(valor)
        if math.isfinite(convertir) and -50 <= convertir <= 60:
            return convertir
        else:
            return None
    except (ValueError, TypeError):
        return None

def procesar_temperaturas(ruta):
    datos = {}
    rechazados = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                campos = linea.split(";")
                if len(campos) != 2:
                    rechazados += 1
                    continue
                ciudad, temperatura = campos
                normalizar_temperatura = validar_temperatura(temperatura)
                normalizar_ciudad = ciudad.strip().title()
                if not normalizar_ciudad:
                    rechazados += 1
                    continue
                if normalizar_temperatura is not None:
                    if normalizar_ciudad in datos:
                        datos[normalizar_ciudad].append(normalizar_temperatura)
                    else:
                        datos[normalizar_ciudad] = [normalizar_temperatura]
                else:
                    rechazados += 1
    except FileNotFoundError:
        return None
    return datos, rechazados

def calcular_promedios(datos):
    promedio = {}
    total = 0
    if not datos:
        return promedio
    for dato in datos:
        cantidad = len(datos[dato])
        total = sum(datos[dato])
        promedio[dato] = total / cantidad
    return promedio
```

**Resultado de referencia:** `{'Lima': [22.5, 23.5], 'Cusco': [14.0, 15.0], 'Tacna': [19.0]}`, rechazados `3`; promedios `{'Lima': 23.0, 'Cusco': 14.5, 'Tacna': 19.0}`.

**Razonamiento — 4/4:** `math.isfinite()` excluye no finitos; el diccionario agrupa temperaturas por ciudad; sin normalizar, `LIMA` y `Lima` serían claves diferentes; separar funciones facilita pruebas, mantenimiento y reutilización. **Mejora opcional:** eliminar `total = 0` inicial, pues se reasigna en el bucle.

## 6. Mutación — `mutacion_011.py` — 10/10

**Objetivo:** leer inventario `codigo;nombre;cantidad;precio`, validar, acumular cantidades de duplicados compatibles y calcular resumen.

```python
import math

def convertir_cantidad(valor):
    try:
        if type(valor) is bool:
            return None
        cantidad_entera = int(valor)
        if cantidad_entera > 0:
            return cantidad_entera
        else:
            return None
    except (ValueError, TypeError):
        return None

def convertir_precio(valor):
    try:
        if type(valor) is bool:
            return None
        cantidad_decimal = float(valor)
        if math.isfinite(cantidad_decimal) and cantidad_decimal > 0:
            return cantidad_decimal
        else:
            return None
    except (ValueError, TypeError):
        return None

def procesar_inventario(ruta):
    datos = {}
    rechazados = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                campos = linea.split(";")
                if len(campos) != 4:
                    rechazados += 1
                    continue
                codigo, nombre, cantidad, precio = campos
                normalizar_codigo = codigo.strip().upper()
                if not len(normalizar_codigo) == 4 or not normalizar_codigo[:1] == "P" or not normalizar_codigo[-3:].isdigit():
                    rechazados += 1
                    continue
                normalizar_nombre = nombre.strip().title()
                if not normalizar_nombre:
                    rechazados += 1
                    continue
                nueva_cantidad = convertir_cantidad(cantidad)
                if nueva_cantidad is None:
                    rechazados += 1
                    continue
                nuevo_precio = convertir_precio(precio)
                if nuevo_precio is None:
                    rechazados += 1
                    continue
                if normalizar_codigo in datos:
                    if normalizar_nombre == datos[normalizar_codigo]["nombre"] and nuevo_precio == datos[normalizar_codigo]["precio"]:
                        datos[normalizar_codigo]["cantidad"] += nueva_cantidad
                    else:
                        rechazados += 1
                        continue
                else:
                    datos[normalizar_codigo] = {
                        "nombre": normalizar_nombre,
                        "cantidad": nueva_cantidad,
                        "precio": nuevo_precio
                    }
    except FileNotFoundError:
        return None
    return datos, rechazados

def calcular_resumen(datos):
    productos_distintos = len(datos)
    unidades_totales = 0
    valor_total = 0
    contador = 0
    codigo_mayor_valor = None
    valor_mayor = 0
    for dato in datos:
        unidades_totales += datos[dato]["cantidad"]
        valor_total_producto = datos[dato]["cantidad"] * datos[dato]["precio"]
        valor_total += valor_total_producto
        contador += 1
        if contador == 1:
            codigo_mayor_valor = dato
            valor_mayor = valor_total_producto
        else:
            if valor_total_producto > valor_mayor:
                codigo_mayor_valor = dato
                valor_mayor = valor_total_producto
    return productos_distintos, unidades_totales, valor_total, codigo_mayor_valor
```

**Archivo de prueba:**

```text
P001;Teclado;10;45.50
P002;Mouse;5;25
P003;Monitor;3;750
P001;Teclado;4;45.50
P004;Cable;abc;12
P005;USB;8;nan
P006;Laptop;2;2500
registro incorrecto
P007;Hub;0;30
P008;Soporte;6;40
```

**Resultados correctos (se corrigió un error aritmético en el enunciado original):**

| Código | Cantidad | Precio unitario | Valor |
|---|---:|---:|---:|
| P001 | 14 | S/ 45.50 | S/ 637.00 |
| P002 | 5 | S/ 25.00 | S/ 125.00 |
| P003 | 3 | S/ 750.00 | S/ 2,250.00 |
| P006 | 2 | S/ 2,500.00 | S/ 5,000.00 |
| P008 | 6 | S/ 40.00 | S/ 240.00 |
| **TOTAL** | **30** | | **S/ 8,252.00** |

**Resumen esperado:** `(5, 30, 8252.0, 'P006')`; **rechazados:** `4`.

**Razonamiento — 5/5:** cantidad cero incumple la regla de negocio; precios distintos para un código impiden una valoración única; el mayor valor depende de `cantidad * precio`; la lectura secuencial evita cargar todo el archivo; si todos son rechazados, `procesar_inventario` devuelve `({}, rechazados)` y `calcular_resumen({})` devuelve `(0, 0, 0, None)`.

**Mejoras opcionales:** simplificar la selección del primer máximo; estudiar `decimal.Decimal` para cálculos monetarios. Ninguna de estas mejoras es necesaria para aprobar el ejercicio.

## 7. Evaluación final

| Componente | Resultado |
|---|---|
| Repaso activo | 3/3 |
| `practica.py` | 10/10 |
| Control conceptual | 4/4 |
| `desafio.py` | 10/10 |
| Razonamiento del desafío | 4/4 |
| `mutacion_011.py` | 10/10 |
| Razonamiento de mutación | 5/5 |

**Semáforo final:** 🟢 VERDE. **Día 011 cerrado.**

## 8. Reflexión y próximos pasos

- Aprendí a leer archivos reales y a controlar errores de lectura y conversión.
- Puedo rechazar registros inválidos sin detener el procesamiento de los demás.
- Sé agrupar datos por claves, consolidar duplicados compatibles y calcular resúmenes.
- Debo seguir practicando la verificación de resultados numéricos y la separación de responsabilidades.
- **Día 012:** desbloqueado para la próxima sesión; todavía no iniciado.
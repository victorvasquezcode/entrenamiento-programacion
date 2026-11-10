# Día 016 — Modularización y reutilización de funciones

**Fecha:** 10/11/2026  
**Ruta:** Python desde cero → Ciencia e Ingeniería de Datos  
**Estado final:** 🟢 VERDE — APROBADO  
**Próxima sesión:** Día 017

---

## 1. Objetivo del día

Aprender a dividir un programa en funciones pequeñas, reutilizables y comprobables.

### Competencias desarrolladas

- Responsabilidad única.
- Modularización y composición de funciones.
- Reutilización de validaciones.
- Pruebas unitarias con `assert`.
- Manejo de errores con `InvalidOperation`.
- Precisión monetaria con `Decimal`.
- Normalización de productos.
- Agrupación de registros.
- Promedio ponderado.
- Inmutabilidad.
- Refactorización.
- Modificación de funcionalidades sin regresiones.

---

## 2. Repaso activo — 🟢 APROBADO

**Resultado:** 4/4.

### A. Precisión decimal

`Decimal("0.10")` conserva exactamente el decimal indicado por la cadena.

`Decimal(0.10)` recibe la aproximación binaria del tipo `float`.

### B. Funciones puras

Una función que modifica directamente un diccionario recibido como argumento no es pura.

### C. Promedio ponderado

Dos unidades a S/ 12 y tres unidades a S/ 22:

- Cantidad total: 5.
- Importe total: S/ 90.
- Promedio ponderado: S/ 18.

### D. Tipos de datos

```python
type(True) is int        # False
isinstance(True, int)    # True
```

`bool` es una subclase de `int`, pero no es exactamente el mismo tipo.

---

## 3. Conceptos fundamentales

### Responsabilidad única

Una función debe tener una responsabilidad claramente definida.

Una responsabilidad puede necesitar varias condiciones.

Ejemplo: `validar_cantidad()` comprueba el tipo y el valor, pero ambas comprobaciones pertenecen a la misma responsabilidad.

### Composición de funciones

Consiste en construir una operación mediante la reutilización de otras funciones.

En el proyecto:

- `validar_cantidad()` comprueba cantidades.
- `convertir_precio()` convierte y valida precios.
- `calcular_importe()` reutiliza ambas.
- `normalizar_producto()` limpia nombres.
- `resumir_ventas_monetarias()` coordina la validación, agrupación y resumen.

### Funciones puras

Una función pura:

1. Produce el mismo resultado para las mismas entradas, bajo las mismas condiciones.
2. No modifica datos externos ni genera efectos secundarios observables.

Puede llamar a otras funciones puras y continuar siendo pura.

### Validación previa

Primero se validan todos los registros y después se agrupan.

Esto permite rechazar una entrada inválida sin devolver un resumen parcial.

### Pruebas unitarias

Permiten comprobar funciones individuales y localizar errores antes de integrar el programa completo.

---

## 4. Código final — Día 016

**Archivo sugerido:** `dia_016.py`

Incluye la práctica, el desafío y la mutación.

```python
from decimal import Decimal, InvalidOperation


def validar_cantidad(cantidad):
    if type(cantidad) is int and cantidad > 0:
        return True
    else:
        return False


def convertir_precio(precio):
    if type(precio) is str:
        try:
            precio_decimal = Decimal(precio)

            if not precio_decimal.is_finite() or precio_decimal < 0:
                return None

        except InvalidOperation:
            return None

    else:
        return None

    return precio_decimal


def calcular_importe(cantidad, precio):
    if not validar_cantidad(cantidad):
        return None

    precio_decimal = convertir_precio(precio)

    if precio_decimal is None:
        return None

    total = cantidad * precio_decimal
    return total


def normalizar_producto(producto):
    if type(producto) is str:
        producto_limpio = producto.strip()

        if not producto_limpio:
            return None

        return producto_limpio

    return None


def resumir_ventas_monetarias(ventas):
    if type(ventas) is not list:
        return None

    ventas_validadas = []

    # Fase 1: validar todos los registros.
    for venta in ventas:
        if type(venta) is not dict:
            return None

        claves = ("producto", "cantidad", "precio")

        if not all(clave in venta for clave in claves):
            return None

        producto = normalizar_producto(venta["producto"])
        cantidad = venta["cantidad"]
        precio = venta["precio"]

        if producto is None:
            return None

        importe = calcular_importe(cantidad, precio)

        if importe is None:
            return None

        ventas_validadas.append({
            "producto": producto,
            "cantidad": cantidad,
            "importe": importe
        })

    # Fase 2: agrupar registros validados.
    resumen_ventas = {}

    for venta in ventas_validadas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        importe = venta["importe"]

        if producto in resumen_ventas:
            resumen_ventas[producto]["cantidad"] += cantidad
            resumen_ventas[producto]["total"] += importe
            resumen_ventas[producto]["operaciones"] += 1
        else:
            resumen_ventas[producto] = {
                "cantidad": cantidad,
                "total": importe,
                "operaciones": 1
            }

    # Fase 3: calcular el promedio ponderado.
    for datos in resumen_ventas.values():
        cantidad = datos["cantidad"]
        total = datos["total"]

        datos["precio_promedio"] = total / cantidad

    return resumen_ventas
```

### Contrato de la función principal

| Entrada | Resultado |
|---|---|
| Lista vacía | `{}` |
| Lista de ventas válidas | Diccionario agrupado |
| Registro inválido | `None` |
| Precio inválido | `None` |
| Cantidad inválida | `None` |
| Producto inválido | `None` |

Los registros originales no deben modificarse.

---

## 5. Pruebas de práctica — 🟢 APROBADAS

```python
assert validar_cantidad(3) is True
assert validar_cantidad(True) is False
assert validar_cantidad(0) is False
assert validar_cantidad(-2) is False

assert convertir_precio("0.10") == Decimal("0.10")
assert convertir_precio("abc") is None
assert convertir_precio("NaN") is None
assert convertir_precio("Infinity") is None
assert convertir_precio(10.5) is None

assert calcular_importe(3, "19.90") == Decimal("59.70")
assert calcular_importe(2, "0.10") == Decimal("0.20")
assert calcular_importe(0, "10.00") is None
assert calcular_importe(True, "10.00") is None

assert convertir_precio("-0.10") is None
assert convertir_precio("0") == Decimal("0")
assert convertir_precio("") is None
assert validar_cantidad(3.0) is False
assert calcular_importe(1, "0.001") == Decimal("0.001")
```

**Resultado:** 18 pruebas revisadas satisfactoriamente por inspección.

---

## 6. Pruebas del desafío — 🟢 APROBADO

Se evaluaron diez grupos de pruebas:

1. Lista vacía.
2. Productos repetidos con espacios.
3. Productos independientes.
4. Precio cero.
5. Cantidad booleana.
6. Precios especiales e inválidos.
7. Registro incompleto.
8. Inmutabilidad de entradas.
9. Promedio ponderado.
10. Registro inválido después de uno válido.

**Resultado:** 10/10 grupos revisados satisfactoriamente.

---

## 7. Mutación 016 — 🟢 APROBADA

### Nuevo requisito

Incorporar `operaciones` al resumen.

Cada registro válido cuenta como una operación, independientemente de la cantidad de unidades vendidas.

### Ejemplo

```python
ventas = [
    {"producto": " Teclado ", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"}
]
```

Resultado esperado:

```python
{
    "Teclado": {
        "cantidad": 5,
        "total": Decimal("80.00"),
        "operaciones": 2,
        "precio_promedio": Decimal("16.00")
    },
    "Mouse": {
        "cantidad": 1,
        "total": Decimal("5.00"),
        "operaciones": 1,
        "precio_promedio": Decimal("5.00")
    }
}
```

### Pruebas de mutación

```python
# PRUEBA 1: Una venta de 10 unidades = 1 operación.
assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 10, "precio": "15.00"}
]) == {
    "Teclado": {
        "cantidad": 10,
        "total": Decimal("150.00"),
        "operaciones": 1,
        "precio_promedio": Decimal("15.00")
    }
}

# PRUEBA 2: Tres registros = 3 operaciones.
assert resumir_ventas_monetarias([
    {"producto": "Mouse", "cantidad": 2, "precio": "10.00"},
    {"producto": " Mouse ", "cantidad": 3, "precio": "20.00"},
    {"producto": "Mouse", "cantidad": 5, "precio": "30.00"}
]) == {
    "Mouse": {
        "cantidad": 10,
        "total": Decimal("230.00"),
        "operaciones": 3,
        "precio_promedio": Decimal("23.00")
    }
}

# PRUEBA 3: Contadores independientes.
assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"}
]) == {
    "Teclado": {
        "cantidad": 5,
        "total": Decimal("80.00"),
        "operaciones": 2,
        "precio_promedio": Decimal("16.00")
    },
    "Mouse": {
        "cantidad": 1,
        "total": Decimal("5.00"),
        "operaciones": 1,
        "precio_promedio": Decimal("5.00")
    }
}

# PRUEBA 4: Registro inválido.
assert resumir_ventas_monetarias([
    {"producto": "Mouse", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": True, "precio": "15.00"}
]) is None

# PRUEBA 5: Lista vacía.
assert resumir_ventas_monetarias([]) == {}
```

**Resultado:** 5/5 pruebas revisadas satisfactoriamente.

Las pruebas de este documento se evaluaron mediante revisión estática; no se ejecutaron de forma independiente durante la revisión.

---

## 8. Evaluación conceptual final

### Pregunta 1 — Responsabilidad única

Una función debe tener una responsabilidad definida.

No significa que solo pueda contener una condición.

`validar_cantidad()` comprueba que el dato sea un entero y que sea positivo. Ambas condiciones pertenecen a la responsabilidad de validar cantidades.

### Pregunta 2 — Reutilización

Reutilizar funciones evita duplicar código y mantiene las reglas de validación centralizadas.

### Pregunta 3 — Pruebas unitarias

Probar funciones auxiliares por separado ayuda a identificar dónde se origina un resultado incorrecto.

### Pregunta 4 — Manejo de None

Si `convertir_precio()` devuelve `None`, `calcular_importe()` debe detener el cálculo y devolver `None`, porque no dispone de un precio válido para multiplicar.

### Pregunta 5 — Pureza

Una función pura puede llamar a otras funciones puras y continuar siendo pura si:

- No produce efectos secundarios observables.
- No modifica los argumentos recibidos.
- Devuelve el mismo resultado para las mismas entradas, bajo las mismas condiciones.

**Resultado conceptual:** aprobado con precisiones en responsabilidad única y pureza.

---

## 9. Observaciones de calidad

### Mejoras aplicadas al código final

- Se corrigió `resumir_ventas_monetarios()` a `resumir_ventas_monetarias()`.
- Se reemplazó la variable local `normalizar_producto` por `producto_limpio`.
- Se eliminó una variable de iteración innecesaria al calcular promedios.

### Mejoras futuras

- Simplificar funciones que devuelven expresiones booleanas.
- Incorporar anotaciones de tipos.
- Organizar las pruebas en archivos independientes.
- Investigar la precisión del contexto decimal.
- Evaluar errores por operaciones decimales extremadamente grandes.

Estas mejoras no bloquean la aprobación del Día 016.

---

## 10. Semáforo final

| Actividad | Estado |
|---|---|
| Día 014 | 🟢 VERDE |
| Día 015 | 🟢 VERDE |
| Día 016 — Repaso activo | 🟢 VERDE |
| Día 016 — Práctica | 🟢 VERDE |
| Día 016 — Desafío | 🟢 VERDE |
| Día 016 — Mutación | 🟢 VERDE |
| Día 016 — Evaluación conceptual | 🟢 VERDE |
| **Día 016 completo** | **🟢 APROBADO** |
| Día 017 | DESBLOQUEADO |

---

## 11. Preparación para el Día 017

### Repaso activo pendiente

Antes de comenzar el nuevo tema, recordar:

1. La diferencia entre responsabilidad única y una sola condición.
2. Las propiedades de una función pura.
3. La diferencia entre cantidad de unidades y cantidad de operaciones.
4. Por qué se validan los registros antes de agrupar.
5. Cómo se calcula un promedio ponderado con `Decimal`.

### Próximo objetivo

Continuar avanzando hacia el desarrollo de programas Python mantenibles, comprobables y orientados al procesamiento de datos.

**Cierre:** Día 016 finalizado satisfactoriamente.

**Semáforo:** 🟢 VERDE.

**Continuación:** Día 017 — próxima sesión.
# Día 015 — Precisión numérica y cálculos monetarios

**Ruta:** Python desde cero → Ciencia e Ingeniería de Datos  
**Fecha:** 07/11/2026  
**Estado final:** 🟢 VERDE — APROBADO

---

## 1. Objetivo del día

Aprender a realizar cálculos monetarios utilizando `decimal.Decimal`, evitando errores de representación binaria y aplicando validaciones estrictas.

**Competencias desarrolladas:**

- Precisión decimal.
- Validación de tipos y valores.
- Manejo específico de excepciones.
- Funciones puras.
- Agrupación de registros.
- Acumulación monetaria.
- Promedio ponderado.
- Pruebas automatizadas.

## 2. Conceptos aprendidos

### Float y precisión binaria

Los números `float` utilizan representación binaria y algunos valores decimales no pueden representarse exactamente.

```python
print(0.1 + 0.2)
# 0.30000000000000004

print(0.1 + 0.2 == 0.3)
# False
```

### Decimal

```python
from decimal import Decimal

Decimal("0.1")  # Decimal exacto
Decimal(0.1)    # Conserva la aproximación del float
```

Para importes monetarios, utilizar preferentemente cadenas decimales.

### Manejo de excepciones

`InvalidOperation` permite capturar determinados errores de conversión y operaciones decimales.

```python
from decimal import Decimal, InvalidOperation

try:
    precio = Decimal("abc")
except InvalidOperation:
    precio = None
```

### Valores finitos

```python
Decimal("10.50").is_finite()     # True
Decimal("NaN").is_finite()       # False
Decimal("Infinity").is_finite()  # False
```

Los importes monetarios válidos deben ser finitos.

### Redondeo monetario

Los sistemas monetarios utilizan reglas de redondeo, pero deben aplicarse en el momento adecuado y siguiendo una política definida.

No redondear automáticamente cada operación sin conocer los requisitos del sistema.

---

## 3. Repaso activo — 🟢 APROBADO

### A. Funciones puras

Una función que modifica un diccionario recibido como argumento no es pura.

### B. Validaciones

```python
math.isfinite(float("inf"))  # False
type(True) is int            # False
```

### C. Promedio ponderado

| Cantidad | Precio | Importe |
|---:|---:|---:|
| 2 | 10 | 20 |
| 3 | 20 | 60 |
| 5 | 30 | 150 |
| **10** | | **230** |

Promedio ponderado: `230 / 10 = 23`.

**Resultado:** 3/3 aprobado.

---

## 4. Práctica — 🟢 APROBADA

### Función `calcular_importe()`

```python
from decimal import Decimal, InvalidOperation

def calcular_importe(cantidad, precio_unitario):
    if not type(cantidad) is int:
        return None

    if cantidad <= 0:
        return None

    if not type(precio_unitario) is str:
        return None

    try:
        precio_decimal = Decimal(precio_unitario)
    except InvalidOperation:
        return None

    if not precio_decimal.is_finite():
        return None

    if precio_decimal < 0:
        return None

    resultado = cantidad * precio_decimal
    return resultado
```

### Pruebas

```python
assert calcular_importe(3, "19.90") == Decimal("59.70")
assert calcular_importe(2, "0.10") == Decimal("0.20")
assert calcular_importe(1, "0") == Decimal("0")

assert calcular_importe(0, "10.00") is None
assert calcular_importe(-20, "10.00") is None
assert calcular_importe(True, "10.00") is None

assert calcular_importe(2, "abc") is None
assert calcular_importe(2, "NaN") is None
assert calcular_importe(2, "Infinity") is None
assert calcular_importe(2, 12.6) is None

resultado = calcular_importe(3, "19.90")
assert type(resultado) is Decimal
```

**Resultado:** 11 pruebas aprobadas por revisión estática.

---

## 5. Desafío y mutación — 🟢 APROBADOS

### Función final `resumir_ventas_monetarias()`

```python
from decimal import Decimal, InvalidOperation

def resumir_ventas_monetarias(ventas):
    resumen_ventas = {}

    if not type(ventas) is list:
        return None

    # Primera etapa: validación
    for registro in ventas:
        if not type(registro) is dict:
            return None

        claves = ("producto", "cantidad", "precio")
        if not all(clave in registro for clave in claves):
            return None

        producto = registro["producto"]
        cantidad = registro["cantidad"]
        precio = registro["precio"]

        if not type(producto) is str:
            return None

        normalizar_nombre = producto.strip()
        if not normalizar_nombre:
            return None

        if not type(cantidad) is int:
            return None

        if cantidad <= 0:
            return None

        if not type(precio) is str:
            return None

        try:
            precios_decimal = Decimal(precio)
        except InvalidOperation:
            return None

        if not precios_decimal.is_finite():
            return None

        if precios_decimal < 0:
            return None

    # Segunda etapa: agrupación
    for registro in ventas:
        producto = registro["producto"]
        cantidad = registro["cantidad"]
        precio = registro["precio"]

        normalizar_nombre = producto.strip()
        precios_decimal = Decimal(precio)
        total = cantidad * precios_decimal

        if normalizar_nombre in resumen_ventas:
            resumen_ventas[normalizar_nombre]["cantidad"] += cantidad
            resumen_ventas[normalizar_nombre]["total"] += total
        else:
            resumen_ventas[normalizar_nombre] = {
                "cantidad": cantidad,
                "total": total
            }

    # Tercera etapa: promedio ponderado
    for clave, datos in resumen_ventas.items():
        cantidad = datos["cantidad"]
        total = datos["total"]
        promedio = total / cantidad
        datos["precio_promedio"] = promedio

    return resumen_ventas
```

### Pruebas finales de la mutación

```python
assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"}
]) == {
    "Teclado": {
        "cantidad": 2,
        "total": Decimal("20.00"),
        "precio_promedio": Decimal("10.00")
    }
}

assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"}
]) == {
    "Teclado": {
        "cantidad": 5,
        "total": Decimal("80.00"),
        "precio_promedio": Decimal("16.00")
    }
}

assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"}
]) == {
    "Teclado": {
        "cantidad": 3,
        "total": Decimal("60.00"),
        "precio_promedio": Decimal("20.00")
    },
    "Mouse": {
        "cantidad": 1,
        "total": Decimal("5.00"),
        "precio_promedio": Decimal("5.00")
    }
}

assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 2, "precio": "0"}
]) == {
    "Teclado": {
        "cantidad": 2,
        "total": Decimal("0"),
        "precio_promedio": Decimal("0")
    }
}

assert resumir_ventas_monetarias([]) == {}

assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 3}
]) is None

assert resumir_ventas_monetarias([
    {"producto": "Teclado", "cantidad": 0, "precio": "10.00"}
]) is None

import copy

ventas_original = [
    {"producto": "Teclado", "cantidad": 2, "precio": "10.00"},
    {"producto": "Teclado", "cantidad": 3, "precio": "20.00"},
    {"producto": "Mouse", "cantidad": 1, "precio": "5.00"}
]

copia = copy.deepcopy(ventas_original)
resultado = resumir_ventas_monetarias(ventas_original)

assert copia == ventas_original
assert resultado is not ventas_original
```

**Resultado:** 8 pruebas finales aprobadas por revisión estática.

### Diseño de la solución

La función se organiza en tres etapas:

1. **Validación:** comprueba todos los registros antes de procesarlos.
2. **Agrupación:** acumula cantidades e importes utilizando `Decimal`.
3. **Promedio:** calcula el precio promedio ponderado después de acumular cada producto.

Los datos originales permanecen sin modificaciones.

---

## 6. Evaluación conceptual final — 🟢 5/5

### 1. ¿Por qué float puede producir resultados inesperados?

Porque utiliza representación binaria y algunos valores decimales no pueden representarse exactamente.

### 2. ¿Qué diferencia existe entre Decimal("0.1") y Decimal(0.1)?

El primero construye el valor decimal exacto. El segundo conserva la aproximación binaria del `float`.

### 3. ¿Por qué rechazar NaN e infinito?

Porque no representan importes monetarios finitos válidos.

### 4. ¿Por qué utilizar InvalidOperation?

Porque permite capturar errores específicos de operaciones decimales sin ocultar otros errores del programa.

### 5. ¿Por qué no redondear automáticamente?

Porque el redondeo debe aplicarse en el momento adecuado y según una política monetaria definida.

---

## 7. Observaciones técnicas para futuras sesiones

### Precisión del contexto decimal

```python
Decimal("1") / Decimal("3")
```

Una división periódica se aproxima según la precisión del contexto decimal.

### Desbordamientos

Los valores decimales extremadamente grandes pueden producir excepciones durante las operaciones, aunque sean finitos antes de calcular.

### Mejoras futuras

- Gestionar excepciones aritméticas avanzadas.
- Definir políticas explícitas de redondeo.
- Evitar conversiones repetidas cuando sea conveniente.
- Separar la validación en funciones reutilizables.
- Ampliar pruebas con casos extremos.

Estas mejoras no forman parte de los requisitos básicos aprobados del Día 015.

---

## 8. Semáforo definitivo

| Actividad | Estado |
|---|---|
| Repaso activo | 🟢 APROBADO |
| Práctica | 🟢 APROBADA |
| Desafío | 🟢 APROBADO |
| Mutación | 🟢 APROBADA |
| Evaluación conceptual | 🟢 APROBADA |
| **Día 015** | **🟢 VERDE** |
| Día 016 | DESBLOQUEADO |

**Nota:** las implementaciones y pruebas fueron evaluadas mediante inspección estática, no mediante ejecución independiente.

## 9. Próxima sesión — Día 016

**Fecha:** 08/11/2026

Comenzar con repaso activo del Día 015, sin consultar estas notas, y continuar con el siguiente concepto de la ruta hacia Ciencia e Ingeniería de Datos.

No es necesario avanzar más hoy.

---

**Conclusión:** Día 015 completado satisfactoriamente. Se demostró dominio de los fundamentos de precisión decimal, validación, agrupación monetaria y promedio ponderado.

**Estado final: 🟢 VERDE.**
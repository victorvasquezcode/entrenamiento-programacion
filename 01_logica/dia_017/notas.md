# Día 017 — Excepciones, validación estricta y procesamiento de inventario

**Estado:** 🟢 VERDE — COMPLETADO  
**Especialización:** Ciencia e Ingeniería de Datos  
**Lenguaje:** Python

---

## 1. Objetivos alcanzados

- Validar cadenas utilizando contratos estrictos.
- Diferenciar `is`, `==` e `in`.
- Utilizar `all()` con expresiones generadoras.
- Manejar `ValueError` mediante `try/except`.
- Reutilizar funciones de validación.
- Procesar movimientos de inventario secuencialmente.
- Rechazar operaciones que producen stock negativo.
- Evitar devolver resultados parciales.
- Calcular acumuladores y máximos.
- Conservar los argumentos originales.

## 2. Conceptos fundamentales

### Validación estricta

Una conversión válida para Python no necesariamente cumple las reglas de negocio.

Por ejemplo, `int("+5")` funciona, pero nuestro contrato no permite signos.

### all() y generadores

```python
all(caracter in valores_validos for caracter in texto)
```

Comprueba que cada carácter pertenezca al conjunto permitido.

Una secuencia vacía produce `True` con `all()`. Por eso es necesario rechazar las cadenas vacías previamente.

### Manejo de excepciones

```python
try:
    numero = int(texto)
except ValueError:
    return None
```

`ValueError` representa un error de conversión esperado.

`None` comunica al código que llama a la función que la entrada no pudo procesarse según el contrato.

### Validación técnica y de negocio

**Validación técnica:** comprueba tipos, formatos, claves y valores permitidos.

**Validación de negocio:** comprueba que la operación tenga sentido según el estado del inventario.

### Funciones puras

Una función pura produce el mismo resultado para las mismas entradas, bajo las mismas condiciones, y no genera efectos secundarios observables.

Modificar variables locales de tipo `int` no modifica los argumentos originales.

---

## 3. practica.py — Aprobado

```python
def convertir_stock(valor):
    if type(valor) is not str:
        return None

    normalizar_valor = valor.strip()

    if not normalizar_valor:
        return None

    valores_validos = (
        "0", "1", "2", "3", "4",
        "5", "6", "7", "8", "9"
    )

    if not all(
        caracter in valores_validos
        for caracter in normalizar_valor
    ):
        return None

    try:
        normalizar_valor = int(normalizar_valor)
        return normalizar_valor
    except ValueError:
        return None


def calcular_stock_final(stock_inicial, entradas, salidas):
    convertir_stock_inicial = convertir_stock(stock_inicial)
    convertir_entradas = convertir_stock(entradas)
    convertir_salidas = convertir_stock(salidas)

    if convertir_stock_inicial is None:
        return None

    if convertir_entradas is None:
        return None

    if convertir_salidas is None:
        return None

    stock_disponible = convertir_stock_inicial + convertir_entradas

    if convertir_salidas > stock_disponible:
        return None

    stock_final = stock_disponible - convertir_salidas

    return stock_final
```

### Pruebas de la práctica

- 16 pruebas obligatorias.
- 7 pruebas adicionales de casos límite.
- **Resultado: 23/23 aprobadas.**

---

## 4. desafio.py — Versión final aprobada

```python
from practica import convertir_stock


def procesar_movimientos_stock(stock_inicial, movimientos):
    total_entradas = 0
    total_salidas = 0
    cantidad_operaciones = 0

    if type(movimientos) is not list:
        return None

    stock_actual = convertir_stock(stock_inicial)

    if stock_actual is None:
        return None

    stock_maximo = stock_actual

    for movimiento in movimientos:
        if type(movimiento) is not dict:
            return None

        claves_validas = ("tipo", "cantidad")

        if not all(
            clave in claves_validas
            for clave in movimiento
        ):
            return None

        if len(movimiento) != 2:
            return None

        tipo = movimiento["tipo"]
        cantidad = movimiento["cantidad"]

        if type(tipo) is not str:
            return None

        if tipo not in ("entrada", "salida"):
            return None

        convertir_cantidad = convertir_stock(cantidad)

        if convertir_cantidad is None:
            return None

        if tipo == "entrada":
            stock_actual += convertir_cantidad
            total_entradas += convertir_cantidad

        elif tipo == "salida":
            if convertir_cantidad > stock_actual:
                return None

            stock_actual -= convertir_cantidad
            total_salidas += convertir_cantidad

        cantidad_operaciones += 1

        if stock_actual > stock_maximo:
            stock_maximo = stock_actual

    resultado = {
        "stock_final": stock_actual,
        "operaciones": cantidad_operaciones,
        "total_entradas": total_entradas,
        "total_salidas": total_salidas,
        "stock_maximo": stock_maximo
    }

    return resultado
```

*Se conservaron la lógica y las validaciones aprobadas. Solo se mejoraron los nombres de algunas variables para facilitar su lectura.*

---

## 5. Mutación 017 — Aprobada

### Requisitos incorporados

- `total_entradas`: unidades ingresadas.
- `total_salidas`: unidades retiradas.
- `stock_maximo`: mayor existencia alcanzada, incluyendo el stock inicial.

### Ejemplo

Entrada:

```python
movimientos = [
    {"tipo": "entrada", "cantidad": "10"},
    {"tipo": "salida", "cantidad": "4"},
    {"tipo": "entrada", "cantidad": "2"}
]

print(procesar_movimientos_stock("5", movimientos))
```

Resultado:

```python
{
    "stock_final": 13,
    "operaciones": 3,
    "total_entradas": 12,
    "total_salidas": 4,
    "stock_maximo": 15
}
```

### Casos evaluados

- Procesamiento de entradas y salidas.
- Lista vacía.
- Stock máximo igual al inicial.
- Stock máximo intermedio.
- Movimientos inválidos.
- Salidas superiores a las existencias.

**Resultado: 5/5 pruebas de mutación aprobadas.**

---

## 6. Evaluación conceptual final

**Pregunta 1:** El máximo se inicializa con el stock inicial porque también forma parte de los estados del inventario que debemos considerar.

**Pregunta 2:** Los movimientos se procesan en orden. Una salida inválida no puede compensarse mediante una entrada posterior.

**Pregunta 3:** `total_entradas` suma unidades ingresadas; `operaciones` cuenta movimientos; `stock_final` representa las existencias restantes.

**Pregunta 4:** Modificar una variable local que contiene un entero no altera el argumento original.

**Pregunta 5:** Si algún movimiento incumple el contrato, se devuelve `None`, sin entregar un resultado parcial.

**Resultado: 5/5 — APROBADO.**

---

## 7. Aprendizajes para Ingeniería de Datos

Este ejercicio introduce fundamentos que utilizaremos en procesos ETL:

1. Validar registros antes de aceptarlos.
2. Aplicar reglas de negocio de manera consistente.
3. Reutilizar componentes de validación.
4. Evitar publicar resultados incompletos.
5. Producir resúmenes a partir de registros procesados.

**Importante:** devolver `None` evita publicar resultados parciales desde esta función, pero no equivale a una transacción atómica en una base de datos.

---

## 8. Semáforo definitivo

| Actividad | Estado |
|---|---|
| Repaso activo | 🟢 APROBADO |
| Práctica | 🟢 APROBADA |
| Desafío autónomo | 🟢 APROBADO |
| Mutación | 🟢 APROBADA |
| Evaluación conceptual | 🟢 APROBADA |
| Día 017 | 🟢 VERDE |
| Día 018 | DESBLOQUEADO |

---

## 9. Próxima sesión

**Día 018 — Pendiente de iniciar.**

Comenzaremos con repaso activo de los días verdes y un nuevo concepto técnico, seguido de práctica, desafío autónomo y mutación.

No se considerará aprobado ningún contenido nuevo sin evidencias.

**DÍA 017 COMPLETADO — 🟢 VERDE.**
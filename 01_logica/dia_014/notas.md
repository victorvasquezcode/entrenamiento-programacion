# Día 014 — Funciones puras y transformación de datos

**Ruta:** Python desde cero → Ciencia e Ingeniería de Datos  
**Fecha:** 06/11/2026  
**Estado final:** 🟢 VERDE — APROBADO

---

## 1. Objetivo alcanzado

Aprender a validar, transformar y agrupar información mediante funciones sin efectos secundarios observables y sin modificar las entradas originales.

## 2. Conceptos dominados

### Funciones puras

Una función pura:

1. Produce el mismo resultado para los mismos argumentos.
2. No produce efectos secundarios observables.

Esto facilita las pruebas automatizadas, porque no requiere preparar archivos, bases de datos ni otros recursos externos.

### Inmutabilidad de entradas

Crear un diccionario nuevo evita modificar accidentalmente los datos recibidos.

Una función puede modificar estructuras locales creadas por ella misma sin alterar el estado externo.

### Validación numérica

- Utilizar `math.isfinite()` para rechazar NaN e infinito.
- Rechazar booleanos cuando se requieren números.
- Comprobar tipos, rangos y campos obligatorios.
- Normalizar nombres mediante `.strip()`.

### Separación de responsabilidades

Dividir las operaciones en validación, transformación y persistencia permite:

- Comprender mejor el código.
- Realizar pruebas independientes.
- Facilitar el mantenimiento y la refactorización.
- Reutilizar las transformaciones en distintos sistemas.

## 3. Repaso activo — 🟢 APROBADO

- [x] Copias superficiales y referencias.
- [x] Comparaciones con NaN.
- [x] Escritura segura y fallos de `os.replace()`.

**Resultado:** 3/3.

## 4. `practica.py` — 🟢 APROBADA

**Función:** `aplicar_descuentos(productos, porcentaje)`

Se implementaron:

- Validación estricta de productos y porcentajes.
- Normalización de nombres.
- Detección de duplicados.
- Rechazo de valores inválidos.
- Cálculo de descuentos.
- Creación de un diccionario independiente.

**Pruebas:** ocho casos revisados y aprobados por inspección.

## 5. `desafio.py` — 🟢 APROBADO

**Función:** `transformar_ventas(ventas)`

Se implementaron:

- Validación de registros.
- Comprobación de campos obligatorios.
- Agrupación de ventas por producto.
- Acumulación de cantidades e importes.
- Conservación de los datos originales.

**Pruebas:** casos normales, entradas inválidas, lista vacía e inmutabilidad.

## 6. `mutacion_014.py` — 🟢 APROBADA

Se incorporó el precio promedio ponderado por unidad.

### Ejemplo

```python
ventas = [
    {"producto": "Teclado", "cantidad": 2, "precio": 40.0},
    {"producto": "Teclado", "cantidad": 3, "precio": 50.0}
]
```

Resultado:

```python
{
    "Teclado": {
        "cantidad": 5,
        "total": 230.0,
        "promedio": 46.0
    }
}
```

### Aprendizajes

- Acumular cantidades e importes antes de calcular promedios.
- Diferenciar promedio simple de promedio ponderado.
- Modificar estructuras locales sin alterar los argumentos.
- Mantener la validación separada de la transformación.

**Pruebas:** ocho casos revisados y aprobados por inspección.

## 7. Evaluación conceptual — 🟢 4/4

### 1. ¿Por qué las funciones puras facilitan las pruebas?

Porque permiten comparar resultados reales y esperados sin preparar archivos, bases de datos ni otros efectos secundarios.

### 2. ¿Por qué crear un diccionario nuevo?

Para devolver resultados sin modificar los valores del diccionario original cuando el contrato exige conservarlo.

### 3. ¿Una función que utiliza `print()` es pura?

No. Escribir en la salida estándar constituye un efecto secundario observable.

### 4. ¿Por qué separar transformación y almacenamiento?

Porque facilita la refactorización, divide responsabilidades grandes en componentes pequeños y permite probar la lógica sin acceder a archivos o bases de datos.

**Resultado:** cuatro respuestas correctas.

## 8. Observaciones técnicas para el futuro

- Una copia superficial puede compartir objetos mutables internos.
- Los cálculos con `float` extremadamente grandes pueden desbordarse hasta infinito.
- Separar validación, agrupación y cálculo mejora la claridad, aunque implique varios recorridos.
- Los cálculos monetarios reales pueden requerir `decimal.Decimal` para evitar errores de representación binaria.

Estas observaciones no bloquean la aprobación del día.

## 9. Semáforo definitivo

| Actividad | Estado |
|---|---|
| Repaso activo | 🟢 APROBADO |
| `practica.py` | 🟢 APROBADO |
| `desafio.py` | 🟢 APROBADO |
| `mutacion_014.py` | 🟢 APROBADO |
| Evaluación conceptual | 🟢 APROBADO |
| Día 014 | 🟢 VERDE |
| Día 015 | DESBLOQUEADO |

## 10. Próxima sesión

Continuar con el Día 015.

Iniciar con recuperación activa de funciones puras, validación de datos, agrupación y promedios ponderados antes de introducir el siguiente concepto.

**Cierre:** Día 014 completado satisfactoriamente. La aprobación se basa en revisión técnica del código y las pruebas presentadas, sin ejecución independiente de estas últimas.
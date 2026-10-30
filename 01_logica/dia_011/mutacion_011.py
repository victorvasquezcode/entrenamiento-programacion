#Análisis de inventario desde archivos
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
    except (ValueError,TypeError):
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
    except(ValueError,TypeError):
        return None
def procesar_inventario(ruta):
    datos = {}
    rechazados = 0
    try:
        with open(ruta, "r",encoding="utf-8") as archivo:
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
                        "precio" : nuevo_precio
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

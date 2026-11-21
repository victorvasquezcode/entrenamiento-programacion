#Persistencia y actualización de inventario
import math

from escritura_segura import escribir_texto_seguro
def cargar_inventario(ruta):
    inventario_cargado = {}
    try:
        with open(ruta,"r",encoding="utf-8") as archivos:
            for archivo in archivos:
                campos = archivo.split(";")
                if len(campos) != 4:
                    continue
                codigo, nombre, stock, precio = campos
                normalizar_codigo = codigo.strip()
                if not normalizar_codigo:
                    continue
                normalizar_nombre = nombre.strip()
                if not normalizar_nombre:
                    continue
                try:
                    normalizar_stock = stock.strip()
                    convertir_stock = int(normalizar_stock)
                except ValueError:
                    continue
                if convertir_stock < 0:
                    continue
                try:
                    normalizar_precio = precio.strip()
                    convertir_precio = float(normalizar_precio)
                except ValueError:
                    continue
                if convertir_precio < 0 or not math.isfinite(convertir_precio):
                    continue
                if normalizar_codigo in inventario_cargado:
                    continue
                inventario_cargado[normalizar_codigo] ={
                    "nombre": normalizar_nombre,
                    "stock" : convertir_stock,
                    "precio": convertir_precio
                }
    except (OSError, UnicodeError):
        return None
    return inventario_cargado
def actualizar_stock(inventario,codigo,cantidad,operacion):
    if type(operacion) is not str:
        return False
    normalizar_operacion = operacion.strip().lower()
    if not isinstance(inventario, dict) or not isinstance(codigo, str) or codigo not in inventario:
        return False
    if type(cantidad) is not int:
        return False
    if cantidad <= 0:
        return False
    if normalizar_operacion == "entrada":
        inventario[codigo]["stock"] += cantidad
        return True
    elif normalizar_operacion == "salida":
        if cantidad > inventario[codigo]["stock"]:
            return False
        inventario[codigo]["stock"] -= cantidad
        return True
    else:
        return False
def guardar_inventario(ruta, inventario):
    lineas = []
    for codigo in sorted(inventario):
        producto = inventario[codigo]
        nombre = producto["nombre"]
        if any(separador in campo for campo in (codigo, nombre) for separador in (";", "\n", "\r")):
            return False
        lineas.append(f"{codigo};{nombre};{producto['stock']};{producto['precio']:.2f}\n")
    return escribir_texto_seguro(ruta, lineas)


if __name__ == "__main__":
    inventario_cargado = cargar_inventario("inventario.txt")
    if inventario_cargado is None:
        print("No se pudo cargar el inventario.")
    else:
        print("Inventario cargado. Llama a actualizar_stock con los movimientos que quieras aplicar.")

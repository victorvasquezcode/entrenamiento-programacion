#Persistencia y actualización de inventario
import math
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
    except OSError:
        return None
    return inventario_cargado
def actualizar_stock(inventario,codigo,cantidad,operacion):
    if type(operacion) is not str:
        return False
    normalizar_operacion = operacion.strip().lower()
    if codigo not in inventario:
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
def guardar_inventario(ruta,inventario):
    try:
        with open(ruta,"w", encoding="utf-8") as archivo:
            inventario_ordenado = sorted(inventario)
            for codigo in inventario_ordenado:
                archivo.write(f"{codigo};{inventario[codigo]['nombre']};{inventario[codigo]['stock']};{inventario[codigo]['precio']:.2f}\n")
            return True
    except OSError:
        return False
        
inventario_cargado = cargar_inventario("inventario.txt")
prueba_1 = actualizar_stock(inventario_cargado,"P001",5,"entrada")
prueba_2 = actualizar_stock(inventario_cargado,"P002",8,"salida")
prueba_3 = actualizar_stock(inventario_cargado,"P003",10,"salida")
prueba_4 = actualizar_stock(inventario_cargado,"P003","5","entrada")
prueba_5 = actualizar_stock(inventario_cargado,"P999","5","entrada")
guardado = guardar_inventario("inventario.txt",inventario_cargado)
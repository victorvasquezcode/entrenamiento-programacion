import math
import os
import tempfile
inventario = {
    "P001": {
        "nombre": "Teclado",
        "stock": 10,
        "precio": 45.50
    },
    "P002": {
        "nombre": "Mouse",
        "stock": 20,
        "precio": 25.00
    },
    "P003": {
        "nombre": "Monitor",
        "stock": 5,
        "precio": 750.00
    }
}
def guardar_inventario_seguro(ruta, inventario):
    if not type(inventario) is dict:
        return None
    duplicados = set([])
    for producto in inventario:
        if not type(producto) is str:
            return None
        normalizar_codigo = producto.strip()
        if not normalizar_codigo:
            return None
        if not type(inventario[producto]) is dict:
            return None
        if not "nombre" in inventario[producto] :
            return None
        if not "stock" in inventario[producto]:
            return None
        if not "precio" in inventario[producto]:
            return None
        nombre = inventario[producto]["nombre"]
        stock = inventario[producto]["stock"]
        precio = inventario[producto]["precio"]
        if not type(nombre) is str:
            return None
        normalizar_nombre = nombre.strip()
        if not normalizar_nombre:
            return None
        if not type(stock) is int or stock < 0:
            return None
        if not type(precio) is int and not type(precio) is float:
            return None
        if precio < 0:
            return None
        if not math.isfinite(precio):
            return None
        for simbolo in (";","\n","\r"):
            if simbolo in normalizar_codigo or simbolo in normalizar_nombre:
                return None
        if normalizar_codigo in duplicados:
            return None
        else:
            duplicados.add(normalizar_codigo)
    temporal = None
    try:
        directorio = os.path.dirname(os.path.abspath(ruta))
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=directorio,
            delete=False
        ) as archivo:
            temporal = archivo.name
            for codigo in sorted(inventario, key=lambda codigo: codigo.strip()):
                producto = inventario[codigo]
                nombre = producto["nombre"].strip()
                stock = producto["stock"]
                precio = producto["precio"]
                archivo.write(
                    f"{codigo.strip()};{nombre};{stock};{precio:.2f}\n"
                )
        os.replace(temporal, ruta)
        return True
    except OSError:
        return False
    finally:
        if temporal is not None:
            try:
                if os.path.exists(temporal):
                    os.remove(temporal)
            except OSError:
                pass
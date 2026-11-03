import os
def guardar_seguro(ruta,lineas):
    if not type(lineas) is list:
        return False
    temporal = ruta + ".tmp"
    for linea in lineas:
        if not type(linea) is str:
            return False
    try:
        with open(temporal, "w", encoding="utf-8") as archivo:
            for linea in lineas:
                    if not linea.endswith("\n"): 
                        archivo.write(f"{linea}\n")
                    else:
                        archivo.write(f"{linea}")
        os.replace(temporal, ruta)
        return True
    except OSError:
        try:
            if os.path.exists(temporal):
                os.remove(temporal)
        except OSError:
            return False
        return False